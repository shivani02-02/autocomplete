'''
Created on Oct 31, 2019

@author: shivani.chauhan
'''
from flask import Flask, Response, render_template, request, jsonify
import json
from src.readtsv import Logic
from flask_restplus import Resource, Api, reqparse
from flask_cors import CORS
from flask_restplus import Api, reqparse
import datetime
import logging
from flask.helpers import make_response

app = Flask(__name__)
CORS(app)
api = Api(app)

logger=logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
fmt = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(fmt)
logger.addHandler(ch)


@api.route('/index')
class autocomplete1(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('index.html'),200,headers)

# created a parser to accept the user input, We can provide the input in the Swagger UI as well.
# parser = reqparse.RequestParser()
# parser.add_argument('input', type=str, help='Type the letter to see autocomplete feature..!')

# A GET request which accepts the user input and provides a json response containing top 25 matches based on ranking.
@api.route('/search')
class autocomplete(Resource):
    def get(self):
#         args = parser.parse_args()
        logic = Logic()
        try:
            start_time = datetime.datetime.now()
            list_of_words=[]
            input_word = request.args['input']
            print(input_word)
            input_related_words = logic.search_word(input_word.lower())
            words = logic.sorting(input_related_words, input_word.lower())
            if len(words)==0:
                empty_dict = {"Message":"No word found"}
                return jsonify(results = empty_dict)
            for word in words :
                list_of_words.append(word[0])
                
        except Exception as e:
            end_time = datetime.datetime.now()
            time_elapsed = end_time - start_time
            logger.error('Some error occurred, please check logs : ' +str(e))
            logger.info("API Response Time (On Failure) : " + str(time_elapsed))
            dict_of_error_message = {}
            dict_of_error_message['Error'] = str(e)
            return jsonify(results = dict_of_error_message)

        end_time = datetime.datetime.now()
        time_elapsed = end_time - start_time 
        logger.info("API Response Time : " + str(time_elapsed))
        print(list_of_words)
        return jsonify(results=list_of_words)

            
# A Get request that takes user input and returns input string and its frequency as key value pair.
# @nm_space.route('/wordcount')
# class show_word_freq(Resource):
#       
#     @nm_space.expect(parser)
#     def get(self):
#         args = parser.parse_args()
#         logic = Logic()
#         dic = {}
#         try:
#             start_time = datetime.datetime.now()
#             input = args['input']
#             if input == '':
#                 return Response('We need a input string..!', status = 500, mimetype = 'application/json')
#             else:
#                 related_words = logic.search_word(input.lower())
#                 words = logic.sorting(related_words, input.lower())
#                 if len(words)==0:
#                     return Response('No words found..!', status = 404, mimetype = 'text/plain')
#                 else:
#                     for tup in words :
#                         if input == tup[0]:
#                             dic[tup[0]] = tup[1]       
#         except Exception as e:
#             end_time = datetime.datetime.now()
#             time_elapsed = end_time - start_time
#             logger.error('Some error occurred, please check logs : ' +str(e))
#             logger.info("API Response Time (On Failure) : " + str(time_elapsed))
#             return Response(str(e), mimetype='text/plain', status=500)
#         
#         end_time = datetime.datetime.now()
#         time_elapsed = end_time - start_time 
#         logger.info("API Response Time : " + str(time_elapsed))
#         return Response(json.dumps(dic), status = 200, mimetype = 'application/json')
#                         

if __name__ == '__main__':
    app.run(debug=True)