from pyexpat import features
from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
import os
import pandas as pd
import numpy as np
import json

from PIL import Image
import base64


import time

import collaborative_filtering as cf
import preprocessing as pp
import content_based as cb
import graph_based as gb

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
    print(request.json["userId"])
    print(request.json)

    print(type(request.json["userId"]))
    print(type(request.json))

    if users.loc[lambda users: users["userId"] == int(request.json["userId"])].empty == True:
        data = pd.DataFrame(data=request.json, index=[0])
        data["userId"] = data["userId"].apply(pd.to_numeric)
        result = pd.concat([users, data], ignore_index=True)
        users = result
        print(users)
    return request.json




@app.route("/get_recomendaciones/<id>", methods=["POST", "GET"])
def get_recomendaciones(id):
    print(id)
    type(id)
    

    recommendations = generate_recommendations(int(id), K_rec, ratings, movies)
    print(recommendations)


    return jsonify(recommendaciones=recommendations)


@app.route("/get_grafo", methods=["POST", "GET"])
def get_grafo():
    filename = 'recommended_movies_graph.png'

    return send_file(filename, mimetype='image/png')


@app.route("/get_movies", methods=["POST", "GET"])
def get_movies():

    return jsonify(movies = movies.to_json(orient="records"))


@app.route("/add_preferencias", methods= ["POST"])
def add_preferencias_df():
    print(request.json)

    global ratings
    data = pd.DataFrame(data=request.json)
    print(data)

    result = pd.concat([ratings, data], ignore_index=True)
    ratings = result
    print(ratings)
    
    return data.to_json()