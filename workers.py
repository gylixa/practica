from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QWidget, QTextEdit, QPushButton, QTableWidget, QTableWidgetItem
import sys
from library import *

app = QtWidgets.QApplication([])
win = uic.loadUi("workers.ui")

Gr = Grup()
Gr.read_data_from_file("text.txt")
print("!!!", Gr.count)

def btnLoadTable():
    win.tableWidget.setRowCount(Gr.count)
    row = 0
    for key in Gr.A:
        person = Gr.A[key]
        win.tableWidget.setItem(row, 0, QTableWidgetItem(person.fam))
        win.tableWidget.setItem(row, 1, QTableWidgetItem(person.name))
        win.tableWidget.setItem(row, 2, QTableWidgetItem(person.surname))
        win.tableWidget.setItem(row, 3, QTableWidgetItem(str(person.department)))
        win.tableWidget.setItem(row, 4, QTableWidgetItem(str(person.days)))
        win.tableWidget.setItem(row, 5, QTableWidgetItem(str(person.salary)))
        row += 1

def btnAppendPerson():
    List = [str(win.lineEdit_4.text()), str(win.lineEdit_5.text()), str(win.lineEdit_6.text()),\
            str(win.lineEdit_7.text()), str(win.lineEdit_8.text()), str(win.lineEdit_9.text())]
    Gr.appendPerson(List)
    win.tableWidget.clear()
    btnLoadTable()

def btnEditPerson():
    if win.lineEdit_2.text() == '':
        win.lineEdit_2.setText('1')
    if win.lineEdit_3.text() == '':
        win.lineEdit_3.setText('1')

    x = int(win.lineEdit_2.text()) - 1
    y = int(win.lineEdit_3.text()) - 1

    if x <= win.tableWidget.rowCount() and y <= win.tableWidget.columnCount():
        List = [str(win.tableWidget.item(x, 0).text()),
                str(win.tableWidget.item(x, 1).text()),
                str(win.tableWidget.item(x, 2).text()),
                str(win.tableWidget.item(x, 3).text()),
                str(win.tableWidget.item(x, 4).text()),
                str(win.tableWidget.item(x, 5).text())]

        key = Gr.find_keyPerson(List)

        if key != -1:
            win.tableWidget.setItem(x, y, QTableWidgetItem(str(win.lineEdit.text())))

            List = [str(win.tableWidget.item(x, 0).text()),
                    str(win.tableWidget.item(x, 1).text()),
                    str(win.tableWidget.item(x, 2).text()),
                    str(win.tableWidget.item(x, 3).text()),
                    str(win.tableWidget.item(x, 4).text()),
                    str(win.tableWidget.item(x, 5).text())]

            print(List)
            Gr.editPerson(key, List)

def btnDelPerson():
    List = [str(win.lineEdit_4.text()), str(win.lineEdit_5.text()), str(win.lineEdit_6.text()),\
            str(win.lineEdit_7.text()), str(win.lineEdit_8.text()), str(win.lineEdit_9.text())]

    Gr.delPerson(List)
    win.tableWidget.clear()
    btnLoadTable()

win.pushButton.clicked.connect(btnLoadTable)
win.pushButton_3.clicked.connect(btnAppendPerson)
win.pushButton_4.clicked.connect(btnEditPerson)
win.pushButton_5.clicked.connect(btnDelPerson)

win.show()
sys.exit(app.exec())

