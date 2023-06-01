from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
import sys

width = 800
height = 400


class win_RFproPE(QMainWindow):
    def __init__(self):
        super(win_RFproPE, self).__init__()
        self.setGeometry(100, 100, width, height)
        self.setWindowTitle("RFproPE v1.0 rev0")
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("test")
        self.label.move(100, 0)

        self.btnInit = QtWidgets.QPushButton(self)
        self.btnInit.setText("Initialize")
        # self.btnInit.clicked.connect

        self.Cmbx = QtWidgets.QComboBox(self)
        self.Cmbx.setGeometry(0, 100, 200, 20)
        self.Cmbx.addItems(["Test1", "Test2"])
        self.Cmbx.setCurrentIndex(1)
        print(self.Cmbx.currentIndex())
        print(self.Cmbx.findText("Test2"))
        print(self.Cmbx.currentText())

    def btnInitialize_Click(self):
        self.label.setText("Init pressed")
        self.update()

    def update(self):
        self.label.adjustSize()

    def show_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("RFproPE... Critical error")
        msg.setText("Main text")
        msg.setIcon(QMessageBox.Critical)
        msg.setStandardButtons(
            QMessageBox.Ignore | QMessageBox.Retry | QMessageBox.Cancel
        )
        msg.setDefaultButton(QMessageBox.Retry)
        msg.setInformativeText("Informatiove text...")
        msg.setDetailedText("Detailed text")
        msg.buttonClicked.connect(self.popup_button)

        x = msg.exec_()

    def popup_button(self, i):
        print(i.text())


def window():
    app = QApplication(sys.argv)
    win = win_RFproPE()
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    from random import randint as r

#    x = r(1, 5)
#    y = 3
#    z = x / y
#    print(x, y, z)
    window()
