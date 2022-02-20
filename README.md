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
       
       iteams() # 把字典中的元素以列表的形式输出为元组
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
