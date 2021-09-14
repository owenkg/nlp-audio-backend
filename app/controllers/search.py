import json
import os
"""
from app.models.tag import Tag
from app.models.audiotag import AudioTag
from app.models.audio import Audio
from app.models.topic import Topic
from app.schemas import TagInSchema
from app.schemas import TopicSchema
"""
from flask_restful import Resource, request

"""os.chdir("../../data")
path = os.getcwd()"""

class TagSearchView(Resource):

    os.chdir(os.getcwd()+"/data/audios")

    # searches for particular tag(s) and returns all audios attached to it
    def post(self):
        #os.chdir("/")
        #print(os.getcwd())
        path = os.getcwd()
        #print(f"this path:{path}")

        data = request.get_json()

        collection = []



        results = data["tag_name"]

        if (type(results) is list):
            # check whether tag is passed as one string or array
            all_data = dict(Tag = "", Audios=[], Start_time=[])

            for item in results:

                name = item


                #print(name)
                for root, dir, file in os.walk("."):
                    for filename in file:
                        #print(filename)

                        with open(filename, 'r') as infile:
                             file_data = json.loads(infile.read())

                        words = file_data['transcripts'][0]['words']

                        for word in words:
                            #print(word['word'])
                            if word['word'] == name:
                                #print(f"Word: { word['word'] }, Audio: { filename }, Start Time: { word['start_time']}")
                                all_data["Tag"] = word['word']
                                all_data["Audios"].append(filename)
                                all_data["Start_time"].append(word['start_time'])
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

            #tagschema = TagInSchema()



            for root, dir, file in os.walk("."):
                for filename in file:
                    print(filename)

                    with open(filename, 'r') as infile:
                         file_data = json.loads(infile.read())

                    words = file_data['transcripts'][0]['words']

                    for word in words:
                        #print(word['word'])
                        if word['word'] == name:
                            #print(f"Word: { word['word'] }, Audio: { filename }, Start Time: { word['start_time']}")
                            all_data["Audios"].append(filename)
                            all_data["Start_time"].append(word['start_time'])
                        else:
                            continue

            #tag = Tag.find_first(tag_name=name)

            #if not tag:
            #    return dict(status="fail", message=f"Tag with name {name} does not exist!"), 404

            if len(all_data['Audios']) < 1:
                return dict(status="fail", message=f"no audios with {name}"), 404
            else:
                return dict(status="success", data=all_data), 200

class TopicSearchView(Resource):

    # searches for particular topic(s) and returns all audios attached to it
    def post(self):
        data = request.get_json()
        results = data["topic_name"]

        if (type(results) is list):
            # check whether tag is passed as one string or array
            collection = []

            for item in results:

                name = item

                for root, dir, file in os.walk("."):
                    for filename in file:
                        #print(filename)

                        with open(filename, 'r') as infile:
                             data = json.loads(infile.read())

                        words = data['transcripts'][0]['words']

                        for word in words:
                            #print(word['word'])
                            if word['word'] == name:
                                #print(f"Word: { word['word'] }, Audio: { filename }, Start Time: { word['start_time']}")
                                all_data["Audios"].append(filename)
                                all_data["Start_time"].append(word['start_time'])
                            else:
                                continue

                collection.append(all_data)

            if (len(collection) < 1):
                return dict(status="fail", message=f"no under topics {results} "), 404
            else:
                return dict(status='success', data=collection), 200

        else:
            #print("its not a list")
            name = data["topic_name"]

            #tagschema = TagInSchema()

            for root, dir, file in os.walk("."):
                for filename in file:
                    #print(filename)

                    with open(filename, 'r') as infile:
                         data = json.loads(infile.read())

                    words = data['transcripts'][0]['words']

                    for word in words:
                        #print(word['word'])
                        if word['word'] == name:
                            print(f"Word: { word['word'] }, Audio: { filename }, Start Time: { word['start_time']}")
                            all_data["Audios"].append(filename)
                            all_data["Start_time"].append(word['start_time'])
                        else:
                            continue

            #tag = Tag.find_first(tag_name=name)

            #if not tag:
            #    return dict(status="fail", message=f"Tag with name {name} does not exist!"), 404

            if len(all_data['Audios']) < 1:
                return dict(status="fail", message=f"no audios with {name}"), 404
            else:
                return dict(status="success", data=all_data), 200
