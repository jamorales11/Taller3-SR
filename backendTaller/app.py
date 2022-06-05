from pyexpat import features
from flask import Flask, jsonify, request
from flask_cors import CORS
import os
import pandas as pd
import numpy as np
import json
import folium


import time

from sklearn.model_selection import train_test_split
from scipy import spatial

from sklearn.metrics import pairwise_distances
from scipy.spatial.distance import cosine
from sklearn.feature_selection import chi2

from sklearn.neighbors import KNeighborsClassifier

from sklearn.metrics import precision_recall_fscore_support

import User_User_RS as uu_rs
import Content_Based_RS as cb_rs
import preprocessing as pp


dataset_path = 'dataset/ml-latest-small/'

df_movies = pd.read_json(dataset_path + 'movies.json', lines=True)

print(df_movies)

df_ratings = pd.read_json(dataset_path + 'ratings.json', lines=True)

print(df_ratings)



app = Flask(__name__)
CORS(app)


@app.route("/")
def hello_from_root():
    return jsonify(message = "Hello from Root")



@app.route("/get_usuario/<id>", methods= ["POST", "GET"])
def get_usuario_df(id):
    print(id)

    #user_info = df_users[df_users['user_id'] == id][['name', 'review_count', 'yelping_since']]

    return user_info.to_json(orient="records")




@app.route("/get_business/<id>", methods=["POST", "GET"])
def get_business(id):
    print(request.json)

    return request.json




@app.route("/get_recomendaciones/<id>", methods=["POST", "GET"])
def get_recomendaciones(id):
    print(id)

    recommendations = [{"name": "1", "latitude":4.713991455266561, "longitude": -74.0299935}, 
                        {"name": "2", "latitude":4.705394596794235, "longitude": -74.03334089677242}]

    imp_feat = ["Ford", "Ford", "Ford"]
    imp_user = [{"model": "Mustang"}, {"model": "Mustang"}, {"model": "Mustang"}]
    print(recommendations)
    return jsonify(recommendaciones=recommendations.to_json(orient="records"), features= imp_feat, usuarios = imp_user.to_json(orient="records"))

