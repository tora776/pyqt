from PyQt5 import QtCore, QtWidgets

from sql import *

class viewMain():
    def __init__(self, ui, form) -> None:
        self.ui = ui
        self.ui.setupUi(form)
        self.db = DB()

        self.ui.pushButton.clicked.connect(self.onClickSelectBtn)
        self.ui.pushButton_2.clicked.connect(self.onClickInsertBtn)
        self.ui.pushButton_3.clicked.connect(self.onClickUpdateBtn)
        self.ui.pushButton_4.clicked.connect(self.onClickDeleteBtn)

        self.ids = []  # ids リストを初期化    

    ###################################
    # イベントハンドラ
    ###################################
    # 表示ボタン押下
    def onClickSelectBtn(self):

        # データ取得
        datas = self.db.selectAll()
        # テーブルにデータ設定
        self.setTableData(datas)

    # 追加ボタン押下
    def onClickInsertBtn(self):
        
        # 入力値取得
        res = self.getInputTexts()
        # DB追加
        ret = self.db.insert_data(res['name'], res['address'], res['tel'], res['mail'])

    # 更新ボタン押下
    def onClickUpdateBtn(self):

        selected_row = self.getSelectedRow()
        if selected_row == -1:
            return

        # 選択した行の id を取得
        item_id = self.ids[selected_row]

        # 更新するデータを取得
        res = self.getInputTexts()
        # DB更新
        ret = self.db.update_data(res['name'], res['address'], res['tel'], res['mail'], item_id)


    # 削除ボタン押下
    def onClickDeleteBtn(self):

        selected_row = self.getSelectedRow()
        if selected_row == -1:
            return

        # 削除するデータを取得
        res = self.getSelectDatas(selected_row)
        # DB削除
        ret = self.db.delete_data(res['name'], res['address'], res['tel'], res['mail'])
        

    ###################################
    # コントローラ処理
    ###################################
    # テーブルコントロールにデータを設定
    def setTableData(self, datas):
        self.ids.clear()  # 現在のデータをクリア

        self.ui.tableWidget.setRowCount(len(datas))
        for row_number, row_data in enumerate(datas):
            for column_number, data in enumerate(row_data[1:]):  # id を除外してデータを設定
                item = QtWidgets.QTableWidgetItem(str(data))
                self.ui.tableWidget.setItem(row_number, column_number, item)
            # id を非表示で保存
            self.ids.append(row_data[0])
            item_id = QtWidgets.QTableWidgetItem(str(row_data[0]))
            item_id.setFlags(QtCore.Qt.ItemIsEnabled)  # 編集不可に設定
            self.ui.tableWidget.setItem(row_number, len(row_data)-1, item_id)  # 最後の列に id を追加

    # テキストの入力値取得
    def getInputTexts(self):
        
        ret = {}

        name = self.ui.lineEdit.text()
        address = self.ui.lineEdit_2.text()
        tel = self.ui.lineEdit_3.text()
        mail = self.ui.lineEdit_5.text()

        ret = {'name': name, 'address': address, 'tel': tel, 'mail': mail}

        return ret
    
    # テーブルコントロールの選択行のデータ取得
    def getSelectDatas(self, selected_row):
        
        ret = {}

        name = self.ui.tableWidget.item(selected_row, 0).text()
        address = self.ui.tableWidget.item(selected_row, 1).text()
        tel = self.ui.tableWidget.item(selected_row, 2).text()
        mail = self.ui.tableWidget.item(selected_row, 3).text()

        ret = {'name': name, 'address': address, 'tel': tel, 'mail': mail}

        return ret
    
    # テーブルコントロールの選択されている行取得
    def getSelectedRow(self):
        selected_row = self.ui.tableWidget.currentRow()
        if selected_row == -1:
            print("No row selected")
        return selected_row