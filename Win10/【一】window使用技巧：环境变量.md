一、windows路径默认查找方式
=

  主要通过 PATH 路径查找, 1、我们将 路径添加到PATH 里面，即可在cmd 下面运行
                         2、我们新建变量，然后将变量添加到PATH 里同样可以找到
                         
  如：
      ![imag](https://github.com/fengxunzhe/index/blob/main/Win10/1.png)
      
 然后在PATH 中 加入NODE_PATH即可
 
 
二、用户变量和系统环境变量
= 
  1、首先，windows会查找 系统环境变量PATH 的值，所以
    【系统环境变量操作】
    
      第一种：直接在 系统环境变量PATH 添加路径
      
      第二种：新建系统变量，把变量值添加进PATH
      
    【用户环境操作变量】
    
      第三种：在用户环境变量的PATH 加入路径， windows加载完系统的PATH路径后  会 加载 用户的 PATH路径
      
      第四种：新建用户变量，把变量值添加进用户PATH
