import os
import sys

from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot

from test import Ui_MainWindow  # 加载主界面
from middle_data import Pane  # 获取数据

from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QMenu


class example(QMainWindow):
    def __init__(self):
        super(example, self).__init__()
        self.doc_Windows = Ui_MainWindow()

        self.dataBase = []  # 存放临时数据，以提供筛选
        # 加载test.ui界面
        self.doc_Windows.setupUi(self)
        self.s = None

        # 添加删除对话框
        self.doc_Windows.tableWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.doc_Windows.tableWidget.customContextMenuRequested[QtCore.QPoint].connect(self.context_menu)

        # 取数据
        print("连接server中...")
        self.res = str(self.connect())
        print("返回结果--->>>", self.res)
        if "Error" in self.res:
            msg_box = QMessageBox.warning(self, "错误信息", self.res, QMessageBox.Cancel)
        else:
            print("server连接成功！")

    # 远程连接方法
    def connect(self):
        try:
            s = Pane('192.168.58.133:5985', auth=('administrator', 'Wh123456'), transport='ntlm')
            self.s = s
            r = s.run_cmd('ipconfig')

            code = r.status_code
            if code == 0:
                return "success"
            else:
                return r.std_err
        except Exception as e:
            return e  #

    # 执行cmd命令
    def execu_cmd(self, cmdfile):
        print(cmdfile)
        r = self.s.run_cmd(cmdfile)
        code = r.status_code
        content = r.std_out if code == 0 else r.std_err
        import chardet
        # print(chardet.detect(self.content))  # 检测server的编码格式
        result = content.decode("GB2312")
        return str(result)

    # 处理远程返回数据
    def del_res(self, res):
        if "Error" in res:
            msg_box = QMessageBox.warning(self, "错误信息", res, QMessageBox.Cancel)
        if "没有找到打开的共享文件" in res:
            msg_box = QMessageBox.warning(self, "提示信息", "没有找到打开的共享文件！", QMessageBox.Cancel)
        else:
            data_string = res.split("====================================")[-1].strip()
            # print("===", data_string)
            import re
            res = re.compile(r'(?P<id>\d+)\s+(?P<user>\S+)\s+(?P<pla>\S+)\s+(?P<doc>\S+)',
                             re.S)  # .不匹配换行符,re.S 代表.匹配换行符
            # 通过?P<link>设置定位.通过group(定位符) 定位

            data = res.finditer(data_string)
            # print(data)
            for y in data:
                id = y.group("id")
                user = y.group("user")
                pla = y.group("pla")
                doc = y.group("doc")
                # print(id, user, pla, doc)
                self.dataBase.append([id, user, pla, doc])  # 储存返回的数据，以供查询筛选
                self.inser_row(self.doc_Windows.tableWidget.rowCount(), id, user, pla, doc)

    # 处理查询的数据
    def serach_res(self, res):

        for i in range(len(self.dataBase)):
            get_DateBase = self.dataBase[i]  # 1、获取每一条记录
            # print(res, "====", get_DateBase)
            # ['8', 'administrator', 'Windows', 'C:\\test\\444']
            for x in get_DateBase:  # 2、取每一条['8', 'administrator', 'Windows', 'C:\\test\\444']里的单个数据
                if res in x:  # 如果匹配上了
                    print("条件遍历查询---", get_DateBase)
                    id = get_DateBase[0]
                    user = get_DateBase[1]
                    pla = get_DateBase[2]
                    doc = get_DateBase[3]

                    self.inser_row(self.doc_Windows.tableWidget.rowCount(), id, user, pla, doc)
                else:  # 没找到
                    print("未找到匹配结果")

    # 菜单栏
    def context_menu(self, pos):
        pop_menu = QMenu()
        # pop_menu.setGeometry(50)

        delete_all = pop_menu.addAction("关闭所有文件")
        delete_sel = pop_menu.addAction("关闭选中文件")
        # 1、判断有没有选中文件
        # 2、openfiles Disconnect /ID 88  断开连接
        action = pop_menu.exec_(self.doc_Windows.tableWidget.mapToGlobal(pos))

        if action == delete_sel:
            self.close_file()
        if action == delete_all:
            self.close_file()


    # 关闭数据
    def close_file(self):
        pass
        # action == delete_event:
        # r = QMessageBox.warning(self, "注意", "删除可不能恢复了哦！", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        # if r == QMessageBox.No:
        #     return
        # items = self.tableWidget.selectedItems()
        # if items:
        #     selected_rows = []
        #     for i in items:
        #         row = i.row()
        #         print(row, 'row---->>>>>')  # 记录是第几条记录
        #         if row not in selected_rows:
        #             selected_rows.append(row)  # 把row id全集中
        #     selected_rows = sorted(selected_rows, reverse=True)
        #     for r in selected_rows:
        #         sid = self.tableWidget.item(r, 0).text()
        #         del data[sid]
        #         self.tableWidget.removeRow(r)

    # 插入表格数据
    def inser_row(self, row, sid, name, sex, address):
        # 插入数据到里面前，需要先把dataBae清空  待做
        sid_item = QTableWidgetItem(sid)
        name_item = QTableWidgetItem(name)
        sex_item = QTableWidgetItem(sex)
        address_item = QTableWidgetItem(address)
        self.doc_Windows.tableWidget.insertRow(row)
        self.doc_Windows.tableWidget.setItem(row, 0, sid_item)
        self.doc_Windows.tableWidget.setItem(row, 1, name_item)
        self.doc_Windows.tableWidget.setItem(row, 2, sex_item)
        self.doc_Windows.tableWidget.setItem(row, 3, address_item)

    # 清空表格数据
    def del_All_row(self):
        self.doc_Windows.tableWidget.setRowCount(0)
        self.doc_Windows.tableWidget.clearContents()

    # 查找按钮点击事件
    @pyqtSlot()
    def on_btn_select_clicked(self):
        # 我只要点击了查询按钮， 没填筛选工号的时候，直接返回(不管填不填数据先存储着)
        # 填了筛选工号的时候
        print('点击了查询按钮')
        self.del_All_row()
        self.dataBase = []  # 每次查询之前清空之前存储的数据
        data = self.execu_cmd("openfiles")
        self.del_res(data)  # 处理取得的数据
        input_text = self.doc_Windows.line_filter.text()  # 取出填入的筛选条件
        if not input_text:
            print("选择值为空")
            return
        else:
            print("选择值  不为空")  # 输入的工号不为空的时候，不为空的话判断输入的是工号还是关键字
            # 判断选择了什么
            choseText = self.doc_Windows.comboBox_filter.currentText()
            # print("查询所有数据返回---------------------", data)
            self.del_All_row()  # 清空所有
            self.serach_res(input_text)  # 重新查询


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 实例化窗口
    form = example()
    # 窗口显示
    form.show()
    # 进入程序的主循环，遇到退出情况，终止程序
    sys.exit(app.exec_())
