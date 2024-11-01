import mysql.connector as d
import tabulate as t
import datetime
mycon=d.connect(host="localhost",user="root",password="1234",charset="utf8")
crs=mycon.cursor()
crs.execute("create database if not exists Dairy_Product_Shop")
crs.execute("use Dairy_Product_Shop")
mycon.commit()
print("database created succcessfully")
crs.execute("create table if not exists LOGIN(User_id varchar(20) primary key,Passwd varchar(20)not null)")
crs.execute("create table if not exists CUSTOMER(Customer_id int(5) primary key not null,Customer_name varchar(20) not null,Customer_phno varchar(10) unique not null,Customer_email_id varchar(15) not null,Customer_add varchar(20)unique not null,product_purchased varchar(20)not null,date date not null)")
crs.execute("create table if not exists DAIRY_PRODUCTS(Product_id int(5) primary key not null,Product_name varchar(20) not null,Brand_name varchar(20) not null,Quantity int(5),Product_price decimal(8,2) not null, Date_of_exp varchar(15) not null)")
crs.execute("create table if not exists BILL(Bill_id int(5)primary key,Customer_id int(5)not null,product_id int(5),foreign key(Customer_id)references CUSTOMER(Customer_id)on delete cascade on update cascade,foreign key(Product_id)references DAIRY_PRODUCTS(Product_id)on delete cascade on update cascade,Item_qty varchar(5)not null)")
mycon.commit()
print("Table created successfully")


def date():
    x=datetime.datetime.now()
    a=x.strftime('%d')
    b=x.strftime('-%d')
    c=x.strftime('-%Y')
    d=x.strftime('%a')
    f=a+b+c+' | '+d
    return f
date()


def add():
    ans='y'
    while ans=='y':
        print(' '*30,"1.Insert product deatils.")
        print(' '*30,"2.Insert customer details.")
        print(' '*30,"3.Insert bill details")
        print(' '*30,"4.Exit.")
        ch=int(input("Enter your choice:"))
        if ch==1:
            print(''*30,"INSERT PRODUCT DETAILS",''*30)
            p_id=int(input("Enter product id:"))
            p_name=input("Enter product name:")
            p_brand=input("Enter brand name:")
            p_price=float(input("Enter product price:"))
            mfg=input("Enter date of mfg:")
            exp=input("Enter date of exp:")
            crs.execute("insert into Dairy_Products values({},'{}','{}',{},'{}','{}')".format(p_id,p_name,p_brand,p_price,mfg,exp))
            mycon.commit()
            print("Records added successfully")
        elif ch==2:
            print(''*30,"INSERT CUSTOMER DETAILS",''*30)
            c_id=int(input("Enter customer id:"))
            c_name=input("Enter customer name:")
            phno=int(input("Enter customer phno:"))
            em_id=input("Enter email id:")
            add=input("Enter address:")
            purchased_p=input("Enter purchased product:")
            date=input("Enter date:")
            crs.execute("insert into Customer values({},'{}',{},'{}','{}','{}','{}')".format(c_id,c_name,phno,em_id,add,purchased_p,date))
            mycon.commit()
            print("Records added successfully")
        elif ch==3:
            print(''*30,"INSERT BILL DETAILS",''*30)
            b_id=int(input("Enter Bill id:"))
            c_id=int(input("Enter Customer id:"))
            p_id=int(input("Enter Product id:"))
            qty=input("Enter quantity:")
            crs.execute("insert into Bill values({},{},{},'{}')".format(b_id,c_id,p_id,qty))
            mycon.commit()
            print("Records added successfully")
        elif ch==4:
            print("You choose to exit")
            exit()
        else:
            print("!!!INVALID CHOICE!!!")
            ans=input("Want to enter more records?(y/n):")

    
def display():
        print(' '*38,'DISPLAY  MENU',' '*38,)
        print(' '*30,'1)DISPLAY CUSTOMER',' '*30,)
        print(' '*30,'2)DISPLAY DAIRY_PRODUCTS',' '*30,)
        print(' '*30,'3)DISPLAY BILL ',' '*30)
        print(' '*30,'4)Exit',' '*30,)
        ch=int(input("ENTER YOUR CHOICE:"))
        if ch==1:
            print()
            a="select*from Customer "
            crs.execute(a)
            data=crs.fetchall()
            if data is None:
                print("No records Available!!!!!!!")
            else:
               a="select  * from Customer"
               crs.execute(a)
               data=crs.fetchall()
               print("HERE ARE THE CUSTOMER RECORDS")
               g=['Customer_id','Customer_name','Customer_phno','Customer_email_id','Customer_add']
               print(t.tabulate(data,headers=g,tablefmt="psql"))   
        elif ch==2:
            crs.execute("select* from DAIRY_PRODUCTS")
            data=crs.fetchall()
            if data is None:
                print("No records Available!!!!!!!")
            else:
              crs.execute("select* from DAIRY_PRODUCTS")
              data=crs.fetchall()
              print("HERE ARE THE DAIRY_PRODUCTS")
              hep=['Product_id','Product_name','Brand_name','Product_price','Date_of_mfg','Date_of exp']
              print(t.tabulate(data,headers=hep,tablefmt="psql"))
        elif ch==3:
            crs.execute("select* from BILL")
            data=crs.fetchall()
            if data is None:
                print("No records Available!!!!!!!")
            else:
               crs.execute("select* from BILL")
               data=crs.fetchall()
               print("HERE ARE THE BILL RECORDS")
               hep=['Bill_id','Customer_id','Product_id','product_qty','Product_price','Total_amt']
               print(t.tabulate(data,headers=hep,tablefmt="psql"))
        elif ch==4:
            print("you choose to exit")
            exit()

def delete():
    print(' '*25,"Select Table to delete records")
    print(' '*30,"1. Customer")
    print(' '*30,"2. Products")
    print(' '*30,"3. Bill")
    ch=int(input("Enter your choice:"))
    if ch==1:
        print(' '*70,"YOU CHOOSE TO DELETE CUSTOMER RECORDS")
        print("What do you want to delete")
        print("")
        a=input("Enter customer id to Delete:")
        crs.execute("Select Customer_id from Customer where Customer_id='{}'".format(a))
        r=crs.fetchone()
        if r!=None:
            crs.execute("delete from Customer where Customer_id='{}'".format(a))
            mycon.commit()
            print("Records deleted Successfully!")
        else:
            print("Invalid Choices!!!")
    elif ch==2:
        print(' '*70,"YOU CHOOSE TO DELETE PRODUCT RECORDS")
        print("Enter product id you want to delete records of")
        print()
        a=input("Enter Product id to Delete:")
        crs.execute("Select Product_id from Dairy_Products where Product_id='{}'".format(a))
        r=crs.fetchone()
        if r!=None:
            crs.execute ("delete from Dairy_Products where Product_id='{}'".format(a))
            mycon.commit()
            print("Successfully deleted records!")
        else:
            print("Invalid Choices!!!")
    elif ch==3:
         print("Enter bill id you wnt to delete")
         print()
         a=input("Enter bill id to Delete:")
         crs.execute("Select Bill_id from bill where BILL_id='{}'".format(a))
         r=crs.fetchone()
         if r!=None:
             crs.execute ("delete from BILL where Bill_id='{}'".format(a))
             mycon.commit()
             print("Successfully deleted records!")
         else:
             print("Invalid Choices!!!")
             ans=input("want to delete more records...")

            
def update():
        print('='*70,'UPDATION MENU','='*70)
        print(' '*30,"1)UPDATE CUSTOMER ",' '*30)
        print(' '*30,"2)UPDATE DAIRY_PRODUCTS ",' '*30)
        print(' '*30,"3)UPDATE BILL ",' '*30)
        print(' '*30,"4)EXIT",' '*30)
        ch=int(input("ENTER YOUR CHOICE:"))
        if ch==1:
            print(' '*40,"You have selected to Update Customer ",' '*40)
            print("What do you want to update")
            print("1)Customer_phno")
            print("2)Customer_add")
            print("3)EXIT")
            ch=int(input("Enter your choice :"))
            if ch==1:
                CS=input("Enter Customer_id:")
                crs.execute("select Customer_id from CUSTOMER where Customer_id='{}'".format(CS))
                f=crs.fetchone()
                if f is None:
                    print("WRONG ENTRY")
                else:
                    n=int(input("Enter NEW customer_phno :"))
                    crs.execute("update CUSTOMER set Customer_phno='{}' where Customer_id='{}' ".format(n,CS))
                    mycon.commit()
                    print("Updation successfully")
            elif ch==2:
                CS=input("Enter Customer id:")
                crs.execute("Select Customer_id from CUSTOMER where Customer_id='{}'".format(CS))
                data=crs.fetchone()
                if data is None:
                    print("No such customer id exist")
                else:
                    n=input("Enter NEW Customer_add:")
                    a="update CUSTOMER set Customer_add='{}'where Customer_id='{}'".format(n,CS)
                    crs.execute(a)
                    mycon.commit()
                    print("Updation successsfully")
                    crs.execute('select*from CUSTOMER where Customer_id="{}"'.format(cs))
                    data=crs.fetchall()
                    g=['Customer_id','Customer_name','Customer_phno','Customer_email_id','Customer_add','Product_purchased','date']
                    print(t.tabulate(data,headers=g,tablefmt='psql'))
            elif ch==3:
                print("You choose to exit")
            else:
                print("!!!INVALID CHOICES!!!")
            
        elif ch==2:
            print(' '*65,"You have selected to Update Dairy_Products ",' '*65)
            print("What do you want to update")
            print("1)Product's price")
            print("2)Brand name")
            print("3)EXIT")
            ch=int(input("Enter your choice:"))
            if ch==1:
                cs=input("Enter Product id in which you want to update:")
                crs.execute("select Product_id  from dairy_products where Product_id='{}'".format(cs))
                data=crs.fetchone()
                if data is None:
                    print("No such product is exist")
                else:
                   n=input("Enter NEW Product price :")
                   a="update Dairy_products set Product_price ='{}'where Product_id ='{}'".format(n,cs)
                   crs.execute(a)
                   mycon.commit()
                   print("Updation successfull")
                   f=crs.fetchall()
                   g=['Product_id','Product_name','Brand_name','Quantity','Product_price']
                   print(t.tabulate(data,headers=g,tablefmt='psql'))
            elif ch==2:
                cs=input("Enter product id in which you want to update:")
                crs.execute("select Product_id from dairy_products where Product_id='{}'".format(cs))
                data=crs.fetchone()
                if data is None:
                    print("No such product id exists")
                else:
                   n=input("Enter NEW Brand name:")
                   a='Update dairy_products set Brand_name="{}"where Product_id="{}"'.format(n,cs)
                   crs.execute(a)
                   mycon.commit()
                   print("Updation successfully")
                   crs.execute('select*dairy_products where Product_id="{}"'.format(cs))
                   data=crs.fetchall()
                   g=['Product_id','Product_name','Brand_name','Quantity','Product_price']
                   print(t.tabulate(data,headers=g,tablefmt='psql'))
            

def search():
    try:
        print(' '*38,'SEARCH MENU',' '*38)
        print(' '*30,'1)SEARCH CUSTOMER',' '*30)
        print(' '*30,'2)SEARCH DAIRY_PRODUCTS',' '*30)
        print(' '*30,'3)SEARCH BILL ',' '*30)
        print(' '*30,'4)EXIT',' '*30)
        ch=int(input("ENTER YOUR CHOICE:"))
        if ch==1:
            print("You Choose to SEARCH FOR CUSTOMER RECORDS")
            N=int(input("ENTER CUSTOMER_ID:"))
            crs.execute("select*from Customer where Customer_id='{}'".format(N))
            data=crs.fetchone()
            if data is None:
                print("No records found!!!!!!")
            else:
              crs.execute("select*from Customer where Customer_id='{}'".format(N))
              data=crs.fetchall()
              hep=['Customer_id','Customer_name','Customer_phno','Customer_add','Product_purchased','Date']
              print(t.tabulate(data,headers=hep,tablefmt="psql"))
        elif ch==2:
              print("YOU CHOOSE TO SEARCH FOR DAIRY_PRODUCTS RECORDS ")
              N=input("ENTER PRODUCT_ID:")
              crs.execute("select* from Dairy_products WHERE Product_id='{}'".format(N))
              data=crs.fetchone()
              if data is None:
                  print("No records are available")
              else:
                  crs.execute("select* from Dairy_products WHERE Product_id='{}'".format(N))
                  data=crs.fetchall()
                  hep=['Product_id','Product_name','Brand_name','Product_price','Date_of_mfg','Date_of_exp']
                  print(t.tabulate(data,headers=hep,tablefmt="psql"))
        elif ch==3:
             print("YOU CHOSE TO SEARCH FOR BILL RECORDS")
             N=input("ENTER BILL_ID:")
             crs.execute("select* from bill where bill_id='{}'".format(N))
             data=crs.fetchone()
             if data is None:
                 print("No records are available")
             else:
                 crs.execute("select* from bill where bill_id='{}'".format(N))
                 data=crs.fetchall()
                 hep=['Bill_id','Customer_id','Product_id','Product_price','Product_amt','Total_amt']
                 print(t.tabulate(data,headers=hep,tablefmt="psql"))
        elif ch==4:
            print("you choose to exit")
            exit()
    except:
        print("")


def bill():
    print("DAIRY PRODUCT SHOP")
    print("--------------------------BILL-------------------------------")
    print("")
    a=input("Enter bill id :")
    b=input("Enter customer id :")
    crs.execute("select bill_id,Customer_name,Product_name,Qunatity,Product_price,Qunatity*Product_price as 'Total amount' from  dairy_products p , customer c, bill b where b.bill_id='{}' and c.Customer_id='{}'and b.Product_id=p.Product_id and b.Customer_id=c.Customer_id ".format(a,b))
    data=crs.fetchall()
    if data!=0:
        for row in data:
                print('-'*158)
                print()
                print(' '*78,'DAIRY PRODUCT SHOP',' '*78)
                from time import gmtime,strftime
                a=strftime("%d %b %Y",gmtime())
                c=strftime("%a ",gmtime())
                print(''*45,'Date : ',a)
                print('BILL ID:',row [0])
                print('CUSTOMER NAME : ',row [1])
                print('PRODUCT NAME: ',row [2])
                print('PRODUCT QTY :',row [3])
                print('PRODUCT PRICE:',row [4])
                print('TOTAL AMOUNT: ',row [5],'rs')
                print('-'*158) 
                  
                   
def login():
    print()
    print("*"*24,"SHREE VAISHNAV KANYA VIDHYALAYA","*"*23)
    print("="*80)
    print("*"*23,"DAIRY PRODUCTS MANAGEMENT SYSTEM","*"*23)
    print("="*80)
    print("*"*30,"ALL STAR DAIRY","*"*32)
    print("="*80)
    print("*"*18,"DESIGNED AND MNAGEMENT BY DIVYANSHI CHOUHAN","*"*17)
    print("="*80)
    print("*"*37,"MENU","*"*37)
    print(" "*120,date())
    print(" "*45,"1.REGISTER")
    print(" "*45,"2.LOGIN" )
    print()
    a=int(input("Enter your choice:"))
    if a==1:
        user_id=input("Enter user id:")
        passwd=input("Enter password:")
        crs.execute("insert into LOGIN values('{}','{}')".format(user_id,str(passwd)))
        mycon.commit()
        print("Registered Successfully")
    elif a==2:
        c=input("Enter user id:")
        p=input("Enter password:")
        crs.execute("select User_id from LOGIN where User_id='{}' and Passwd='{}'".format(c,p))
        a=crs.fetchone()
        if a is None:
            print("Invalid user id or password")
        else:
            print("logged in successfully.")
            menu()
         
    
def menu():
    while True:
        print()
        print("*"*90)
        print(" "*35,"MAIN MENU")
        print(" "*71,date())
        print(" "*34,"1.Insert")
        print(" "*34,"2.Display")
        print(" "*34,"3.Delete")
        print(" "*34,"4.Update")
        print(" "*34,"5.Search")
        print(" "*34,"6.Bill")
        print(" "*34,"7.Exit")
        print("*"*90)
        print()
        ch=int(input("Enter your choice:"))
        if ch==1:
            add()
        elif ch==2:
           display()
        elif ch==3:
           delete()
        elif ch==4:
           update()
        elif ch==5:
           search()
        elif ch==6:
           bill()
        elif ch==7:
           break
        else:
            print("!!!INVALID CHOICE!!!")


login()
menu()
