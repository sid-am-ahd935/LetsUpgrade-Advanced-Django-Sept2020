#Shallow Copy vs Deep Copy

dict1 = {'A':"Apple",'B':"Ball",'C':["Cat"]}
list1 = [1,2,[3],{4:'Four'}]

l = list1
d = dict1
#Creates An Exact Duplicate Of The Object Itself

print("Copy Using 'ob = Object':")
print("l is list1 ?:->", id(l) == id(list1))
print("d is dict1 ?:->", id(d) == id(dict1))
print('\n'*3)

dict2 = dict1.copy()
dict3 = dict(dict1)
#dict4= dict[:] Not Possible
list2 = list1.copy()
list3 = list(list1)
list4 = list1[:]
'''
Copies All The Addresses Of Values Into The The New One. 
As The Addresses Of The Value Are Same For Both Objects, 
Any Changes Done To The Value Without Changing The Addresses,
Will Reflect On Both The Objects
'''

print("\nInitially All Dicts:")
print("Dict1: ", dict1)
print("Dict2: ", dict2)
print("Dict3: ", dict3)

print("\nInitially All Lists:")
print("List1: ", list1)
print("List2: ", list2)
print("List3: ", list3)
print("List4: ", list4)
print('\n')


dict1['D'] = "Dog" #No Change In Copied Dicts For Adding New Values
dict2['B'] = "Banana" #No Change In Value In Copied As Value Address Changes
dict3['C'].append("Cake") #Change In Mutables At Index Keeps Same Address
#As Value Address Was Same But The Value Was Changed (Appended), Changes All

print("\nChanging All Dicts:")
print("Dict1: ", dict1)
print("Dict2: ", dict2)
print("Dict3: ", dict3)


list1.append(7) #No Change In Copied Lists For Adding New Values
list2[1] = "Two" #No Change In Value In Copied As Value Address Changes
list3[2].append(6) #Change In Mutables At Index Keeps Same Address
#As Value Address Was Same But The Value Was Changed (Appended), Changes All

list4[3][5] = "Five" #Change In Mutables At Index Keeps Same Address
#As Value Address Was Same But The Value Was Changed (Indexed), Changes All

print("\nChanging All Lists:")
print("List1: ", list1)
print("List2: ", list2)
print("List3: ", list3)
print("List4: ", list4)
print('\n'*3)

'''
These Were Examples Of Shallow Copy.

Adding New Values Did Not Affect All The Copies,
As It Was Added To A New Address Unaware To The Copies.

Changes In Values But Keeping The Same Address Changed All
As The Addresses Of Values Were Same,
And All The Indexes, Pointing To The Values Remained Same
The Mutables Changed In Every Copied Object

The Fact That These Copies Could Still Keep The
Vulnerability To Change According To It's Originals,
These Copies Are Known As Shallow Copies
'''

from copy import deepcopy

print('\nOriginal Dict:\n', d) #d Completely Changed Along With The Original
print('\nOriginal List:\n', l) #l Completely Changed Along With The Original
print()
dict5 = deepcopy(d) #Creating A Deep Copy Of Dict d
list5 = deepcopy(l) #Creating A Deep Copy Of List l
print()
print('\nCopied Dict:\n', dict5)
print('\nCopied List:\n', list5)
print('\n'*3)


d['C'][0] = 'Cup'
d['C'][0] += 'Cake'
d['C'][1] = 'Coffee Table'
del d['D']

l[2].append(9)
del l[-1]
l[3][6] = 'Six'

print('\nChanging Original Dict:\n', d)
print('\nChanging Original List:\n', l)
print()
print()
print('\nUnchanged DeepCopied Dict:\n', dict5)
print('\nUnchanged DeepCopied List:\n', list5)
