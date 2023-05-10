import sqlite3
con = sqlite3.connect("project.db")
cur = con.cursor()
   
# cur.execute("CREATE TABLE input(temperature, rainfall, humidity, nitrogen, phosphorous, potassium, soil pH)")
# cur.execute("INSERT INTO input(temperature, rainfall, humidity, nitrogen, phosphorous, potassium, soil pH) VALUES (?, ?, ?, ?, ?, ?)", 
#             ('temperature', 'rainfall', 'humidity', 'nitrogen', 'phosphorous', 'potassium', 'soil pH'))

cur.execute("CREATE TABLE IF NOT EXISTS data(temperature, rainfall, humidity, nitrogen, phosphorous, potassium, soil pH)")
cur.execute("""
    INSERT INTO data VALUES
        (25, 125, 20, 15, 18, 21, 7),
        (30, 155, 25, 20, 23, 27, 14)
""")

con.commit()

for row in cur.execute('SELECT * FROM data'):
    print(row)


# con.close()



