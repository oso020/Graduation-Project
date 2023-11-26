
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
from login import *
from index import *
from main import *

LoginUI,_= loadUiType('login.ui')


employee_id=1
class Page(QWidget ,LoginUI):
    def __init__(self, parent=None):
        super(Page ,self).__init__(parent)
        QWidget.__init__(self)
        self.setupUi(self)
        self.Handle_Button()
        self.Ui_Handle()
        self.Db_Connect_login()


    def Handle_Button(self):
        self.pushButton.clicked.connect(self. User_login_Permissions)
        self.pushButton_3.clicked.connect(self.Reset_Button)
        self.pushButton_4.clicked.connect(self.Back_Button)


    def Db_Connect_login(self):
        ## connection between app and Database
        self.db = MySQLdb.connect(host='localhost', user='root', password='',db='library')
        self.cur=self.db.cursor()
        print('Connection Succsfully')


    def Ui_Handle(self):
        self.tabWidget.tabBar().setVisible(False)
        self.setWindowTitle('Login - Osmanyat')
        self.setWindowIcon(QtGui.QIcon('login.png'))






    def User_login_Permissions(self):
        try:
            username=self.lineEdit_2.text()
            password=self.lineEdit_3.text()

            self.cur.execute('''
                    SELECT id,name , password,branch FROM employee
                ''')
            data_=self.cur.fetchall()


            for row in data_:
                if row[1] == username and row[2] == password:
                    self.page2 = page2()
                    self.page2.show()
                    Page.hide(self)
                    self.cur.execute('''
                                                SELECT * FROM employe_permissions WHERE empolyee_name =%s
                                            ''', (username,))
                    user_permissions = self.cur.fetchone()
                    self.page2.pushButton.setEnabled(True)
                    self.page2.groupBox_16.setEnabled(True)
                    global employee_id, employee_branch
                    employee_id = row[0]
                    print(employee_id)


                    if user_permissions[2] == 1:
                        self.page2.pushButton_2.setEnabled(True)

                    if user_permissions[3] == 1:
                        self.page2.pushButton_3.setEnabled(True)

                    if user_permissions[4] == 1:
                        self.page2.pushButton_4.setEnabled(True)

                    if user_permissions[5] == 1:
                        self.page2.pushButton_6.setEnabled(True)

                    if user_permissions[6] == 1:
                        self.page2.pushButton_5.setEnabled(True)

                    if user_permissions[7] == 1:
                        self.page2.pushButton_7.setEnabled(True)

                    if user_permissions[8] == 1:
                        self.page2.pushButton_17.setEnabled(True)

                    if user_permissions[9] == 1:
                        self.page2.pushButton_19.setEnabled(True)

                    if user_permissions[10] == 1:
                        self.page2.pushButton_20.setEnabled(True)
                    if user_permissions[11] == 1:
                        self.page2.pushButton_30.setEnabled(True)
                    if user_permissions[12] == 1:
                        self.page2.pushButton_16.setEnabled(True)

                    if user_permissions[13] == 1:
                        self.page2.pushButton_21.setEnabled(True)
                    if user_permissions[14] == 1:
                        self.page2.pushButton_22.setEnabled(True)
                        

                    if user_permissions[15] == 1:
                        self.page2.pushButton_24.setEnabled(True)

                    if user_permissions[16] == 1:
                        self.page2.pushButton_30.setEnabled(True)

                    if user_permissions[17] == 1:
                        self.page2.pushButton_16.setEnabled(True)

                    if user_permissions[18] == 1:
                        self.page2.pushButton_27.setEnabled(True)

                    if user_permissions[19] == 1:
                        self.page2.pushButton_28.setEnabled(True)

                    if user_permissions[20] == 1:
                        self.page2.pushButton_29.setEnabled(True)

                    if user_permissions[21] == 1:
                        self.page2.pushButton_32.setEnabled(True)

                    if user_permissions[22] == 1:
                        self.page2.pushButton_37.setEnabled(True)

                    if user_permissions[23] == 1:
                        self.page2.pushButton_39.setEnabled(True)



                    date = datetime.datetime.now()
                    action = 1
                    table = 7

                    self.cur.execute('''
                                      INSERT INTO history (employee_id,employee_action,affected_table,operation_date,employee_branch,data)
                                      VALUES (%s,%s,%s,%s,%s,%s)
                                  ''', (employee_id, action, table, date, employee_branch, username))
                    self.db.commit()
                    self.page2.Show_History()

        except:
            if row[1] != username   and row[2] != password:
                 QMessageBox.about(self, "Error", "User Or Password Is InCorrect")

 

    def Reset_Button(self):
        self.tabWidget.setCurrentIndex(1)

    def Back_Button(self):
        self.tabWidget.setCurrentIndex(0)












def main():
    app = QApplication(sys.argv)
    window = Page()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()