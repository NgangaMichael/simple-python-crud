import sqlite3 as lite


# functionality goes here 


# class to manage data base 
class DatabaseManage(object):
    def _init_(self):
        global conn
        try:
            conn = lite.connect('courses.db')
            with conn:
                cur = conn.cursor()
                cur.execute('CREATE TABLE IF NOT EXISTS course(Id INTERGER PRIMARY KEY AUTOINCREMENT, name TEXT, description TEXT, price TEXT, is_private BOOLEAN NOT NULL DEFAULT 1)')
        except Exception:
            print('Unable to connect to DB')

# code for entering data into the db its a class 
# this is basic crud 

def insert_data(self, data):
    
    try:
        with conn:
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO course(name, description, price, is_private) VALUES(?,?,?,?)", data
            )
    except Exception:
        return False

def fetch_data(self):
    
    try:
        with conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM course")
            return cur.fetchall()
    except Exception:
        return False

def delete_data(self, id):
    
    try:
        with conn:
            cur = conn.cursor()
            sql = "DELETE FROM course WHERE id = ?"
            cur.execute(sql, [id])
            
    except Exception:
        False
    

#TODO user interface goes here