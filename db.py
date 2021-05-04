import sqlite3


CONN = sqlite3.connect("patient.db")

def getCardiologistList():
        c = CONN.cursor() 
        cardio = c.execute(f''' SELECT * FROM cardiologist''').fetchall()
        list = []
        for row in cardio:
                data = "%s %s %s" % (row[0], row[1], row[2])
                list.append(data)
        print(list)
        CONN.commit()
        CONN.close()
        return list