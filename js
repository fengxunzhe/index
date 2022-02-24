一、js的数据类型

  undefined 、null、  boolean、 string、 number
  1、undefined 和 null 的区别
    undefined代表了不存在的值（nonexistence of value），null代表了无值（no value）。
        let a;
        console.log(a);
        // undefined
        let b = null;
        console.log(b);
        //null

    由上面的代码得知，undefined表示变量已经声明，但是没有赋值。因为它的值是不存在的，所以为undefined。

    null表示变量已经声明，且变量赋值为null（为空），所以为结果为null。
  
二、函数
  1、函数可以通过arguments取出传入的参数
      function test(){
        console.log(atguments[0])  # 取出第一个参数
      }
      test(name, age, six) # 传入三个参数
      
  2、函数没有重载
      function test(){
        var name = "xxx"
        return name
      }

      function test(age, six){
          console.log("+++++", age,six)
      }

      var res = test()
      默认情况下相当的函数,后面的会替换前面的，所有此时执行的是第二个test方法
    
三、循环语句
    和pyhton没有区别
    for while continue if else break

四、swithch语句
    switch(arguments[0]){
        case 1:
            console.log("")
            break
        case 2:
            console.log("XX")
            break
    }

五、三元运算符
    表达式？test_test_success:test_failed
    判断表达式是否成立.成立执行test_success,否则执行test_failed
    
六、对象
    创建对象：三种创建对象方式
    1、var a = new object()
    2、var test = {} // test是个对象
    3、var a = Object.create(Object) 
    =================================
    对象都具有的方法：
    constructor   构造方法
    hasOwnProperty  是否具有某个属性
    W.isPrototypeOf(0) W是否在传入的O的继承链上
    propertyIsEnumerable  属性是否可以迭代
    toLocalStrig  根据当地语言转化字符串
    toString  转化为字符串
    valueOf   返回内容,通常和toString一致
    
    
