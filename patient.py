import mysql.connector as a
con= a.connect(host="localhost",user="root",passwd="root",database="hospital")
# if con.is_connected():
#     print("Sucessfully Connected..")
# else:
#     print("Error!")    

def newPatient():
    nam = input("Enter Name: ")
    umr = int(input("Enter Age: "))
    varn = input("Enter Gender: ")
    fees = int(input("Enter Fee: "))
    tn = int()

    data1 =(nam,umr,varn,fees,tn)
    sql1 = "insert into patient values(%s,%s,%s,%s,%s)"
    c = con.cursor()
    c.execute(sql1,data1)
    con.commit()
    print("Data Entered Sucessfully")
    main()

def displayAll():
    sql ="SELECT * FROM patient"
    c = con.cursor()
    c.execute(sql)
    myresult = c.fetchall()
    for i in myresult:
        print(i)
    main()    


def removePatient():
    inp = input("Enter Token No You Whose Data You Want  To Delete: ")
    sql = "delete from patient where tokenno = %s"
    data =(inp,)
    c= con.cursor()
    c.execute(sql,data)
    con.commit()
    main()


def oderByName():
    sql = "SELECT * FROM patient order by name"
    c = con.cursor()
    c.execute(sql)
    myresult = c.fetchall()
    for i in myresult:
        print(i)
    main()


def orderByGender():
    sql = "SELECT * FROM patient order by gender"
    c = con.cursor()
    c.execute(sql)
    myresult = c.fetchall()
    for i in myresult:
        print(i)
    main()

def tokenNo():
    sql = "SELECT * FROM patient order by tokenno"
    c = con.cursor()
    c.execute(sql)
    myresult = c.fetchall()
    for i in myresult:
        print(i)
    main()
        
        
def age():
    sql = "SELECT * FROM patient order by age"
    c = con.cursor()
    c.execute(sql)
    myresult = c.fetchall()
    for i in myresult:
        print(i)
    main()

def exitCode():
    exit()

def updateFee():
    upFee=int(input("Enter Fee: "))    
    forUpdate=int(input("Enter token No. : "))
    sql1 = "select fee from patient where tokenno = %s"
    data = (forUpdate,)
    c = con.cursor()
    c.execute(sql1,data)
    myresult = c.fetchone()
    totalFee = myresult[0] + upFee
    sql2 = "update patient set fee = %s where tokenno = %s"
    d = (totalFee,forUpdate)
    c.execute(sql2,d)
    con.commit()
    main()
     
def main():
    print('''
    1. NEW PATIENT ENTRY
    2. DISPLAY ALL PATIENTS
    3. REMOVE PATIENT FROM LIST BY TOKEN NUMBER
    4. DISPLAY PATIENTS ORDER BY NAME 
    5. DISPLAY PATIENTS ORDER BY GENDER  
    6. DISPLAY PATIENTS ORDER BY TOKEN NUMBER 
    7. DISPLAY PATIENTS ORDER BY AGE  
    8. UPDATE PATIENT'S FEE 
    9. EXIT''')
    choise = input("Enter Your Choise [1-9] :")
    if(choise=='1'):
        newPatient()
    elif(choise=='2'):
        displayAll()
    elif(choise=='3'):
        removePatient()
    elif(choise=='4'):
        oderByName()
    elif(choise=='5'):
        orderByGender()
    elif(choise=='6'):
        tokenNo()
    elif(choise=='7'):
        age()
    elif(choise=='8'):
        updateFee()
    elif(choise=='9'):
        exitCode()
    else:
        print('INVALID ENTRY!')
        main()
main()                                

