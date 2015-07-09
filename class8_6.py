#使用元类
#============================================================================
#动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的。
#比方说我们要定义一个Hello的class，就写一个hello.py模块
class Hello(object):
    def hello(self, name='world'):
		print('Hello, %s.' % name)
		
#当Python解释器载入hello模块时，就会依次执行该模块的所有语句，执行结果就是动态创建出一个Hello的class对象
#测试如下
from hello import Hello

h = Hello()
h.hello()				#Hello, world.
print(type(h))			#<class 'hello.Hello'>

#type()函数可以查看一个类型或变量的类型，Hello是一个class，它的类型就是type，而h是一个实例，它的类型就是class Hello。