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

    
     
