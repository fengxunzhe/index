#### 一、下载QT库
    pyqt5 和  pyqt-tools （pip install xxx）
    
#### 二、使用QT designer
###### 2.1、直接使用desinger
    在qt5-applications--QT--bin中使用designer
    
###### 2.2、 Pycharm中配置
![imag](https://github.com/fengxunzhe/index/blob/main/PyQT/img/5.png)
![imag](https://github.com/fengxunzhe/index/blob/main/PyQT/img/6.png)
![imag](https://github.com/fengxunzhe/index/blob/main/PyQT/img/7.png)

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
UI--->>>Py文件===默认安装PyQT5会安装pyuic5；使用pyuic5 -o 保存文件.py 要转换的文件.ui

qrc(资源图片文件)--->>>Py文件===默认安装PyQT5会安装pyrcc5；使用pyrcc5 -o 保存文件.py 要转换的文件.qrc  (图片在转为py后会以二进制储存)

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
         QtCore.QMetaObject.connectSlotsByName(MainWindow)
         
 -------------------------------------------------------------------       
         class example(QMainWindow):
            def __init__(self):
                super(example, self).__init__()
                self.doc_Windows = Ui_MainWindow()
                # 加载test.ui界面
                self.doc_Windows.setupUi(self)
                # 取数据
                print("读取数据中")
                self.res = getDataBase()
                
         加载界面UI
         
--------------------------------------------------------------------
      
        
#### 六、PyQT5启动窗口原理（*重要）
    
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

    方法2:
        import sys

        from PyQt5.QtWidgets import QApplication, QWidget


        class Example(QWidget):
            def __init__(self):
                super(Example, self).__init__()
                pass
            # --------------------------------------------------------------------------
            # 对象在创建后初始化默认调用__init__方法，调用父类super即QWidget的初始化方法可以新建个空白窗口
            # slef是QWidget对象，此处可通过
            # self.resize(400, 300)   self..setWindowTitle("测试测试测试市场") 等等重新修改空白窗口属性
            # 想当于win = QWidget()  win.resize(400, 300)  等等 /win = QWidget win是一个QWidget对象， self继承了QWidget，拥有父类的属性和方法，所以self相当于QWidget
            # --------------------------------------------------------------------------

        if __name__ == '__main__':
            app = QApplication(sys.argv) # 创建QApplication实例  
            
            # --------------------------------------------------------------------------
            # print(sys.argv)      sys.argv 是默认接收控制台下面输出的参数       
            # PS C:\Users\zy\Downloads\PyQt5_example-main\PyQt5_example-main> PYTHON test002.py   1  2  3
            # ['test002.py', '1', '2', '3']
            # print(QApplication(sys.argv))   <PyQt5.QtWidgets.QApplication object at 0x000001D61F8B3F78>    QApplication创建一个应用程序对象
            # --------------------------------------------------------------------------

            ex = Example()  # 创建一个QWidget窗口对象
            ex.show()  # 显示窗口

            sys.exit(app.exec_())
            
            # --------------------------------------------------------------------------
            #   sys.exit 是python程序退出时执行  print(sys.exit())
            #  进程已结束,退出代码0  正常退出是0
            #  进程已结束,退出代码1  程序异常退出是1 或者 是 十六进制代码
            #  app.exec_() 代表QApplication对象在正常运行中会处于无限循环中，在循环中监视消息事件(如点击，触摸等等事件)，直到程序异常，sys.exit捕捉异常代码
            # --------------------------------------------------------------------------
            # 总结： 创建一个QApplication对象，该对象会处于无限循环中监视消息事件
 
 #### 七、Pycharm模板设置
 ![imag](https://github.com/fengxunzhe/index/blob/main/PyQT/img/3.png)
 
 第三步：在Pycharm中输入 qaa 会自动调用该模板
 
 第五步：代码模板
 
 第六步：模板适用范围
 
  #### 八、PyQT5  API
                              QObject
                                |
                              QWidget
                                |
    QAbatractButton-----QFrame-----QAbstractSlider-----QDiglog-----QMenu--......
           |               |               
       QPushButton  QAbstractScrollArea
                           |
                QAbstractItemView--QTextView 
  
  
  ##### 8.1、QWidget
  QWidget本身是一个空白窗口;继承QWidget后相当于新建了个空白窗口，后面其他组件都会显示在该空白组件内
  
#### 九、信号 和 槽
![imag](https://github.com/fengxunzhe/index/blob/main/PyQT/img/4.png)

第二步: pushButton发送一个点击事件的信号--->>> 即按钮被点击

第五步: 槽  即按钮被点击后触发的操作，这里自定义为Login函数，点击之后调用Login函数

第六步: 方框中都是系统默认推荐的

#### 十、常用表格API

//设置表格整行选择

self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)

self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)

//设置表格不可编辑

self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

//禁用窗口最大化

MainWindow.setFixedSize(MainWindow.width(), MainWindow.height())

//设置第三个的列宽

self.tableWidget.setColumnWidth(3, 245)

//设置窗口ICO

MainWindow.setWindowIcon(QIcon("./re.png"))

