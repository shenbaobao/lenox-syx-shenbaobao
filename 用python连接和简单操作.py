>>> #coding=utf-8
>>> import MySQLdb
>>> conn=MySQLdb.connect(
	host='localhost',
	port=3306,
	user='root',
	passwd='Qq123456789',
	db='attend',
	)#连接数据库connect（host，端口3306，用户root，密码，数据库
>>> cur=conn.cursor()#想要操作数据库需要游标，此处创建一个游标
>>> cur.execute('select*from common_hdwlog')#获得表中有多少条数据
317L
>>> cur.fetchone()
(1L, '0010338524', datetime.datetime(2017, 9, 20, 20, 41, 6), '1', None, None, '1', None, None, None)
>>> cur.fetchone()
(2L, '0018961305', datetime.datetime(2017, 9, 20, 20, 44, 37), '1', None, None, '1', None, '201510733028', None)
#fetchone()方法可以帮助我们获得表中的数据，
#可是每次执行cur.fetchone() 获得的数据都不一样
#换句话说每执行一次，游标会从表中的第一条数据移动到下一条数据的位置
#所以，我再次执行的时候得到的是第二条数据。
>>>info=cur.fetchmany(10)#fetchmany()方法可以获得多条数据，但需要指定数据的条数，这里指定获取10条
>>> print info
((3L, '0018961305', datetime.datetime(2017, 9, 20, 20, 45, 58), '1', None, None, '1', None, '201510733028', None), (4L, '0010338524', datetime.datetime(2017, 9, 20, 20, 46, 7), '1', None, None, '1', None, None, None), (5L, '0020813974', datetime.datetime(2017, 9, 20, 21, 18, 42), '1', None, None, '1', None, '201510733115', None), (6L, '0007254992', datetime.datetime(2017, 9, 20, 21, 18, 49), '1', None, None, '1', None, '201510733021', None), (7L, '0007254992', datetime.datetime(2017, 9, 20, 21, 18, 57), '1', None, None, '1', None, '201510733021', None), (8L, '0007254992', datetime.datetime(2017, 9, 20, 21, 19, 3), '1', None, None, '1', None, '201510733021', None), (9L, '0004450128', datetime.datetime(2017, 9, 20, 21, 19, 10), '1', None, None, '1', None, '201510733046', None), (10L, '0004450128', datetime.datetime(2017, 9, 20, 21, 19, 14), '1', None, None, '1', None, '201510733046', None), (11L, '0007254992', datetime.datetime(2017, 9, 20, 21, 18, 34), '1', None, None, '1', None, '201510733021', None), (12L, '0024511926', datetime.datetime(2017, 9, 20, 21, 18, 33), '1', None, None, '1', None, '201510733006', None))
>>> 