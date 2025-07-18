
import sqlite3

connect_to_db = sqlite3.connect("Cars.db")

k = connect_to_db.cursor()

k.execute("""
        UPDATE TBCars SET
            name = "sena"
        WHERE   
            id = 103
            """)
print(k.fetchall())

connect_to_db.commit()
connect_to_db.close()
