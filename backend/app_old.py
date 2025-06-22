from flask import Flask, request, jsonify
from flask_cors import CORS
from icecream import ic
from dotenv import load_dotenv
import os
import pymysql
import pymysql.cursors

load_dotenv()

app = Flask(__name__)
CORS(app)

def get_db_connection():
    return pymysql.connect(
        host=os.getenv("MYSQL_HOST"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        database=os.getenv("MYSQL_DB"),
        cursorclass=pymysql.cursors.DictCursor
    )

@app.route("/api/",  methods = ['GET'] )
def Home() :
    ic("Inventory API is Running")
    return jsonify("Inventory API is Running")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port =5000, debug=False)