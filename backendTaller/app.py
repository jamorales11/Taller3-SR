from pyexpat import features
from flask import Flask, jsonify, request
from flask_cors import CORS
import os
import pandas as pd
import numpy as np
import json


import time

import preprocessing as pp

user_id = 216006
K_rec = 50

#Load datasets
ratings, movies = pp.load_datasets()
print('Datasets loaded.')

print(movies)

print(ratings)



#dataset_path = 'dataset/ml-latest-small/'

#df_movies = pd.read_csv(dataset_path + 'movies.csv')

#print(df_movies)

#df_ratings = pd.read_csv(dataset_path + 'ratings.csv')

#print(df_ratings)

users = pd.DataFrame(ratings["userId"].unique(), columns = ['userId'])

print(users)


app = Flask(__name__)
CORS(app)


@app.route("/")
def hello_from_root():
    return jsonify(message = "Hello from Root")



@app.route("/get_usuario/<id>", methods= ["POST", "GET"])
def get_usuario_df(id):
    print(id)
    usuario = False

    if users.loc[lambda users: users["userId"] == int(id)].empty == True:
        print("No existe este usuario")
    else:
        print("usuario encontrado")
        return users.loc[lambda users: users["userId"] == int(id)].to_json()
    return jsonify(False)
    

    
@app.route("/create_usuario", methods= ["POST"])
def create_usuario_df():
    global users

    if users.loc[lambda users: users["userId"] == int(request.json["userId"])].empty == True:
        data = pd.DataFrame(data=request.json, index=[0])
        result = pd.concat([users, data], ignore_index=True)
        users = result
        print(users)
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

