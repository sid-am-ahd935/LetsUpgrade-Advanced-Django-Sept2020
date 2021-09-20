from collections import Counter

data = '''
Class methods are for when you need to have methods that aren't specific to any particular instance, but still involve the class in some way. The most interesting thing about them is that they can be overridden by subclasses, something that's simply not possible in Java's static methods or Python's module-level functions.

If you have a class MyClass, and a module-level function that operates on MyClass (factory, dependency injection stub, etc), make it a classmethod. Then it'll be available to subclasses.

Factory methods (alternative constructors) are indeed a classic example of class methods.

Basically, class methods are suitable anytime you would like to have a method which naturally fits into the namespace of the class, but is not associated with a particular instance of the class.

As an example, in the excellent unipath module:
'''

class MyCounter(Counter):
	def __call__(self,data):
		self.update(Counter(data))
		#self = Counter(data) 
		#Creates New Value & Points self To It
		#But That Value Is Never Directly Sent
		#To The Creator Object
		#Hence By Updating self, Changes Are
		#Done In The Memory Address  Of Self 
		#Itself Which Is The Same Memory As 
		#New co1 Being Created
	
#Original Counter Object
a = Counter(data)
print(a)
print("\n\n")

#Custom Counter Object
co1 = MyCounter()
#As MyCounter() Is A Child Class Of Counter,
#co1 Is An Object Of Counter

#Passing Value/Data Into Object Using call()
co1(data)

#This Object Prints Exactly As Counter Object
print((co1))