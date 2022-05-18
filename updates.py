
# 修改信息界面

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import Qt, QtGui, QtCore, QtWidgets
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql

class MainWindow4(object):
    def xiugai(self, MainWindow):
        MainWindow.setWindowTitle('修改信息系统')
        MainWindow.resize(400, 400)
        MainWindow.move(950, 350)
        MainWindow.move(600, 200)
        MainWindow.setWindowIcon(QtGui.QIcon('Imgs/章若楠.jpg'))
        self.centralwidget = MainWindow
        self.centralwidget.setObjectName("centralwidget")

        # 修改信息标签
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily('方正舒体')
        font.setBold(True)
        font.setPointSize(17)
        self.label.setFont(font)
        self.label.setText('请输入要修改的学生信息')
        self.label.resize(350, 30)
        self.label.move(40, 20)

        # 学号标签
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        font.setFamily('楷体')
        font.setBold(True)
        font.setPointSize(14)
        self.label1.setFont(font)
        self.label1.setText('学号：')
        self.label1.resize(100, 30)
        self.label1.move(60, 65)

        # 学号输入框
        self.textbox1 = QtWidgets.QLineEdit(self.centralwidget)
        font.setFamily('楷体')
        font.setBold(True)
        font.setPointSize(14)
        self.textbox1.setFont(font)
        self.textbox1.resize(150, 40)
        self.textbox1.move(130, 60)

        # 查看按键
        self.button = QtWidgets.QPushButton('查看', self.centralwidget)
        font.setFamily('楷体')
        font.setBold(True)
        font.setPointSize(14)
        self.button.setFont(font)
        self.button.resize(80, 40)
        self.button.move(300, 60)
        self.button.clicked.connect(self.Click_Chakan)

        # 姓名标签
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        font.setFamily('楷体')
        font.setBold(True)
        font.setPointSize(14)
        self.label2.setFont(font)
        self.label2.setText('姓名：')
        self.label2.resize(100, 30)
        self.label2.move(60, 125)

        # 学号输入框
        self.textbox2 = QtWidgets.QLineEdit(self.centralwidget)
        font.setFamily('楷体')
        font.setBold(True)
        font.setPointSize(14)
        self.textbox2.setFont(font)
        self.textbox2.resize(150, 40)
        self.textbox2.move(130, 120)

        # 性别标签
        self.label3 = QtWidgets.QLabel(self.centralwidget)
        font.setFamily('楷体')
        font.setBold(True)
        font.setPointSize(14)
        self.label3.setFont(font)
        self.label3.setText('性别：')
        self.label3.resize(100, 30)
        self.label3.move(60, 185)

        # 性别输入框
        self.textbox3 = QtWidgets.QLineEdit(self.centralwidget)
        font.setFamily('楷体')
        font.setBold(True)
        font.setPointSize(14)
        self.textbox3.setFont(font)
        self.textbox3.resize(150, 40)
        self.textbox3.move(130, 180)

        # 年龄标签
        self.label4 = QtWidgets.QLabel('年龄', self.centralwidget)
        font.setFamily('楷体')
        font.setBold(True)
        font.setPointSize(14)
        self.label4.setFont(font)
        self.label4.resize(100, 30)
        self.label4.move(60, 245)

        # 年龄输入框
        self.textbox4 = QtWidgets.QLineEdit(self.centralwidget)
        font.setFamily('楷体')
        font.setBold(True)
        font.setPointSize(14)
        self.textbox4.setFont(font)
        self.textbox4.resize(150, 40)
        self.textbox4.move(130, 240)

        # 完成修改按键
        self.button1 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily('方正舒体')
        font.setPointSize(18)
        font.setBold(True)
        self.button1.setFont(font)
        self.button1.setText('完成修改')
        self.button1.resize(150, 50)
        self.button1.move(100, 300)
        self.button1.clicked.connect(self.Click_FINISH1)

        # 设置退出按键
        self.button2 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily('方正舒体')
        font.setPointSize(18)
        font.setBold(True)
        self.button2.setFont(font)
        self.button2.setText('退出')
        self.button2.resize(100, 30)
        self.button2.move(270, 350)
        self.button2.clicked.connect(self.Click_tuichu)


    def Click_Chakan(self):
        db = pymysql.connect(host='localhost', user='root', password='2933364109', database='itname', port=3306)
        cur = db.cursor()
        # xuehao = self.textbox1.text()
        sqr_search = "SELECT * FROM students WHERE 学号=%s"
        try:
            if self.textbox1.text() == "":
                QtWidgets.QMessageBox.warning(self.centralwidget, '提示', '学号不能为空！')
            else:
                cur.execute(sqr_search, self.textbox1.text())
                # print("查找成功！")
                db.commit()
                results = cur.fetchall()
                # print(results)
                if results == ():
                    QtWidgets.QMessageBox.warning(self.centralwidget, '提示', '学号不存在！')
                for result in results:
                    name = result[0]
                    gender = result[2]
                    age = result[3]
                    # print(name, gender, age)
                    self.textbox2.setText(name)
                    self.textbox3.setText(gender)
                    self.textbox4.setText(age)

        except Exception as e:
            print(e)
            print('查找失败！')
            db.rollback()
        finally:
            db.close()
            cur.close()

    def Click_FINISH1(self):
        if self.textbox1.text() == "":
            QtWidgets.QMessageBox.information(self.centralwidget, '提示', '学号为空')
        elif self.textbox2 == "":
            QtWidgets.QMessageBox.information(self.centralwidget, '提示', '姓名为空')
        elif self.textbox3.text() == "":
            QtWidgets.QMessageBox.information(self.centralwidget, '提示', '性别为空')
        else:
            reply = QtWidgets.QMessageBox.question(self.centralwidget, '提示', '确认修改吗？', QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
            if reply == QtWidgets.QMessageBox.Yes:
                db = pymysql.connect(host='localhost', user='root', password='2933364109', database='itname', port=3306)
                cur = db.cursor()
                sqr = "UPDATE students set 姓名=%s, 性别=%s, 年龄=%s where 学号=%s"
                try:
                    cur.execute(sqr, (self.textbox2.text(), self.textbox3.text(), self.textbox4.text(), self.textbox1.text()))
                    db.commit()
                    # print('修改成功！')
                    QtWidgets.QMessageBox.information(self.centralwidget, '提示', '修改成功！')
                except Exception as e:
                    print(e)
                    print("修改失败！")
                    db.rollback()
                finally:
                    db.close()
                    cur.close()

    def Click_tuichu(self):
        # print("退出成功！")
        self.centralwidget.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    windows = QMainWindow()
    ui = MainWindow4()
    ui.xiugai(windows)
    windows.show()
    sys.exit(app.exec_())