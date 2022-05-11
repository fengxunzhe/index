import sys
from Splash import *
from PyQt5.QtWidgets import QApplication, QWidget
from main_window import *
from mind import *


class Example(QApplication):  # 在第一步实例化QApplication中 调用初始化界面
    def __init__(self):
        super(Example, self).__init__(sys.argv)


    def initWinodws(self):
        splash = SplashScreen()  # 启动界面  初始化
        splash.loadProgress()  # 启动界面  进度条
        

# 第三步   加载主窗口
        # 加载主窗口 -->>前提是要创建一个空白窗口，把空白窗口传递给主窗口，主窗口覆盖空白窗口
        self.qw = QWidget()
        self.qw.show()
        # 为什么此处要用self.变量   不能直接 qw=XXX
        # 因为 qw 是 局部变量，所以窗口在使用一下就闪退了
        # 而self.qw是 随着类Example销毁才会销毁,所以一直存在

        splash.finish(self.qw)



if __name__ == '__main__':
    example = Example()  # 第一步  实例化QApplication，此处相当于 QApplication(sys.argv)

    example.initWinodws()  # 第二步 实例化之后加载初始化界面

    # 第三步   加载主窗口

    sys.exit(example.exec_())  # 第四步 进入主循环  相当于sys.exit(app.exec_())  app是QApplication对象  example是app是QApplication子类的对象
