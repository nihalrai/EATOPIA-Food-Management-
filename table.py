import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",passwd="123456",database="infosys")
cur=con.cursor()
#cur.execute("CREATE TABLE ADMIN(User_Id int NOT NULL PRIMARY KEY,Name varchar(100) NOT NULL,Password varchar(20) NOT NULL)")
cur.execute("CREATE TABLE BILL(Order_Id int ,Customer_Name varchar(100) NOT NULL,Customer_id int NOT NULL,Total_Amount int NOT NULL)")
cur.execute("CREATE TABLE MENU_BILL(Order_Id int NOT NULL,Name varchar(100) NOT NULL,Quantity varchar(20) NOT NULL,Price varchar(20) NOT NULL,FOREIGN KEY(Order_Id) REFERENCES BILL(Order_Id))")
cur.execute("""CREATE TABLE CUSTOMER(
	Customer_Id int NOT NULL PRIMARY KEY,
	Name varchar(100) NOT NULL,
	Contact varchar(20) DEFAULT NULL,
	Email_Id varchar(50) DEFAULT NULL,
)""")
cur.execute("""CREATE TABLE MENU(
	Menu_Id int NOT NULL PRIMARY KEY,
	Name varchar(100) NOT NULL,
	Price varchar(20) NOT NULL,
)""")
#table changed culumns added and removed
cur.execute("""CREATE TABLE SALE_DETAIL(
	Date date NOT NULL,
	id int
	Total_Amount int
)""")
