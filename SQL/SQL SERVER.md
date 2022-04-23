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

## 三、数据库操作
	1、新建数据库
	CREATE DATABASE test01 Primary ON(
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

