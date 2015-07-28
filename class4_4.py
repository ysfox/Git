#生成器
#=========================================================================
#在Python中，这种一边循环一边计算的机制，称为生成器：generator
#要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：
#创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator。
L = [x * x for x in range(10)];
print(L);
g = (x * x for x in range(10));
print(g);

#打印出generator的每一个元素
#我们讲过，generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素，
#没有更多的元素时，抛出StopIteration的错误
print(next(g));
print(next(g));
print(next(g));


#上面这种不断调用next(g)实在是太变态了，正确的方法是使用for循环，因为generator也是可迭代对象
#所以，我们创建了一个generator后，基本上永远不会调用next()，而是通过for循环来迭代它，并且不需要关心StopIteration的错误
g = (x * x for x in range(10));
for n in g:
	print(n);

	
#generator非常强大。如果推算的算法比较复杂，用类似列表生成式的for循环无法实现的时候，还可以用函数来实现
#比如，著名的斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到
def fib(max):
	n,a,b = 0,0,1;
	while n < max:
		print(b);
		a,b = b,a +b;
		n = n + 1;
	return 'done';
#上面的函数可以输出斐波那契数列的前N个数
print(fib(6));

#可以看出，fib函数实际上是定义了斐波拉契数列的推算规则，可以从第一个元素开始，推算出后续任意的元素，这种逻辑其实非常类似generator
#也就是说，上面的函数和generator仅一步之遥。要把fib函数变成generator，只需要把print(b)改为yield b就可以了
def fib(max):
	n,a,b = 0,0,1;
	while n < max:
		yield b;
		a,b=b,a+b;
		n = n+1;
	return 'done';
f = fib(6);
print(f);

#最难理解的就是generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
#而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行
#举个简单的例子，定义一个generator，依次返回数字1，3，5
def odd():
	print('step 1');
	yield(1);
	print('step 2');
	yield(3);
	print('step 3');
	yield(5);
	
#调用该generator时，首先要生成一个generator对象，然后用next()函数不断获得下一个返回值
#可以看到，odd不是普通函数，而是generator，在执行过程中，遇到yield就中断，下次又继续执行。
#执行3次yield后，已经没有yield可以执行了，所以，第4次调用next(o)就报错。
o = odd();
print(next(o));
print(next(o));
print(next(o));


#同样的，把函数改成generator后，我们基本上从来不会用next()来获取下一个返回值，而是直接使用for循环来迭代：
for n in fib(6):
	print(n);



#但是用for循环调用generator时，发现拿不到generator的return语句的返回值。
#如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中
#关于如何捕获错误，后面的错误处理还会详细讲解
g = fib(6);
while True:
	try:
		x = next(g);
		print('g:',x);
	except StopIteration as e:
		print('Generator return value:',e.value);
		break;




#请注意区分普通函数和generator函数，普通函数调用直接返回结果：
r = abs(6);
print(r);

#generator函数的“调用”实际返回一个generator对象：
g = fib(6);
print(g);

#=========================================================================








































