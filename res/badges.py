from flask import Flask, json, jsonify, request
from flask.wrappers import Response
from flask_restful import Resource, abort
from flask_pymongo import pymongo
from bson.json_util import dumps, ObjectId
import db_config as database

class Badges(Resource):
    ''' get all badges '''
    def get(self):
        response = list(database.db.Badges.find())
        
        for doc in response:
            doc['_id'] = str(doc['_id'])
            
        return jsonify(response)
    
    def post(self):
        _ids = list(database.db.Badges.insert_many([
            {
                'header_img_url':request.json[0]['header_img_url'],
                'profile_picture_url':request.json[0]['profile_picture_url'],
                'name':request.json[0]['name'],
                'age':request.json[0]['age'],
                'city':request.json[0]['city'],
                'followers':request.json[0]['followers'],
                'likes':request.json[0]['likes'],
                'post':request.json[0]['post'],
                   
            },
            {
                'header_img_url':request.json[1]['header_img_url'],
                'profile_picture_url':request.json[1]['profile_picture_url'],
                'name':request.json[1]['name'],
                'age':request.json[1]['age'],
                'city':request.json[1]['city'],
                'followers':request.json[1]['followers'],
                'likes':request.json[1]['likes'],
                'post':request.json[1]['post'],
                         
            }
            
        ]).inserted_ids)
        
        results = []
        
        for _id in _ids:
            results.append(str(_id))
            
        return jsonify({'inserted_ids': results})
    
    def delete(self):
        return database.db.Badges.delete_many({}).deleted_count
        