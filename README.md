一、字符串操作String
=
  1、字符串定义
-
 
      ''单引号  ""双引号  """""""三引号(定义大段的数据,如JS源码)
      
  2、常用内置方法
-

    strip()   # 去除首尾空格，返回字符串
        #################
        data = "  python string  字符串  "
        print(data.strip())  # python string  字符串
        #################
        
    lstrip()  # 去除左边空格, 返回字符串
    
    rstrip()  # 去除右边空格, 返回字符串
    
    replace(arg1,arg2) # 文本替换,arg1:待替换文本, arg2:替换的文本  返回字符串
        #################
        data.replace("python", "java").replace("string", "math") # 多次替换,python替换成java，string替换成math
        #################
        
    spilt(arg1)   # 分割文本,arg1分割符 返回列表
        #################
        data.split(' ')[3] #data.spilt返回list列表，取出list中的第三个
        #################
        
     upper()  # 到大写  返回字符串
     lower()  # 到小写  返回字符串
     
     find(str, start, end)   # 文本寻找 str:要查找的字符串 start:起始查找位置(参考), end:结束查找的位置(参考)  返回数字
         #################
         index = data.find("ing") # 查找ing字符串,返回所在的位置, 数字
         data[index]  # 通过位置取出第index之后的文本
         #################

二、列表操作List（list可出现重复元素）list()
=
  1、常用方法
-
     append(obj) # 列表加入一个obj对象
         #################
         data = ['AAA', 'BBB', 'CCC']
         data.append(3)
         print(data)  # data = ['AAA', 'BBB', 'CCC', 3]
         #################
         
     extend(list) #  列表加入多个远程:list:迭代器list
        #################     
        data = ['AAA', 'BBB', 'CCC']
        data.extend(["33", "44", 55, (6, 7)])
        print(data)  # data = ['AAA', 'BBB', 'CCC', '33', '44', 55, (6, 7)]
        #################     
     
     index(str,start,end) #  str:要查找的字符串 start:起始查找位置(参考), end:结束查找的位置(参考)  返回数字位置
     
     insert(index, obj)   # index：要插入的位置,obj：插入的对象(可结合index方法使用)
     
     pop() # 把列表中最后一个元素删除 ， 返回删除的元素
     
     remove(val) # 删除指定元素第一次出现的时候删除,不会全部删除
     
     count(val)  # 返回一个元素在列表中出现的次数   
         #################  
         data = ['AAA', 'BBB', 'CCC', "AAA"]
         for x in range(0, data.count('AAA')):
             data.remove('AAA') # 删除所有指定的元素 注: for x in y: y代表可迭代的对象，如list
         print(data)  # ['BBB', 'CCC']
         #################  
         
     reverse()  # 列表元素反转
     
     sort(key, reverse)  #  列表排序 reverse:true反转结果，false:不反转结果
         #################      
         def t(x):
            print("---", x)
            return x[0]
         data = ['AAA', 'BBB', 'CCC', "AAA"]
         data.sort(key=t)
         print(data) # ['AAA', 'AAA', 'BBB', 'CCC']
         #################  

三、元组(只能读不能改动)tuble()
=
    count(val) # 元组中元素出现的次数，返回num
        #################  
        data = (1, 2, 3, 1, 4)
        print(data.count(1)) # 2
        ################# 
        
    index(str,start,end) #  str:要查找的字符串 start:起始查找位置(参考), end:结束查找的位置(参考)  返回数字位置

四、字典dict{key，val}
=
    1、常用方法
-
       clear() # 清除字典所有元素
       
       get(key) # 获取元素 通过key获取val值
       
       iteams() # 把字典中的元素以元组的形式输出为列表
         #################      
         data = {'python': 1,'GO': 2, 'java': 3 }
         print(data.items())  # dict_items([('python', 1), ('GO', 2), ('java', 3)])
         ################# 
       
       key() # 取key值
       
       value() # 取value值
       
       update(**argv) # 更新或者 添加字典元素
         ################# 
         data = {'python': 1,'GO': 2, 'java': 3 }
         data.update({'python': 2, 'C++': 4})
         print(data)  # {'python': 2, 'GO': 2, 'java': 3, 'C++': 4}
         ################# 

五、类Class对象
=
    1、私有\公有属性和方法
-
       class student():
          write = 1 # 公有属性
          __write = 2 # 私有属性

          def read(self):
              print(self.write)  # 调用公有属性
              print(self.__write)  # 调用私有属性
              print(self.__read())  # 调用私有方法

          def __read(self):
              print(self.write)
              print(self.__write)


      stu = student() # 实例化类对象
      print(stu.write)  # 外部可以调用类的方法和属性
      print(stu.read())
      print(stu.__read())  # ERROR 外部不能调用class的私有方法和属性

   总结: 类 的私有公有方法和属性在 类的内部可以随便调用, 在类的外部 私有属性和方法不能调用 

六、for循环实现原理常用方法:enumerate   和  zip
=
    1、enumerate()   循环的时候自带计数(从0开始)
          ################# 
             原始方法：
              list = ['GO', 'JAVA', 'C++', 'PYTHON', 'JAVASCRIPT']
              i = 0
              for x in list:
                  print(i, x)
                  i += 1
              输出：
              0 GO
              1 JAVA
              2 C++
              3 PYTHON
              4 JAVASCRIPT
          ################# 
          ################# 
             改进方法：
              list = ['GO', 'JAVA', 'C++', 'PYTHON', 'JAVASCRIPT']
              for num, x in enumerate(list):
                 print(num, x)
              输出：
              0 GO
              1 JAVA
              2 C++
              3 PYTHON
              4 JAVASCRIPT
          ################# 
          
     2、zip()  # 合并多个list
          #################     
          >>>a = [1,2,3]
          >>> b = [4,5,6]
          >>> c = [4,5,6,7,8]
          >>> zipped = zip(a,b)     # 打包为元组的列表
          [(1, 4), (2, 5), (3, 6)]
          >>> zip(a,c)              # 元素个数与最短的列表一致
          [(1, 4), (2, 5), (3, 6)]
          ################# 
          list = ['GO', 'JAVA', 'C++', 'PYTHON', 'JAVASCRIPT']
          list2 = ['111', '222', '333']
          for num, x in zip(list, list2):
              print(num)
          ################# 
          
     3、for循环实现原理
          class a:
              def __init__(self, num):
                  print("1111111")
                  self.num = num

              def __next__(self):
                  print("3333333333")
                  if self.num <= 0:
                      raise StopIteration
                  self.num -= 1
                  return self.num

              def __iter__(self):
                  print("222222222")
                  return self


          for x in a(10):
              print("----------")
              print(x)
          输出结果：
          1111111
          222222222
          3333333333
          ----------
          9
          3333333333
          ----------
          8
          3333333333
          总结：先init  然后iter.然后next
    
七、with open实现原理
=
     class A:
        def __enter__(self):
            print("进入enter")
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            print(exc_tb, exc_val, exc_type)
            print("进入了exit")
            self.file.close() 

        def file_open(self):
            self.file = open('test.txt', mode='w', encoding='utf-8')
            self.file.write("testtesttest")
            print("写入完成")


    with A() as a:
        print("进入了with内部作用域")
        a.file_open()
    ========================================
    进入enter
    进入了with内部作用域
    写入完成
    None None None
    进入了exit
    ========================================
    总结: 首先进入__enter__方法,   然后"进入了with内部作用域"，  再打开文件file_open，写入完成后;  进入__exit__方法
    
八、参数args  和 参数kwargs
=
    def foo(one, *args, **kwargs):
      print(one)  # 1

      print(args)  # (2, 3, 4, 5, [1, 2, 3], (22, 33)) # 返回元组集合
      print(*args)  # 2 3 4 5 [1, 2, 3] (22, 33)  # 元组去掉了

      print(kwargs)  # {'kk': 2, 's': 3}  返回dict字典
      print(*kwargs) # kk s  只返回key

    foo(1, 2, 3, 4, 5,[1,2,3],(22,33),kk=2,s=3)    
九、OS模块
=
      # -*- coding：utf-8 -*-
      import os

      # 1 获取当前文件所在路径C:\Users\AF\PycharmProjects\pythonProject3  --->>> os.getcwd()
      print("1、" + "--->>>", os.getcwd())

      # 2 获取指定路径下所有的文件;默认不写参数为C:\Users\AF\PycharmProjects\pythonProject3   --->>>os.listdir(str:path)  返回list列表
      print("2、" + "--->>>", os.listdir())
      print("2、" + "--->>>", os.listdir("C:/Users/AF/Desktop/tl"))

      # 3 使用os.removedirs()函数删除多级目录。os.removdirs(path)删除的目录必须是空目录
      print("3、" + "--->>>", "os.removdirs(path)删除一个空目录")
      print("3、" + "--->>>", "os.remove(path, str),删除指定目录文件,注意一定是一个文件")
      try:
          os.removedirs(r"C:/Users/AF/Desktop/mrp/test")
      except IOError:
          print("Error: 没有找到文件或读取文件失败")
      else:
          print("内容写入文件成功")

      # 4 os.path.isfile(path) 检测路径是否是一个文件,注意不是文件夹
      print("4、" + "--->>>", os.path.isfile('C:/Users/AF/Desktop/tl/TL_3_9.apk'))

      # 5 os.path.isdir() 检测路径是否是一个目录
      print("5、" + "--->>>", os.path.isdir("C:/Users/AF/Desktop/tl/"))

      # 6 os.path.isabs()  是否是绝对路径
      print("6、" + "--->>>", os.path.isabs("C:/Users/AF/Desktop/tl/"))
      print("6、" + "--->>>", os.path.isabs("./Desktop/tl/"))

      # 7 os.path.exists 检测路径是否存在
      print("7、" + "--->>>", os.path.exists("./Desktop/tl/"))
      print("7、" + "--->>>", os.path.exists("C:/Users/AF/Desktop/tl/"))

      # 8 os.path.split("C:/Users/AF/Desktop/tl/TL_3_9.apk") 取出路径最后一个/后的文件  此处返回TL_3_9.apk  返回元组
      print("8、" + "--->>>", os.path.split("C:/Users/AF/Desktop/tl/"))
      print("8、" + "--->>>", os.path.split("C:/Users/AF/Desktop/tl/TL_3_9.apk"))
      print("8、" + "--->>>", "os.path.splitext取出文件格式", os.path.splitext("C:/Users/AF/Desktop/tl/TL_3_9.apk"))

      # 9 print(os.path.dirname("C:/Users/AF/Desktop/tl/TL_3_9.apk"))  获取文件的路径  去掉文件名，返回目录 __file__表示了当前文件的path
      print("9、" + "--->>>", __file__ + "--去掉文件名，返回目录", os.path.dirname(__file__))

      # 10 返回文件最后的文件名 os.path.basename('D:/file/cat/dog.jpg')  return dog.jpg
      print("10、" + "--->>>", os.path.basename('D:/file/cat/dog.jpg'))

      # 11 执行命令行 os.system("cmd")
      print("11、" + "--->>>", "执行命令行", "os.system('cmd')")

      # 12 获取指定系统环境变量os.getenv("PATH")
      print("12、" + "--->>>", "获取指定系统环境变量", os.getenv("PATH"))

      # 13 获取所有系统环境变量os.environ
      print("13、" + "--->>>", "获取所有系统环境变量", os.environ)

      # 14 设置临时系统环境变量os.environ.setdefault("", "")
      print("14、" + "--->>>", "设置临时系统环境变量", os.environ.setdefault("HOME", "/home/test"))

      # 15 文件重命名
      # 列出目录
      print("15、" + "--->>>", "文件重命名", "目录为: %s" % os.listdir(os.getcwd()))
      try:
          os.rename("转换后的素描图.jpg", "转换ss的素描图.jpg")
      except IOError:
          print("15、" + "--->>>", "文件重命名", "Error: 没有找到文件或读取文件失败")

      # 16 创建多级目录  os.makedirs(r"C:/test/test")  os.mkdir(str)
      try:
          print("16、" + "--->>>", "创建多级/单级目录", os.makedirs(r"C:/test/test"))
      except IOError:
          print("16、" + "--->>>", "创建多级/单级目录", "Error: 没有找到文件或读取文件失败")

      # 17 获取文件属性os.stat(str)
      print("17、" + "--->>>", "获取文件属性", os.stat(path="C:/Users/AF/Desktop/tl/TL_3_9.apk"))

      print("18、" + "--->>>", "os.chmod()修改文件权限")
      print("19、" + "--->>>", "os.path.getSize(path)获取文件大小")
      print("20、" + "--->>>", "os.path.join(dir,path)组合目录与文件")
      print("21、" + "--->>>", "os.kill(10844,signal.SIGKILL)杀死进程")
     
十、闭包
=
    1、闭包的应用场景
-
        理解：
        简单来说，闭包就是在函数里面声明函数，实际开发中主要应用于封装变量，保护变量不受外界污染，也相当于是在函数作用域里面再声明一个内部作用域，这样执行结果拿到的变量都是不同的，拿的就不是全局变量。

        特性：函数内部嵌套函数

        缺点：闭包容易消耗内存

        注意：
        子函数可以访问父函数中所有的局部变量，，但是父函数不能访问子函数的变量
        

    2、源码分析
-
            def outer(a):
              b = 10

              # inner是内函数
              def inner():
                  print(a + b)
              print(inner)
            return inner


          if __name__ == '__main__':
              demo = outer(5)
              demo()  # 15
           闭包条件：
      　　 1 在一个外函数中定义了一个内函数。

           2 内函数里运用了外函数的临时变量。

           3 并且外函数的返回值是内函数的引用。
             
十一、异常
=
    1、普通异常
-
        try:
            a = 1
            print(b)
        except Exception as e:
            print("异常代码", e)
        finally:
            print("一定会执行")
       输出====================
           异常代码 name 'b' is not defined
           一定会执行
           
     2、自定义异常
-
        class MyException(BaseException):
            def __init__(self):
                print("实例化之后运行")

            def __str__(self):
                return "这是自定义的异常"

        # 在一个函数中我们可以通过Raise主动抛出我们的异常
        raise MyException
        输出==================
        Traceback (most recent call last):
            File "<input>", line 1, in <module>
            File "C:\Program Files\JetBrains\PyCharm 2020.3.5\plugins\python\helpers\pydev\_pydev_bundle\pydev_umd.py", line 197, in runfile
              pydev_imports.execfile(filename, global_vars, local_vars)  # execute the script
            File "C:\Program Files\JetBrains\PyCharm 2020.3.5\plugins\python\helpers\pydev\_pydev_imps\_pydev_execfile.py", line 18, in execfile
              exec(compile(contents+"\n", file, 'exec'), glob, loc)
            File "C:/Users/AF/PycharmProjects/pythonProject3/1.py", line 10, in <module>
              raise MyException
          MyException: 这是自定义的异常
          
      3、捕获输出异常信息
-
        import traceback

          try:
              print(a)
          except Exception as e:
              print(e)
              print(traceback.print_exc(file=open('error.txt', 'a+', encoding='utf8'))) # 把异常错误信息输出到error.txt文件中     
 

十二、super()方法
=
        class A():
        def say(self):
            print('A的 say方法')


        class B(A):
            def say(self):
                print("B的 say方法")


        class C(B):
            def say(self):
                print("C的 say方法")
                super(C, self).say()  # 调用父类B的方法

        data = C()
        print(data.say())  # 调用C的方法
        adata = A()
        print(adata.say()) # 调用A的方法

十三、描述符： __get（）__' ; __set()__；__del()__
 =
    在 Python 中，允许把一个类属性，托管给一个类，这个属性就是一个「描述符」
    具体见：https://zhuanlan.zhihu.com/p/336926012
    

十四、属性操作hasattr、setattr、getattr
=
      class A:
      def __init__(self, val):
          self.val = val
      print(hasattr(A, 'val'))  # False 对象A中val是否有值
      print(hasattr(A(999), 'val'))  # True 对象A先赋值val,在判断是否有值
      print(hasattr(A, '__init__'))  # 对象A中是否存在init方法
      print(setattr(A, 'val', '888'))  # 对象A中val赋值888
      print(getattr(A, 'val')) # 取出对象A中val的值

十五、property 方法当属性使用
=
  1、常规调用方法
  
    class A:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def cs(self):
            return self.x * self.y

    data = A(10, 20)
    print(data.cs())
    
  2、property调用
    class A:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        @property
        def cs(self):
            return self.x * self.y

    data = A(10, 20)
    print(data.cs)

十六、__str（）__、__repr()__方法
=
    class A:
        def __str__(self):
            print("这个是object对象")

        def __repr__(self):
            print("这个是object对象22")

    data = A()
    print(data)   # <__main__.A object at 0x0000019C9EEDEF10> 此处按道理应该输出一个object+内存地址信息，但若是类实现了__repr__或者__str__方法;
    那么就会输出该方法的内容,此处输出【这个是object对象/这个是object对象22】  str默认覆盖repr

十七、不可变对象修改 及 __new()__方法的使用
=
    不可变对象: int 、string、元组 --->>>> 当值改变时, 内存地址也发生变化
    可变对象  ：list列表、dict字典 --->>>> 当值改变时, 内存地址不发生变化; 列表 字典可以append加入
    
    万物皆对象：此处以int为例; 尝试修改
    class A(int):  # 继承int对象
    
    def __init__(self, val, name):
        self.val = val   # 1、赋值 999
        self.name = name   # 1、赋值 fengxunzhe

        super(A, self).__init__(val)  # 2、调用int方法的__init__方法,该方法传入一个参数,此处传入 999 修改init方法，报错  (因为self是不可变对象,要在self形成之前即cls改变才行)


    data = A(999, 'fengxunzhe') # 1、赋值
    print(data) 
    print(data.val)  # 取值val
    print(data.name)  # 取值name
    
    输出报错信息:TypeError: 'str' object cannot be interpreted as an integer
    
    ================
    正确修改：对象  首先调用 __new__方法， 然后调用__init__方法
    class A(int):  # 继承int对象
    def __new__(cls, val, name):  # 形成self的过程
        instance = super().__new__(cls, val)  # 实例化int的new方法，赋值int; 此处instance相当于self    
        instance.val = val
        instance.name = name
        return instance  # 返回实例化  self


    data = A(999, 'fengxunzhe')
    print(data.val)
    print(data.name)

十八、迭代器、生成器、装饰器
=
  1、迭代器
-
    迭代器指的就是【支持迭代的容器】，更确切的说，是支持迭代的容器类对象，这里的容器可以是列表、元组等这些 Python 提供的基础容器，也可以是自定义的容器类对象，只要该容器支持迭代即可。
    所有迭代器对象都有__next__(self)：返回容器的下一个元素。 __iter__(self)：该方法返回一个迭代器（iterator）
                                                 
    
    1.1、支持迭代的容器操作:List   首先【转换为迭代器对象】  iter(可迭代的对象)
        data = ['JAVA', 'PHP', 'C++', 'PYTHON']
        lst = iter(data)  #  转换为迭代器对象
        print(lst)  # <list_iterator object at 0x00000218C2825320> 返回迭代器对象
        print(lst.__next__())  # 迭代器对象具有的方法  JAVA
        print(lst.__next__())  # php
    
    1.2、自定义【迭代器对象】(首先实现所有迭代器对象具有的方法 __iter__(self), __next__(self) 
        class listDemo:
            def __init__(self):
                self.__date=[]
                self.__step = 0
            def __next__(self):
                if self.__step <= 0:
                    raise StopIteration
                self.__step -= 1
                #返回下一个元素
                return self.__date[self.__step]
            def __iter__(self):
                #实例对象本身就是迭代器对象，因此直接返回 self 即可
                return self
            #添加元素
            def __setitem__(self,key,value):
                self.__date.insert(key,value)
                self.__step += 1
            mylist = listDemo()
            mylist[0]=1
            mylist[1]=2
            for i in mylist:
                print (i)
      
  2、生成器
-
        生成器本质上也是迭代器;以 list 容器为例，在使用该容器迭代一组数据时，必须事先将所有数据存储到容器中，才能开始迭代；而生成器却不同，它可以实现在迭代的同时生成元素。
        也就是说，对于可以用某种算法推算得到的多个数据，生成器并不会一次性生成它们，而是【什么时候需要，才什么时候生成】。
    
    def intNum():
        print("开始执行")
        for i in range(5):
            yield i
            print("继续执行")
        num = intNum()
        print(num)  # <generator object intNum at 0x00000186B2EFA390>  返回生成器对象
        print(num.__next__())  # 0  第一次输出 0  yield相当于return 返回 0
        print(num.__next__())  # 1  第二次输出1  从上一次yield后继续执行  返回1 
        print(num.__next__())  # 2  第三次输出1  从上一次yield后继续执行  返回2
    输出:
        <generator object intNum at 0x0000017AB5DEA390>
        开始执行
        0
        继续执行
        1
        继续执行
        2
        
  3、装饰器     
-
     #funA 作为装饰器函数
      def funA(fn):
          print("C语言中文网")
          fn() # 执行传入的fn参数
          print("http://c.biancheng.net")
          return "装饰器函数的返回值"
      @funA
      def funB():
          print("学习 Python")
          return "xxxxx"
      print(funB)
      
     输出结果：
       C语言中文网
       学习 Python
       http://c.biancheng.net
       装饰器函数的返回值
       
    A装饰B，相当于在B的外边套一层装饰物,把B当参数传入;将 A() 函数执行完成的返回值反馈回  B(print(funB))；函数本身不返回
    ==============
      带参数装饰器：
      def funA(fn):
    # 定义一个嵌套函数
        def say(arc):
            print("Python教程:",arc)
        return say
        
        @funA
        def funB(arc):
            print("funB():", a)
        funB("http://c.biancheng.net/python")
        
        输出：Python教程: http://c.biancheng.net/python
        
        上面相当于：
          def funA(fn):
            # 定义一个嵌套函数
            def say(arc):
                print("Python教程:",arc)
            return say

         def funB(arc):
             print("funB():", a)

         funB = funA(funB)
         funB("http://c.biancheng.net/python")
         输出：Python教程: http://c.biancheng.net/python
         
    参考：http://c.biancheng.net/view/2270.html
   
Python编程技巧汇总：
=
    1、if  else的简单写法
        return bytes[:-2] if bytes.endswith('.0') else bytes + "bytes"
        # if bytes.endswith('.0')  判断butes是否以.0结尾, 是的话直接反返回bytes+"bytes",  反之，从后往前取倒数第2个之前的数据
        
    2、python字符串加r、f、b、u的作用
        r:   r"\n\n\n\n”　　# 表示一个普通生字符串 \n\n\n\n，而不表示换行了
        f:   格式化字符串    name = zhangsan  print(f'{name} done in) 此处会自动把name替换成zhangsan
        b:   b" "前缀表示：后面字符串是bytes 类型。 response = b'<h1>Hello World!</h1>'     # b' ' 表示这是一个 bytes 对象
        u:   data = u'我是中文'  后面字符串以 Unicode格式进行编码，一般用在中文字符串前面，防止因为源码储存格式问题，导致再次使用时出现乱码。
       
       
       
