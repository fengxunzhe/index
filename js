一、【js的数据类型】

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
  
二、【函数】
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
  
  3、匿名函数
    func:function(){} 函数名是func
    
三、【循环语句】
    和pyhton没有区别
    for while continue if else break

四、【swithch语句】
    switch(arguments[0]){
        case 1:
            console.log("")
            break
        case 2:
            console.log("XX")
            break
    }

五、【三元运算符】
    表达式？test_test_success:test_failed
    判断表达式是否成立.成立执行test_success,否则执行test_failed
    
六、【对象】
    创建对象：三种创建对象方式
    1、var a = new object()
    2、var test = {可以是任何类型的参数} // test是个对象
    3、var a = Object.create(Object) 
    =================================================================================
    对象都具有的方法：
    constructor   构造方法
    hasOwnProperty  是否具有某个属性
    W.isPrototypeOf(0) W是否在传入的O的继承链上
    propertyIsEnumerable  属性是否可以迭代
    toLocalStrig  根据当地语言转化字符串
    toString  转化为字符串
    valueOf   返回内容,通常和toString一致
    ================================================================================
    var a = new Oject() # 创建对象a
    a = 1000 # 
    a.na = 10000
    a.sa = "javascript learning"
    console.log(a)
    {na: 10000, sa: 'javascript learning'}
      en: 10000
      [[Prototype]]: Object
      constructor: ƒ Object()  # 构造方法
      hasOwnProperty: ƒ hasOwnProperty()  是否具有某个属性a.hasOwnProperty("sa")
      isPrototypeOf: ƒ isPrototypeOf()
      propertyIsEnumerable: ƒ propertyIsEnumerable()
      toLocaleString: ƒ toLocaleString()
      toString: ƒ toString()
      valueOf: ƒ valueOf()
      __defineGetter__: ƒ __defineGetter__()
      __defineSetter__: ƒ __defineSetter__()
      __lookupGetter__: ƒ __lookupGetter__()
      __lookupSetter__: ƒ __lookupSetter__()
      __proto__: (...)
      get __proto__: ƒ __proto__()
      set __proto__: ƒ __proto__()
      ================================================================================
      
七、【自执行函数】：
    把扣下来的js代码放在以下代码块中可直接执行
    1、
      (function(){
      console.log("test");
      })();
    2、
      (function(){
          console.log("test");
      }());
    3、
      !function(){
          console.log("tests")
      }();

八、【数组】
    1、数组的两种创建方法
        var name = [1, 2,3 ,4]
        var naem = new Array(1,2,3,4)
    2、确认对象是否为数组
        Arrar.isArray()
    3、栈方法(先入后出)
        Array.push()
        Array.pop()
    4、队列方法
        Array.shift()  从头部删除 
        Array.unshift() 从头部添加，哪里空就填哪
    5、排序方法
        Array.reverse() 倒过来
        Array.sort()  排序
    6、常用方法
        concat 合并
        slice 切分
        spllice 删除
        indexOf 定位
    
九、【时间】
    var da = new Date()  # 返回时间对象Thu Feb 24 2022 21:07:47 GMT+0800 (中国标准时间)

    var da = Date.now()  # 返回时间戳
    
    Data.UTF(年，月，日，时，分，秒)  # 基于UTC国际协调时间
    
    toDateString  返回星期、年月日
    toTimeString 返回时分秒，时区
    
 10、【this】
    this想当于python中的self
    
    var xjb = {
        "name":"XX",
         age：100
        func:function(){  ### 匿名函数
          console.log("===")
        }
        func2:function(){
          this.func(),  ### this调用父类的方法
          this.name-666
        }
    }
    
    
    
