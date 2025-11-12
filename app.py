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

@app.route('/db_create')
def db_create(): 
    """ Creating a table in the database """
    conn = psycopg2.connect("postgresql://hello_world_wkh9_user:BULUeupbH97YGIOoiYBn1nxxGaBUIpXy@dpg-d4a2htidbo4c73c3lcd0-a/hello_world_wkh9")
    """ Create a connection cursor that will allow us to execute SQL statements from inside of route """
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Basektball(
            First varchar(255), 
            Last varchar(255), 
            City varchar(255), 
            Name varchar(255), 
            Number int
            ); 
    ''')
    conn.commit()
    conn.close()
    return "Table created successfully!"
