from PyQt5 import QtCore, QtGui, QtWidgets
import sys, psycopg2


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(420, 382)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(10, 130, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.selectDB)
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 130, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.insert_data)

        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(170, 130, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(250, 130, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 40, 31, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 10, 31, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(40, 100, 31, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(40, 70, 31, 16))
        self.label_4.setObjectName("label_4")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(25, 161, 371, 191))
        self.tableWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tableWidget.setMidLineWidth(0)
        self.tableWidget.setRowCount(30)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(75)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(23)
        self.tableWidget.verticalHeader().setDefaultSectionSize(24)
        self.tableWidget.verticalHeader().setMinimumSectionSize(24)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(100, 10, 231, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 70, 231, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(100, 40, 231, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_5 = QtWidgets.QLineEdit(Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(100, 100, 231, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "表示"))
        self.pushButton_2.setText(_translate("Form", "追加"))
        self.pushButton_3.setText(_translate("Form", "更新"))
        self.pushButton_4.setText(_translate("Form", "削除"))
        self.label.setText(_translate("Form", "住所"))
        self.label_2.setText(_translate("Form", "名前"))
        self.label_3.setText(_translate("Form", "mail"))
        self.label_4.setText(_translate("Form", "TEL"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "名前"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "住所"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "TEL"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "mail"))


    def selectDB(self):
        # PostgreSQLに接続してデータを取得する
        try:
            conn =  psycopg2.connect('postgresql://{user}:{password}@{host}:{port}/{dbname}'.format( 
                    user="postgres",        #ユーザ
                    password="root",  #パスワード
                    host="localhost",       #ホスト名
                    port="5432",            #ポート
                    dbname="accounts"))    #データベース名
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM account")
            records = cursor.fetchall()
            for row_number, row_data in enumerate(records):
                for column_number, data in enumerate(row_data):
                    item = QtWidgets.QTableWidgetItem(str(data))
                    self.tableWidget.setItem(row_number, column_number, item)
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)
        finally:
            # 接続をクローズ
            if conn:
                cursor.close()
                conn.close()
                print("PostgreSQL connection is closed")

    def insert_data(self):
        # 入力されたデータを取得
        name = self.lineEdit.text()
        address = self.lineEdit_2.text()
        tel = self.lineEdit_3.text()
        mail = self.lineEdit_5.text()

        # PostgreSQL に接続してデータを挿入
        try:
            conn = psycopg2.connect(
                user="postgres",
                password="root",
                host="localhost",
                port="5432",
                dbname="accounts"
            )
            cursor = conn.cursor()
            cursor.execute("INSERT INTO account (name, address, tel, mail) VALUES (%s, %s, %s, %s)",
                           (name, address, tel, mail))
            conn.commit()
            print("Data inserted successfully")
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)
        finally:
            # 接続をクローズ
            if conn:
                cursor.close()
                conn.close()
                print("PostgreSQL connection is closed")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
