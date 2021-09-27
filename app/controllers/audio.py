import os
import json
from os.path import join, dirname, realpath
from flask import current_app, send_from_directory, send_file, make_response
from flask_restful import Resource, request
from werkzeug.utils import secure_filename


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']


def uploaded_file(filename):
    return send_from_directory(current_app.config['UPLOAD_FOLDER'], filename)


class AudioView(Resource):

    def post(self):

        request_data = request.files['file']
        request_url = request.form['url']

        if not request_data:

            return dict(status="fail", message="BAD REQUEST (No File Selected!)"), 400

        elif not request_url:

            return dict(status="fail", message="BAD REQUEST (No Audio given!)"), 400

        else:

            if allowed_file(request_data.filename):

                file_data = json.loads(request_data.read())

                uploaded_data = dict(
                    transcripts=[dict(
                        confidence=file_data['transcripts'][0]['confidence'],
                        date=file_data['transcripts'][0]['date'],
                        time=file_data['transcripts'][0]['time'],
                        filename=file_data['transcripts'][0]['filename'],
                        radio_station=file_data['transcripts'][0]['radio_station'],
                        words=file_data['transcripts'][0]['words'],
                        url=request_url
                    )]
                )

                new_file = secure_filename(request_data.filename)
                location = current_app.config['UPLOAD_FOLDER'] + new_file

                if os.path.isfile(location) == True:
                    return dict(status="fail", message="File Already Exists"), 412

                else:
                    with open(f'{location}', 'w') as outfile:
                        json.dump(uploaded_data, outfile)
                    return dict(status="success", message="Uploaded Successfully!"), 200

            else:
                return dict(status="fail", message="Wrong File Format"), 412

    def get(self):

        collection = []

        for root, dir, file in os.walk(current_app.config['UPLOAD_FOLDER']):
            for filename in file:

                if filename == ".DS_Store":
                    continue
                else:

                    file_string = current_app.config['UPLOAD_FOLDER'] + filename

                    with open(file_string, 'r') as infile:
                        data = json.loads(infile.read())

                    collection.append(data)

        return dict(status="success", data=collection), 200
