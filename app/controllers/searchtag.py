import json
import os
from flask_restful import Resource, request


class TagSearchView(Resource):

    os.chdir(os.getcwd()+"/data/audios")

    # searches for particular tag(s) and returns all audios attached to it
    def post(self):
        #os.chdir("/")
        #print(os.getcwd())
        path = os.getcwd()
        print(f"this path:{path}")

        data = request.get_json()

        collection = []

        results = data["tag_name"]

        if (type(results) is list):
            # check whether tag is passed as one string or array
            for item in results:

                all_data = dict(Tag = "", URLs=[], Audios=[], Start_time=[])

                name = item

                for root, dir, file in os.walk("."):
                    for filename in file:

                        with open(filename, 'r') as infile:
                            if filename == ".DS_Store":
                                continue
                            else: 
                                """ print(filename) """
                                file_data = json.loads(infile.read())

                                words = file_data['transcripts'][0]['words']

                                for word in words:

                                    if word['word'] == name:
                                        all_data["Audios"].append(filename.replace(".json",".wav"))
                                        all_data["URLs"].append(file_data['transcripts'][0]['audio_url'])
                                        all_data["Start_time"].append(word['start_time'])
                                    else:
                                        continue
                                
                collection.append(dict(Tag=all_data['Tag'],Audios=all_data['Audios'],Start_time=all_data['Start_time']))

            if (len(collection) < 1):
                return dict(status="fail", message=f"no audios with {results} "), 404
            else:
                return dict(status='success', data=collection), 200

        else:
            #print("its not a list")
            name = data["tag_name"]

            all_data = dict(Tag = "", URLs=[], Audios=[], Start_time=[])

            all_data['Tag'] = name

            for root, dir, file in os.walk("."):
                for filename in file:

                    with open(filename, 'r') as infile:
                        if filename == ".DS_Store":
                            continue
                        else: 
                            """ print(filename) """
                            file_data = json.loads(infile.read())

                            words = file_data['transcripts'][0]['words']

                            for word in words:

                                if word['word'] == name:
                                    all_data["Audios"].append(filename.replace(".json",".wav"))
                                    all_data["URLs"].append(file_data['transcripts'][0]['audio_url'])
                                    all_data["Start_time"].append(word['start_time'])
                                else:
                                    continue
                    
            if len(all_data['Audios']) < 1:
                return dict(status="fail", message=f"no audios with {name}"), 404
            else:
                return dict(status="success", data=all_data), 200

