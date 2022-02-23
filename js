一、js的数据类型
=
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
  
