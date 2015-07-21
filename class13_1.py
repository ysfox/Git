#datetime
#============================================================================
#datetime是Python处理日期和时间的标准库
#获取当前日期和时间
#我们先看如何获取当前日期和时间
from datetime import datetime
now = datetime.now() # 获取当前datetime
print(now)
#2015-05-18 16:28:07.198690
print(type(now))
#<class 'datetime.datetime'>

#注意到datetime是模块，datetime模块还包含一个datetime类，通过from datetime import datetime导入的才是datetime这个类
#如果仅导入import datetime，则必须引用全名datetime.datetime。
#datetime.now()返回当前日期和时间，其类型是datetime
#============================================================================

#获取指定日期和时间
#============================================================================
#要指定某个日期和时间，我们直接用参数构造一个datetime：
from datetime import datetime
dt = datetime(2015, 4, 19, 12, 20) # 用指定日期时间创建datetime
print(dt)
#2015-04-19 12:20:00
#============================================================================

#datetime转换为timestamp
#============================================================================
#在计算机中，时间实际上是用数字表示的。
#我们把1970年1月1日 00:00:00 UTC+00:00时区的时刻称为epoch time，记为0（1970年以前的时间timestamp为负数）
#当前时间就是相对于epoch time的秒数，称为timestamp。

#你可以认为：
#timestamp = 0 = 1970-1-1 00:00:00 UTC+0:00

#对应的北京时间是：
#timestamp = 0 = 1970-1-1 08:00:00 UTC+8:00

#可见timestamp的值与时区毫无关系，因为timestamp一旦确定，
#其UTC时间就确定了，转换到任意时区的时间也是完全确定的，这就是为什么计算机存储的当前时间是以timestamp表示的，
#因为全球各地的计算机在任意时刻的timestamp都是完全相同的（假定时间已校准）。

#把一个datetime类型转换为timestamp只需要简单调用timestamp()方法：
from datetime import datetime
dt = datetime(2015, 4, 19, 12, 20) # 用指定日期时间创建datetime
dt.timestamp() # 把timestamp转换为datetime
#1429417200.0

#注意Python的timestamp是一个浮点数。如果有小数位，小数位表示毫秒数。
#某些编程语言（如Java和JavaScript）的timestamp使用整数表示毫秒数，这种情况下只需要把timestamp除以1000就得到Python的浮点表示方法。
#============================================================================

#timestamp转换为datetime
#============================================================================
#要把timestamp转换为datetime，使用datetime提供的fromtimestamp()方法：
from datetime import datetime
t = 1429417200.0
print(datetime.fromtimestamp(t))
#2015-04-19 12:20:00

#注意到timestamp是一个浮点数，它没有时区的概念，而datetime是有时区的。上述转换是在timestamp和本地时间做转换。

#本地时间是指当前操作系统设定的时区。例如北京时区是东8区，则本地时间：2015-04-19 12:20:00
#实际上就是UTC+8:00时区的时间：2015-04-19 12:20:00 UTC+8:00
#而此刻的格林威治标准时间与北京时间差了8小时，也就是UTC+0:00时区的时间应该是:2015-04-19 04:20:00 UTC+0:00

#timestamp也可以直接被转换到UTC标准时区的时间：
from datetime import datetime
t = 1429417200.0
print(datetime.fromtimestamp(t)) # 本地时间
#2015-04-19 12:20:00
print(datetime.utcfromtimestamp(t)) # UTC时间
#2015-04-19 04:20:00
#============================================================================

#str转换为datetime
#============================================================================
#很多时候，用户输入的日期和时间是字符串，要处理日期和时间，首先必须把str转换为datetime。
#转换方法是通过datetime.strptime()实现，需要一个日期和时间的格式化字符串：
from datetime import datetime
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)
#2015-06-01 18:19:59
#字符串'%Y-%m-%d %H:%M:%S'规定了日期和时间部分的格式。详细的说明请参考Python文档。
#注意转换后的datetime是没有时区信息的。
#============================================================================

#datetime转换为str
#============================================================================


















