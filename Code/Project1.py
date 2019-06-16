from flask import Flask, jsonify, request, url_for, json
from flask_cors import CORS
from flask_socketio import SocketIO

# Custom imports
from database.DP1Database import Database

# status verkiezingen
is_published = False

# Start app 
app = Flask(__name__)
CORS(app)
socketio = SocketIO(app)

conn = Database(app=app, user='mct', password='mct', db='badgesystem')

# Custom endpoint
endpoint = '/api/v1'

@app.route(endpoint + '/werknemer', methods=['GET'])
def get_data():
    if (request.method == 'GET'):
        try:
            werknemer_data = conn.get_data('SELECT voornaam, naam FROM badgesystem.werknemer;')
            print(jsonify(werknemer_data))
            return jsonify(werknemer_data), 200
        except Exception as e:
            return jsonify(e), 500

#werkt nog niet, nog eens bekijken
@app.route(endpoint + '/aanhetwerk', methods=['GET'])
def get_aan_het_werk():
    if (request.method == 'GET'):
        try:
            werknemer_data = conn.get_data('SELECT * from badgesystem.gemeente')
            print(jsonify(werknemer_data))
            return jsonify(werknemer_data), 200
        except Exception as e:
            return jsonify(e), 500

@app.route(endpoint + '/allewerknemers', methods=['GET'])
def get_werkend():
    if (request.method == 'GET'):
        try:
            allewerknemes_data = conn.get_data('SELECT * FROM badgesystem.werknemer;')
            print(jsonify(allewerknemes_data))
            return jsonify(allewerknemes_data), 200
        except Exception as e:
            return jsonify(e), 500

@app.route(endpoint + '/addwerknemer', methods=['POST'])
def add_wernemer():
    if (request.method == 'POST'):
        try:
            werknemer_data = request.get_json()
            BadgeID = werknemer_data['BadgeID']
            voornaam = werknemer_data['Voornaam']
            naam = werknemer_data['Naam']
            adres = werknemer_data['StraatEnNummer']
            geboortedatum = werknemer_data['Geboortedatum']
            postcode = werknemer_data['PostcodeID']
            werknemer = conn.set_data('INSERT INTO badgesystem.werknemer (BadgeID, Voornaam, Naam, StraatEnNummer, Geboortedatum, PostcodeID) VALUES ({0},{1} , {2},{3} ,{4} ,{5});').format(BadgeID, voornaam, naam,adres, geboortedatum, postcode)
            return jsonify(werknemer), 201
        except:
            print(Exception)
            return 'Er ging iets mis', 500

# Start app
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)