#######العوسه بيعمل عظمه #########

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType
import sys
from PyQt5 import QtGui
import MySQLdb
import datetime
from xlsxwriter import *
from xlrd import *
import pyqtgraph as pg

from Login_Handle import *

from login import *


MainUI,_= loadUiType('main.ui')


employee_id=0
employee_branch=1
class page2(QMainWindow ,MainUI):
    def __init__(self, parent=None):
        super(page2 ,self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.UI_Changes()
        self.Db_Connect()
        self.Handel_Buttons()
        self.Show_All_Categories()
        self.Show_Branchies()
        self.Show_Puplishers()
        self.Show_Authors()
        self.Show_All_Books()
        self.Show_All_Clients()
        self.Retreive_Day_Work()
        self.Show_Employee()
        self.Show_History()
        self.get_dashbord_data()

        self.Employe_123()







        
    ##############################################

    def Inventory_management(self):
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.insertRow(0)

        self.cur.execute('''
                    SELECT Code_Book,Book_Name,First_Balance,Period_Movement,Last_Balance,Stock_value,Order_Limit FROM management
                ''')
        data = self.cur.fetchall()
        for row, form in enumerate(data):
            for col, item in enumerate(form):
                self.tableWidget_2.setItem(row, col, QTableWidgetItem(str(item)))
                col += 1
            row_position = self.tableWidget_2.rowCount()
            self.tableWidget_2.insertRow(row_position)

    def Export_Inventory_management(self):
        self.cur.execute('''
                    SELECT Code_Book,Book_Name,First_Balance,Period_Movement,Last_Balance,Stock_value,Order_Limit  FROM management
                ''')
        data = self.cur.fetchall()
        excel_file = Workbook('Inventory_management_report.xlsx')
        sheet1 = excel_file.add_worksheet()

        sheet1.write(0, 0, 'CodeBook')
        sheet1.write(0, 1, 'Book Name')
        sheet1.write(0, 2, 'First Balance')
        sheet1.write(0, 3, 'Period Movement')
        sheet1.write(0, 4, 'Last Balance')
        sheet1.write(0, 5, 'Stock value')
        sheet1.write(0, 6, 'Order Limit')
        row_number = 1
        for row in data:
            column_number = 0
            for item in row:
                sheet1.write(row_number, column_number, str(item))
                column_number += 1
            row_number += 1
        excel_file.close()
        self.statusBar().showMessage('تم انشاء التقرير بنجاح')




    def Employe_123(self):
        self.cur.execute('''
                            SELECT id,name , password,branch FROM employee
                        ''')
        data_ = self.cur.fetchall()
        for row in data_:
            global employee_id, employee_branch
            employee_id = row[0]






    def UI_Changes(self):
      self.tabWidget.tabBar().setVisible(False)
      self.setWindowIcon(QtGui.QIcon('library.png'))
      self.setWindowTitle('Osmanyat - Library Program')
        
        
        
    
    def Db_Connect(self):
        ## connection between app and Database
        self.db = MySQLdb.connect(host='localhost', user='root', password='',db='library')
        self.cur=self.db.cursor()
        print('Connection Succsfully')
        


    def Handel_Buttons(self):
        ## Handle All Buttons in app
        self.pushButton.clicked.connect(self.Open_Daily_movements_Tab)
        self.pushButton_2.clicked.connect(self.Open_Books_Tap)
        self.pushButton_3.clicked.connect(self.Open_Clients_Tap)
        self.pushButton_4.clicked.connect(self.Open_Dashboard_Tap)
        self.pushButton_6.clicked.connect(self.Open_History_Tap)
        self.pushButton_5.clicked.connect(self.Open_Report_Tap)
        self.pushButton_7.clicked.connect(self.Open_Settings_Tap)
        self.pushButton_8.clicked.connect(self.Handle_to_Day_Work)
        self.pushButton_27.clicked.connect(self.Add_Branch)
        self.pushButton_28.clicked.connect(self.Add_Puplisher) 
        self.pushButton_29.clicked.connect(self.Add_Author)      
        self.pushButton_32.clicked.connect(self.Add_Category)
        self.pushButton_37.clicked.connect(self.Add_Employee)
        self.pushButton_17.clicked.connect(self.Add_New_Book)
        self.pushButton_21.clicked.connect(self.Add_New_Client)
        self.pushButton_18.clicked.connect(self.Edit_Book_Search )
        self.pushButton_19.clicked.connect(self.Edit_book)
        self.pushButton_23.clicked.connect(self.Edit_Client_Search)
        self.pushButton_22.clicked.connect(self.Edit_client)
        self.pushButton_20.clicked.connect(self.Delete_Book)
        self.pushButton_24.clicked.connect(self.Delete_Client)
        self.pushButton_9.clicked.connect(self.All_Books_Filter)
        self.pushButton_15.clicked.connect(self.Book_Export_Report)
        self.pushButton_40.clicked.connect(self.Check_Employee)
        self.pushButton_39.clicked.connect(self.Edit_Employee_Data)
        self.pushButton_10.clicked.connect(self.Add_Employee_Permissions)
        self.pushButton_16.clicked.connect(self.Client_Export_Report)
        self.pushButton_38.clicked.connect(self.logout_Button)
        self.pushButton_12.clicked.connect(self.Edit_Client_Search)
        self.pushButton_30.clicked.connect(self.Inventory_management)
        self.pushButton_34.clicked.connect(self.Export_Inventory_management)



        self.pushButton_49.clicked.connect(self.get_dashbord_data)


    def Handel_Login(self):
        ## Handle login 
        pass
    
    def Handle_Reset_passwords(self):
        #Handle Reset Password
        pass

    
    def Handle_to_Day_Work(self):
        ##Handle Day to Day operations
        book_title=self.lineEdit.text()
        client_national_id=self.lineEdit_13.text()
        type=self.comboBox.currentIndex()
        from_date =str(datetime.date.today())
        #to_date=self.dateEdit_6.date()
        to_date=str(datetime.date.today())
        date=datetime.datetime.now()
        branch=1
        employee =1
        
        
        self.cur.execute('''
            INSERT INTO daily_movements (book_id ,client_id , type, date , branch_id , Book_from ,Book_to,employee_id )
           VALUES(%s , %s ,%s ,%s ,%s ,%s ,%s,%s)
        ''',(book_title, client_national_id,type,date,branch,from_date,to_date,employee))

        global employee_id ,employee_branch

        print(employee_id)
        date = datetime.datetime.now()
        action=3
        table=6
        data='day to day work'

        self.cur.execute('''
            INSERT INTO history (employee_id,employee_action,affected_table,operation_date,employee_branch,data)
            VALUES (%s,%s,%s,%s,%s,%s)
        ''',(employee_id,action,table,date,employee_branch,data))


        self.db.commit()

        print('done')
        self.statusBar().showMessage('تم اضافه معلومات الكتاب بنجاح')
        self.Retreive_Day_Work()
        
    
    def Retreive_Day_Work(self):
        self.cur.execute('''
            SELECT book_id , type , client_id ,Book_from,Book_to FROM daily_movements
        ''')
        
        data=self.cur.fetchall()
        self.tableWidget.setRowCount(0)
        self.tableWidget.insertRow(0)
        for row, form in enumerate(data):
            self.tableWidget.insertRow(row)  # move insertRow here
            for column, item in enumerate(form):
                if column == 1:
                    if item == 0:
                        self.tableWidget.setItem(row, column, QTableWidgetItem("Borrow"))  # remove unnecessary str() conversion
                    else:
                        self.tableWidget.setItem(row, column, QTableWidgetItem("Return"))  # fix typo
                elif column == 2:
                    sql = "SELECT name FROM clients WHERE national_id = %s"  # remove unnecessary parentheses
                    self.cur.execute(sql, (item,))  # pass item as a tuple instead of a list
                    client_name = self.cur.fetchone()  # use fetchone instead of fetchmany
                    if client_name is not None:  # check if a row was returned
                        self.tableWidget.setItem(row, column, QTableWidgetItem(client_name[0]))
                else:
                    self.tableWidget.setItem(row, column, QTableWidgetItem(str(item)))  # add str() conversion for consistency



       
        
    
    ################# Books ############################
    
    def Show_All_Books(self):

        self.tableWidget_3.setRowCount(0)
        self.tableWidget_3.insertRow(0)
        
        self.cur.execute('''
            SELECT code ,title ,category_id ,author_id ,price FROM books
        ''')
        data=self.cur.fetchall()


        for row, form in enumerate(data):
            for col, item in enumerate(form):
                if col == 2:
                    sql = "SELECT Category_name FROM category WHERE id=%s "
                    self.cur.execute(sql, [(item)])
                    category_name = self.cur.fetchone()
                    if category_name is not None:  # check if a row was returned
                        self.tableWidget_3.setItem(row, col, QTableWidgetItem(str(category_name[0])))
                elif col==3:
                    sql = "SELECT name FROM author WHERE id=%s "
                    self.cur.execute(sql, [(item+1)])
                    author_name = self.cur.fetchone()
                    if author_name is not None:  # check if a row was returned
                        self.tableWidget_3.setItem(row, col, QTableWidgetItem(str(author_name[0])))


                else:
                    self.tableWidget_3.setItem(row, col, QTableWidgetItem(str(item)))
                col+=1
            row_postion=self.tableWidget_3.rowCount()
            self.tableWidget_3.insertRow(row_postion)








            
    
    def All_Books_Filter(self):
        book_title=self.lineEdit_3.text()
        #category=self.comboBox_3.currentIndex()

        sql=('''
            SELECT code , title ,category_id,publisher_id,price FROM books WHERE title=%s
        ''')
        self.cur.execute(sql, ([book_title]))
        data=self.cur.fetchall()
        print(data)

        self.tableWidget_3.setRowCount(0)
        self.tableWidget_3.insertRow(0)
        for row ,form in enumerate(data):
            for col , item in enumerate(form):
               if col== 2 :
                    sql=(''' SELECT Category_name FROM category WHERE id = %s ''')
                    self.cur.execute(sql,[(item)])
                    self.tableWidget_3.setItem(row,col,QTableWidgetItem(str(item)))
               else:
                    self.tableWidget_3.setItem(row,col,QTableWidgetItem(str(item)))
               col+=1
            row_postion=self.tableWidget_3.rowCount()
            self.tableWidget_3.insertRow(row_postion)


    
    def Add_New_Book(self):
        book_title = self.lineEdit_4.text()
        category=self.comboBox_4.currentIndex()
    
        description=self.textEdit.toPlainText()
        price=self.lineEdit_5.text()
        code=self.lineEdit_6.text()
        puplisher=self.comboBox_7.currentIndex()
    
        author = self.comboBox_8.currentIndex()
    
        status=self.comboBox_9.currentIndex()
        part_order=self.lineEdit_11.text()
        bar_code=self.lineEdit_12.text()
        date=datetime.datetime.now()
     
        
        self.cur.execute('''
            INSERT INTO books (title,description,category_id,code,bar_code,part_order,price,publisher_id,author_id,status,date)
            VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        ''',(book_title,description,category,code,bar_code,part_order,price,author,puplisher,status,date))
        global employee_id ,employee_branch
        print(employee_id)

        action=4
        table=0


        self.cur.execute('''
            INSERT INTO history (employee_id,employee_action,affected_table,operation_date,employee_branch,data)
            VALUES (%s,%s,%s,%s,%s,%s)
        ''',(employee_id,action,table,date,employee_branch,book_title))


        self.db.commit()
        print('done')
        self.Show_History()
        self.statusBar().showMessage('تم اضافه الكتاب بنجاح')
        self.Show_All_Books()
    
    def Edit_Book_Search(self):
        ##edit book
        book_code=self.lineEdit_19.text()
        sql=(''' SELECT * FROM books WHERE code = %s ''')
        self.cur.execute(sql,[(book_code)])
        data = self.cur.fetchone()
        print(data)
        self.lineEdit_18.setText(data[1])
        self.comboBox_18.setCurrentIndex(int(data[10]))
        self.lineEdit_20.setText(str(data[6]))
        self.textEdit_4.setPlainText(data[2])
        self.comboBox_17.setCurrentIndex(int(data[11]))
        self.comboBox_16.setCurrentIndex(int(data[12]))
        self.comboBox_15.setCurrentIndex(int(data[8]))
        self.lineEdit_17.setText(str(data[5]))
    
    def Edit_book(self):
        book_title = self.lineEdit_18.text()
        category=self.comboBox_18.currentIndex()
    
        description=self.textEdit_4.toPlainText()
        price=self.lineEdit_20.text()
        code=self.lineEdit_19.text()
        puplisher=self.comboBox_17.currentIndex()

        author = self.comboBox_16.currentIndex()
    
        status=self.comboBox_15.currentIndex()
        part_order=self.lineEdit_17.text()
        date=datetime.datetime.now()
        self.cur.execute('''
            UPDATE books SET title=%s ,description=%s,code=%s,part_order=%s,price=%s,status=%s,category_id=%s,publisher_id=%s,author_id=%s  WHERE code =%s           
        ''',(book_title, description,code,part_order,price,status,category,puplisher,author,code))

        global employee_id ,employee_branch
        print(employee_id)

        action=3
        table=0

        self.cur.execute('''
            INSERT INTO history (employee_id,employee_action,affected_table,operation_date,employee_branch,data)
            VALUES (%s,%s,%s,%s,%s,%s)
        ''',(employee_id,action,table,date,employee_branch,book_title))





        self.db.commit()
        print('done')
        self.Show_History()
        self.statusBar().showMessage('تم تعديل معلومات الكتاب بنجاح')
        #QMessageBox.information(self,"Success",'تم تعديل معلومات الكتاب بنجاح')
        self.Show_All_Books
        
        
    
    
    def Delete_Book(self):
        #delete book from db
        book_code=self.lineEdit_19.text()
        date = datetime.datetime.now()
        global employee_id ,employee_branch


        action=5
        table=1

        self.cur.execute('''
            INSERT INTO history (employee_id,employee_action,affected_table,operation_date,employee_branch,data)
            VALUES (%s,%s,%s,%s,%s,%s)
        ''',(employee_id,action,table,date,employee_branch,book_code))



        sql=('''
             DELETE FROM books WHERE code =%s
        ''')
        self.cur.execute(sql,[( book_code)])
        self.db.commit()
        self.Show_History()
        self.Show_All_Books()
        self.statusBar().showMessage('تم مسح الكتاب بنجاح')
    
    ############### Clients ###############################
    
    
    def Show_All_Clients(self):
        ##show all Clients
        self.tableWidget_6.setRowCount(0)
        self.tableWidget_6.insertRow(0)
        
        self.cur.execute('''
            SELECT name ,mail ,phone,national_id, date  FROM clients
        ''')
        data=self.cur.fetchall()
        for row ,form in enumerate(data):
            for col , item in enumerate(form):
                self.tableWidget_6.setItem(row,col,QTableWidgetItem(str(item)))
                col += 1
            row_position=self.tableWidget_6.rowCount()
            self.tableWidget_6.insertRow(row_position)
    
    
    
    def Add_New_Client(self):
        #add new Clients
        client_name=self.lineEdit_23.text()
        client_email=self.lineEdit_22.text()
        client_phone=self.lineEdit_24.text()
        client_national_id=self.lineEdit_25.text()
        date=datetime.datetime.now()
        self.cur.execute('''
            INSERT INTO clients (name,mail, phone,date,national_id)
            VALUES(%s,%s,%s,%s,%s)
        ''',(client_name,client_email,client_phone, date,client_national_id))
        global employee_id ,employee_branch
        date = datetime.datetime.now()
        action=3
        table=2

        self.cur.execute('''
            INSERT INTO history (employee_id,employee_action,affected_table,operation_date,employee_branch,data)
            VALUES (%s,%s,%s,%s,%s,%s)
        ''',(employee_id,action,table,date,employee_branch,client_name))

        self.db.commit()
        self.Show_History()
        self.statusBar().showMessage('تم اضافه العميل بنجاح')
        self.Show_All_Clients()
    
    def Edit_Client_Search(self):
        ##edit Clients
        client_data=self.lineEdit_30.text()

        
        if self.comboBox_19.currentIndex()==0:
            sql=(''' SELECT * FROM clients WHERE name = %s ''')
            self.cur.execute(sql,[(client_data)])
            data = self.cur.fetchone()
            print(data)
            
        if self.comboBox_19.currentIndex()==1:
            sql=(''' SELECT * FROM clients WHERE mail = %s ''')
            self.cur.execute(sql,[(client_data)])
            data = self.cur.fetchone()
            print(data)
        if self.comboBox_19.currentIndex()==2:
            sql=(''' SELECT * FROM clients WHERE phone = %s ''')
            self.cur.execute(sql,[(client_data)])
            data = self.cur.fetchone()
            print(data)
        if self.comboBox_19.currentIndex()==3:
            sql=(''' SELECT * FROM clients WHERE national_id = %s ''')
            self.cur.execute(sql,[(client_data)])
            data = self.cur.fetchone()
            print(data)


        self.lineEdit_28.setText(str(data[1]))
        self.lineEdit_27.setText(data[2])
        self.lineEdit_29.setText(data[3])
        self.lineEdit_26.setText(str(data[5]))
    
    def Edit_client(self):

            client_name=self.lineEdit_28.text()
            client_mail=self.lineEdit_27.text()
            client_phone=self.lineEdit_29.text()
            client_id=self.lineEdit_26.text()
            
            self.cur.execute('''
                UPDATE clients SET name = %s , mail = %s , phone = %s , national_id =%s WHERE  mail=%s
            ''',(client_name , client_mail , client_phone ,client_id ,client_mail))

            global employee_id, employee_branch
            date = datetime.datetime.now()
            action = 4
            table = 2

            self.cur.execute('''
                INSERT INTO history (employee_id,employee_action,affected_table,operation_date,employee_branch,data)
                VALUES (%s,%s,%s,%s,%s,%s)
            ''', (employee_id, action, table, date, employee_branch,client_name))

            self.db.commit()
            self.Show_All_Clients
            self.statusBar().showMessage('تم تعديل الداتا بنجاح')
            self.Show_History()

        
            
        

        
        
    
    def Delete_Client(self):
        #delete Clients from db
        client_data=self.pushButton_24.text()
        date = datetime.datetime.now()
        
        if self.comboBox_19.currentIndex()==0:
            sql=(''' DELETE  FROM clients WHERE name = %s ''')
            self.cur.execute(sql,[(client_data)])

                
        if self.comboBox_19.currentIndex()==1:
            sql=(''' DELETE FROM clients WHERE mail = %s ''')
            self.cur.execute(sql,[(client_data)])
                
        if self.comboBox_19.currentIndex()==2:
            sql=(''' DELETE FROM clients WHERE phone = %s ''')
            self.cur.execute(sql,[(client_data)])
                
        if self.comboBox_19.currentIndex()==3:
            sql=(''' DELETE  FROM clients WHERE national_id = %s ''')
            self.cur.execute(sql,[(client_data)])

        global employee_id ,employee_branch

        action=5
        table=2
        date = datetime.datetime.now()
        self.cur.execute('''
            INSERT INTO history (employee_id,employee_action,affected_table,operation_date,employee_branch,data)
            VALUES (%s,%s,%s,%s,%s,%s)
        ''',(employee_id,action,table,date,employee_branch,client_data))




        self.db.commit()
        self.Show_History()
        self.statusBar().showMessage('تم مسح العميل بنجاح')
        self.Show_All_Clients()
          
    
    ###################### History ###########################  
    
    def Show_History(self):
        #show All History
        self.tableWidget_7.setRowCount(0)
        self.tableWidget_7.insertRow(0)

        self.cur.execute('''
             SELECT employee_id,employee_branch ,employee_action ,affected_table,operation_date,data FROM history
         ''')
        data = self.cur.fetchall()
        for row, form in enumerate(data):
            for col, item in enumerate(form):
                if col == 0:
                    sql = "SELECT name FROM employee WHERE id=%s "
                    self.cur.execute(sql, [(item)])
                    employee_name = self.cur.fetchone()
                    self.tableWidget_7.setItem(row, col, QTableWidgetItem(str(employee_name[0])))
                elif col == 1:
                    sql = "SELECT name FROM branch WHERE id=%s "
                    self.cur.execute(sql, [(item)])
                    branch_name = self.cur.fetchone()
                    self.tableWidget_7.setItem(row, col, QTableWidgetItem(str(branch_name[0])))

                elif  col == 2:
                    action=''
                    if item==1:
                        action='Login'
                    if item == 2:
                        action = 'Logout'
                    if item == 3:
                        action = 'Add'
                    if item == 4:
                        action = 'Edit'
                    if item == 5:
                        action = 'Delete'
                    if item == 6:
                        action = 'Search'

                    self.tableWidget_7.setItem(row, col, QTableWidgetItem(str(action)))

                elif  col == 3:
                    table = ''
                    if item == 1:
                        table = 'Books'
                    if item == 2:
                        table = 'Clients'
                    if item == 3:
                        table = 'History'
                    if item == 4:
                        table = 'Branch'
                    if item == 5:
                        table = 'Category'
                    if item == 6:
                        table = 'Daily Movements'
                    if item == 7:
                         table = 'Employee'
                    if item == 8:
                        table = 'Publisher'
                    if item == 9:
                        table = 'Author'
                    self.tableWidget_7.setItem(row, col, QTableWidgetItem(str(table)))
                else:
                    self.tableWidget_7.setItem(row, col, QTableWidgetItem(str(item)))
                col += 1
            row_position = self.tableWidget_7.rowCount()
            self.tableWidget_7.insertRow(row_position)
    
    ########################## Books report ###################################


    def logout_Button(self):
        # Create a new instance of the Page class
        self.Page = Page()
        self.close()
        self.Page.show()




    def Book_Export_Report(self):
        #export books data to excel file
        self.cur.execute('''
            SELECT code ,title ,category_id ,author_id ,price FROM books
        ''')
        data=self.cur.fetchall()
        excel_file=Workbook('bookS_report.xlsx')
        sheet1=excel_file.add_worksheet()
        
        sheet1.write(0,0,'Book code')
        sheet1.write(0,1,'Book title')
        sheet1.write(0,2,'Category')
        sheet1.write(0,3,'Author')
        sheet1.write(0,4,'Price')
        
        row_number=1
        for row in data:
            column_number=0
            for item in row:
                sheet1.write(row_number,column_number,str(item))
                column_number+=1
            row_number +=1
        excel_file.close()
        self.statusBar().showMessage('تم انشاء التقرير بنجاح')
        
        
        
    ########################## Client Report ######################################
    






    def Client_Export_Report(self):
        #export Clients data to excel file
        self.cur.execute('''
            SELECT name , mail , phone ,national_id FROM clients
        ''')

        data=self.cur.fetchall()
        print(data)
        excel_file=Workbook('Client_report.xlsx')
        sheet1=excel_file.add_worksheet()
        
        sheet1.write(0,0,'Client Name')
        sheet1.write(0,1,'Client mail')
        sheet1.write(0,2,'Client phone')
        sheet1.write(0,3,'national_id')

        
        row_number=1
        for row in data:
            column_number=0
            for item in row:
                sheet1.write(row_number,column_number,str(item))
                column_number+=1
            row_number +=1
        excel_file.close()
        self.statusBar().showMessage('تم انشاء التقرير بنجاح')
                
        
    

    
    ####################### Settings ########################
    
    def Add_Branch(self):
       branch_name=self.lineEdit_37.text()
       branch_code=self.lineEdit_38.text()
       branch_location=self.lineEdit_39.text()
       self.cur.execute('''
            INSERT INTO branch (name,code,location)
            VALUES(%s , %s , %s)               
            ''',(branch_name,branch_code,branch_location))

       global employee_id, employee_branch
       date = datetime.datetime.now()
       action = 3
       table = 4

       self.cur.execute('''
           INSERT INTO history (employee_id,employee_action,affected_table,operation_date,employee_branch,data)
           VALUES (%s,%s,%s,%s,%s,%s)
       ''', (employee_id, action, table, date, employee_branch,branch_name))


       self.db.commit()
       self.Show_History()
       print('Branch Added')
        
    def Add_Category(self):
        #add new categroy
        categroy_name=self.lineEdit_49.text()
        parent_categroy_Text=self.comboBox_21.currentIndex()
        

        
        self.cur.execute('''
            INSERT INTO category(Category_name,parent_category)
            VALUES(%s,%s)               
            ''', (categroy_name,parent_categroy_Text))

        global employee_id ,employee_branch
        date = datetime.datetime.now()
        action=3
        table=5

        self.cur.execute('''
            INSERT INTO history (employee_id,employee_action,affected_table,operation_date,employee_branch,data)
            VALUES (%s,%s,%s,%s,%s,%s)
        ''',(employee_id,action,table,date,employee_branch,categroy_name))

        self.db.commit()
        self.Show_History()
        print('Category Added')
        self.Show_All_Categories()        
        
    
    def Add_Puplisher(self):
        publisher_name=self.lineEdit_40.text()
        publisher_location=self.lineEdit_41.text()
        self.cur.execute('''
            INSERT INTO publisher (name,location)
            VALUES(%s , %s )               
            ''',( publisher_name,publisher_location))

        global employee_id ,employee_branch
        date = datetime.datetime.now()
        action=3
        table=8

        self.cur.execute('''
            INSERT INTO history (employee_id,employee_action,affected_table,operation_date,employee_branch,data)
            VALUES (%s,%s,%s,%s,%s,%s)
        ''',(employee_id,action,table,date,employee_branch,publisher_name))


        self.db.commit()
        self.Show_History()
        print('Puplisher Added')
       
    
    
    
    def Add_Author(self):
        author_name=self.lineEdit_43.text()
        author_location=self.lineEdit_44.text()
        self.cur.execute('''
            INSERT INTO author (name,location)
            VALUES(%s , %s )               
            ''',( author_name,author_location))

        global employee_id ,employee_branch
        date = datetime.datetime.now()
        action=3
        table=9

        self.cur.execute('''
            INSERT INTO history (employee_id,employee_action,affected_table,operation_date,employee_branch,data)
            VALUES (%s,%s,%s,%s,%s,%s)
        ''',(employee_id,action,table,date,employee_branch,author_name))

        self.db.commit()
        self.Show_History()
        print('Author Added') 
    
    ###########################################################
    def Show_All_Categories(self):
        self.comboBox_21.clear()
        self.cur.execute('''
            SELECT Category_name FROM category
        ''')
        categories = self.cur.fetchall()
        #print(categories)
        for category in categories:
            self.comboBox_21.addItem(str(category[0]))
            self.comboBox_4.addItem(str(category[0]))
            self.comboBox_3.addItem(str(category[0]))
            self.comboBox_18.addItem(str(category[0]))

            
            
            
    
    def Show_Branchies(self):
        self.cur.execute('''
            SELECT name FROM branch
        ''')
        branchies =self.cur.fetchall()
        for branch in branchies :
            self.comboBox_6.addItem(branch[0])
            self.comboBox_5.addItem(branch[0])
            
            
    def Show_Puplishers(self):
        self.cur.execute('''
            SELECT name FROM publisher
        ''')
        publishers=self.cur.fetchall()
        for publisher in publishers:
            self.comboBox_7.addItem(publisher[0])
            self.comboBox_17.addItem(publisher[0])


            
    def Show_Authors(self):
        self.cur.execute('''
            SELECT name FROM author
        ''')
        authors =self.cur.fetchall()
        for author in authors:
            self.comboBox_8.addItem(author[0])
            self.comboBox_16.addItem(author[0])
        
    def Show_Employee(self):
        self.cur.execute('''
                SELECT name FROM employee
        ''')
        employees=self.cur.fetchall()
        for employee in employees:
            self.comboBox_27.addItem(employee[0])
            self.comboBox_28.addItem(employee[0])

    
    
    
               
    
    
    ############ setting add or edit Employee############
    
    def Add_Employee(self):
        ##add new employee
        employee_name=self.lineEdit_52.text()
        employee_mail=self.lineEdit_53.text()
        employee_phone=self.lineEdit_54.text()
        branch=self.comboBox_5.currentIndex()
        employee_national_id=self.lineEdit_55.text()
        periority=self.lineEdit_58.text()
        password=self.lineEdit_56.text()
        password2=self.lineEdit_57.text()
        date=datetime.datetime.now()
        if password == password2:
            self.cur.execute('''
                INSERT INTO employee (name,mail,phone,branch,national_id,Periority,password,date)
                VALUES (%s ,%s ,%s ,%s ,%s,%s,%s,%s)
            ''',(employee_name,employee_mail,employee_phone, branch,employee_national_id,periority, password,date))

            global employee_id, employee_branch
            date = datetime.datetime.now()
            action = 3
            table = 7

            self.cur.execute('''
                INSERT INTO history (employee_id,employee_action,affected_table,operation_date,employee_branch,data)
                VALUES (%s,%s,%s,%s,%s,%s)
            ''', (employee_id, action, table, date, employee_branch,employee_mail))

            self.db.commit()
            self.Show_History()
            self.lineEdit_52.setText('')
            self.lineEdit_53.setText('')
            self.lineEdit_54.setText('')
            self.lineEdit_55.setText('')
            self.lineEdit_58.setText('')
            self.lineEdit_56.setText('')
            self.lineEdit_57.setText('')
            self.statusBar().showMessage('تم اضافه الموظف بنجاح')
            
            
        else:
            print('wrong password')
        
    def Check_Employee(self):
        employee_name= self.lineEdit_64.text()
        employee_password=self.lineEdit_69.text()
        
        #sql=""" SELECT name,password FROM employee """
        #for row in self.cur.execute(sql):
        #    print(row)
        self.cur.execute(""" SELECT * FROM employee  """)
        data=self.cur.fetchall()
        print(data)
        for row in data:
            if row[1]==employee_name and row[7]==employee_password:
                self.groupBox_11.setEnabled(True)
                self.lineEdit_66.setText(row[2])
                self.lineEdit_65.setText(row[3])
                self.comboBox_6.setCurrentIndex(row[8])
                self.lineEdit_67.setText(str(row[5]))
                self.lineEdit_59.setText(str(row[6]))
                self.lineEdit_68.setText(str(row[7]))
            
        
    def Edit_Employee_Data(self):
        ##edit employee data
        employee_name=self.lineEdit_64.text()
        employee_password=self.lineEdit_69.text()
        employee_email=self.lineEdit_66.text()
        employee_phone=self.lineEdit_65.text()
        employee_branch_=self.comboBox_6.currentIndex()
        employee_id_=self.lineEdit_67.text()
        employee_periority=self.lineEdit_59.text()
        employee_password2=self.lineEdit_68.text()

        
        if employee_password == employee_password2:
            self.cur.execute('''
                UPDATE employee SET mail=%s,phone=%s ,national_id=%s ,Periority=%s,password=%s , branch=%s  WHERE mail=%s  
            ''',( employee_email,employee_phone, employee_id_,employee_periority,employee_password2,employee_branch_,employee_email))

            global employee_id, employee_branch
            action = 4
            table = 7
            date = datetime.datetime.now()
            self.cur.execute('''
                INSERT INTO history (employee_id,employee_action,affected_table,operation_date,employee_branch,data)
                VALUES (%s,%s,%s,%s,%s,%s)
            ''',(employee_id,action,table,date,employee_branch,employee_email))


        self.db.commit()
        self.Show_History()
        self.statusBar().showMessage('تم تعديل البيانات بنجاح')
        
    ############ setting user permisions############
    
    def Add_Employee_Permissions(self):
        #add permission to all any employee
        employee_name=self.comboBox_27.currentText()
        
        if self.checkBox_41.isChecked()==True:
            self.cur.execute('''
                INSERT employe_permissions (empolyee_name,books_tab,client_tab,dashbord_tab,history_tab,reports_tab,settings_tab,
               add_book,edit_book,delete_book,import_book,export_book,add_client,
               edit_client,delete_client,import_client,export_client,
               add_branch,add_publisher,add_author,add_category,add_employee,edit_employee,is_admin)
                VALUES (%s ,%s ,%s ,%s ,%s ,%s , %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            ''', (employee_name,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1))
            self.db.commit()
            print('permissions addd')
            self.statusBar().showMessage('تم اضافه كل الصلاحيات للموظف بنجاح')
        else:
        
            books_tap=0
            clients_tap=0
            dashbord=0
            history=0
            reports_tab=0
            setting=0
            
            add_book=0
            edit_book=0
            delete_book=0
            import_book=0
            export_book=0
            
            add_client=0
            edit_client=0
            delete_client=0
            import_client=0
            export_client=0
            
            add_branch=0
            add_publisher=0
            add_author=0
            add_category=0
            add_employee=0
            edit_employee=0
                    #taps#
            if self.checkBox_8.isChecked()==True:
                books_tap=1
            if self.checkBox_7.isChecked()==True:
                clients_tap=1
            if self.checkBox_9.isChecked()==True:
                dashbord=1
            if self.checkBox_11.isChecked()==True:
                history=1
            if self.checkBox_10.isChecked()==True:
                reports_tab=1
            if self.checkBox_12.isChecked()==True:
                setting=1 
                
                #books#
            if self.checkBox.isChecked()==True:
                add_book=1
            if self.checkBox_2.isChecked()==True:
                edit_book=1
            if self.checkBox_3.isChecked()==True:
                delete_book=1
            if self.checkBox_28.isChecked()==True:
                import_book=1
            if self.checkBox_27.isChecked()==True:
                export_book=1
                
                #clients#
            if self.checkBox_5.isChecked()==True:
                add_category=1
            if self.checkBox_4.isChecked()==True:
                edit_client=1
            if self.checkBox_6.isChecked()==True:
                delete_cleint=1
            if self.checkBox_37.isChecked()==True:
                import_client=1
            if self.checkBox_36.isChecked()==True:
                export_client=1
                
                #settings#
            if self.checkBox_34.isChecked()==True:
                add_branch=1
            if self.checkBox_35.isChecked()==True:
                add_publisher=1
            if self.checkBox_33.isChecked()==True:
                add_author=1
            if self.checkBox_39.isChecked()==True:
                add_category=1
            if self.checkBox_38.isChecked()==True:
                add_employee=1
            if self.checkBox_40.isChecked()==True:
                edit_employee=1
                

                
            self.cur.execute('''
                INSERT employe_permissions (empolyee_name,books_tab,client_tab,dashbord_tab,history_tab,reports_tab,settings_tab,
               add_book,edit_book,delete_book,import_book,export_book,add_client,
               edit_client,delete_client,import_client,export_client,
               add_branch,add_publisher,add_author,add_category,add_employee,edit_employee)
                VALUES (%s ,%s ,%s ,%s ,%s ,%s , %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            ''', (employee_name,books_tap,clients_tap,dashbord,history,reports_tab,setting,
                  add_book,edit_book,delete_book,import_book,export_book,
                  add_client,edit_client,delete_client,import_client,edit_client,
                  add_branch,add_publisher,add_author,add_category,add_employee,edit_employee))
            self.db.commit()
            print('permissions addd')
            self.statusBar().showMessage('تم اضافه الصلاحيات للموظف بنجاح')
            
    def Admin_Report(self):
        #send report to the admin
        pass
#################################### Open taps #########################

        
    def Open_Daily_movements_Tab(self):
        self.tabWidget.setCurrentIndex(0)
        print('Daily Movements Tap ')
    
    def Open_Books_Tap(self):
       self.tabWidget.setCurrentIndex(1)
       print('Books Tap ')
       
    def Open_Clients_Tap(self):
        self.get_dashbord_data()
        self.tabWidget.setCurrentIndex(2)
        print('Clients Tap ')
        
    def Open_Dashboard_Tap(self):
        self.tabWidget.setCurrentIndex(3)
        print('Dashbord Tap ')
        
    def Open_History_Tap(self):
        self.tabWidget.setCurrentIndex(4)
        print('History Tap ')
        
    def Open_Report_Tap(self):
        self.tabWidget.setCurrentIndex(5)
        print('Report Tap ')  
    
    def Open_Settings_Tap(self):
        self.tabWidget.setCurrentIndex(6)
        print('Settings Tap ')

        ################### User_login#################











    #########dashbord##############
    def get_dashbord_data(self):


        filter_date=self.dateEdit_7.date()
        filter_date = filter_date.toPyDate()
        year = (str(filter_date).split('-')[0])
        print(year)


        #######
        self.cur.execute(
            """
            SELECT COUNT(book_id), EXTRACT(MONTH FROM Book_from) AS month
            FROM daily_movements
            WHERE year(Book_from) =%s
            GROUP BY month;
            """%(year))

        data_ = self.cur.fetchall()

        book_conut=[]
        rent_count=[]

        for row in data_:
            book_conut.append(row[0])
            rent_count.append(row[1])

        barchart=pg.BarGraphItem(x=rent_count,height=book_conut,width=.2)
        self.widget.addItem(barchart)
        self.widget.setTitle('التعاملات')
        self.widget.addLegend()
        self.widget.setLabel('left','عدد الكتب المعاره',color='red',size=40)
        self.widget.setLabel('bottom', 'الشهر', color='red', size=40)
        self.widget.showGrid(x=True , y=True)



    def Report_Export (self):
        self.cur.execute('''
                    SELECT title , code , category_id,author_id ,status FROM books
                ''')

        data = self.cur.fetchall()
        print(data)
        excel_file = Workbook('Report Book.xlsx')
        sheet1 = excel_file.add_worksheet()

        sheet1.write(0, 0, 'Title')
        sheet1.write(0, 1, 'Code')
        sheet1.write(0, 2, 'Category')
        sheet1.write(0, 3, 'Author')
        sheet1.write(0, 4, 'Status')

        row_number = 1
        for row in data:
            column_number = 0
            for item in row:
                sheet1.write(row_number, column_number, str(item))
                column_number += 1
            row_number += 1
        excel_file.close()
        QMessageBox.about(self, "عمليه ناجحه", "تم انشاء التقرير بنجاح")



def main():
    app =QApplication(sys.argv)
    window=page2()
    window.show()
    app.exec_()
    
    
if __name__ =='__main__':
    main()
    