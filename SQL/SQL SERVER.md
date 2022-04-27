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
	
## 四、数据类型
#### 1、整数类型
	tinyint   0~255   1字节
	smaillint  (-32768 ~ 32767) 2字节
	int  (-2^31 ~ 2^31)  4字节
	bigint  (-2^63 ~ 2^63)  8字节

#### 2、浮点数类型
	float  
	
#### 3、时间类型
	time    12:21:21.231334(时：分：秒.毫秒)
	date    2022-04-26
	smalldatetime   2022-04-26   12:21
	datetime   2022-04-26   12:21:21.231
	datetime2  2022-04-26   12:21:21.231334
	
#### 4、字符串类类型
	char 固定长度 char(n)  n取值1~8000  (非Unicode)
	varchar 可变长度  varchar(n|max) n取值1~8000  (非Unicode)
	nchar 固定unicode字符串 nchar(n)  n取值1~4000
	nvarchar 可变长度  nvarchar(n|max) n取值1~4000 
	
## 五、表操作(table)
#### 1、创建表操作(增)
	creat table userinfo(
		ID int primary key not null,  # 主键
		name varchar(10)  not null,  
		age int null
	)
	

#### 2、删除表操作(删)	
	DROP TABLE userinfo,......;
	
#### 3、修改表操作(改)	
	EXEC sp_rename '表1'，'新表1';

#### 4、查询表操作(查)	
	SELECT * FROM USERINFO;   # 查询表信息

## 六、字段操作(COIUMN)
#### 1、添加字段(增)
	ALTER TABLE USERINFO   # 添加xxx字段
	ADD XXX varchar(50) not null;
	
#### 2、删除字段(删)
	ALTER TABLE USERINFO
	DROP COLUMN age;  # 删除age字段

#### 3、修改字段(改)
	3.1、更改表字段类型长度
		ALTER TABLE USERINFO
		ALTER COLUMN name varchar(100); # 修改name的长度从10到改为100
	
	3.2、更改表字段类型
		ALTER TABLE USERINFO 
		ALTER COLUMN name int；     # 修改name的字段类型
		
	3.3、更改表字段的约束(是否为空)
		ALTER TABLE USERINFO  
		ALTER COLUMN name null;    # 修改name的字段约束为可以为空
	
	3.4、更改字段为主键(主键唯一)
		ALTER TABLE USERINFO 
		ALTER COLUMN KID primary key(ID)   # 修改ID的字段为唯一主键
		
	3.5、更改字段名称
		ALTER TABLE USERINFO
		EXEC sp_rename 'USERINFO.age','userage' ,'COLUMN';  # 将age字段修改为userage字段
		
#### 4、查询字段(查)	


	
	
