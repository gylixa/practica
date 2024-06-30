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
        print(1)
        person = Gr.A[key]
        win.tableWidget.setItem(row, 0, QTableWidgetItem(person.fam + ' ' + person.name + ' ' + person.surname))
        win.tableWidget.setItem(row, 1, QTableWidgetItem(str(person.department)))
        win.tableWidget.setItem(row, 2, QTableWidgetItem(str(person.days)))
        win.tableWidget.setItem(row, 3, QTableWidgetItem(str(person.salary)))
        
        row += 1


def btnAppendPerson():
    
    strPerson = win.lineEdit.text()
   
    Gr.appendPerson(strPerson)
  
    win.tableWidget.clear()
    btnLoadTable()

    

win.pushButton.clicked.connect(btnLoadTable)
print(Gr.A[0].getPerson_forTable())

win.pushButton_3.clicked.connect(btnAppendPerson)

win.show()
sys.exit(app.exec())
