# 删除信息

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import Qt, QtGui, QtCore, QtWidgets
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql


class MainWindow3(object):
    def shanchu(self, MainWindow):
        MainWindow.setWindowTitle('删除信息系统')
        MainWindow.resize(350, 330)
        MainWindow.move(950, 350)
        MainWindow.move(600, 200)
        MainWindow.setWindowIcon(QtGui.QIcon('Imgs/章若楠.jpg'))
        self.centralwidget = MainWindow
        self.centralwidget.setObjectName("centralwidget")

        # 删除信息标签
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily('方正舒体')
        font.setBold(True)
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setText('删除学生信息')
        self.label.resize(250, 30)
        self.label.move(90, 5)

        # 学号标签
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont('楷体')
        font.setPointSize(14)
        font.setBold(True)
        self.label1.setFont(font)
        self.label1.setText('学 号：')
        self.label1.resize(100, 50)
        self.label1.move(60, 60)

        # 学号输入框
        self.textbox1 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont('楷体')
        font.setPointSize(14)
        font.setBold(True)
        self.textbox1.setFont(font)
        self.textbox1.resize(130, 30)
        self.textbox1.move(140, 68)

        # 查看标签
        self.button3 = QtWidgets.QPushButton('查看', self.centralwidget)
        font = QtGui.QFont('楷体')
        font.setPointSize(14)
        font.setBold(True)
        self.button3.setFont(font)
        self.button3.resize(60, 50)
        self.button3.move(280, 60)
        self.button3.clicked.connect(self.Click_Search)

        # 姓名标签
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont('楷体')
        font.setPointSize(14)
        font.setBold(True)
        self.label2.setFont(font)
        self.label2.setText('姓名为：')
        self.label2.resize(100, 50)
        self.label2.move(50, 120)

        # 姓名显示框
        self.textbox2 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont('楷体')
        font.setPointSize(14)
        font.setBold(True)
        self.textbox2.setFont(font)
        self.textbox2.resize(130, 50)
        self.textbox2.move(140, 120)


        # 删除按键
        self.button1 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont('方正舒体')
        font.setPointSize(16)
        font.setBold(True)
        self.button1.setFont(font)
        self.button1.setText('开始删除')
        self.button1.resize(120, 50)
        self.button1.move(130, 200)
        self.button1.clicked.connect(self.Click_DELETE)


        # 退出按键
        self.button2 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont('楷体')
        font.setPointSize(14)
        font.setBold(True)
        self.button2.setFont(font)
        self.button2.setText('退出')
        self.button2.resize(50, 30)
        self.button2.move(280, 270)
        self.button2.clicked.connect(self.Click_tuichu)

    def Click_Search(self):
        db = pymysql.connect(host='localhost', user='root', password='2933364109', database='itname', port=3306)
        cur = db.cursor()
        sql = "SELECT * FROM students WHERE 学号=%s"

        try:
            if self.textbox1.text() == "":
                QtWidgets.QMessageBox.warning(self.centralwidget, "警告", '学号不能为空')
            else:
                cur.execute(sql, self.textbox1.text())
                db.commit()
                self.results = cur.fetchall()
                if self.results == ():
                    QtWidgets.QMessageBox.about(self.centralwidget, '提示', '学号不存在！')
                for result in self.results:
                    name = result[0]
                    # print('查询成功')
                    # print(name)
                    self.textbox2.setText(name)
        except Exception as e:
            print(e)
            print("查询失败！")
            QtWidgets.QMessageBox.about(self.centralwidget, '提示', '学号不存在！')
            db.rollback()
        finally:
            db.close()
            cur.close()


    def Click_DELETE(self):
        if self.textbox1.text() == "":
            QtWidgets.QMessageBox.information(self.centralwidget, '提示', '学号为空')
        elif self.textbox2.text() == "":
            QtWidgets.QMessageBox.information(self.centralwidget, '提示', '姓名为空')
        else:
            reply = QtWidgets.QMessageBox.question(self.centralwidget, '提示', '确认删除该学生信息吗？', QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
            if reply == QtWidgets.QMessageBox.Yes:
                db = pymysql.connect(host='localhost', user='root', password='2933364109', database='itname', port=3306)
                cur = db.cursor()
                sqr = "DELETE from students where 学号=%s"
                try:
                    cur.execute(sqr, self.textbox1.text())
                    QtWidgets.QMessageBox.information(self.centralwidget, '提示', '删除成功！')
                    # print("删除成功")
                    db.commit()
                except Exception as e:
                    # print(e)
                    # print("删除失败")
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
    ui = MainWindow3()
    ui.shanchu(windows)
    windows.show()
    sys.exit(app.exec_())
