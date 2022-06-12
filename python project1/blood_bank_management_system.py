import os
import pymysql
import random as r
host = os.getenv('#MYSQL_HOST')
conn = pymysql.connect(
host=host,
port=int(3306),
user="root",
passwd="dhivya",
database="dhivya",
charset='utf8mb4')
print(conn)
cursor=conn.cursor()

#a="drop table Stack;"
#cursor.execute(a)
#a="drop table Inventory;"
#cursor.execute(a)
#a="drop table Blooddonor;"
#cursor.execute(a)
#a="drop table Receiver;"
#cursor.execute(a)
#a="drop table Camp;"
#cursor.execute(a)
#a="drop table Waiting;"
#cursor.execute(a)


q1="create table Blooddonor(ID integer(11) primary key,Name varchar(30),Gender varchar(10),Address varchar(50),Date date,BloodGroup varchar(10),Qty integer(11));"
cursor.execute(q1)
print('blooddonor')
q2="create table Inventory(BloodGroup varchar(10),Qty integer(11),BlooddonorID integer(11),foreign key(BlooddonorID) references Blooddonor(ID));"
cursor.execute(q2)
print('Inventory')
q3="create table Stack( BloodGroupID integer(11) primary key,BloodGroup varchar(30),Qty integer(11));"
cursor.execute(q3)
print('Stack')
q4="create table Receiver(ReceiverID integer(10) primary key,Date date,Name varchar(30),Gender varchar(10),BloodGroup varchar(10),Contact varchar(20),DoctorName varchar(30),Amount integer(20),Qty integer(11));"
cursor.execute(q4)
print('receiver')
q5="create table Camp(CampID integer(10) primary key,Date varchar(10),Location varchar(90));"
cursor.execute(q5)
print('camp')
q6="create table Waiting( WaiterID integer(10) primary key,Date date,Name varchar(30),Gender varchar(10),BloodGroup varchar(10),Contact varchar(20),DoctorName varchar(30),Qty integer(11));"
cursor.execute(q6)
print('waiting')




#b='truncate table Inventory;'
#cursor.execute(b)
a='insert into Stack values(%s,%s,%s);'
a1=(1,'A+',0)
cursor.execute(a,a1)
a='insert into Stack values(%s,%s,%s);'
a1=(2,'A-',0)
cursor.execute(a,a1)
a='insert into Stack values(%s,%s,%s);'
a1=(3,'B+',0)
cursor.execute(a,a1)
a='insert into Stack values(%s,%s,%s);'
a1=(4,'B-',0)
cursor.execute(a,a1)
a='insert into Stack values(%s,%s,%s);'
a1=(5,'O+',0)
cursor.execute(a,a1)
a='insert into Stack values(%s,%s,%s);'
a1=(6,'O-',0)
cursor.execute(a,a1)
a='insert into Stack values(%s,%s,%s);'
a1=(7,'AB+',0)
cursor.execute(a,a1)
a='insert into Stack values(%s,%s,%s);'
a1=(8,'AB-',0)
cursor.execute(a,a1)
conn.commit()


q='insert into Camp values(%s,%s,%s);'
a=(111,"20-05-2021","GTN Arts College,Dindigul")
b=(112,"01-06-2021","Kongu Engineering College,Perundurai")
c=(113,"20-06-2021","Krishnammal Arts College,Coimbatore")
cursor.execute(q,a)
cursor.execute(q,b)
cursor.execute(q,c)
conn.commit()


from datetime import date
print(" ***********************************")
print(" ==========DC BLOOD BANK 🩸🩸🩸======")
print(" ***********************************")

x=True
try:
    while x:
            print('\n')
            print('===1-Donate Blood====')
            print('===2-Recieve Blood===')
            print('===3-To check available blood===')
            print('===4-Total availability===')
            print('===5-Blood camp details===')
            print("===6-Blood needy's Queue===")
            print('===7-Quit===')
            c=int(input('Your Choice?'))
            if c==1:
                id1=int(input('Aadhar no?-'))
                name=input('Name?-')
                gender=input('Gender?-')
                address=input('Address?-')
                #date=input('Date?-')
                date=date.today()
                bgroup=input('BloodGroup?-')
                q1='insert into Blooddonor values(%s,%s,%s,%s,%s,%s,%s);'
                a=(id1,name,gender,address,date,bgroup,1)
                cursor.execute(q1,a)
                q2='select Qty from Stack where BloodGroup=%s;'
                q21=(bgroup,)
                cursor.execute(q2,q21)
                for i in cursor:
                    q=i[0]
                q=q+1
                q3='update Stack set Qty=%s where BloodGroup=%s;'
                q31=(q,bgroup)
                cursor.execute(q3,q31)
                q4='insert into Inventory values(%s,%s,%s);'
                q41=(bgroup,1,id1)
                cursor.execute(q4,q41)
            if c==2:
                id1=int(input('Aadhar no?-'))
                #date=input('Date?-')
                date=date.today()
                name=input('Name?-')
                gender=input('Gender?-')
                bgroup=input('BloodGroup?-')
                con=int(input('Phone no?-'))
                d_name=input('Doctor name?-')
                Qty=int(input('Quantity(Unit)?-'))
                q1='select Qty from Stack where BloodGroup=%s;'
                q11=(bgroup,)
                cursor.execute(q1,q11)
                for i in cursor:
                    q=i[0]
                if(q>=Qty):
                    print('\nREQUIRED BLOODGROUP AVAILABLE😊😊')
                    print('-------------------------------------')
                    amount=Qty*1000
                    print('Amount-',amount)
                    q2='insert into Receiver values(%s,%s,%s,%s,%s,%s,%s,%s,%s);'
                    q21=(id1,date,name,gender,bgroup,con,d_name,amount,Qty)
                    cursor.execute(q2,q21)
                    q=q-Qty
                    q3='update Stack set Qty=%s where BloodGroup=%s;'
                    q31=(q,bgroup)
                    cursor.execute(q3,q31)
                else:
                    print('\nREQUIRED BLOODGROUP OR QUANTITY NOT AVAILABLE😥😥')
                    print('-----------------------------------------------------')
                    print('\nYOU WILL BE ADDED TO WAITING LIST😊')
                    print('--------------------------------------')
                    q4='insert into Waiting values(%s,%s,%s,%s,%s,%s,%s,%s);'
                    q41=(id1,date,name,gender,bgroup,con,d_name,Qty)
                    cursor.execute(q4,q41)
            if c==3:
                bgroup=input('BloodGroup?-')
                Qty=int(input('Quantity(Unit)?-'))
                q1='select Qty from Stack where BloodGroup=%s;'
                q11=(bgroup,)
                cursor.execute(q1,q11)
                for i in cursor:
                    q=i[0]
                if(q>=Qty):
                    print('\nREQUIRED BLOODGROUP AND QUANTITY AVAILABLE👍')
                    print('-----------------------------------------------')
                elif(q==0):
                    print('\nREQUIRED BLOODGROUP NOT AVAILABLE😐')
                    print('---------------------------------------')
                elif(q<Qty):
                    print('\nREQUIRED BLOODGROUP AVAILABLE BUT QUANTITY IS LESSER THAN 👉 REQUIREMENT')
                    print('----------------------------------------------------------------------------')
                    print('AVAILABLE QUANTITY-',q,'Units')
            if c==4:
                q1='select * from Stack;'
                cursor.execute(q1)
                for i in cursor:
                    print('BloodGroup=',i[1],'🩸, Quantity(Units)=',i[2])
            if c==5:
                q1='select * from Camp;'
                cursor.execute(q1)
                print('\nBLOOD CAMP DETAILS')
                print('--------------------')
                for i in cursor:
                    print('\nCampID=',i[0],', Date=',i[1],', Location=',i[2])
            if c==6:
                q1='select * from Waiting;'
                cursor.execute(q1)
                for i in cursor:
                    #print('----------------------------------------')
                    print('\nWaiterID=',i[0],',Name=',i[2],',Gender=',i[3],',BloodGroup=',i[4],'🩸, Contact No=',i[5],',Quantity=',i[7],'units')
            if c==7:
                x=False
            conn.commit()
except Exception as e:
        print("The following exception is happened",e)