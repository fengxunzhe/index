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

