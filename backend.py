import sqlite3

def connect():
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS routined (Id INTEGER PRIMARY KEY , date text , earnings integer , exercise text , study text , diet text ,python text)")
    conn.commit()
    conn.close()

def insert(date , earnings , exercise , study , diet , python):
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO routined VALUES (NULL , ?,?,?,?,?,?)" , (date , earnings , exercise, study , diet , python))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM routined")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows


def delete(id):
    conn = sqlite3.connect("Routine.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM routined WHERE Id =?",(id, ))
    conn.commit()
    conn.close()


connect()


insert('10','12','10','12','10','12')
insert('10','12','10','12','10','12')
insert('10','12','10','12','10','12')
print(view())