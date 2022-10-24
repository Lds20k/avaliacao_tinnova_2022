import sqlite3
import os
from flask import Flask

import globals
from routes.vehicle_route import vehicle_route


def create_database(test=False):
    if test:
        globals.database = 'test.db'
    else:
        globals.database = 'vehicle.db'
    
    with open("create_tables.sql", 'r') as stream:
        conn = sqlite3.connect(globals.database)
        cursor = conn.cursor()

        table = cursor.execute("""
            SELECT name FROM sqlite_master WHERE type='table' AND name='brand';
        """).fetchall()
        if table:
            print('Tabela "brand" já existe!')
            conn.close()
            return

        table = cursor.execute("""
            SELECT name FROM sqlite_master WHERE type='table' AND name='vehicle';
        """).fetchall()
        if table:
            print('Tabela "vehicle" já existe!')
            conn.close()
            return

        cursor.executescript(stream.read())
        conn.commit()
        conn.close()

def create_app(test=False):
    create_database(test)
    
    app = Flask(__name__)
    app.register_blueprint(vehicle_route)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
