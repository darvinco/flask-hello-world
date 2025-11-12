import psycopg2

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from -- Darvin Contreras -- in 3308!'

@app.route('/db_test')
def db_test():
    """
    Test route to confirm database connection.
    Connects to the PostgreSQL database and returns a success message.
    """
    conn = psycopg2.connect("postgresql://hello_world_wkh9_user:BULUeupbH97YGIOoiYBn1nxxGaBUIpXy@dpg-d4a2htidbo4c73c3lcd0-a/hello_world_wkh9")
    conn.close()
    return "Database connection successful!"