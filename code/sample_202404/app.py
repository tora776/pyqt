import sys
from PyQt5 import QtWidgets
from view import *
from mainForm import *

class App():
    def __init__(self) -> None:
        pass

    # 処理開始
    def exec(self):
        app = QtWidgets.QApplication(sys.argv)
        form = QtWidgets.QWidget()
        ui = Ui_Form()
        vm = viewMain(ui, form)
        form.show()
        sys.exit(app.exec_())

if __name__ == "__main__":
    app = App()
    app.exec()