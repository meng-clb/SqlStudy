# SqlStudy
# My SQL 学习
<hr>

## 查看数据库
**列出所有的库**
```mysql
show databases; 
```
**所有的clb均可替换为你的库名**

**创建库**
```mysql
create database 创建的库名;
create database clb;
```

**使用库**
```mysql
use 库名
use clb
```

**查看当前选择的库/表**
```mysql
select database();
select table();
```

**查看某个库/表的创建语句**
```mysql
show create database 库 \G
show create table 表 
show create database clb \G
```

**删除某个库/表名**
```mysql
drop database 库/表;
drop table 库/表;
```

**创建表**
```mysql
create table 表名(
    表头 类型,
    表头 类型
);
```
**查看表**
```mysql
show tables;
decs 表名; // 查看表的具体信息
```
