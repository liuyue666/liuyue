Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> dict1 = { 'abc': 456 }
>>> dict1
{'abc': 456}
>>> dict1['abc']
456
>>> dict1['abc']=678
>>> dict1['abc']
678
>>> del dict1['abc']
>>> dict1
{}
>>> users = {
	'A':{
	'first':'liu',
	'last':'yue',
	'location':'hs'
	},
	'B':{
	'first':'lu',
	'last':'lei',
	'location':'hs',
	},
}
>>> for username, userinfo in users.items():
	print("userid£º" + username)
	print("userinfo:" + str(userinfo))

	
userid£ºA
userinfo:{'last': 'yue', 'location': 'hs', 'first': 'liu'}
userid£ºB
userinfo:{'last': 'lei', 'location': 'hs', 'first': 'lu'}
>>> dict = {'Name': 'Zara', 'Age': 7}
>>> print "Value : %s" % dict.keys()
Value : ['Age', 'Name']
>>> print "Key : %s" % dict.keys()
Key : ['Age', 'Name']
>>> for key in dict.keys():
	print key

	
Age
Name
>>> for key in dict.keys():
	print dict[key]

	
7
Zara
>>> 
