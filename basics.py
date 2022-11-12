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
                return True
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
            return True

        except Exception:
            False
    

#TODO user interface goes here

def main():
    print("*"*40)
    print("\n:: COURSE MANAGEMENT ::\n")
    print("*"*40)
    print("\n")

    db = DatabaseManage()

    print("#"*40)
    print("\n :: USER MANUAL :: \n")
    print("#"*40)

    print("\n1. INSERT A NEW COURSE\n")
    print("2. SHOW ALL COURSES\n")
    print("3. DELETE A COURSE\n")
    print("#"*40)
    print("\n")

    choice = input("\n Enter a choice:")

    if choice == "1":
        name = input("\n Enter course name: ")
        description = input("\n Enter course description: ")
        price = input("\n Enter course price: ")
        private = input("\n is this course private (0/1): ")

        if db.insert_data([name, description, price, private]):
            print('Course was inserted succesfully')
        else:
            print('Something went wrong')
    
    elif choice == '2':
        print("\n Course LIst")

        for index, item in (db.fetch_data()):
            print("\n Sl no : " + str(index + 1))
            print("Course ID : " + str(item[0]))
            print("Course name : " + str(item[1]))
            print("Course description : " + str(item[2]))
            print("Course price : " + str(item[3]))
            private = "Yes" if item[4] else "No"
            print("Is private : " + private)
            print("\n")
    elif choice == "3":
        record_id = input('Enter the course ID: ')
        if db.delete_data(record_id):
            print("Course was deleted succesfully")
        else :
            print("Something went wrong")
    
    else :
        print("\n Bad choice")

# how you run your app 
if __name__ == '__main__':
    main()
