#### 一、下载QT库
    pyqt5 和  pyqt-tools （pip install xxx）
    
#### 二、使用QT designer
    在qt5-applications--QT--bin中使用designer
   
#### 三、窗体介绍
![imag](https://github.com/fengxunzhe/index/blob/main/PyQT/img/1.png)

Dialog with Buttons Buttom --->>> 底部两个按钮的弹窗

Dialog with Buttons Right --->>> 右边两个按钮的弹窗

Dialog without Buttons --->>> 没有按钮的弹窗

Main --->>> 主窗体(相当于易语言的新建窗口)

Widget --->>> 次窗体(相当于易语言中主窗口外新建个窗体，可插入到主窗体中)

#### 三、常用组件
List Widget 列表框

PushButton 按钮

RadioButton 单选框

CheckBox 选择框

#### 四、PyQT5中布局UI文件转换为python文件
默认安装PyQT5会安装pyuic5；使用pyuic5 -o 保存文件.py 要转换的文件.ui

#### 五、PyQT5默认案例
#下面这行代码是为了避免在所生成的pyqt中出现中文乱码的问题

    # -*- coding:UTF-8 -*-
    import sys
    from PyQt5.QtWidgets import QApplication,QMainWindow
    from PyQt5.QtGui import QIcon
    class MainWindow(QMainWindow):
        def __init__(self,parent=None):
            #初始化继承的父类（Qmainwindow）
            super(MainWindow, self).__init__(parent)
            #设置窗口的大小
            self.resize(400,200)
            #实例化创建状态栏
            self.status=self.statusBar()
            #将提示信息显示在状态栏中showMessage（‘提示信息’，显示时间（单位毫秒））
            self.status.showMessage('这是状态栏提示',4000)
            #创建窗口标题
            self.setWindowTitle('PyQt MainWindow例子')


    if __name__ == '__main__':
        # 每一个pyqt程序中都需要有一个QApplication对象，sys.argv是一个命令行参数列表
        app=QApplication(sys.argv)
        #实例化窗口
        form=MainWindow()
        #窗口显示
        form.show()
        #进入程序的主循环，遇到退出情况，终止程序
        sys.exit(app.exec_())
        
#### 六、PyQT5默认案例二
![imag](https://github.com/fengxunzhe/index/blob/main/PyQT/img/2.png)    

    # 按钮点击回调事件
    def QueryMusic(self):
        print("点击事件")
        resp = requests.get("https://api.zhuolin.wang/api.php?callback=jQuery111305657767350626339_1651659515133&types"
                            "=search&count=20&source=netease&pages=1&name=%E8%AE%B8%E5%B5%A9&_=1651659515135")
        data = re.findall(self.Re, resp.text)
        for r in data:
            title = r[0].encode('utf8').decode('unicode-escape')
            author = r[1].encode('utf8').decode('unicode-escape')
            rorle = r[2].encode('utf8').decode('unicode-escape')
            self.ui.listWidget.addItem(title + '---' + author + '---' + rorle)
            
     # 界面UI  
     def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(459, 338)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(90, 60, 256, 192))
        self.listWidget.setObjectName("listWidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(150, 20, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(280, 20, 61, 23))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 30, 54, 12))
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 260, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(270, 260, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 459, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
-------------------------------------------------------------------
        self.retranslateUi(MainWindow)
        # 注册按钮按钮点击事件
        self.pushButton_2.clicked.connect(MainWindow.QueryMusic)
        # 注册列表框点击事件
        self.listWidget.itemDoubleClicked.connect(MainWindow.ClickItem)
--------------------------------------------------------------------
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
#### 六、PyQT5启动窗口原理
    
    方法1:
        import sys

        from PyQt5.QtWidgets import QApplication, QWidget

        if __name__ == '__main__':
            app = QApplication(sys.argv)  # 创建QApplication实例

            win = QWidget()   # 创建一个窗口
            win.resize(400, 300)  # 设置窗口大小
            win.move(300, 300)  # 设置窗口位置
            win.setWindowTitle("测试测试测试市场")  # 设置窗口标题
            win.show()  # 显示窗口

            sys.exit(app.exec_())  # 进入程序的主循环，并通过exit确保主程序安全退出

    
