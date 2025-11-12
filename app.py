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
    return "Basketball Table Successfully Created"

@app.route('/db_insert')
def inserting(): 
    conn = psycopg2.connect("postgresql://hello_world_wkh9_user:BULUeupbH97YGIOoiYBn1nxxGaBUIpXy@dpg-d4a2htidbo4c73c3lcd0-a/hello_world_wkh9")
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO Basketball(First, Last, City, Name, Number)
        Values
        ('Jayson', 'Tatum', 'Boston', 'Celtics', 0), 
        ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30), 
        ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15), 
        ('Kawhi', 'Leonard', 'Los Angeles', Clippers', 2); 
        ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Populated"

@app.route('/db_select')
def selecting(): 
    conn = psycopg2.connect("postgresql://hello_world_wkh9_user:BULUeupbH97YGIOoiYBn1nxxGaBUIpXy@dpg-d4a2htidbo4c73c3lcd0-a/hello_world_wkh9")
    cur = conn.cursor()
    cur.execute('''
        SELECT * FROM Basketball; 
    ''')
    records = cur.fetchall()
    conn.close()
    response_string = ""
    response_string += "<table>"
    for player in records: 
        response_string += "<tr>"
        for info in player: 
            response_string += "<td> {} </td>".format(info)
        response_string += "</tr>"
    response_string += "</table>"
    return response_string

@app.route('/db_drop')
def dropping(): 
    conn = psycopg2.connect("postgresql://hello_world_wkh9_user:BULUeupbH97YGIOoiYBn1nxxGaBUIpXy@dpg-d4a2htidbo4c73c3lcd0-a/hello_world_wkh9")
    cur = conn.cursor()
    cur.execute('''
        DROP TABLE Basketball; 
    ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Dropped"


