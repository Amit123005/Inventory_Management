import pymysql
import os
from dotenv import load_dotenv
from icecream import ic
from flask import jsonify, request, Flask
import pymysql.cursors

load_dotenv()

def get_db_connection():
    return pymysql.connect(
        host=os.getenv("MYSQL_HOST"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        database=os.getenv("MYSQL_DB"),
        cursorclass=pymysql.cursors.DictCursor
    )

class Inventory:

    # def __init__(self):
    #     self.connection = get_db_connection()
    #     cursor = self.connection()

    def add_item(data):
        ic("Add item API is called")
        try:
            conn = get_db_connection()
            with conn.cursor() as cursor:
                sql = """
                    INSERT INTO items (name, category, quantity)
                    VALUES (%s, %s, %s)
                """
                cursor.execute(sql, (
                    data.get("name"),
                    data.get("category"),
                    data.get("quantity"),
                ))
                conn.commit()

                # Optionally, get the inserted ID
                inserted_id = cursor.lastrowid

            return {
                "status": "success",
                "message": "Item added successfully",
                "item": {
                    "id": inserted_id,
                    "name": data.get("name"),
                    "category": data.get("category"),
                    "quantity": data.get("quantity")
                }
            }

        except Exception as e:
            ic("Database error:", e)
            return {
                "status": "error",
                "message": "Failed to add item",
                "error": str(e)
            }

        finally:
            conn.close()

    def view_item():
        ic("View item API is called")
        try:
            connection = get_db_connection()
            cursor = connection.cursor()
            sql = """select * from items"""
            cursor.execute(sql)
            data = cursor.fetchall()

            return data

        except Exception as e:
            ic("Database error:", e)
            return {
                "status": "error",
                "message": "Failed to add item",
                "error": str(e)
            }

        finally:
            connection.close()