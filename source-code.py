import pymysql
import sys
import time
from tabulate import tabulate
#Commands for creation of tables
#Database creation
db = pymysql.connect(host="localhost",user="flower",password="lily")
cur=db.cursor()
cur.execute("drop DATABASE PetShop")
cur.execute("CREATE DATABASE PetShop")
def sp(s): #For giving effect of slow printing
    for i in s + '\n':
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(1./50)
def sp2(s): #For giving effect of slow printing
    for i in s + '\n':
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(1./5)


#Creation of Employee List
db=pymysql.connect(host='localhost',user="flower",password="lily",db="PetShop")
cur=db.cursor()
cur.execute("Create table EmployeeList(EmployeeID int(5),Name varchar(20),Position varchar(20),DateJoined varchar(30),Salary int(9));")
cur.execute("insert into EmployeeList values( 901 , ' Shikha Sharma ' , 'Veterinarian ' , ' 2018-09-13 ' , 1000000 );")
cur.execute("insert into EmployeeList values( 902 , ' Rakesh Sharma ' , 'Veterinarian ' , ' 2017-07-23 ' , 800000 );")
cur.execute("insert into EmployeeList values( 903 , ' Rtik Chaudhary ' , 'Cashier ' , ' 2020-12-28 ' , 500000 );")
cur.execute("insert into EmployeeList values( 904 , ' Richa Arora ' , ' Cashier' , ' 2019-12-08 ' , 500000 );")
cur.execute("insert into EmployeeList values( 905 , ' Rajat Kohli ' , ' Pet Trainer ' , ' 2019-06-19 ' , 700000 );")
cur.execute("insert into EmployeeList values( 906 , ' Raman Singh ' , ' Pet Trainer ' , ' 2018-04-13 ' , 900000 );")
cur.execute("insert into EmployeeList values( 907 , ' Jitesh Kumar ' , 'Technician ' , ' 2020-09-19 ' , 400000 );")
cur.execute("insert into EmployeeList values( 908 , ' Nehal Chopra ' , 'Technician ' , ' 2019-06-20 ' , 350000 );")
cur.execute("insert into EmployeeList values( 909 , ' Manan Singh ' , ' Helper' , ' 2018-06-19 ' , 300000 );")
cur.execute("insert into EmployeeList values( 910 , ' Dinesh Kumar ' , 'Helper ' , ' 2019-12-19 ' , 300000 );")
cur.execute("insert into EmployeeList values( 911 , ' Mohan Singh ' , ' PetGroomer ' , ' 2019-06-30 ' , 250000 );")
cur.execute("insert into EmployeeList values( 912 , ' Mrinal Kapoor ' , ' PetGroomer ' , ' 2019-07-31 ' , 250000 );")
cur.execute("insert into EmployeeList values( 913 , ' Megha Verma ' , ' PetGroomer ' , ' 2022-06-18 ' , 225000 );")
cur.execute("insert into EmployeeList values( 914 , ' Minakshi Ghose ' , ' PetGroomer ' , ' 2023-01-11 ' , 225000 );")
cur.execute("insert into EmployeeList values( 915 , ' Gautam Sharma ' , 'Sweeper ' , ' 2019-12-08 ' , 200000 );")
cur.execute("insert into EmployeeList values( 916 , ' Naveen Kumar Singh ' ,' Sweeper ' , ' 2018-07-21 ' , 200000 );")
cur.execute("insert into EmployeeList values( 917 , ' Kapil Verma ' , 'Sweeper ' , ' 2020-12-28 ' , 225000 );")
cur.execute("insert into EmployeeList values( 918 , ' Saurav Pandey ' , 'Sweeper ' , ' 2019-12-08 ' , 225000 );")
db.commit()
#Creation of profit
cur.execute("Create table Profit(Month varchar(20),Total_Expenditure int(20),Total_Earnings int(20),Net_Profit int(10));")
cur.execute("insert into profit values( ' May(2022) ' , 2000000 , 2350000 ,350000 );")
cur.execute("insert into profit values( ' June(2022) ' , 2200000 , 2850000 ,650000 );")
cur.execute("insert into profit values( ' July(2022) ' , 2200000 , 2850000 ,650000 );")
cur.execute("insert into profit values( ' August(2022) ' , 2300000 , 2450000 ,150000 );")
cur.execute("insert into profit values( ' September(2022) ' , 2500000 ,2850000 , 350000 );")
cur.execute("insert into profit values( ' October(2022) ' , 2500000 , 2850000 ,350000 );")
cur.execute("insert into profit values( ' November(2022) ' , 2550000 ,2850000 , 300000 );")
cur.execute("insert into profit values( ' December(2022) ' , 2550000 ,2850000 , 300000 );")
cur.execute("insert into profit values( ' January(2023) ' , 3000000 , 3500000 ,500000 );")
cur.execute("insert into profit values( ' February(2023) ' , 3100000 ,3660000 , 560000 );")
cur.execute("insert into profit values( ' March(2023) ' , 3100000 , 3700000 ,600000 );")
cur.execute("insert into profit values( ' April(2023) ' , 3200000 , 4000000 ,800000 );")
db.commit()
#DIVIDER
#Command of creation of tables(Staff)
#creation of Available pets
db=pymysql.connect(host='localhost',user="flower",password="lily",db="PetShop")
cur=db.cursor()
cur.execute("Create table AvailablePets(PetID int(7),PetType varchar(20),PetBreed varchar(40),Age varchar(30),Price int(9));")
cur.execute("insert into AvailablePets values( 101 , ' Dog ' , ' Golden Retriever ' , ' 4 months ', 20000 );")
cur.execute("insert into AvailablePets values( 102 , ' Dog ' , ' GermanShepherd ' , ' 6 months ', 45000 );")
cur.execute("insert into AvailablePets values( 103 , ' Dog ' , ' American Bully' , ' 2 months ', 52000 );")
cur.execute("insert into AvailablePets values( 104 , ' Cat ' , ' Birman ' , ' 4months ' ,17000 );")
cur.execute("insert into AvailablePets values( 105 , ' Cat ' , ' Korat ' , ' 3months ', 55000 );")
cur.execute("insert into AvailablePets values( 106 , ' Cat ' , ' Persian ' , ' 7months ', 25000 );")
cur.execute("insert into AvailablePets values( 107 , ' Canary ' , ' Harz Roller ', ' 2 months ', 8000 );")
cur.execute("insert into AvailablePets values( 108 , ' Rabbit ' , ' Lionhead ' , '2 months ', 8000 );")
cur.execute("insert into AvailablePets values( 109 , ' Rabbit ' , ' Angora ' , ' 4months ', 4000 );")
cur.execute("insert into AvailablePets values( 110 , ' Rabbit ' , ' Holland Lop ', ' 3 months ' ,5000 );")
db.commit()
#Creation of NewPets
db=pymysql.connect(host='localhost',user="flower",password="lily",db="PetShop")
cur=db.cursor()
cur.execute("Create table NewPets(PetBreed varchar(30),SoldBy varchar(20),Price int(20),PetID int(30));")
cur.execute("insert into NewPets values( ' BullDog ' , ' Ramesh Kumar ' ,4000 , 111 );")
cur.execute("insert into NewPets values( ' Dobermann ' , ' Ayush Sharma ' ,6000 , 112 );")
cur.execute("insert into NewPets values( ' Husky ' , ' Mrinal Gupta ' , 6000 ,113 );")
cur.execute("insert into NewPets values( ' Rottweiler ' , ' Manan Verma ' ,5000 , 114 );")
db.commit()
#Nourishment cost
db=pymysql.connect(host='localhost',user="flower",password="lily",db="PetShop")
cur=db.cursor()
cur.execute("Create table NourishmentCost(PetID int(7),PetFood varchar(20),PricePerPack varchar(20),ConsumptionPerDay varchar(30),NetExpenditure int(9));")
cur.execute("insert into NourishmentCost values( 101 , ' Dog Food ' , ' 200 ' ,' 2 ', 12000 );")
cur.execute("insert into NourishmentCost values( 102 , ' Dog Food ' , ' 300 ' ,' 2 ', 15000 );")
cur.execute("insert into NourishmentCost values( 103 , ' Dog Food ' , ' 500 ' ,' 1 ', 15000 );")
cur.execute("insert into NourishmentCost values( 104 , ' Cat Food ' , ' 200 ' , '1 ', 6000 );")
cur.execute("insert into NourishmentCost values( 105 , ' Cat Food ' , ' 300 ' , '1 ', 9000 );")
cur.execute("insert into NourishmentCost values( 106 , ' Cat Food ' , ' 200 ' , '2 ', 12000 );")
cur.execute("insert into NourishmentCost values( 107 , ' Organic Seeds ' , '100 ' , ' 0.5 ', 1500 );")
cur.execute("insert into NourishmentCost values( 108 , ' Carrots ' , ' 100 ' , ' 1', 3000 );")
cur.execute("insert into NourishmentCost values( 109 , ' Carrots ' , ' 100 ' , ' 1' ,3000 );")
cur.execute("insert into NourishmentCost values( 110 , ' Carrots ' , ' 100 ' , ' 1' ,3000 );")
cur.execute("insert into NourishmentCost values( 111 , ' Dog Food ' , ' 200 ' ,' 2 ', 12000 );")
cur.execute("insert into NourishmentCost values( 112 , ' Dog Food ' , ' 300 ' ,' 2 ' ,15000 );")
cur.execute("insert into NourishmentCost values( 113 , ' Dog Food ' , ' 500 ' ,' 1 ' ,15000 );")
cur.execute("insert into NourishmentCost values( 114 , ' Dog Food ' , ' 300 ' ,' 1 ' ,9000 );")
db.commit()
#Creation of Health Checkup
db=pymysql.connect(host='localhost',user="flower",password="lily",db="PetShop")
cur=db.cursor()
cur.execute("Create table HealthCheckup(PetID int(7),VeterinarianName varchar(20),Weight varchar(20),Temperature varchar(30),Status varchar(20));")
cur.execute("insert into HealthCheckup values( 101 , ' Shikha Sharma ' ,'20kg' , ' 98F ' , ' Healthy ' );")
cur.execute("insert into HealthCheckup values( 102 , ' Rajesh Sharma ' ,'12kg' , ' 103F ' , ' Unhealthy ' );")
cur.execute("insert into HealthCheckup values( 103 , ' Shikha Sharma ' ,'22kg' , ' 97F ' , ' Healthy ' );")
cur.execute("insert into HealthCheckup values( 104 , ' Rajesh Sharma ' ,'17kg' , ' 99F ' , ' Healthy ' );")
cur.execute("insert into HealthCheckup values( 105 , ' Rajesh Sharma ' ,'19kg' , ' 100F ' , ' Healthy ' );")
cur.execute("insert into HealthCheckup values( 106 , ' Rajesh Sharma ' ,'28kg' , ' 102F ' , ' Unhealthy ' );")
cur.execute("insert into HealthCheckup values( 107 , ' Shikha Sharma ' ,'200g' , ' 97F ' , ' Healthy ' );")
cur.execute("insert into HealthCheckup values( 108 , ' Rajesh Sharma ' , '5kg', ' 99.5F ' , ' Healthy ' );")
cur.execute("insert into HealthCheckup values( 109 , ' Shikha Sharma ' ,'4kg' , ' 97F ' , ' Healthy ' );")
cur.execute("insert into HealthCheckup values( 110 , ' Rajesh Sharma ' , '5kg', ' 99F ' , ' Healthy ' );")
cur.execute("insert into HealthCheckup values( 111 , ' Shikha Sharma ' ,'27kg' , ' 97F ' , ' Unhealthy ' );")
cur.execute("insert into HealthCheckup values( 112 , ' Shikha Sharma ' ,'20kg' , ' 103F ' , ' Unhealthy ' );")
cur.execute("insert into HealthCheckup values( 113 , ' Shikha Sharma ' ,'18kg' , ' 96F ' , ' Healthy ' );")
cur.execute("insert into HealthCheckup values( 114 , ' Shikha Sharma ' ,'19kg' , ' 97F ' , ' Healthy ' );")
db.commit()
#DIVVIDER
#Creation of OtherItems
db=pymysql.connect(host='localhost',user="flower",password="lily",db="PetShop")
cur=db.cursor()
cur.execute("Create table OtherItems(ItemName varchar(30),Price int(9));")
cur.execute("insert into OtherItems values( ' Dog Food ' , 5000 );")
cur.execute("insert into OtherItems values( ' Cat Food ' , 4000 );")
cur.execute("insert into OtherItems values( ' Playing Ball ' , 800 );")
cur.execute("insert into OtherItems values( ' Rubber Bone ' , 600 );")
cur.execute("insert into OtherItems values( ' Frisbee ' , 400 );")
cur.execute("insert into OtherItems values( ' Artificial Mice ' , 500 );")
cur.execute("insert into OtherItems values( ' Wool Textured Ball ' , 500 );")
cur.execute("insert into OtherItems values( ' Fish Food ' , 1000 );")
cur.execute("insert into OtherItems values( ' Aquarium Tank ' , 4000 );")
cur.execute("insert into OtherItems values( ' Aquarium Plants ' , 200 );")
db.commit()
#Creation of user ratings
db=pymysql.connect(host='localhost',user="flower",password="lily",db="PetShop")
cur=db.cursor()
cur.execute("Create table URating(User varchar(30),Ratings varchar(20));")
cur.execute("insert into URating values( ' Ayaan Chaudhary ' , ' ***** ' );")
cur.execute("insert into URating values( ' Namrata Kulkarni ' , ' ***** ' );")
cur.execute("insert into URating values( ' Pallavi Gupta ' , ' **** ' );")
cur.execute("insert into URating values( ' Jyoti Jain ' , ' ***** ' );")
cur.execute("insert into URating values( ' Vivek Patel ' , ' ***** ' );")
cur.execute("insert into URating values( ' Isha Gupta ' , ' ***** ' );")
db.commit()
#Creationn of total available pets
db=pymysql.connect(host='localhost',user="flower",password="lily",db="PetShop")
cur=db.cursor()
cur.execute("Create table Upets(PetID int(7),PetType varchar(20),PetBreed varchar(20),Age varchar(30),Price int(9));")
cur.execute("insert into Upets values( 101 , ' Dog ' , ' Golden Retriever ' , ' 4months ' ,20000 );")
cur.execute("insert into Upets values( 102 , ' Dog ' , ' German Shepherd ' , ' 6months ' ,45000 );")
cur.execute("insert into Upets values( 103 , ' Dog ' , ' American Bully ' , ' 2months ' ,52000 );")
cur.execute("insert into Upets values( 104 , ' Cat ' , ' Birman ' , ' 4 months ',17000 );")
cur.execute("insert into Upets values( 105 , ' Cat ' , ' Korat ' , ' 3 months' ,55000 );")
cur.execute("insert into Upets values( 106 , ' Cat ' , ' Persian ' , ' 7 months' ,25000 );")
cur.execute("insert into Upets values( 107 , ' Canary ' , ' Harz Roller ' , ' 2months ', 8000 );")
cur.execute("insert into Upets values( 108 , ' Rabbit ' , ' Lionhead ' , ' 2months ' ,8000 );")
cur.execute("insert into Upets values( 109 , ' Rabbit ' , ' Angora ' , ' 4 months' ,4000 );")
cur.execute("insert into Upets values( 110 , ' Rabbit ' , ' Holland Lop ' , ' 3months ' ,5000 );")
cur.execute("insert into Upets values( 111,' Dog',' BullDog ' , ' 3 months ' ,40000 );")
cur.execute("insert into Upets values( 112,' Dog',' Dobermann ' , ' 2 months' , 60000 );")
cur.execute("insert into Upets values( 113, ' Dog',' Husky ' , ' 4 months ' ,60000 );")
cur.execute("insert into Upets values( 114 ,' Dog',' Rottweiler ' , ' 2 months ' ,50000 );")
db.commit()
''''''
#IMPORTANT CODES USED TO CREATE THE TABLES


def modify(t): #For editing tables
    db=pymysql.connect(host='localhost',user="flower",password="lily",db="PetShop")
    cur=db.cursor()
    c=input("Enter the primary key on the basis of which you want to modiy the other details =>")
    for i in range(len(head)):
        if c == head[i]:
            k= input("Enter the "+head[i]+" which you want to edit")
            for j in range (len(head)):
                if c !=head[j]:
                    a=input("Enter new "+head[j])
                    kk = head[j]
                    kl=head[i]
                    query= f"update {t} set {kk} = '{a}' where {kl} = "+k+';'
                    cur.execute(query)
                    db.commit()


#Usermode = ADMIN
def elist():
    db=pymysql.connect(host='localhost',user="flower",password="lily",db="PetShop")
    cur=db.cursor()
    cur.execute("SELECT * FROM EmployeeList;")
    y=()
    x=cur.fetchall()
    global head
    head=('EmployeeID','Name','Position','DateJoined','Salary')
    print(tabulate(x,headers=head,numalign="center",stralign="center",maxcolwidths=[20,20],tablefmt="pretty"))
    print()
    print()
    elch=input("Do you want to make changes to this table?\n=>")
    if elch == "no" or elch =="No":
        return
    elif elch== "yes" or elch == "Yes":
        elch2=int(input("Which action do you want to perform? \n1. Hire employees \n2. Fire Employees\n3.Modify Table\n=>"))
        if elch2 ==1:
            num_records = int(input("Enter the number of records to insert:"))
            for i in range(num_records):
                print(f"\nEnter details for record {i+1}:")
                c1 = int(input("Enter value for EmployeeID: "))
                c2 = input("Enter value for Name: ")
                c3=input("Enter value for Position: ")
                c4=input("Enter value for DateJoined: ")
                c5=int(input("Enter value for Salary: "))
                sql = f"INSERT INTO EmployeeList(EmployeeID,Name,Position,DateJoined,Salary) VALUES (%s, %s,%s, %s,%s)"
                cur.execute(sql, (c1,c2,c3,c4,c5))
                db.commit()
        elif elch2 == 2:
            ask=int(input("How many employees do you want to fire =>"))
            for i in range(ask):
                j=int(input("Enter employee id =>"))
                cur.execute("Delete from EmployeeList where EmployeeID =%d;"%(j))
                db.commit()
        elif elch2== 3:
            modify("EmployeeList")
def prof():
    db=pymysql.connect(host='localhost',user="flower",password="lily",db="PetShop")
    cur=db.cursor()
    cur.execute("SELECT * FROM PROFIT;")
    y=()
    x=cur.fetchall()
    global head
    head=('Month','Total_Expenditure','Total_Earnings','Net_Profit')
    print(tabulate(x,headers=head,numalign="center",stralign="center",maxcolwidths=[20,20],tablefmt="pretty"))
    print()
    print()
    prch=input("Do you want to make changes to this table?\n=>")
    if prch == "no" or prch =="No":
        return
    elif prch== "yes" or prch == "Yes":
        xyz=int(input("What changes do you want to make?\n1.Add profits of another month \n2.Modify Table\n=>"))
        if xyz ==1:
            num_records = int(input("Enter the number of records to insert:"))
            for i in range(num_records):
                print(f"\nEnter details for record {i+1}:")
                c1 = input("Enter value for Month: ")
                c2 = int(input("Enter value for Total_Expenditure: "))
                c3=int(input("Enter value for Total_Earnings: "))
                c4=int(input("Enter value for Net_Profit"))
                sql = f"INSERT INTO PROFIT(Month,Total_Expenditure,Total_Earnings,Net_Profit) VALUES (%s, %s,%s,%s)"
                cur.execute(sql, (c1,c2,c3,c4))
                db.commit()
        elif xyz == 2:
            modify("PROFIT")
def admin():
    while True:
        print("There are 3 options available in this usermode:- \n1.EmployeeList \n2.Monthly Profit \n3.Switch to different usermode")
        ch=int(input("So what is your choice? =>"))
        if ch ==1:
            elist()
        elif ch ==2:
            prof()
        elif ch ==3:
            return
    #Usermode = STAFF
def apets():
    db=pymysql.connect(host='localhost',user="flower",password="lily",db
    ="PetShop")
    cur=db.cursor()
    cur.execute("SELECT * FROM AvailablePets;")
    y=()
    x=cur.fetchall()
    global head
    head=('PetID' ,'PetType' ,'PetBreed' ,'Age' ,'Price' )
    print(tabulate(x,headers=head,numalign="center",stralign="center",tablefmt="pretty"))
    print()
    print()
    apch=input("Do you want to make changes to this table?\n=>")
    if apch == "no" or apch =="No":
        return
    elif apch== "yes" or apch == "Yes":
        abd=int(input("What changes do you want to makes?\n1.Add more pets \n2.Modify table"))
        if abd ==1:
            num_records = int(input("Enter the number of records to insert:"))
            for i in range(num_records):
                print(f"\nEnter details for record {i+1}:")
                c1 = int(input("Enter value for PetID: "))
                c2 = input("Enter value for PetType : ")
                c3=input("Enter value for PetBreed : ")
                c4=input("Enter value for Age : ")
                c5=int(input("Enter value for Price : "))
                sql= f"INSERT INTO AvailablePets(PetID ,PetType ,PetBreed ,Age ,Price ) VALUES (%s, %s,%s, %s,%s)"
                cur.execute(sql, (c1,c2,c3,c4,c5))
                db.commit()
        elif abd ==2:
                modify("AvailablePets")
def npets():
    db=pymysql.connect(host='localhost',user="flower",password="lily",db ="PetShop")
    cur=db.cursor()
    cur.execute("SELECT * FROM NewPets;")
    y=()
    x=cur.fetchall()
    global head
    head=('PetBreed','SoldBy','Price','PetID' )
    print(tabulate(x,headers=head,numalign
    ="center",stralign="center",tablefmt="pretty"))
    print()
    print()
    npch=input("Do you want to make changes to this table?\n=>")
    if npch == "no" or npch =="No":
        return
    elif npch== "yes" or npch == "Yes":
        msd=int(input("What changes do you want to makes?\n1.Add more pets \n2.Modify table"))
        if msd ==1:
            num_records = int(input("Enter the number of records to insert:"))
            for i in range(num_records):
                print(f"\nEnter details for record {i+1}:")
                c1 = input("Enter value for PetBreed: ")
                c2 = input("Enter value for SoldBy : ")
                c3=int(input("Enter value for Price : "))
                c4=int(input("Enter value for PetID : "))
                sql = f"INSERT INTO NewPets(PetBreed ,SoldBy ,Price ,PetID ) VALUES (%s, %s, %s,%s)"
                cur.execute(sql, (c1,c2,c3,c4,))
                db.commit()
        elif msd ==2:
            modify("NewPets")
def ncost():
    db=pymysql.connect(host='localhost',user="flower",password="lily",db ="PetShop")
    cur=db.cursor()
    cur.execute("SELECT * FROM NourishmentCost;")
    global head
    y=()
    x=cur.fetchall()
    head=('PetID' ,'PetFood' ,'PricePerPack' ,'ConsumptionPerDay','NetExpenditure' )
    print(tabulate(x,headers=head,numalign="center",stralign="center",tablefmt="pretty"))
    print()
    print()
    npch=input("Do you want to make changes to this table?\n=>")
    if npch == "no" or npch =="No":
        return
    elif npch== "yes" or npch == "Yes":
        vk=int(input("What changes do you want to makes?\n1.Add more records \n2.Modify table"))
        if vk ==1:
            num_records = int(input("Enter the number of records to insert:"))
            for i in range(num_records):
                print(f"\nEnter details for record {i+1}:")
                c1 = int(input("Enter value for PetID: "))
                c2 = input("Enter value for PetFood : ")
                c3=input("Enter value for PricePerPack : ")
                c4=input("Enter value for ConsumptionPerDay : ")
                c5=int(input("Enter value for NetExpenditure : "))
                sql = f"INSERT INTO NourishmentCost(PetID ,PetFood ,PricePerPack ,ConsumptionPerDay ,NetExpenditure ) VALUES (%s, %s,%s, %s,%s)"
                cur.execute(sql, (c1,c2,c3,c4,c5))
                db.commit()
                return
        elif vk == 2:
            modify("NourishmentCost")
def hcheck():
    db=pymysql.connect(host='localhost',user="flower",password="lily",db
    ="PetShop")
    cur=db.cursor()
    cur.execute("SELECT * FROM HealthCheckup;")
    global head
    y=()
    x=cur.fetchall()
    head=('PetID' ,'VeterinarianName' ,'Weight' ,'Temperature' ,'Status')
    print(tabulate(x,headers=head,numalign="center",stralign="center",tablefmt="pretty"))
    print()
    print()
    npch=input("Do you want to make changes to this table?\n=>")
    if npch == "no" or npch =="No":
        return
    elif npch== "yes" or npch == "Yes":
        rs=int(input("What changes do you want to makes?\n1.Add more records \n2.Modify table"))
        if rs ==1:
            num_records = int(input("Enter the number of records to insert:"))
            for i in range(num_records):
                print(f"\nEnter details for record {i+1}:")
                c1 = int(input("Enter value for PetID: "))
                c2 = input("Enter value for VeterinarianName : ")
                c3=input("Enter value for Weight : ")
                c4=input("Enter value for Temperature : ")
                c5=input("Enter value for Status : ")
                sql = f"INSERT INTO HealthCheckup(PetID ,VeterinarianName ,Weight ,Temperature ,Status ) VALUES (%s, %s,%s, %s,%s)"
                cur.execute(sql, (c1,c2,c3,c4,c5))
                db.commit()
                return
        elif rs ==2:
            modify("HealthCheckup")
def oitem():
    db=pymysql.connect(host='localhost',user="flower",password="lily",db
="PetShop")
    cur=db.cursor()
    cur.execute("SELECT * FROM OtherItems;")
    global head
    y=()
    x=cur.fetchall()
    head=('ItemName' ,'Price')
    print(tabulate(x,headers=head,numalign
    ="center",stralign="center",tablefmt="pretty"))
    print()
    print()
    npch=input("Do you want to make changes to this table?\n=>")
    if npch == "no" or npch =="No":
        return
    elif npch== "yes" or npch == "Yes":
        yuzi=int(input("What changes do you want to makes?\n1.Add more items \n2.Modify table"))
        if yuzi ==1:
            num_records = int(input("Enter the number of records to insert:"))
            for i in range(num_records):
                print(f"\nEnter details for record {i+1}:")
                c1 = int(input("Enter value for ItemName: "))
                c2 = int(input("Enter value for Price : "))
                sql = f"INSERT INTO OtherItems (ItemName ,Price) VALUES(%s, %s)"
                cur.execute(sql, (c1,c2))
                db.commit()
                return
        elif yuzi ==2:
            modify("OtherItems")
def staff():
    while True:
        print("There are 6 options available in this usermode:- \n1.Available Pets \n2.New Pets \n3.Nourishment Cost \n4.Health Check-up Record \n5.Other Items Available In The Store \n6.Switch to different usermode")
        ch=int(input("So what is your choice? =>"))
        if ch == 1:
            apets()
        elif ch ==2:
            npets()
        elif ch == 3:
            ncost()
        elif ch ==4:
            hcheck()
        elif ch == 5:
            oitem()
        else:
            return
        #Usermode = USER
def uapets():
    db=pymysql.connect(host='localhost',user="flower",password="lily",db="PetShop")
    cur=db.cursor()
    cur.execute("SELECT * FROM upets;")
    y=()
    x=cur.fetchall()
    global head
    head=('PetID' ,'PetType' ,'PetBreed' ,'Age' ,'Price' )
    print(tabulate(x,headers=head,numalign
    ="center",stralign="center",tablefmt="pretty"))
    print()
    print()
    apch=input("Do you want to buy any pet?\n=>")
    if apch == "no" or apch =="No":
        return
    elif apch== "yes" or apch == "Yes":
        sp("Thanks for showing interest in our pets but unfortunately we dont take online orders yet so you would have to visit our store in order tobuy any pet.")
        return
def uoitem():
    db=pymysql.connect(host='localhost',user="flower",password="lily",db="PetShop")
    cur=db.cursor()
    cur.execute("SELECT * FROM OtherItems;")
    global head
    y=()
    x=cur.fetchall()
    head=('ItemName' ,'Price')
    print(tabulate(x,headers=head,numalign="center",stralign="center",tablefmt="pretty"))
    print()
    print()
    apch=input("Do you want to buy any item?\n=>")
    if apch == "no" or apch =="No":
        return
    elif apch== "yes" or apch == "Yes":
        sp("Thanks for showing interest in our pets but unfortunately we dont take online orders yet so you would have to visit our store in order to buy any product.")
        return
def urate():
    db=pymysql.connect(host='localhost',user="flower",password="lily",db="PetShop")
    cur=db.cursor()
    cur.execute("SELECT * FROM URating;")
    x=cur.fetchall()
    global head
    head=('User' ,'Ratings')
    print(tabulate(x,headers=head,numalign="center",stralign="center",tablefmt="pretty"))
    print()
    print()
    npch=input("Do you want to add your ratings?\n=>")
    if npch == "no" or npch =="No":
        return
    elif npch== "yes" or npch == "Yes":
        for i in range(1):
            c1 = input("Enter your name ")
            c2 = input("Enter your rating : ")
            sql = f"INSERT INTO URating (User ,Ratings) VALUES (%s, %s)"
            cur.execute(sql, (c1,c2))
            db.commit()
            return
def user():
    while True:
        print("There are 4 options available in this usermode:- \n1.Available Pets\n2.Other Items Available In The Store \n3.User Ratings \n4.Switch todifferent usermode")
        ch=int(input("So what is your choice? =>"))
        if ch == 1:
            uapets()
        elif ch ==2:
            uoitem()
        elif ch == 3:
            urate()
        else:
            return
sp("Welcome to this project of representing management system of a PetShop,\n In this project I have made different tables which have data about all the necessary information of the store \n It is divided into 3 user modes:\nAdmin(For owners)\nStaff\nUser \nHope you like my project!!")
sp2("Made By:Avani")
while True:
    print("Which usermode do you want to choose?")
    z= int(input("1.Admin \n2.Staff \n3.User \n4.End \n=>"))
    if z == 1:
        az= int(input("Enter owner password =>"))
        if az == 23022005 :
            sp2("Checking Password. .. ")
            sp("Password Matched!!")
            admin()
        else:
            sp2("Checking Password. .. ")
            sp("Wrong Password!! please do not try to open it if you are not an owner")
    elif z == 2:
        bz= int(input("Enter your staff id =>"))
        if bz in range(901,919) :
            sp2("Checking ID. ..")
            sp("ID Matched!!")
            cur.execute("Select Name from EmployeeList where employeeid =%d"%(bz))
            d=cur.fetchall()
            sp2("WELCOME Mr./Ms.%s"%(d[0]))
            staff()
        else:
            sp2("Checking ID. ..")
            sp("Wrong ID!! please do not try to open it if you are not staff")
    elif z ==3:
        user()
    else:
        sp("Thanks for checking out our project!")
        break
