import sqlite3

connect_to_db = sqlite3.connect("Cars.db")

k = connect_to_db.cursor()

k.execute("""
    INSERT OR IGNORE INTO TBCars (
        id,
        name,
        brand,
        model,
        price
    ) 
    VALUES
        ('101', 'Subaru Brz', 'Subaru', 'Carbon', 1000),
        ('102', 'Nisan s15', 'Nisan', 'Carbon', 2000),
        ('103', 'GT 3', 'Porsche', 'Carbon', 3000)
""")


connect_to_db.commit()
connect_to_db.close()
