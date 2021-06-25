import mysql.connector as connector

class DBEmployer:
    def __init__(self):
        self.con = connector.connect(host='localhost',port='3306',user='root',password='Abhyudaya28',database='employer', auth_plugin='mysql_native_password')

        query='create table if not exists user(EmployerID varchar(100),  First_NAME varchar(50), Last_NAME varchar(50), Email_ID varchar(50), Contact_NO varchar(11))'
        cur = self.con.cursor()
        cur.execute(query)
        print("created")

#insert
    def insert_user(self,EmployerID, FirstNAME, LastNAME, EmailID, ContactNO):
        query="insert into user(EmployerID, First_NAME, Last_NAME, Email_ID ,Contact_NO) Values('{}','{}','{}','{}','{}')".format(EmployerID, FirstNAME, LastNAME, EmailID, ContactNO)
        print(query)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print('DATA IS SAVED TO DB')

    #Fech all
    def fetch_all(self):
        query="select * from user"
        cur=self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("EmployerID :",row[0])
            print("FirstNAME :",row[1])
            print("LastNAME :",row[2])
            print("EmailID :",row[3])
            print("ContectNO :",row[4])
            print()
            print()
    
    #delete user
    def delete_user(self, EmployerID):
        query = f"delete from user where EmployerID = '{EmployerID}'"
        print(query)
        c = self.con.cursor()
        c.execute(query)
        self.con.commit()
        print("DELETE")

    #update

    def update_user(self,EmployerID,newFirstNAME,newLastNAME,newEmailID,newContactNO):
        query="update user set First_NAME='{}',Last_NAME='{}',Email_ID='{}',Contact_NO='{}'".format(newFirstNAME,newLastNAME,newEmailID,newContactNO)
        print(query)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("UPDATE")
        
        