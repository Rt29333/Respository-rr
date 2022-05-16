# from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
# from PyQt5 import Qt, QtGui, QtCore, QtWidgets
# import sys
# # from TEST import zhujiemian
# from TEST.zhujiemian import *
#
# app = QApplication(sys.argv)
# windows = QMainWindow()
# windows.setWindowTitle('信息管理系统')
# windows.resize(650, 550)
# windows.move(600, 200)
#
# # 标签用户名
# label = Qt.QLabel(windows)
# label.setText('用户名：')
# # label1.resize(300, 200)
# label.move(300, 250)
#
# # 用户名输入框
# textbox = Qt.QLineEdit(windows)
# textbox.resize(150, 30)
# textbox.move(380, 250)
#
# # 密码标签
# label1 = Qt.QLabel(windows)
# label1.setText('密  码：')
# # label1.resize(300, 200)
# label1.move(300, 300)
#
# # 密码输入框
# textbox1 = QtWidgets.QLineEdit(windows)
# textbox1.resize(150, 30)
# textbox1.move(380, 300)
# # 设置密码不可见
# textbox1.setEchoMode(2)
#
#
# def Click_button():
#     # print('登陆成功！')
#     name = QtWidgets.QLineEdit.text(textbox1)
#     if name == 'password':
#         windows.close()
#         # app1 = QApplication(sys.argv)
#         # windows1 = QMainWindow()
#         # ui1 = MainWindow1()
#         # ui1.xianshi(windows1)
#         # windows1.show()
#         # sys.exit(app1.exec_())
#
#
#     else:
#         msg_box = QMessageBox(QMessageBox.Warning, '警告', '您输入的内容为空！')
#         msg_box.exec_()
#
#
# # 登录标签
# button = Qt.QPushButton(windows)
# button.setText('登陆')
# button.resize(100, 50)
# button.move(350, 380)
# button.clicked.connect(Click_button)
#
# windows.show()
# # windows.close()
# sys.exit(app.exec_())

from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QDialog
from PyQt5 import Qt, QtGui, QtCore, QtWidgets
import sys
import pymysql
from InformationSystem.insertdates import *
from InformationSystem.deletedates import *
from InformationSystem.updates import *
# from TEST.test48denglujiemian import *
import xlwt
class Denglujiem(object):
    def setupUi(self, MainWindow):
        MainWindow.setWindowTitle("信息管理")
        MainWindow.resize(450, 400)
        MainWindow.move(600, 200)
        MainWindow.setWindowIcon(QtGui.QIcon('章若楠.jpg'))
        background_img = QtGui.QPalette()
        background_img.setBrush(MainWindow.backgroundRole(), QtGui.QBrush(QtGui.QPixmap('登陆背景.jpg').scaled(669, 450)))
        MainWindow.setPalette(background_img)
        self.centralwidget = MainWindow
        self.centralwidget.setObjectName("centralwidget")

        # 欢迎标签
        self.label2 = QtWidgets.QLabel('欢迎使用学生信息管理系统', self.centralwidget)
        font = QtGui.QFont('方正舒体')
        font.setPointSize(20)
        font.setBold(True)
        self.label2.setFont(font)
        self.label2.resize(430, 50)
        self.label2.move(20, 30)

        # 标签用户名
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont('方正舒体')
        font.setPointSize(18)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setText('账 号：')
        self.label.resize(150, 30)
        self.label.move(150, 150)

        # 用户名输入框
        # self.textbox = Qt.QLineEdit(self.centralwidget)
        # self.textbox.resize(150, 30)
        # self.textbox.move(380, 250)
        self.textbox2 = Qt.QIntValidator(self.centralwidget)
        self.textbox = Qt.QLineEdit(self.centralwidget)
        font = QtGui.QFont('方正舒体')
        font.setPointSize(18)
        font.setBold(True)
        self.textbox.setFont(font)
        self.textbox2.setRange(1, 1000000000)
        self.textbox.resize(150, 40)
        self.textbox.move(250, 145)
        self.textbox.setValidator(self.textbox2)

        # 密码标签
        self.label1 = Qt.QLabel(self.centralwidget)
        font = QtGui.QFont('方正舒体')
        font.setPointSize(18)
        font.setBold(True)
        self.label1.setFont(font)
        self.label1.setText('密 码：')
        self.label1.resize(150, 30)
        self.label1.move(150, 210)

        # 密码输入框
        self.textbox1 = QtWidgets.QLineEdit(self.centralwidget)
        self.textbox1.resize(150, 40)
        self.textbox1.move(250, 205)
        # 设置密码不可见
        self.textbox1.setEchoMode(2)
        # 回车登录
        self.textbox1.returnPressed.connect(self.Click_button)

        # 登录按键
        self.button = Qt.QPushButton(self.centralwidget)
        font = QtGui.QFont('方正舒体')
        font.setPointSize(18)
        font.setBold(True)
        self.button.setFont(font)
        self.button.setText('登陆')
        self.button.resize(100, 50)
        self.button.move(150, 290)
        self.button.clicked.connect(self.Click_button)

        # 退出按键
        self.button1 = QtWidgets.QPushButton('退出', self.centralwidget)
        font = QtGui.QFont('方正舒体')
        font.setPointSize(18)
        font.setBold(True)
        self.button1.setFont(font)
        self.button1.resize(100, 50)
        self.button1.move(320, 290)
        self.button1.clicked.connect(self.Click_Close)


    def Click_Close(self):
        reply = QMessageBox.question(self.centralwidget, '提示', '确认退出吗？', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.centralwidget.close()
        else:
            pass


    def Click_button(self):
        # print('登陆成功！')
        self.user_name = QtWidgets.QLineEdit.text(self.textbox)
        self.password = QtWidgets.QLineEdit.text(self.textbox1)
        try:
            db = pymysql.connect(host='localhost', user='root', password='2933364109', database='itname', port=3306)
            cur = db.cursor()
            sql = "SELECT * FROM admin where 账号=%s"
            if self.user_name == "":
                QMessageBox.warning(self.centralwidget, '提示', '账号不能为空！')
            elif self.password == "":
                QMessageBox.warning(self.centralwidget, '提示', '密码不能为空！')
            else:
                try:
                    cur.execute(sql, self.user_name)
                    # print("登录成功!")
                    results = cur.fetchall()
                    # print(results)
                    if results == ():
                        QMessageBox.warning(self.centralwidget, '提示', '账号不存在！')
                    else:
                        for result in results:
                            pwd = result[1]
                            if self.password == pwd:
                                # print('登录完成')
                                self.open()
                            else:
                                QMessageBox.warning(self.centralwidget, '提示', '密码错误！！')
                except Exception as e:
                    print(e)
                    print("登录失败")
                    db.rollback()
                finally:
                    db.close()
                    cur.close()
        except:
            # print("请连接数据库！")
            QMessageBox.warning(self.centralwidget, '提示', '请先连接数据库！！')
        # if self.user_name == '123456':
        #     if self.password == 'password':
        #         self.open()
        #         # app1 = QApplication(sys.argv)
        #         # windows1 = QMainWindow()
        #         # ui1 = MainWindow1()
        #         # ui1.xianshi(windows1)
        #         # windows1.show()
        #         # sys.exit(app1.exec_())
        #         # self.centralwidget.close()
        #     else:
        #         self.msg_box = QMessageBox(QMessageBox.Warning, '警告', '密码或用户名错误！')
        #         self.msg_box.exec_()
        # elif self.password == "":
        #     self.msg_box = QMessageBox(QMessageBox.Warning, '警告', '密码不能为空！')
        #     self.msg_box.exec_()
        # elif self.user_name == "":
        #     self.msg_box = QMessageBox(QMessageBox.Warning, '警告', '用户名不能为空！')
        #     self.msg_box.exec_()
        # else:
        #     self.msg_box = QMessageBox(QMessageBox.Warning, '警告', '密码或用户名错误！')
        #     self.msg_box.exec_()

    def open(self):
        # self.UI_MAN.xianshi(self.centralwidget)
        # self.centralwidget.show()
        self.centralwidget.close()
        self.windows1 = QMainWindow()
        self.UI_MAN = MainWindow1()
        self.UI_MAN.xianshi(self.windows1)
        self.windows1.show()

class MainWindow1(object):
    def xianshi(self, MainWindow):
        MainWindow.setWindowTitle("信息管理系统")
        MainWindow.resize(780, 700)
        MainWindow.move(600, 220)
        MainWindow.setWindowIcon(QtGui.QIcon('章若楠.jpg'))
        self.centralwidget = MainWindow
        self.centralwidget.setObjectName("centralwidget")
        # MainWindow.setWindowTitle("信息管理")
        # MainWindow.resize(650, 550)
        # MainWindow.move(600, 200)
        # 信息查询标签
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("方正舒体")
        font.setPointSize(20)
        font.setBold(True)
        self.label1.setFont(font)
        self.label1.setText('欢迎使用信息管理系统')
        self.label1.resize(400, 30)
        self.label1.move(30, 50)

        # 姓名标签
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont('楷体')
        font.setPointSize(16)
        font.setBold(True)
        self.label2.setFont(font)
        self.label2.setText('姓名：')
        self.label2.move(70, 110)

        # 学号标签
        self.label3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont('楷体')
        font.setPointSize(16)
        font.setBold(True)
        self.label3.setFont(font)
        self.label3.setText('学号：')
        self.label3.move(70, 200)

        # 性别标签
        self.label4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont('楷体')
        font.setPointSize(16)
        font.setBold(True)
        self.label4.setFont(font)
        self.label4.setText('性别：')
        # self.label4.resize()
        self.label4.move(70, 290)

        # 信息显示标签
        self.label5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily('方正舒体')
        font.setBold(True)
        font.setPointSize(20)
        self.label5.setFont(font)
        self.label5.setText('查询结果')
        self.label5.resize(150, 50)
        self.label5.move(490, 50)

        # 姓名输入框
        self.textbox1 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont('楷体')
        font.setPointSize(16)
        font.setBold(True)
        self.textbox1.setFont(font)
        self.textbox1.resize(130, 50)
        self.textbox1.move(150, 100)

        # 学号输入框
        self.textbox = Qt.QIntValidator(self.centralwidget)
        self.textbox.setRange(1, 1000000000)
        self.textbox2 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont('楷体')
        font.setPointSize(16)
        font.setBold(True)
        self.textbox2.setFont(font)
        self.textbox2.resize(150, 30)
        self.textbox2.move(150, 200)
        self.textbox2.setValidator(self.textbox)

        # 性别多选框
        self.textbox3 = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont('楷体')
        font.setPointSize(16)
        font.setBold(True)
        self.textbox3.setFont(font)
        self.textbox3.resize(100, 30)
        self.textbox3.move(170, 290)
        self.textbox3.addItems(['男', '女'])

        # # 信息显示文本框
        # self.label6 = QtWidgets.QTextBrowser(self.centralwidget)
        # self.label6.resize(300, 300)
        # self.label6.move(370, 110)

        # 开始查询按键
        self.button1 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont('方正舒体')
        font.setPointSize(18)
        font.setBold(True)
        self.button1.setFont(font)
        self.button1.setText('开始查询')
        self.button1.resize(150, 50)
        self.button1.move(50, 380)
        self.button1.clicked.connect(self.Click_chaxun)

        # 清空按键
        self.button6 = QtWidgets.QPushButton('清空',self.centralwidget)
        font = QtGui.QFont('方正舒体')
        font.setPointSize(18)
        font.setBold(True)
        self.button6.setFont(font)
        self.button6.resize(100, 50)
        self.button6.move(230, 380)
        self.button6.clicked.connect(self.Click_clear)

        # 导出所有信息按键
        self.button7 = QtWidgets.QPushButton('导出所有信息', self.centralwidget)
        font = QtGui.QFont('方正舒体')
        font.setPointSize(18)
        font.setBold(True)
        self.button7.setFont(font)
        self.button7.resize(200, 50)
        self.button7.move(140, 460)
        self.button7.clicked.connect(self.Click_AllDates)

        # 下载表格
        self.button9 = QtWidgets.QPushButton('下载表格', self.centralwidget)
        font = QtGui.QFont('方正舒体')
        font.setPointSize(18)
        font.setBold(True)
        self.button9.setFont(font)
        self.button9.resize(150, 50)
        self.button9.move(180, 520)
        self.button9.clicked.connect(self.Click_Excel)
        self.button9.setEnabled(False)

        # 排序按键
        self.button8 = QtWidgets.QPushButton('排序', self.centralwidget)
        font = QtGui.QFont('楷体')
        font.setPointSize(16)
        font.setBold(True)
        self.button8.setFont(font)
        self.button8.resize(100, 40)
        self.button8.move(350, 530)
        self.button8.clicked.connect(self.Click_Sort)

        # 排序选项框
        self.textbox4 = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont('楷体')
        font.setPointSize(16)
        font.setBold(True)
        self.textbox4.setFont(font)
        self.textbox4.resize(100, 40)
        self.textbox4.move(500, 530)
        self.textbox4.addItems(['姓名', '学号', '性别', '年龄'])

        # 升降序
        self.textbox5 = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont('楷体')
        font.setPointSize(16)
        font.setBold(True)
        self.textbox5.setFont(font)
        self.textbox5.resize(100, 40)
        self.textbox5.move(650, 530)
        self.textbox5.addItems(['升序', '降序'])

        # 添加信息按键
        self.button2 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont('楷体')
        font.setPointSize(16)
        font.setBold(True)
        self.button2.setFont(font)
        self.button2.setText('添加信息')
        self.button2.resize(150, 70)
        self.button2.move(50, 590)
        self.button2.clicked.connect(self.Click_tianjia)

        # 删除信息按键
        self.button3 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont('楷体')
        font.setPointSize(16)
        font.setBold(True)
        self.button3.setFont(font)
        self.button3.setText('删除信息')
        self.button3.resize(150, 70)
        self.button3.move(230, 590)
        self.button3.clicked.connect(self.Click_shanchu)

        # 修改信息按键
        self.button4 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont('楷体')
        font.setPointSize(16)
        font.setBold(True)
        self.button4.setFont(font)
        self.button4.setText('修改信息')
        self.button4.resize(150, 70)
        self.button4.move(410, 590)
        self.button4.clicked.connect(self.Click_xiugai)

        # 退出系统按键
        self.button5 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont('楷体')
        font.setPointSize(16)
        font.setBold(True)
        self.button5.setFont(font)
        self.button5.setText('退出系统')
        self.button5.resize(150, 70)
        self.button5.move(590, 590)
        self.button5.clicked.connect(self.closeEvent)

        # 信息显示文本框
        self.label6 = QtWidgets.QTableWidget(self.centralwidget)
        font = QtGui.QFont('楷体')
        font.setPointSize(14)
        font.setBold(True)
        self.label6.setFont(font)
        # self.label6.setRowCount(100)
        self.label6.setColumnCount(4)
        # self.list_xianshi = ['姓名', '学号', '性别', '年龄']
        # self.label6.setHorizontalHeaderLabels(self.list_xianshi)
        self.label6.resize(400, 400)
        self.label6.move(350, 110)
        item = QtWidgets.QTableWidgetItem()
        self.label6.setHorizontalHeaderItem(0, item)
        item.setText('姓名')
        item = QtWidgets.QTableWidgetItem()
        self.label6.setHorizontalHeaderItem(1, item)
        item.setText('学号')
        item = QtWidgets.QTableWidgetItem()
        self.label6.setHorizontalHeaderItem(2, item)
        item.setText('性别')
        item = QtWidgets.QTableWidgetItem()
        self.label6.setHorizontalHeaderItem(3, item)
        item.setText('年龄')

    # def Click_chaxun(self):
    #     # print("查询成功！")
    #     self.name_list = QtWidgets.QLineEdit.text(self.textbox1)
    #     self.name_list1 = QtWidgets.QLineEdit.text(self.textbox2)
    #     self.name_list2 = QtWidgets.QComboBox.currentText(self.textbox3)
    #     # print(self.name_list, self.name_list1, self.name_list2)
    #     db = pymysql.connect(host='localhost', user='root', password='2933364109', database='itname', port=3306)
    #     cur = db.cursor()
    #     sql = "SELECT * FROM students where 姓名=%s and 学号=%s and 性别=%s"
    #     if self.name_list == "":
    #         QMessageBox.warning(self.centralwidget, '提示', '姓名不能为空！')
    #     elif self.name_list1 == "":
    #         QMessageBox.warning(self.centralwidget, '提示', '学号不能为空！')
    #     else:
    #         try:
    #             cur.execute(sql, (self.name_list, self.name_list1, self.name_list2))
    #             # print("查询成功！")
    #             results = cur.fetchall()
    #             # print(results)
    #             if results == ():
    #                 # print('信息错误！')
    #                 QtWidgets.QMessageBox.warning(self.centralwidget, '提示', '信息错误！')
    #             else:
    #                 for result in results:
    #                     name = result[0]
    #                     id = result[1]
    #                     gender = result[2]
    #                     age = result[3]
    #                     item = QtWidgets.QTableWidgetItem(name)
    #                     # 内容居中
    #                     item.setTextAlignment(QtCore.Qt.AlignCenter)
    #                     self.label6.setItem(0, 0, item)
    #                     item = QtWidgets.QTableWidgetItem(id)
    #                     item.setTextAlignment(QtCore.Qt.AlignCenter)
    #                     self.label6.setItem(0, 1, item)
    #                     item = QtWidgets.QTableWidgetItem(gender)
    #                     item.setTextAlignment(QtCore.Qt.AlignCenter)
    #                     self.label6.setItem(0, 2, item)
    #                     item = QtWidgets.QTableWidgetItem(age)
    #                     item.setTextAlignment(QtCore.Qt.AlignCenter)
    #                     self.label6.setItem(0, 3, item)
    #
    #         except Exception as e:
    #             print(e)
    #             print('查询失败！')
    #             db.rollback()
    #         finally:
    #             db.close()
    #             cur.close()
    #
    #
    #     # self.label6.
    #     # self.label6.setPlainText("姓名为：{}\n学号为：{}\n性别为：{}".format(self.name_list, self.name_list1, self.name_list2))


    def Click_Sort(self):
        num1 = self.textbox4.currentText()
        num2 = self.textbox5.currentText()
        if num1 == '姓名' and num2 == '升序':
            #  QtCore.Qt.AscendingOrder 升序
            self.label6.sortItems(0, QtCore.Qt.AscendingOrder)
        elif num1 == '姓名' and num2 == '降序':
            #  QtCore.Qt.DescendingOrde  降序
            self.label6.sortItems(0, QtCore.Qt.DescendingOrder)
        elif num1 == '学号' and num2 == '升序':
            self.label6.sortItems(1, QtCore.Qt.AscendingOrder)
        elif num1 == '学号' and num2 == '降序':
            self.label6.sortItems(1, QtCore.Qt.DescendingOrder)
        elif num1 == '性别' and num2 == '升序':
            self.label6.sortItems(2, QtCore.Qt.AscendingOrder)
        elif num1 == '性别' and num2 == '降序':
            self.label6.sortItems(2, QtCore.Qt.DescendingOrder)
        elif num1 == '年龄' and num2 == '升序':
            self.label6.sortItems(3, QtCore.Qt.AscendingOrder)
        elif num1 == '年龄' and num2 == '降序':
            self.label6.sortItems(3, QtCore.Qt.DescendingOrder)

    def Click_chaxun(self):
        # print("查询成功！")
        self.button9.setEnabled(False)
        self.name_list = QtWidgets.QLineEdit.text(self.textbox1)
        self.name_list1 = QtWidgets.QLineEdit.text(self.textbox2)
        self.name_list2 = QtWidgets.QComboBox.currentText(self.textbox3)
        # print(self.name_list, self.name_list1, self.name_list2)
        if self.name_list == "" and self.name_list1 == "":
            QMessageBox.warning(self.centralwidget, '提示', '查询内容不能为空')
        else:
            # 清空表格的所有内容
            self.label6.clearContents()
            # 将表格栏一起删除
            self.label6.setRowCount(0)
            db = pymysql.connect(host='localhost', user='root', password='2933364109', database='itname', port=3306)
            cur = db.cursor()
            sql = "SELECT * FROM students where "
            if self.name_list1 != '':
                sql_id = sql + '学号=' + self.name_list1
                # print(sql_id)
                try:
                    cur.execute(sql_id)
                    results = cur.fetchall()
                    # print(results)
                    if results == ():
                        QtWidgets.QMessageBox.warning(self.centralwidget, '提示', '学号错误！')
                    else:
                        for i in range(len(results)):
                            item = results[i]
                            row = self.label6.rowCount()
                            self.label6.insertRow(row)
                            for j in range(len(item)):
                                item = QtWidgets.QTableWidgetItem(results[i][j])
                                # 内容居中显示
                                item.setTextAlignment(QtCore.Qt.AlignCenter)
                                # 表格为只读，不可修改
                                item.setFlags(QtCore.Qt.ItemIsEnabled)
                                self.label6.setItem(row, j, item)
                except Exception as e:
                    print(e)
                    print('查询失败！')
                    db.rollback()
                finally:
                    db.close()
                    cur.close()

            elif self.name_list != "" and self.name_list2 == "男":
                sql_name = sql + '姓名=' + '\'' + self.name_list + '\'' + ' and ' + '性别=' + '\''+ self.name_list2 + '\''
                try:
                    cur.execute(sql_name)
                    results = cur.fetchall()
                    # print(results)
                    if results == ():
                        # print('信息错误！')
                        QtWidgets.QMessageBox.warning(self.centralwidget, '提示', '信息错误！')
                        self.button9.setEnabled(False)
                    else:
                        for i in range(len(results)):
                            item = results[i]
                            row = self.label6.rowCount()
                            self.label6.insertRow(row)
                            for j in range(len(item)):
                                item = QtWidgets.QTableWidgetItem(results[i][j])
                                # 表格为只读，不可修改
                                item.setFlags(QtCore.Qt.ItemIsEnabled)
                                # 内容居中显示
                                item.setTextAlignment(QtCore.Qt.AlignCenter)
                                self.label6.setItem(row, j, item)
                except Exception as e:
                    print(e)
                    print('查询失败！')
                    db.rollback()
                finally:
                    db.close()
                    cur.close()

            elif self.name_list != "" and self.name_list2 == "女":
                sql_name = sql + '姓名=' + '\'' + self.name_list + '\'' + ' and ' + '性别=' + '\''+ self.name_list2 + '\''
                try:
                    cur.execute(sql_name)
                    results = cur.fetchall()
                    # print(results)
                    if results == ():
                        # print('信息错误！')
                        QtWidgets.QMessageBox.warning(self.centralwidget, '提示', '信息错误！')
                    else:
                        for i in range(len(results)):
                            item = results[i]
                            row = self.label6.rowCount()
                            self.label6.insertRow(row)
                            for j in range(len(item)):
                                item = QtWidgets.QTableWidgetItem(results[i][j])
                                # 表格为只读，不可修改
                                item.setFlags(QtCore.Qt.ItemIsEnabled)
                                # 内容居中显示
                                item.setTextAlignment(QtCore.Qt.AlignCenter)
                                self.label6.setItem(row, j, item)
                except Exception as e:
                    print(e)
                    print('查询失败！')
                    db.rollback()
                finally:
                    db.close()
                    cur.close()
            # elif self.name_list2 == "男":
            #     sql_gender = sql + '性别=' + '\'' + self.name_list2 + '\''
            #     try:
            #         cur.execute(sql_gender)
            #         results = cur.fetchall()
            #         # print(results)
            #         if results == ():
            #             # print('信息错误！')
            #             QtWidgets.QMessageBox.warning(self.centralwidget, '提示', '信息错误！')
            #         else:
            #             for i in range(len(results)):
            #                 item = results[i]
            #                 row = self.label6.rowCount()
            #                 self.label6.insertRow(row)
            #                 for j in range(len(item)):
            #                     item = QtWidgets.QTableWidgetItem(results[i][j])
            #                     self.label6.setItem(row, j, item)
            #     except Exception as e:
            #         print(e)
            #         print('查询失败！')
            #         db.rollback()
            #     finally:
            #         db.close()
            #         cur.close()
            #
            # elif self.name_list2 == "女":
            #     sql_gender = sql + '性别=' + '\'' + self.name_list2 + '\''
            #     try:
            #         cur.execute(sql_gender)
            #         results = cur.fetchall()
            #         # print(results)
            #         if results == ():
            #             # print('信息错误！')
            #             QtWidgets.QMessageBox.warning(self.centralwidget, '提示', '信息错误！')
            #         else:
            #             for i in range(len(results)):
            #                 item = results[i]
            #                 row = self.label6.rowCount()
            #                 self.label6.insertRow(row)
            #                 for j in range(len(item)):
            #                     item = QtWidgets.QTableWidgetItem(results[i][j])
            #                     self.label6.setItem(row, j, item)
            #     except Exception as e:
            #         print(e)
            #         print('查询失败！')
            #         db.rollback()
            #     finally:
            #         db.close()
            #         cur.close()


    def Click_AllDates(self):
        self.button9.setEnabled(True)
        # 清空表格的所有内容
        self.label6.clearContents()
        # 将表格栏一起删除
        self.label6.setRowCount(0)
        db = pymysql.connect(host='localhost', user='root', password='2933364109', database='itname', port=3306)
        cur = db.cursor()
        sql = "SELECT * FROM students"
        try:
            cur.execute(sql)
            # print("导出成功！")
            self.results = cur.fetchall()
            # print(results)
            for i in range(len(self.results)):
                item = self.results[i]
                row = self.label6.rowCount()
                self.label6.insertRow(row)
                for j in range(len(item)):
                    item = QtWidgets.QTableWidgetItem(self.results[i][j])
                    # 表格为只读，不可修改
                    item.setFlags(QtCore.Qt.ItemIsEnabled)
                    # 内容居中显示
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.label6.setItem(row, j, item)
        except Exception as e:
            print(e)
            print("导出失败！")

    def Click_Excel(self):
        try:
            book = xlwt.Workbook(encoding='utf8', style_compression=0)
            sheet = book.add_sheet('信息1', cell_overwrite_ok=True)
            col = ('姓名', '学号', '性别', '年龄')
            for i in range(0, 4):
                sheet.write(0, i, col[i])
            for i in range(0, len(self.results)):
                data = self.results[i]
                for j in range(0, 4):
                    sheet.write(i+1, j, data[j])
            file_path, type = QtWidgets.QFileDialog.getSaveFileName(None, '文件保存', 'F:/表格', 'xls files(*.xls)')
            savepath = file_path
            book.save(savepath)
            # print("写入成功")
            QtWidgets.QMessageBox.information(self.centralwidget, '提示', '下载表格成功')
        except:
            # print("下载失败！")
            QMessageBox.information(self.centralwidget, '提示', '下载表格失败！')




    def Click_clear(self):
        self.button9.setEnabled(False)
        self.textbox1.clear()
        self.textbox2.clear()
        # 清空表格的所有内容
        self.label6.clearContents()
        # 将表格栏一起删除
        self.label6.setRowCount(0)

    def Click_tianjia(self):
        # print('添加成功！')
        self.windows2 = QMainWindow()
        self.UI2 = MainWindow2()
        self.UI2.tianjia(self.windows2)
        self.windows2.show()

    def Click_shanchu(self):
        # print("删除成功！")
        self.windows3 = QMainWindow()
        self.UI3 = MainWindow3()
        self.UI3.shanchu(self.windows3)
        self.windows3.show()

    def Click_xiugai(self):
        # print("修改成功！")
        self.windows4 = QMainWindow()
        self.UI4 = MainWindow4()
        self.UI4.xiugai(self.windows4)
        self.windows4.show()

    # 关闭窗口触发以下事件
    def closeEvent(self):
        # 没有确定事件
        # self.a = QMessageBox(QMessageBox.Question, '退出', '你确定要退出吗?')  # "退出"代表的是弹出框的标题,"你确认退出.."表示弹出框的内容
        # self.a.exec_()

        # 有确定事件
        self.msg_name = QMessageBox.question(self.centralwidget, '退出', '你确定要退出吗?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if self.msg_name == QMessageBox.Yes:
            # event.accept()
            self.Click_Tuichu1()
        # else:
            # event.Ignore()

    def Click_Tuichu1(self):
        self.centralwidget.close()
        self.windows8 = QMainWindow()
        self.UI1 = Denglujiem()
        self.UI1.setupUi(self.windows8)
        self.windows8.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    windows = QMainWindow()
    ui = Denglujiem()
    ui.setupUi(windows)
    windows.show()
    sys.exit(app.exec_())