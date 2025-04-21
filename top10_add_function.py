import top10_DB
import pymysql

def main():
    try:
        ppsn = input("Enter ppsn: ")
        f_name = input("Enter first name: ")
        surname = input("Enter surname: ")
        address = input("Enter address: ")
        doctor_id = input("Enter doctor_id: ")
        top10_DB.add_patient(ppsn, f_name, surname, address, doctor_id)
    except pymysql.err.IntegrityError as e:
        print(e, "Invalid doctor ID or PPSN already exists")
    except pymysql.err.DataError as e:
        print(e, "Insert valid Doctor ID")
        
    
        
        
        
    
    
    
if __name__ == "__main__":
    main()