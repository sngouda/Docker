from flask import Flask
import mysql.connector
 
app = Flask(__name__)
 
@app.route("/")
def home():
 
    try:
 
        connection = mysql.connector.connect(
            host="mysql-db",
            user="root",
            password="root123",
            database="employees"
        )
 
        cursor = connection.cursor()
 
        cursor.execute("SELECT 'Docker Compose Networking Works Successfully!'")
 
        result = cursor.fetchone()
 
        connection.close()
 
        return result[0]
 
    except Exception as e:
        return str(e)
 
app.run(host="0.0.0.0", port=5000)
