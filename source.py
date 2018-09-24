'''
Created on Aug 27, 2018

@author: NIHAL RAI,HARGOBIND SINGH,MUNISH BHANAWAT
'''
import re
import count
import datetime
import cx_Oracle
import banner
import random
import base64
import pandas as pd
#New Edit Use Oracle or just copy paste the new code
print(80 * "%")
print("")
banner.display()
print(80 * "%")
print("")
con=cx_Oracle.connect("system/123456@XE")
cur=con.cursor()
cur.execute("Select Password from ADMIN")
b=str(cur.fetchall()).strip("[]()'',")
b=base64.b64decode(b)
password=str(b,'utf-8')
menu=[]
cur.execute("Select name from MENU")
data=cur.fetchall()
for i in data:
    i=str(i).strip("(),'")
    menu.append(i)
name=''
df = pd.DataFrame(menu, columns=["menu"])
df.loc[:4, "Prices"] = 7.50
df.loc[4:8, "Prices"] = 50.0
df.loc[8:12, "Prices"] = 120.0
df.loc[12:18, "Prices"] = 200.50
df.loc[18:, "Prices"] = 150.0
df.index += 1
total_bill = 0.0
f = open("Order.txt", "a") # breakfast storage
f.write("")
f.close()

print("Welcome to EATOPIA!")
print ("Here's our menu!")
print (df.to_string(justify='left',
                   header=False,
                   formatters={
                    'Pizzas':'{{:<{}s}}'.format(
                        df['menu'].str.len().max()
                        ).format,
                    'Prices':'     ₹{:.2f}'.format}))
cur.execute("Select MAX(CUSTOMER_ID) from CUSTOMER")
cus_id=int(str(cur.fetchall()).strip("[]()'',"))
name='Guest'
email_id='Guest'
contact='Guest'
class Update:
  def __init__(self, cus_id,name,contact,email_id):
    self.name = name
    self.cus_id = cus_id
    self.contact=contact
    self.email_id=email_id

#New Edit     Validation input
print("Recommended item:")
count.recommend()    
#label: new_order
print(80 * "%")
print("")
print("1. Guest")
print(80 * "-")
print("2. Register")
print(80 * "%")
print("")
user=input(">>>")
if user == '2':
    cus_id=cus_id+1
    print("Enter Customer Name:")
    a=True
    while a == True:
        name=input(">>>")
        if name.isalpha():
            a=False
        else:
            print("Bad Syntax")
    print("Enter Customer contact number:")
    a=True
    while a == True:
        contact=input(">>>")
        if len(contact) == 10:
            a=False
        else:
            print('Bad Syntax')
    print("Enter Customer Email_id:")
    a=True
    while a == True:
        email_id=input(">>>")
        match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$',email_id)
        if match == None:
            print('Bad Syntax')
        else:
            a=False
    p1 = Update(cus_id,name,contact,email_id)
    name="\'"+name+"\'"
    contact="\'"+str(int(contact))+"\'"
    email_id="\'"+email_id+"\'"
# Input Valiadtion end
    stmt="Insert into CUSTOMER values(%s,%s,%s,%s)" % (cus_id,name,contact,email_id)
    print(stmt)
    cur.execute(stmt)
elif user == '1':
    cus_id=cus_id+1
    stmt="Insert into CUSTOMER values(%s,'Guest','Guest1','Guest2')" % (cus_id)
    print(stmt)
    cur.execute(stmt)
    p1 = Update(cus_id,name,contact,email_id)
else:
    pass
cus_id=p1.cus_id
name=p1.name
email_id=p1.email_id
contact=p1.contact
quantity=0
while True:
    print(80 * "%")
    print("")
    print("Input a number and press enter to select an item.")
    print("Input 'done' to finish your order and tabulate your bill.")
    print("Input 'exit' to cancel your orders.")
    print("Input 'admin' for admin privilage.")
    print(80 * "%")
    print("")
    order = input(">>>")
    if order == 'exit':
        break
    elif order == 'done':
        print("Your total bill is ₹{:.2f}.".format(total_bill))
        sssname="\'"+name+"\'"
        total_bill="\'"+str(int(total_bill))+"\'"
        stmt="Insert into BILL values(%s,%s,%s,%s)" % (cus_id,name,cus_id,total_bill)
        cur.execute(stmt)
        #stmt="Insert into SALE_DETAIL values((TO_DATE(sysdate,'YYYY-MM-DD')),%s,%s)" % (cus_id,total_bill)
        #cur.execute(stmt)
        name=name.replace("\'","")
        total_bill=total_bill.replace("\'","")
        #ORDER COMPLETE
        input("Press any key to exit.")
        break
    elif order == 'admin':
        login=input("Password : ")
        repeat=True
        while repeat==True:
            if login == password :
                print("ADMIN PRIVILAGES:")
                print("Update")
                print("Delete")
                print("View")
                print("Profile")
                print("Add in Menu: Add")
                choice=input(">>>")
                if choice == 'Update':
                    print("1 : To update MENU table \n2 : To update MENU_BILL table")
                    choice_1=input(">>>")
                    if choice_1 == 'MENU' :
                        value=input("Enter the menu_id to change : ")
                        new_value=input("Enter the new value to change : ")
                        stmt="Update MENU set name=:1 where menu_id=:2"
                        cur.execute(stmt,(new_value,value))
                        print("Press [R to Repeat and Any other key to exit]")
                        response=input(">>>")
                        if response == 'R' :
                            repeat=True
                        else:
                            print("Press any key to exit. ")
                            break
                    elif choice_1 == 'MENU_BILL' :
                        column_name=input("Enter column name for updation : ")
                        value=input("Enter the value to change : ")
                        pre_value=input("Enter the previous value to change : ")
                        check_contraint=input("Enter the check constraint : ")
                        stmt="Update MENU_BILL set %s=%s where %s=%s" % (column_name,value,pre_value,check_constraint)
                        cur.execute(stmt)
                        print("Press [R to Repeat and Any other key to exit]")
                        response=input(">>>")
                        if response == 'R' :
                            repeat=True
                        else:
                            print("Press any key to exit. ")
                            break
                elif choice == 'Delete':
                    print("To delete from MENU table : MENU")
                    print("To delete from MENU_BILL table : MENU_BILL")
                    print("To delete from CUSTOMER table : CUSTOMER")
                    print("To delete from SALE_DETAIL table : SALE_DETAIL")
                    choice_1=input(">>>")
                    if choice_1 == 'MENU':
                        column_name=input("Enter column name for deletion : ")
                        value=input("Enter the value to change : ")
                        cur.execute("Delete from MENU where :1=:2",(column_name,value))
                        print("Press [R to Repeat and Any other key to exit]")
                        response=input(">>>")
                        if response == 'R' :
                            repeat=True
                        else:
                            print("Press any key to exit. ")
                            break
                    elif choice_1 == 'MENU_BILL':
                        column_name=input("Enter column name for deletion : ")
                        value=input("Enter the value to change : ")
                        cur.execute("Delete from MENU_BILL where :1=:2",(column_name,value))
                        print("Press [R to Repeat and Any other key to exit]")
                        response=input(">>>")
                        if response == 'R' :
                            repeat=True
                        else:
                            print("Press any key to exit. ")
                            break
                    elif choice_1 == 'CUSTOMER':
                        column_name=input("Enter column name for deletion : ")
                        value=input("Enter the value to change : ")
                        cur.execute("Delete from CUSTOMER where :1=:2",(column_name,value))
                        print("Press [R to Repeat and Any other key to exit]")
                        response=input(">>>")
                        if response == 'R' :
                            repeat=True
                        else:
                            print("Press any key to exit. ")
                    elif choice_1 == 'SALE_DETAIL':
                        column_name=input("Enter column name for deletion : ")
                        value=input("Enter the value to change : ")
                        cur.execute("Delete from SALE_DETAIL where %s=%s") % column_name %value
                        print("Press [R to Repeat and Any other key to exit]")
                        response=input(">>>")
                        if response == 'R' :
                            repeat=True
                        else:
                            print("Press any key to exit. ")
                            break
                elif choice == 'View':
                    print("MENU")
                    print("MENU_BILL")
                    print("CUSTOMER")
                    print("SALE_DETAIL")
                    choice_1=input(">>>")
                    if choice_1 == 'MENU':
                        print("Enter Columns name separated by comma!")
                        columns=input(">>>")
                        stmt="Select %s from MENU" % (columns)
                        cur.execute(stmt)
                        data=cur.fetchall()
                        for i in data:
                            print(i)
                        print("Press [R to Repeat and Any other key to exit]")
                        response=input(">>>")
                        if response == 'R' :
                            repeat=True
                        else:
                            print("Press any key to exit. ")
                            break
                    elif choice_1 == 'MENU_BILL':
                        print("Enter Columns name separated by comma!")
                        columns=input(">>>")
                        stmt="Select %s from MENU_BILL" % (columns)
                        cur.execute(stmt)
                        data=cur.fetchall()
                        for i in data:
                            print(i)
                        print("Press [R to Repeat and Any other key to exit]")
                        response=input(">>>")
                        if response == 'R' :
                            repeat=True
                        else:
                            print("Press any key to exit. ")
                            break
                    elif choice_1 == 'CUSTOMER':
                        print("Enter Columns name separated by comma!")
                        columns=input(">>>")
                        stmt="Select %s from CUSTOMER" % (columns)
                        cur.execute(stmt)
                        data=cur.fetchall()
                        for i in data:
                            print(i)
                        print("Press [R to Repeat and Any other key to exit]")
                        response=input(">>>")
                        if response == 'R' :
                            repeat=True
                        else:
                            print("Press any key to exit. ")
                            break
                    elif choice_1 == 'SALE_DETAIL':
                        print("Enter Start Date [YYYY-MM-DD]: ")
                        start_date=input(">>>")
                        print("Enter End Date [YYYY-MM-DD]: ")
                        end_date=input(">>>")
                        data=cur.fetchall()
                        stmt="Select sum(Total_Amount) from SALE_DETAIL"
                        cur.execute(stmt)
                        data=cur.fetchall()
                        data=str(data).strip("[](),''")
                        print("Total Bill till entered date is Rs: "+data)
                        print("Press [R to Repeat and Any other key to exit]")
                        response=input(">>>")
                        if response == 'R' :
                            repeat=True
                        else:
                            print("Press any key to exit. ")
                            break
                elif choice == 'Profile':
                    stmt="Select * from ADMIN"
                    cur.execute(stmt)
                    data=cur.fetchall()
                    for i in data:
                        print(i)
                    print("To change Name of Admin account : Name ")
                    print("To change Password of Admin account : Password ")
                    choice_1=input(">>>")
                    if choice_1 == "Name":
                        cur.execute("Select NAME from ADMIN")
                        pre_name=str(cur.fetchall()).strip("[]()'',")
                        new_name=input("Enter the new name : ")
                        cur.execute("Update ADMIN set Name= :1 where Name= :2 ",(new_name,pre_name))
                        print("Done")
                        print("Press [R to Repeat and Any other key to exit]")
                        response=input(">>>")
                        if response == 'R' :
                            repeat=True
                        else:
                            print("Press any key to exit. ")
                            break
                    elif choice_1 == "Password":
                        cur.execute("Select PASSWORD from ADMIN")
                        old_pass=str(cur.fetchall()).strip("[]()'',")
                        new_pass=input(">>>")
                        a=base64.b64encode(bytes(new_pass, 'utf-8'))
                        a=str(a,'utf-8')
                        cur.execute("Update ADMIN set Password= :1 where Password= :2 ",(a,old_pass))
                        print("Done")
                        print("Press [R to Repeat and Any other key to exit]")
                        response=input(">>>")
                        if response == 'R' :
                            repeat=True
                        else:
                            print("Press any key to exit. ")
                            break
                elif choice == 'Add':
                    cur.execute("SELECT menu_id FROM MENU where MENU_id=(select max(MENU_id) from MENU)")
                    old_cus_id=str(cur.fetchall()).strip("[]()'',")
                    old_cus_id=int(old_cus_id)
                    menu_name=input("Enter the menu name : ")
                    menu_price=input("Enter Price : ")
                    cur.execute("Insert into MENU values(:1,:2,:3)",(old_cus_id+1,menu_name,menu_price))
                    menu+=menu_name
                    df.loc[old_cus_id+1, "Prices"]=menu_price
                    print("Press [R to Repeat and Any other key to exit]")
                    response=input(">>>")
                    if response == 'R' :
                        repeat=True
                    else:
                        print("Press any key to exit. ")
                        break
            else :
                print("Wrong Password.")
                input("Press any key to exit.")
                break
                print("Press [R to Repeat and Any other key to exit]")
                response=input(">>>")
                if response == 'R' :
                    repeat=True
                else:
                    print("Press any key to exit. ")
                    break
                
    elif int(order) in df.index:
#  To count the same order quantity and add it and save in menu_bill table
        reply='y'
        if reply == 'Y' or reply == 'y':
            item_quant=[]
            item = df.loc[int(order), "menu"]     # Get the respective items
            price = df.loc[int(order), "Prices"]
            item_quant.append(item)
            if item in item_quant:
                quantity=quantity+1
            else:
                quantity=1                                # by indexing order input.
            print("You've selected {} {}! That would be ₹{:.2f}.".format(quantity,item, price))
            name="\'"+name+"\'"
            price1="\'"+str(int(price))+"\'"
            stmt="Insert into MENU_BILL values(%s,%s,%s,%s)" % (cus_id,str(name),quantity,price1)
            name=name.replace("\'","")
            print(name)
            cur.execute(stmt)
            total_bill += price
            f = open("Order.txt","a+")
            f.write(item)
            f.write("\n")
            f.close()
            continue
    else:
        input("Press any key to exit.")
        break
con.commit()
#Recommendation
'''try:
    input=open("Order.txt","r")
except IOError:
    print("File doesn't exist.")

print("Scramble Successful")
input.close()
output.close() '''
