
'''
message = "Hello python would!"
print(message)
'''

'''
name = "ada lovelace"
print(name.title())
'''

'''
first = "jinze"
last = "chen"
full = first + last
print(full)
'''

'''
print("\nhello")
#转行 可以连续转行

print("\thello")
#空格 可以连续空格
'''
'''

a = "jaSon"
print(a.title())
print(a.upper())
print(a.lower())
'''

'''
age = 15
print("happy " + str(age) + "th birthday")
#str:15转成“15”
'''

'''
print(5 + 3)
print(10 - 2)
'''























#第二章
'''
bicycle = ['Daniel','Leo','Bobo','Max']
print("Hello " + bicycle[0])
print("Fuck you " + bicycle[1])
print("I am you father " + bicycle[2])
print("..." + bicycle[3])
'''

'''
#制表用单引号
a = ['a','b','c','d']
print(a)
a[0] = 'e'   #[]中更改也用单引号
print(a)
'''

'''
a = ['a','b','c','d']
a.append('e')
print(a)
#.append在后面添加
'''

'''
a = []
a.append('a')
a.append('b')
a.append('c')
a.append('d')
a.append('e')
print(a)
'''

'''
a = ['a','b','c','d']
a.insert(0,'r')
print(a)
#.insert添加成为（序号，添加内容）
'''

'''
a = ['a','b','c','d']
print(a)
del a[0]
print(a)
#del (列表名）删除元素
'''


'''
a = ['a','b','c','d','e']
print(a)
popped_a = a.pop()
print(a)
print(popped_a)
#删除末尾元素
'''

'''
a = ['a','b','c','d']
print(a)
a.remove('b')
print(a)
#remove删除列表中的语句remove（‘要移除的元素’）
'''

'''
list = ['Max','Leo','Peter']
print(list)
print("Hello " + list[0] + "!")
print(list[1] + ", Would you like to come to my dinner party?")
print(list[2] +  ", Welcome to my dinner party!")

print("\nEnter to continue")
input("\n")

print("Peter can not come so I will invite Alex to come")
print("the new list:")

list.append('Alex')
del list[2]
print(list)

print("\nEnter to continue")
input("\n")

print("Hello " + list[0] + "!")
print(list[1] + ", Would you like to come to my dinner party?")
print(list[2] +  ", Welcome to my dinner party!")

input()
'''

'''
a = ['d','b','a','c']
a.sort()#.sort进行按字母顺序排列
print(a)
'''

'''
a = ['d','b','a','c']
a.sort(reverse=False)#reverse=true颠倒  reverse=true颠倒后再次颠倒
print(a)
'''

'''
a = ['d','b','a','c']
a.reverse()#倒着打印列表
print(a)
'''

'''
a = ['d','b','a','c']
len(a)#len()获取列表的长度
print(a)
'''

'''
a = ['d','b','a','c']
print(sorted(a))#语句内用sorted()排序
'''

'''
place = ['China','USA','UK','Australia','Japan']
print("我想去的五个地方：")
print(place)

print(sorted(place))
print(place)

place.reverse()
print(place)

place.reverse()
print(place)

place.sort()
print(place)

a = len(place)

print(a)

input()
'''

'''
singers = ['bobo','Max','Jack']
for singer in singers:
	print(singer)#python一遍一遍的读取循环列表，直到列表结束
'''

'''
aas = ['s','d','f','g']
for aa in aas:
	print(aa)
'''

'''
aas = ['bobo','Max','Daniel',]
for aa in aas:
	print(aa.title() + " fuck you")
	print("You son of a bitch!\n")#如果在循环中加入input，则回车以继续
	input()
print("你们一群沙雕")
input()
'''

'''
for a in range(1,6):#range()创建数字列表 括号中（ ，）数字范围 最后一位不计
	print(a)#从1开始到5结束
'''

'''
n = list(range(1,6))#list():转化成列表格式
print(n)
'''

'''
even_numbers = list(range(2,11,2))#括号中的第三位是一次不断相加的数
print(even_numbers)
'''

'''
squares = []
for value in range(1,21):#设定范围并且进行循环
	square = value**2#循环计算
	squares.append (square)循环添加
print(squares)#输出列表
'''

'''
b = []
for a in range(1,11):#设定范围并且进行循环
	b.append(a**2)#一次添加
print(b)
'''

'''
numbers = [1,2,3,4,5,6,7,8,9,0]#对数字列表进行统计计算，赋值并打印

a = min(numbers)#最小数
print(a)

b = max(numbers)#最大数
print(b)

c = sum(numbers)#和
print(c)
'''

'''
a = []
for v in range(1,11):
	a.append(v*2)
print(a)
'''

'''
a = ['1','2','3','4','5','6']
print(a[0:3])#输出列表中用[ : ]，中间用：分隔，分割开的范围也是最后一位不计
'''

'''
a = ['1','2','3','4','5','6']
print(a[:3])#:号左边如果不填的话代表从头开始
'''

'''
a = ['1','2','3','4','5','6']
print(a[0:])#如果：号后面不填的话代表到头结束
'''

'''
a = ['1','2','3','4','5','6']
print(a[-4:3])#一律是从左往右
'''

'''
dimension = (2,3)#定义元组
print(dimension[0])#调用元组，使用[]中加序号
print(dimension[1])
'''


'''
dimensions = (1,2,3,4,5)
for a in dimensions:
	print(a)#
'''

'''
a = ['bmw','toyota','subaru','audi']#创建列表
for b in a:#循环列表
	if b == 'toyota':#创立条件
		print(b.title())#结果
	else:#其余
		print(b)#结果
'''

'''
a = 'Audi'
a.lower() == 'audi'
print(a)
'''

'''
requested_topping = 'mushroom'
if requested_topping != 'anchovies':#!:表示不等于
	print("Hold the anchovies!")
'''

'''
a = 9

a = 20
f
a > 20
f
a < 20
t
a <= 20
t
a >= 20
f
'''

'''
a = ['1','2','3','4']
'1' in a
t
'5' in a
f
'''

'''
banned_user = ['Max','Jack','Bobo']
user = 'Jason'
if user not in banned_user:#not in :不在  和！=的用法一样，意思也一样
	print(user + ", you can post a response is you wish.")
'''

'''
#布尔表达式
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car =='audi'? I predict False")
print(car == 'audi')
'''

#简单if语句
'''
if conditional_test:
	do something
'''

'''
a = input("age:")
if a >= '18':
	print("You are old enough.")
	print("Have you registered yet?")
	input()
else:
	print("Sorry, you are not old enough.")
	print("You can register after you turn 18.")
	input()
'''


'''
age = input("age:")

if age < '4':
	print("Your age is less than 4.")
elif age < '18':#如果第一个测试据不通过，则直接测试elif语句
	print("You are not old enough.")
else:
	print("You are old enough.")
input()
'''

'''
age = 20

if age < 4:
	p = 0
elif age < 18:
	p = 5
elif age < 30:#if else语句中可以添加多个elif
	p = 7
else:#if elif语句中可以省略else
	p = 10

print("Your admision cost is $" + str(p))#str：1转‘1’
'''

'''
rts = ['mushroom','green peppers','extra cheese']

for rt in rts:
	if rt == 'mushroom':
		print("sorry we do not have any " + rt + ".")
	else:
		print("adding " + rt + ".")
'''

'''
rts = ['']

if rts:
	for rt in rts:
		print("Adding " + rt + ".")
	print("Finish making pizza.")
else:
	print("Are you sure you will have a plain pizza?")
'''


'''
available = ['a','b','c','d','e','f','g']

requesting = ['a','b','h']

for r in requesting:
	if r in available:
		print("Adding " + r + ".")
	else:
		print("Sorry we do not have " + r + ".")
print("Finish making pizza.")
'''








'''
alien = {'color':'green','points':'5'}#列出字典，一项和一项中间用逗号连接，项目和类别用冒号连接

print(alien['color'])#打印字典内容
print(alien['points'])#只打印所调用的值
'''


'''
alien = {'color':'green','points':'5'}
print(alien)

alien['x_position'] = 0#字典中添加成分用中括号，并且中间用单引号添加成分
alien['y_position'] = 25
print(alien)
'''



'''
alien = {}#空字典
alien['color'] = 'green'#在字典中添加成分
alien['point'] = 5
print(alien)
'''

'''
alien = {'color':'green','points':'5'}
print(alien)
alien['color'] ='red'#对字典进行直接修改
print(alien)
'''

'''
alien = {'x_position':0,'y_position':25,'speed':'medium'}

print("Original x_position:" + str(alien['x_position']))

if alien['speed'] == 'slow':
	x_increment = 1
elif alien['speed'] == 'medium':
	x_increment = 2
else:
	x_increment = 3

alien['x_position'] = alien['x_position'] + x_increment
print("The new x_position:" + str(alien['x_position']))\
'''

'''
alien = {'x_position':0,'y_position':25,'speed':'medium'}
print(alien)
del alien['speed']#直接删除字典中的某一项，注意是永久性删除
print(alien)
'''

'''
alien = {
	'x_position':0,
	'y_position':25,
	'speed':'medium'}
print(alien)
'''

'''
user = {
	'username': 'Jason',
	'first': 'Jason',
	'last': 'chen'
}
for a,b in user.items():#.items()对字典中的每一条进行调用，a，b是给字典中的每一条进行定义
	print("\nKey: " + a)
	print("Value: " + b)#循环输出每一条
'''

'''
user = {
	'username': 'Jason',
	'first': 'Jason',
	'last': 'chen'
}
for a,b in user.items():
	print(a.title() + ": " + b.title())
'''

'''
user = {
	'username': 'Jason',
	'first': 'Jason',
	'last': 'chen'
}
for a in user.keys():#.keys()不需要字典中的值用.keys()来遍历字典，冒号前面的值
	print(a.title())
'''

'''
user = {
	'username': 'Jason',
	'first': 'Jason',
	'last': 'chen'
}
for name in sorted(user.keys()):
	print(name.title() + ", thank you for taking the poll.")
'''

'''
user = {
	'username': 'Jason',
	'first': 'Jason',
	'last': 'chen'
}
for name in user.values():#.values()遍历字典中冒号后面的值
	print(name.title())
'''

'''
alien_0 = {'color':'green','points':'5'}
alien_1 = {'color':'red','points':'10'}
alien_2 = {'color':'yellow','points':'15'}

aliens = [alien_0,alien_1,alien_2]#字典嵌套在列表中，意思就是挨个分支
for alien in aliens:
	print(alien)
'''


'''
aliens = []

for alien_number in range(30):
	new_alien = {'color':'green','points':'5'}
	aliens.append(new_alien)

for alien in aliens[:5]:
	print(alien)
print("...")

print("Total number of aliens:" + str(len(aliens)))
'''

'''
a = "Tell me your name"
a += "\nwhat is your first name?"#+=接着，建议用\n转行
name = input(a)
print("Hello " + name)
input()
'''

'''
a = input("How tall are you, in inches?")
a = int(a)#int语句转化成量
if a >= 36:
	print("\nYou are tall enough to ride.")
else:
	print("\nYou will be able to ride when you are a littlw older.")
input()
'''

'''
number = input("Tell me a number and I can tell you if it is an even or odd.")
number = int(number)
if number % 2 == 0:#%取模运算，求余数
	print("\nit is an even.")
else:
	print("\nIt is an odd.")
input()
'''

'''
a = 1
while a <= 5:#循环a，直到5
	print(a)#循环输出
	a += 1##每次输出a的值1
'''

'''
a = "\nTell me something I will repeat."
a += "\nEnter 'quit' to end this program."
message = ""
while message != 'quit':
	message = input(a)
	print(message)
'''

'''
a = "\nTell me something I will repeat."
a += "\nEnter 'quit' to end this program."
message = ""
while message != 'quit':#!=意思是输入后面的值时推出循环
	message = input(a)
	if message != quit:
		print(message)
'''

'''
a = "\nTell me something I will repeat."
a += "\nEnter 'quit' to end this program."
active = True
while active:
	message = input(a)

	if message == 'quit':
		active = False
	else:
		print(message)
'''

'''
a = "\nTell me something I will repeat."
a += "\nEnter 'quit' to end this program."

while True:#以while True 开头的循环将会不断的运行，直到看到break才结束
	message = input(a)

	if message == 'quit':
		break#退出，停止循环
	else:
		print(message)
'''

'''
a = 0
while a < 10:#直到10
	a += 1
	if a % 2 == 0:
		continue#继续循环
	print(a)
'''

'''
ucu = ['Max','Jason','Leo']
cu = []

while ucu:
	current_user = ucu.pop()

	print("Verifying user: " + current_user.title())
	cu.append(current_user)

print("People who has been confirmed:")

for b in cu:
	print(b.title())
'''

'''
pets = ['a','b','a','c','d','a']
print(pets)
while 'a' in pets:#把列表中的a全部删去
	pets.remove('a')
print(pets)
'''









'''
def greet_user():#def：定义函数，后期调用
	print("hello")

greet_user()#已定义的函数直接加()可直接进行调用
'''

'''
def greet_user(username):#函数后的括号中的变量和后面所输入的值相符
	print("Hello " + username.title())

greet_user('Jason')#定义username并执行函数
'''

'''
def selfname(f,l):
	print("My first name is " + f)
	print("My last name is " + l)

selfname(f = 'Jason',l = 'Chen')#这里可以不加‘f = 和l =’
'''

'''
def selfname(f,l = 'Chen'):#可固定第二个值
	print("My first name is " + f)
	print("My last name is " + l)
selfname('Jason')#如果第二个值被固定，可只填第一个变量的值
'''

'''
def gfn(fn,ln):
	full = fn + ln
	return full
musician = gfn('Jason','Chen')
print(musician)
'''

'''
def gfn(fn,ln,mn = ''):
	if mn:
		f = fn + ' ' + mn + ' ' + ln
	else:
		f = fn + ' ' + ln
	return f

musician = gfn('Jason','chen')
print(musician)

musician = gfn('Jason','Chen','C')
print(musician)
'''

'''
def bp(fn,ln):
	person = {'first name':fn,'last name':ln}
	return person
musician = bp('Jason','Chen')
print(musician)
'''

'''
def greet_users(names):
	for name in names:
		message = "Hello, " + name.title() + '!'
		print(message)

usernames = ['jason','jack','jim']
greet_users(usernames)

'''


import pizza
pizza.making_pizza(16,'pepperoni')
pizza.making_pizza(12,'mushrooms','green peppers','extra cheese')