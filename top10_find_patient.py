import top10_DB
import pymysql

def main():
    # try:
        surname = input("Enter Surname: ")
        print(top10_DB.find_patient(surname))
    # except Exception as e:
    #     print(e, "Failed to find a patient")
        
    
     
        
  
        
    
        
        
        
    
    
    
if __name__ == "__main__":
    main()