import json
import os
from flask import current_app, send_from_directory, send_file, make_response
from flask_restful import Resource, request


class TagSearchView(Resource):
    # searches for particular tag(s) and returns all audios attached to it
    def post(self):

        data = request.get_json()

        collection = []

        results = data["tag_name"]

        if (type(results) is list):
            # check whether tag is passed as one string or array
            for item in results:

                all_data = dict(Tag="", Audios=[])

                name = item

                for root, dir, file in os.walk(current_app.config['UPLOAD_FOLDER']):
                    for filename in file:

                        if filename == ".DS_Store":
                            continue
                        else:
                            # print(filename)

                            file_string = current_app.config['UPLOAD_FOLDER'] + filename

                            with open(file_string, 'r') as infile:
                                data = json.loads(infile.read())

                            words = data['transcripts'][0]['words']

                            for word in words:
                                if word['word'] == name:
                                    if data not in all_data['Audios']:
                                        all_data['Audios'].append(data)
                                    else:
                                        continue
                                else:
                                    continue
                collection.append(all_data)
            if (len(collection) < 1):
                return dict(status="fail", message=f"no audios with {results} "), 404
            else:
                return dict(status='success', data=collection), 200

        else:
            #print("its not a list")
            name = data["tag_name"]

            all_data = dict(Tag="", Audios=[])

            all_data['Tag'] = name

            for root, dir, file in os.walk(current_app.config['UPLOAD_FOLDER']):
                for filename in file:

                    if filename == ".DS_Store":
                        continue
                    else:
                        # print(filename)

                        file_string = current_app.config['UPLOAD_FOLDER'] + filename

                        with open(file_string, 'r') as infile:
                            data = json.loads(infile.read())

                        words = data['transcripts'][0]['words']

                        for word in words:
                            if word['word'] == name:
                                if data not in all_data['Audios']:
                                    all_data['Audios'].append(data)
                                else:
                                    continue
                            else:
                                continue

            if len(all_data['Audios']) < 1:
                return dict(status="fail", message=f"no audios with {name}"), 404
            else:
                return dict(status="success", data=all_data), 200


class TopicSearchView(Resource):

    # os.chdir(os.getcwd()+"/data/topics")

    # searches for particular topic(s) and returns all audios attached to it
    def post(self):

        data = request.get_json()

        results = data["topic_name"]

        collection = []

        if (type(results) is list):
            # check whether tag is passed as one string or array
            for item in results:

                all_data = dict(Topic="", Audios=[], Start_time=[])

                name = item

                for root, dir, file in os.walk("."):
                    for filename in file:

                        with open(filename, 'r') as infile:
                            file_data = json.loads(infile.read())

                        words = file_data['transcripts'][0]['words']

                        for word in words:

                            if word['word'] == name:

                                all_data["Topic"] = word['word']
                                all_data["Audios"].append(filename)
                                all_data["Start_time"].append(
                                    word['start_time'])
                            else:
                                continue

                collection.append(dict(
                    Topic=all_data['Topic'], Audios=all_data['Audios'], Start_time=all_data['Start_time']))

            if (len(collection) < 1):
                return dict(status="fail", message=f"no audios with {results} "), 404
            else:
                return dict(status='success', data=collection), 200

        else:
            #print("its not a list")
            name = data["topic_name"]

            all_data = dict(Topic="", Audios=[], Start_time=[])

            all_data['Topic'] = name

            for root, dir, file in os.walk("."):
                for filename in file:

                    with open(filename, 'r') as infile:
                        file_data = json.loads(infile.read())

                    words = file_data['transcripts'][0]['words']

                    for word in words:

                        if word['word'] == name:

                            all_data["Audios"].append(filename)
                            all_data["Start_time"].append(word['start_time'])
                        else:
                            continue

            if len(all_data['Audios']) < 1:
                return dict(status="fail", message=f"no audios with {name}"), 404
            else:
                return dict(status="success", data=all_data), 200
