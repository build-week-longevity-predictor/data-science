#!/usr/bin/env python
# coding: utf-8

# import for flask app
from flask import Flask, request, jsonify
# import for db connection
import psycopg2
# import for pkl from dump in ML_model_class
import pickle

# TODO: from ML_model import ML_model_class
# OR PKL File below


# Creating Flask APP
APP = Flask(__name__)
# Flask APP run if called
if __name__ == 'main':
    APP.run()


# database connect info to backend group webserver
# will need to find privacy settings or token user/id for db access

dbname= 'dcbsokv63dln3d'
user= 'gendgbrlvinqze'
password= '201e8bc25cf5579f911dcd131df0a4b9f01822990a58708937b73814120148a9'
host= 'ec2-50-19-222-129.compute-1.amazonaws.com'

# create db connection
conn = psycopg2.connect(database=dbname, user=user, password=password, host=host)


### IDEA FLOW ###

# Query to show stats result of player

# Then pull from model to show similar players


# Flask request for player name
# Page request should look: www.website.com/player_search?player
@app.route('/player_search', methods = ['POST'])
def search_player():
    # create cursor for player search
    curs_player = conn.cursor()
    # get data
    player = request.args.get('player')
    # (a)send searched player info to webpage
    player_one = "SELECT * FROM player WHERE Player == '" + str(player) + "'"
    player_find = curs_player.execute(player_one).fetchone()
    # close curs_player
    curs_player.close()
    
    # TO DO: Pull class from model to predict other likely players
    # similar_nba = pickle.load(open('similar_model.pkl', 'rb'))
    # longevity_nba = pickle.load(open('longevity_model.pkl', 'rb'))
    # TO DO: sim_players = ML_model_class.predict(player)
    # predict_similar = similar_nba.predict(player)
    # predict_longevity = longevity_nba.predict(player)
    
    # List for predicted player stats
    predict_players = []
    
    # Loop for data search of predicted_players
    for single in sim_players:
        # create cursor for predicted_find
        curs_pred = conn.cursor()
        # query string for db
        pred_query = "SELECT * FROM players WHERE Player='" + str(sim_players[single]) + "'"
        # execute query
        finder = curs_pred.execute(pred_query)
        predict_players.append(finder)
        curs_pred.close()
    return jsonify(results=player_find), jsonify(results=predict_players)

