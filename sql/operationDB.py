import sys, psycopg2
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from dialog import Ui_Form
 
class Test(QMainWindow, Ui_Form):
  def __init__(self,parent=None):
    super(Test, self).__init__(parent)
    self.setupUi(self)

  def connectDB(self):
    conn =  psycopg2.connect('postgresql://{user}:{password}@{host}:{port}/{dbname}'.format( 
                    user="postgres",        #ユーザ
                    password="root",  #パスワード
                    host="localhost",       #ホスト名
                    port="5432",            #ポート
                    dbname="accounts"))    #データベース名
    return conn
  
  def selectDB(self, conn):
    cur = conn.cursor()
    # cur.execute("SELECT * FROM account WHERE id = 1;")
    cur.execute("SELECT * FROM account;")
    results = cur.fetchall()

    cur.close()
    conn.close()
    return results

  def showKanji(self):
    # 漢字を押したとき
    return

  def showEnglish(self):
    # 英語を押したとき
    return

if __name__ == '__main__':
  app = QApplication(sys.argv)
  window = Test()
  window.show()
  sys.exit(app.exec_())