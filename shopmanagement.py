import mysql.connector
import numpy as np
import datetime

class Product:

    def __init__(self):
        self.mydb=mysql.connector.connect(host="localhost",user="root",password="",database="shopmanagement")
        self.mycursor=self.mydb.cursor()

    def setData(self,id,name,netAmount,qty,totalAmount):
        self.id=id
        self.name=name
        self.netAmount=netAmount
        self.qty=qty
        self.totalAmount=totalAmount

    def addProduct(self):
        name=input("Enter Product name:")
        netAmount=int(input("Enter Net Amount Of Product:"))
        stock=int(input("Enter Available Stock:"))

        sql="insert into productdetails(productName,netAmount,stock) values (%s,%s,%s)"
        val=(name,netAmount,stock)
        self.mycursor.execute(sql,val)
        print()
        self.mydb.commit()
        print("Product Details Successfully Added")
        print()

    def delProduct(self):
        d_id=int(input("Enter Product Id To Delete The Product:"))

        sql="delete from productdetails where productId=%s"
        val=(d_id,)
        self.mycursor.execute(sql,val)
        self.mydb.commit()
        print()
        print("Product Deleted Succesfully")
        print()

    def updateProduct(self):
        self.showAllProduct()
        
        u_id=int(input("Enter Id For Product Details Updation:"))
        while True:
            sql="select * from productdetails where productId=%s"
            val=(u_id,)
            self.mycursor.execute(sql,val)
            result=self.mycursor.fetchone()
            print()
            if result==None:
                print("PRoduct Not Found")
                print()
                break
            else:
                print("-----------------Product-Updation---------------")
                print("1. Product Name:",result[1])
                print("2. Product Net Amount:",result[2])
                print("3. Product Stock:",result[3])
                print("4. Exit")
                print()
                choice=int(input("Enter Choice:"))
                if choice==1:
                    n_name=input("Enter New name Of Product:")

                    sql="update productdetails set productName=%s where productId=%s"
                    val=(n_name,u_id)
                    self.mycursor.execute(sql,val)
                    self.mydb.commit()
                    print("Updation In name Is Successfully Completed")

                elif choice==2:
                    n_netAmount=input("Enter New Net Amount:")

                    sql="update productdetails set netAmount=%s where productId=%s"
                    val=(n_netAmount,u_id)
                    self.mycursor.execute(sql,val)
                    self.mydb.commit()
                    print("Updation In Net Amount Is Successfully Completed")

                elif choice==3:
                    n_stock=input("Enter New Stock:")

                    sql="update productdetails set stock=%s where productId=%s"
                    val=(n_stock,u_id)
                    self.mycursor.execute(sql,val)
                    self.mydb.commit()
                    print("Updation In stock Is Successfully Completed")

                elif choice==4:
                    break
                else:
                    print("Enter valid Choice")

    def searchProduct(self):
        s_id=int(input("Enter Product Id:"))

        sql="select * from productdetails where productId=%s"
        val=(s_id,)
        self.mycursor.execute(sql,val)
        result=self.mycursor.fetchone()
        print()
        if result==None:
            print("Product Not Found")
            print()
            return
        else:
            print("-----------------Product-Details----------------")
            print("Product Id:",result[0])
            print("Product Name:",result[1])
            print("Product Net Amount:",result[2])
            print("Product Stock:",result[3])
            print()

    def showAllProduct(self):
        sql="select * from productdetails"
        self.mycursor.execute(sql)
        result=self.mycursor.fetchall()

        for i,detail in enumerate(result):
            print(f"--------------------Product-{i+1}---------------------")
            print("Product Id:",result[i][0])
            print("Product Name:",result[i][1])
            print("Product Net Amount:",result[i][2])
            print("Product Stock:",result[i][3])
            print()
        print()
        print()




class Customer:
    def __init__(self):
        self.mydb=mysql.connector.connect(host="localhost",user="root",password="",database="shopmanagement")
        self.mycursor=self.mydb.cursor()

    def addCustomer(self):
        name=input("Enter Custome Name:")
        phoneNumber=input("Enter Customer Phone Number:")
        EmailId=input("Enter Customer Email Id:")

        sql="insert into customerdetails(customerName,customerPhoneNumber,customerEmailId) values (%s,%s,%s)"
        val=(name,phoneNumber,EmailId)
        self.mycursor.execute(sql,val)
        print()
        self.mydb.commit()
        print("Customer Details Successfully Added")
        print()

    def delCUstomer(self):
        try:
            d_id=int(input("Enter Customer Id To Delete The Customer:"))
        except ValueError:
            print("enter valid num ")
        sql="delete from customerdetails where customerId=%s"
        val=(d_id,)
        self.mycursor.execute(sql,val)
        self.mydb.commit()
        print()
        print("Customer Deleted Succesfully")
        print()

    def updateCustomerDetails(self):
        self.showAllCustomerDetails()
        
        u_id=int(input("Enter Id For Customer Details Updation:"))
        while True:
            sql="select * from customerdetails where customerId=%s"
            val=(u_id,)
            self.mycursor.execute(sql,val)
            result=self.mycursor.fetchone()
            print()
            if result==None:
                print("Customer Not Found")
                print()
                break
            else:
                print("-----------------Customer-Updation---------------")
                print("1. Customer Name:",result[1])
                print("2. Customer Phone Number:",result[2])
                print("3. Customer Email Id:",result[3])
                print("4. Exit")
                print()
                choice=int(input("Enter Choice:"))
                if choice==1:
                    n_name=input("Enter New name Of Customer:")

                    sql="update customerdetails set customerName=%s where customerId=%s"
                    val=(n_name,u_id)
                    self.mycursor.execute(sql,val)
                    self.mydb.commit()
                    print("Updation In name Is Successfully Completed")

                elif choice==2:
                    n_phoneNumber=input("Enter New Phone Number:")

                    sql="update customerdetails set customerPhoneNumber=%s where customerId=%s"
                    val=(n_phoneNumber,u_id)
                    self.mycursor.execute(sql,val)
                    self.mydb.commit()
                    print("Updation In Phone Number Is Successfully Completed")

                elif choice==3:
                    n_email=input("Enter New Email Id:")

                    sql="update customerdetails set customerEmailId=%s where customerId=%s"
                    val=(n_email,u_id)
                    self.mycursor.execute(sql,val)
                    self.mydb.commit()
                    print("Updation In Email Id Is Successfully Completed")

                elif choice==4:
                    break
                else:
                    print("Enter valid Choice")

    def searchCustomer(self):
        s_id=int(input("Enter Customer Id:"))

        sql="select * from customerdetails where customerId=%s"
        val=(s_id,)
        self.mycursor.execute(sql,val)
        result=self.mycursor.fetchone()
        print()
        if result==None:
            print("Customer Not Found")
            print()
            return
        else:
            print("-----------------Customer-Details----------------")
            print("Customer Id:",result[0])
            print("Customer Name:",result[1])
            print("Customer Phone Number:",result[2])
            print("Customer Email Id:",result[3])
            print()

    def showAllCustomerDetails(self):
        sql="select * from customerdetails"
        self.mycursor.execute(sql)
        result=self.mycursor.fetchall()

        for i,detail in enumerate(result):
            print(f"--------------------Customer-{i+1}---------------------")
            print("Customer Id:",result[i][0])
            print("Customer Name:",result[i][1])
            print("Customer Phone Number:",result[i][2])
            print("Customer Email Id:",result[i][3])
            print()
        print()
        print()


class Bill:

    def __init__(self):
        self.mydb=mysql.connector.connect(host="localhost",user="root",password="",database="shopmanagement")
        self.mycursor=self.mydb.cursor()
        self.bill=dict()

    def addSpace(self,name,space):
        s=space-len(name)
        return name+" "*s

    def createNewBill(self):
        x=datetime.datetime.now()
        date=x.strftime("%x")
        c_id=int(input("Enter Id Of Customer:"))
        sql="select * from customerdetails where customerId=%s"
        val=(c_id,)
        self.mycursor.execute(sql,val)
        result=self.mycursor.fetchone()

        if result!=None:
            self.name=result[1]
        else:
            print("Customer Not Found")


        while True:
            print("1. Add Item In Bill")
            print("2. Delete Item In Bill")
            print("3. View Bill")
            print("4. Get Bill")
            print("5. Exit")
            choice=int(input("Enter Your Choice: "))

            if choice==1:
                b_id=int(input("Enter Id Of Product To Add In Bill: "))
                qty=int(input("Enter Qty: "))
                sql="select * from productdetails where productId=%s"
                val=(b_id,)
                self.mycursor.execute(sql,val)
                result=self.mycursor.fetchone()
                totalAmount=qty*result[2]
                product=Product()
                product.setData(result[0],result[1],result[2],qty,totalAmount)
                self.bill[b_id]=product
                print("Product Added Successfully")

            elif choice==2:
                d_id=int(input("Enter id of product to delete:"))
                if d_id in self.bill.keys:
                    self.bill.pop(d_id)
                else:
                    print("Product Not Found In Bill")

            elif choice==3:
                total=0
                print(" "+"_"*80)
                print("|"+" "*80+"|")
                print("|"+"Shop Management System".center(80)+"|")
                print("|"+" "*80+"|")
                print("|"+"-"*80+"|")
                print("|"+" NAME :"+self.addSpace(self.name,73)+"|")
                print("|"+"-"*80+"|")
                print("|"+" Date :"+self.addSpace(str(date),73)+"|")
                print("|"+"-"*80+"|")
                print("|"+"No. |"+" Id  "+"|"+"               Product Name                |"+"  Qty  |"+" Price |"+"  Total  "+"|")
                for i,detail in enumerate(self.bill.values()):
                    print("|"+self.addSpace(str(i+1),4)+"|"+self.addSpace(str(detail.id),5)+"|"+self.addSpace(detail.name,43)+"|"+self.addSpace(str(detail.qty),7)+"|"+self.addSpace(str(detail.netAmount),7)+"|"+self.addSpace(str(detail.totalAmount),9)+"|")

                    total=total+detail.totalAmount
                print("|"+"-"*80+"|")
                print("|"+" "*55+"| Total : |",total," "*(12-len(str(total)))+"|")
                print("|"+"-"*80+"|")
              # print("|                                                                                |")
                print("|"+"_"*80+"|")


            elif choice==4:
                f=open(self.name+".txt","w")
                total=0
                f.write(" "+"_"*80+"\n")
                f.write("|"+" "*80+"|\n")
                
                f.write("|"+"Shop Management System".center(80)+"|\n")
                f.write("|"+" "*80+"|\n")
                f.write("|"+"-"*80+"|\n")
                f.write("|"+" NAME :"+self.addSpace(self.name,73)+"|\n")
                f.write("|"+"-"*80+"|\n")
                f.write("|"+" Date :"+self.addSpace(str(x),73)+"|\n")
                f.write("|"+"-"*80+"|\n")
                f.write("|"+"No. |"+" Id  "+"|"+"               Product Name                |"+"  Qty  |"+" Price |"+"  Total  "+"|\n")
                for i,detail in enumerate(self.bill.values()):
                    f.write("|"+self.addSpace(str(i+1),4)+"|"+self.addSpace(str(detail.id),5)+"|"+self.addSpace(detail.name,43)+"|"+self.addSpace(str(detail.qty),7)+"|"+self.addSpace(str(detail.netAmount),7)+"|"+self.addSpace(str(detail.totalAmount),9)+"|\n")

                    total=total+detail.totalAmount
                f.write("|"+"-"*80+"|\n")
                f.write("|"+" "*55+"| Total : | "+str(total)+" "+" "*(12-len(str(total)))+"|\n")
                f.write("|"+"-"*80+"|\n")
                f.write("|"+"_"*80+"|\n")

                f.close()

                for detail in self.bill.values():
                    sql="update productdetails set stock=stock-%s where productId=%s"
                    val=(detail.qty,detail.id)
                    self.mycursor.execute(sql,val)
                    self.mydb.commit()
                print("Bill Created Successfully")
                break    

            elif choice==5:
                break
            else:
                print("Enter Valid Choice")




def stockReport():
    s=[]
    label=[]

    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="shopmanagement")
    mycursor=mydb.cursor()
    sql="select * from productdetails"
    mycursor.execute(sql)
    result=mycursor.fetchall()
    
    print("Stock-Report")
    for i,detail in enumerate(result):
        print((i+1),".",result[i][0],result[i][1],result[i][3])
   

#-------------------------------------Driver Code----------------------------------------------------------

print("||---------------------------------------------------||")
print("||:::::::::::::::::::::::::::::::::::::::::::::::::::||")
print("||       Welcome To Our Shop Management System       ||")
print("||:::::::::::::::::::::::::::::::::::::::::::::::::::||")
print("||---------------------------------------------------||")
product= Product()
customer=Customer()
bill=Bill()
while True:
    print("1. Product Menu")
    print("2. Customer Menu")
    print("3. Create New Bill")
    print("4. Stock Report")
    print("5. Exit")
    choice=int(input("Enter Your Choice:"))
    if choice==1:
        while True:
            print("1. Add Product")
            print("2. Search Product")
            print("3. Show All Products")
            print("4. Update In Product")
            print("5. Delete Product")
            print("6. Exit")
            subChoice=int(input("Enter Your Choice:"))
            if subChoice==1:
                product.addProduct()
            elif subChoice==2:
                product.searchProduct()
            elif subChoice==3:
                product.showAllProduct()
            elif subChoice==4:
                product.updateProduct()
            elif subChoice==5:
                product.delProduct()
            elif subChoice==6:
                break
            else:
                print("Enter Valid Choice")
    elif choice==2:
         while True:
            print("1. Add Customer Details")
            print("2. Search Customer")
            print("3. Show All Customer's Details")
            print("4. Update In Customer Details")
            print("5. Delete Customer Details")
            print("6. Exit")
            subChoice=int(input("Enter Your Choice:"))
            if subChoice==1:
                customer.addCustomer()
            elif subChoice==2:
                customer.searchCustomer()
            elif subChoice==3:
                customer.showAllCustomerDetails()
            elif subChoice==4:
                customer.updateCustomerDetails()
            elif subChoice==5:
                customer.delCUstomer()
            elif subChoice==6:
                break
            else:
                print("Enter Valid Choice")
    elif choice==3:
        bill.createNewBill()
    elif choice==4:
        stockReport()
    elif choice==5:
        break
    else:
        print("Enter Valid Choice")


