import sqlite3

connect_to_db = sqlite3.connect("Cars.db")

k = connect_to_db.cursor()

k.execute("""
        create table if not exists TBCars (
            id integer primary key autoincrement,
            name text not null,
            brand text not null,
            model text not null,
            price real not null
        )
        """)