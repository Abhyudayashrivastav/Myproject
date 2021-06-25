import dbemployer as DB
import traceback
import re

def isValid(s):
    return re.match(r'[789]\d{9}$',s) ==None


def main():
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    db=DB.DBEmployer()
    
    while True:
        print("********WELCOME*******")
        print()
        print("PRESS 1 to insert new Employer")
        print("PRESS 2 to display all user")
        print("PRESS 3 to delete  user")
        print("PRESS 4 to update user")
        print("PRESS 5 to exit program")
        print()
        try:
            choice=int(input())
            if (choice==1):
                Employerid = (input("Enter Employer ID:  "))
                FirstNAME = input("Enter FIRST NAME:  ")
                LastNAME = input("Enter LAST NMAE:  ")
                EmailID = input("Enter EMAIL ID:  ")     
                while(re.search(regex, EmailID) == None):
                    print("Invalid Email")
                    EmailID = input("Enter EMAIL ID:  ")
                ContactNO = input("Enter CONTACT NO:  ")
                while isValid(ContactNO):
                    print("Invalid Contact")
                    ContactNO = input("Enter CONTACT NO:  ")
                db.insert_user(Employerid, FirstNAME, LastNAME, EmailID, ContactNO)
                pass
            elif choice ==2:
                db.fetch_all()
                pass
            elif choice ==3:
                Employerid = (input("Enter the EmployerID which you want to delete:"  ))
                db.delete_user(Employerid)
            elif choice ==4:
                Employerid = (input("Enter id of Employer:  "))
                FirstNAME = input("Enter new First name:  ")
                LastNAME = input("Enter new Last name:  ")
                EmailID = input("Enter new Email ID: ")
                ContactNO = input("Enter new Contact NO:  ")
                db.update_user(Employerid, FirstNAME, LastNAME, EmailID, ContactNO,)
            elif choice == 5:
                break
            else:
                print("Invalid input ! Try again")
        except Exception as e:
            traceback.print_exc()
            print("Invalid Details ! Try again") 

if __name__ =="__main__":
    main()




