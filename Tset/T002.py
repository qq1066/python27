#_*_ coding: UTF-8 _*_

"""时间：2017-06-07; 使用while循环完成
"""
# 练习1：逐一显示指定列表中的所有元素；
l1 = ['centos', 'redhat', 'ubuntu', 'linux mint']
count1 = 0
while count1 < len(l1):
    print l1[count1]
    count1 += 1
count1 = 0
while l1:
    if count1 < len(l1):
        print l1[count1]
    else:
        break
    count1 += 1

l1 = ['centos', 'redhat', 'ubuntu', 'linux mint']
count1 = 0
while l1:
    if count1 < len(l1):
        l1.pop(count1)
    else:
        break
    count1 += 1

# 练习2：求100以内所有偶数之和；
# i = 2
# sum1 = 0
# while i <= 100:
#     if (i % 2) == 0:
#         sum1 = sum1 + i
#     i += 1
# else:
#     print sum1
# 练习3：逐一显示指定字典的所有键；并于显示结束或说明中键数
d1 = {'x': 1, 'y': 2, 'z': 3}
print d1
DictKey = d1.keys()
print DictKey
for i in DictKey:
    print 'Dict Key %s Value' % i, d1[i]
# 练习4，创建一个包含了100以内所有奇数的列表；
l1 = []
i = 0
while i < 100:
    i += 1
    if (i % 2) != 0:
        l1.append(i)
else:
    print l1
# 练习5，逆序逐一显示一个列表的所有元素；
l5 = [1, 2, 3, 4, 5, 6]
i = -1
j = i - 1
le = -len(l5)
while i > le:
    print l5[j:i]
    i = i - 1
    j = i - 1
# 练习6。列表l1 = [0,1,2,3,4,5,6] 列表l2 = ["Sun","Mon","Tue","wed","Thu","Fri","sat"],以第一个列表中的元素为键，以第二个列表中的元素为值生成字典d1
l1 = [0, 1, 2, 3, 4, 5, 6]
l2 = ["Sun", "Mon", "Tue", "wed", "Thu", "Fri", "sat"]
i = 0
d1 = {}
while i < len(l1):
    d = {l1[i]: l2[i]}
    d1.update(d)
    i += 1
else:
    print d1
# 方法2
l1 = [0, 1, 2, 3, 4, 5, 6]
l2 = ["Sun", "Mon", "Tue", "wed", "Thu", "Fri", "sat"]
d1 = {}
count = 0
while count < len(l1):
    d1[l1[count]] = l2[count]
    count += 1
else:
    print d1



"""时间：2017-06-07; 使用for循环完成
"""
#练习1：逐一显示指定列表中的所有元素；
#示例1

l1 = ['centos','redhat','ubuntu','linux mint']
for i in l1:
    print i

#补充：练习1：逆序显示指定列表中的所有元素；

l1 = ['centos','redhat','ubuntu','linux mint']
for i in l1:
    print i
#练习2：求100以内所有偶数之和；
int100 = range(100)
sum100 = 0
for i in int100:
    if (i % 2) == 0:
        sum100 = sum100 + i
print sum100
#练习3：逐一显示指定字典的所有键；并于显示结束或说明中键数
d1 = {'x':1, 'y':2, 'z':3}
for i in d1.keys():
    print i
    len(d1)
else:
    print len(d1)
#练习4，创建一个包含了100以内所有奇数的列表；
list1 = range(100)
l1 = []
for i in list1:
    if (i % 2) != 0:
        l1.append(i)
else:
    print l1
#练习5，逆序逐一显示一个列表的所有元素；
l1 = ['centos','redhat','ubuntu','linux mint']
l1.reverse()
for i in l1:
    print i

#练习6.列表l1 = [0,1,2,3,4,5,6] 列表l2 = ["Sun","Mon","Tue","wed","Thu","Fri","sat"],以第一个列表中的元素为键，以第二个列表中的元素为值生成字典d1
l1 = [0,1,2,3,4,5,6]
l2 = ["Sun","Mon","Tue","wed","Thu","Fri","sat"]
d1 = {}
for i in range(len(l1)):
    d1[l1[i]] = l2[i]
else:
    print d1



