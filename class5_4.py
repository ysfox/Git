#sorted

#排序算法
#============================================================================
#排序也是在程序中经常用到的算法。无论使用冒泡排序还是快速排序，排序的核心是比较两个元素的大小
#对于两个元素x和y，如果认为x < y，则返回-1，如果认为x == y，则返回0，如果认为x > y，
#则返回1，这样，排序算法就不用关心具体的比较过程，而是根据比较结果直接排序

#Python内置的sorted()函数就可以对list进行排序
print(sorted([36,5,-12,9,-21]));

#此外，sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序：
#然后sorted()函数按照keys进行排序，并按照对应关系返回list相应的元素：
print(sorted([36,5,-12,9,-21],key=abs));

#我们再看一个字符串排序的例子：
#默认情况下，对字符串排序，是按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面。
print(sorted(['bob','about','Zoo','Credit']));

#现在，我们提出排序应该忽略大小写，按照字母序排序。要实现这个算法，不必对现有代码大加改动，只要我们能用一个key函数把字符串映射为忽略大小写排序即可
#忽略大小写来比较两个字符串，实际上就是先把字符串都变成大写（或者都变成小写），再比较。
print(sorted(['bob','about','Zoo','Credit'],key=str.lower));

#进行反向排序，不必改动key函数，可以传入第三个参数reverse=True：
print(sorted(['bob','about','Zoo','Credit'],key=str.lower,reverse=True));

#从上述例子可以看出，高阶函数的抽象能力是非常强大的，而且，核心代码可以保持得非常简洁。
#============================================================================

#小结
#============================================================================
#sorted()也是一个高阶函数。用sorted()排序的关键在于实现一个映射函数
#============================================================================