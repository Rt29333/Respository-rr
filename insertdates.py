
# 添加信息界面

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import Qt, QtGui, QtCore, QtWidgets
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
from main1 import *

class MainWindow2(object):
    def tianjia(self, MainWindow):
        MainWindow.setWindowTitle('添加信息')
        MainWindow.resize(500, 500)
        MainWindow.move(600, 200)
        MainWindow.move(600, 200)
        MainWindow.setWindowIcon(QtGui.QIcon('Imgs/章若楠.jpg'))
        self.centralwidget = MainWindow
        self.centralwidget.setObjectName("centralwidget")

        # 主标签
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily('方正舒体')
        font.setBold(True)
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setText('请输入添加的信息')
        self.label.resize(400, 30)
        self.label.move(110, 20)

        # 姓名标签
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont('楷体')
        font.setPointSize(16)
        font.setBold(True)
        self.label1.setFont(font)
        self.label1.setText('姓名：')
        self.label1.move(120, 100)

        # 姓名输入框
        self.textbox1 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont('楷体')
        font.setPointSize(16)
        font.setBold(True)
        self.textbox1.setFont(font)
        self.textbox1.resize(150, 30)
        self.textbox1.move(220, 100)

        # 学号标签
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont('楷体')
        font.setPointSize(16)
        font.setBold(True)
        self.label2.setFont(font)
        self.label2.setText('学号：')
        self.label2.move(120, 150)

        # 学号输入框
        self.textbox2 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont('楷体')
        font.setPointSize(16)
        font.setBold(True)
        self.textbox2.setFont(font)
        self.textbox2.resize(150, 30)
        self.textbox2.move(220, 150)

        # 性别标签
        self.label3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont('楷体')
        font.setPointSize(16)
        font.setBold(True)
        self.label3.setFont(font)
        self.label3.setText('性别：')
        self.label3.move(120, 200)

        # 性别输入框
        self.textbox3 = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont('楷体')
        font.setPointSize(16)
        font.setBold(True)
        self.textbox3.setFont(font)
        self.textbox3.resize(150, 30)
        self.textbox3.move(220, 200)
        self.textbox3.addItems(['男', '女'])

        # 班级标签
        self.label4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont('楷体')
        font.setPointSize(16)
        font.setBold(True)
        self.label4.setFont(font)
        self.label4.setText('年龄：')
        self.label4.move(120, 250)

        # 年龄输入框
        self.textbox4 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont('楷体')
        font.setPointSize(16)
        font.setBold(True)
        self.textbox4.setFont(font)
        self.textbox4.resize(150, 30)
        self.textbox4.move(220, 250)

        # 完成添加按键
        self.button1 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont('方正舒体')
        font.setPointSize(16)
        font.setBold(True)
        self.button1.setFont(font)
        self.button1.setText('完成添加')
        self.button1.resize(150, 50)
        self.button1.move(180, 320)
        self.button1.clicked.connect(self.Click_FINISH)

        # 退出添加信息按键
        self.button2 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont('楷体')
        font.setPointSize(16)
        font.setBold(True)
        self.button2.setFont(font)
        self.button2.setText('退出')
        self.button2.resize(100, 50)
        self.button2.move(340, 400)
        self.button2.clicked.connect(self.Click_tuichu)

    # 添加信息
    def Click_FINISH(self):
        db = pymysql.connect(host='localhost', user='root', password='2933364109', database='itname', port=3306)
        cur = db.cursor()
        sql = "INSERT INTO students VALUES (%s, %s, %s, %s)"
        sql_search = "SELECT * FROM students where 学号=%s"
        insert_tupe = (self.textbox1.text(), self.textbox2.text(), self.textbox3.currentText(), self.textbox4.text())
        # print(insert_tupe)
        insert_list = []
        insert_list.append(insert_tupe)
        # print(insert_list)
        tupe = insert_tupe[1]
        if self.textbox1.text() == "":
            QMessageBox.warning(self.centralwidget, '提示', '姓名不能为空！')
        elif self.textbox2.text() == "":
            QMessageBox.warning(self.centralwidget, '提示', '学号不能为空！')
        elif self.textbox4.text() == "":
            QMessageBox.warning(self.centralwidget, '提示', '年龄不能为空！')
        else:
            try:
                cur.execute(sql_search, tupe)
                results = cur.fetchall()
                # print(results)
                if results != ():
                    # print("该学生信息已存在！")
                    QMessageBox.information(self.centralwidget, '提示', '该学号已存在！')
                else:
                    try:
                        cur.executemany(sql, insert_list)
                        # print("添加成功！")
                        db.commit()
                        QMessageBox.information(self.centralwidget, '提示', '信息添加成功')
                    except Exception as e:
                        # print(e)
                        # print("添加失败！")
                        QMessageBox.information(self.centralwidget, '提示', '信息添加失败')
                        db.rollback()
            except Exception as e:
                print(e)
                print("查找失败！")
                QMessageBox.information(self.centralwidget, '提示', '信息添加失败')
                db.rollback()
            finally:
                db.close()
                cur.close()

    def Click_tuichu(self):
        # print('退出成功！')
        self.centralwidget.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    windows = QMainWindow()
    ui = MainWindow2()
    ui.tianjia(windows)
    windows.show()
    sys.exit(app.exec_())