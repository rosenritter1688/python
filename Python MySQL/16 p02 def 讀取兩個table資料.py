'''
Question 2: 
Fetch Hospital and Doctor Information using hospital Id and doctor Id

Implement the functionality to read the details of a given doctor from the doctor table and Hospital from the hospital table. i.e., read records from Hospital and Doctor Table as per given hospital Id and Doctor Id.
'''

import mysql.connector

def get_connection():
    connection = mysql.connector.connect(host='127.0.0.1',
                                         database='python_db',
                                         user='root',
                                         password='Zs8271911c')
    return connection

def close_connection(connection):
    if connection:
        connection.close()

def get_hospital_detail(hospital_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        select_query = """select * from Hospital where Hospital_Id = %s""" ##%s = def argument "hospital_id"
        cursor.execute(select_query, (hospital_id,)) ##def argument (line 21)
        ##LINE 25 and 26 改成只有一行的話如下
        #cursor.execute("""select * from Hospital where Hospital_Id = %s""", (hospital_id,)) ##def argument (line 21)
        records = cursor.fetchall()
        print("Printing Hospital record")
        for row in records:
            print("Hospital Id:", row[0])
            print("Hospital Name:", row[1])
            print("Bed Count:", row[2])
        close_connection(connection)
    except (Exception, mysql.connector.Error) as error:
        print("Error while getting data", error)

def get_doctor_detail(doctor_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        #select_query = """select * from Doctor where Doctor_Id = %s""" #%s = doctor_id  是DEF get_doctor_detail的argument
        #cursor.execute(select_query, (doctor_id,))# def argument (line 39)
        ##LINE 43 and 44 改成只有一行的話如下
        cursor.execute("""select * from Doctor where Doctor_Id = %s""",(doctor_id,))
        records = cursor.fetchall()
        print("Printing Doctor record")
        for row in records:
            print("Doctor Id:", row[0])
            print("Doctor Name:", row[1])
            print("Hospital Id:", row[2])
            print("Joining Date:", row[3])
            print("Specialty:", row[4])
            print("Salary:", row[5])
            print("Experience:", row[6])
        close_connection(connection)
    except (Exception, mysql.connector.Error) as error:
        print("Error while getting data", error)

print("Question 2: Read given hospital and doctor details \n")
get_hospital_detail(2)
print("\n")
get_doctor_detail(105)
