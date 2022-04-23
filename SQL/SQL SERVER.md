## 一、数据库分类
	1、关系数据库，有【MySQL、MariaDB】；
	2、非关系型数据库，【Cassandra、MongoDB】；
	3、键值【key-value】数据库，有【Dynamo、LevelDB、Redis】。

## 二、SQL Server介绍
	微软推出的 关系型数据库系统 
	特性：
	1、高性能设计： 可充分利用windowsNT的优势(同微软同windows)；
	2、系统管理先进，支持windows图形化管理工具，支持本地和远程的系统管理和配置(图形界面操作)；
	3、强壮的事务处理功能，采用各种方法保证数据的完整性
	4、支持对称多处理器结构、存储过程、ODBC，具有自主的SQL语句

## 三、数据库操作(database)
#### 1、新建数据库(增)
	CREATE DATABASE test01 ON Primary(
		NAME=test01,
		FILENAME='C:\DATA\test01.mdf',
		SIZE=10,
		MAXSIZE=50,
		FILEGROWTH=5
	)
	LOG ON(
		NAME=test01_log,
		FILENAME='C:\DATA\test01_log.ldf',
		SIZE=10,
		MAXSIZE=50,
		FILEGROWTH=5
	)
	/**
		ON [PRIMARY]是表示表是建立在主文件组上。PRIMARY表示主文件组。如果没有指定默认文件组，则主文件组是默认文件组;
		LOG ON 是表示表是建立log文件；
		NAME=test01_log,  文件对应的name id，读取文件的时候调用该name
		FILENAME= 文件存放的位置；
		SIZE=10 文件大大小；
		MAXSIZE=50, 文件最大多少;
		FILEGROWTH=5 每次增长多少；
	**/
	
#### 2、删除数据库(删)
	DROP DATABASE 数据库1，数据库2；
	DROP DATABASE 数据库1；
	
#### 3、修改数据库(改)
	3.1、修改数据库名
		ALTER DATABASE test01 MODIFY NAME=test02;
	
	3.2、修改数据库参数(文件名不能修改，修改之后会新建个数据库文件)
		ALTER DATABASE test01 MODIFY FILE(
			NAME=testxxxx,
			SIZE=80,
			MAXSIZE=50,
			FILEGROWTH=5 
		)

#### 4、查询数据库(查)
	EXECSP_HELPDB test01；
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
