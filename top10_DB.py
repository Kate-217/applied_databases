import pymysql
import pymysql.cursors

conn = None

def connect():
    global conn
    conn = pymysql.connect(host="localhost", user="root", password="rootroot", db="hospital", cursorclass=pymysql.cursors.DictCursor, autocommit=True)

def add_patient(ppsn, f_name, surname, address, doctor_id):
    if (not conn):
        connect()
        print("Connected")
    query = "INSERT INTO patient_table (ppsn, first_name, surname, address, doctorID) VALUES (%s, %s, %s, %s, %s)"

    with conn:
        cursor = conn.cursor()
        cursor.execute(query,(ppsn, f_name, surname, address, doctor_id))

def find_patient(surname):
    if (not conn):
        connect()
        print("Connected")
    query = "SELECT * FROM patient_table WHERE surname LIKE %s"

    with conn:
        cursor = conn.cursor()
        cursor.execute(query,(surname + "%",))
        return cursor.fetchall()
        
        

        

        
        
        
    
    
