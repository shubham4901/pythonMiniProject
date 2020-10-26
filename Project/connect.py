import sqlite3
class myconnect:
      
      def __init__(self):
            #4 Create and connect to a database named “emp.db”
            self.connection = sqlite3.connect("CIE1/Project/emp.db")
            #5 Create a table named emp
            self.connection.execute(''' create table if not exists emp(
                  id integer primary key AUTOINCREMENT,
                  name text,
                  email text,
                  mobile text,
                  type text,
                  experience integer,
                  salary text
            ) ''')  

      def savetodb(self,ename,eemail,emob,etype,eexp,esalary):
            #6 save the employee details entered by user in DB
            with self.connection:
                  self.connection.execute(
                        "insert into emp(name,email,mobile,type,experience,salary) values(:name,:email,:mobile,:type,:experience,:salary)",
                        {'name': ename, 'email': eemail, 'mobile': emob, 'type': etype, 'experience': eexp, 'salary': esalary})
            self.connection.commit()

      def display(self):
            #7 Display details of those Emails
            empid = input("Enter The Emp Id: ")
            with self.connection:
                  dataEmp = self.connection.execute(
                        'select id,name,email,mobile,type,experience,salary from emp where id=:id', {'id': empid})
                  l = dataEmp.fetchall()
                  print ("=========================================================")
                  print ("Name : " + l[0][1])
                  print ("Email : " + l[0][2])
                  print ("Mobile No : " + l[0][3])
                  print ("Type : " + l[0][4])
                  print ("Experience : ", l[0][5])
                  print ("Salary : ", l[0][6])
                  print ("=========================================================")

      
