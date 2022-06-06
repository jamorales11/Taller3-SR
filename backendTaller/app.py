from pyexpat import features
from flask import Flask, jsonify, request
from flask_cors import CORS
import os
import pandas as pd
import numpy as np
import json


import time

import collaborative_filtering as cf
import preprocessing as pp
import content_based as cb
import graph_based as gb

user_id = 216006
K_rec = 50

#Load datasets
ratings, movies = pp.load_datasets()
print('Datasets loaded.')

print(movies)

print(ratings)


users = pd.DataFrame(ratings["user_id"].unique(), columns = ['userId'])

print(users)

def generate_recommendations(user_id, K_rec, ratings, movies):
    
    #Generate collaborative recommendations
    sim_users, recommendations_user_user = cf.get_recommendations(ratings, user_id, K_rec)
    print('Collaborative filtering recommendations created.')
    
    #Generate content based recommendations
    recommendations_content_based = cb.get_recommendations(movies, ratings, user_id, K_rec)
    print('Content based recommendations created.')
    
    #Rank recommendations generated with CB and CF using graphs and PageRank
    movies_rec, df_rec = gb.get_recommendations(movies, ratings, recommendations_user_user, recommendations_content_based)
    print('Recommendations ranked using PageRank.')
    
    #Generation of figure corresponding to user movie recommendations graph
    gb.gen_figure(df_rec)
    print('Graph created.')
    
    return movies_rec


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

    recommendations = generate_recommendations(user_id, K_rec, ratings, movies)
    print(recommendations)

    #recommendations = [{"name": "1", "latitude":4.713991455266561, "longitude": -74.0299935}, 
                        #{"name": "2", "latitude":4.705394596794235, "longitude": -74.03334089677242}]

    #imp_feat = ["Ford", "Ford", "Ford"]
    #imp_user = [{"model": "Mustang"}, {"model": "Mustang"}, {"model": "Mustang"}]

    return jsonify(recommendaciones=recommendations.to_json(orient="records"))

