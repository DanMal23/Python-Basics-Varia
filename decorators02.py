#function decorators

def decor1(func):
    def wrapper():
        print("**************************")
        func()
        print("**************************")
    return wrapper

def decor2(func):
    def wrapper():
        print("*------------------------*")
        func()
        print("*------------------------*")
    return wrapper
   
@decor1
@decor2
def func_inside():
    print("* I'm a wrapped function *")

func_inside()

#---------------------------------------------

def decor(func):
    def wr(*args):
        setx=set()
        for x in args:
            setx.add(str(x))
        print('Some Linux distros: ', ', '.join(setx))
        func(*args)
    return wr
    
@decor
def distro(*distros):
    arr=[]
    for x in distros:
        arr.append(str(x))
    print ('My favourate: ', ', '.join(arr))
            
distro('ArcoLinux', 'Fedora', 'SilverBlue', 'Ubuntu')

#-------------------------------------------------------

# method decorators

def decor(meth):
    def wr (self, discount): #self as 1st arg in methods
        discount = discount /2
        return meth(self, discount)
    return wr
class Item(object):
    def __init__(self):
        self.price = 12
        self.pricex = 10
    
    @decor
    def getPrice(self, discount):
        print("The price for grapes: {0} zlotys per kg. It's half the regular price!"
              .format(round(self.price/2)))
        print("Another super offer: 1 pineapple: {0} zlotys. Only today!"
              .format(round(self.pricex/2)))
price = 12
pricex = 10
i = Item()
i.getPrice(price/2)

#------------------------------------------------------
# **kwargs, for loop: unpacking kwargs

def decor(func):
    def wr(*args, **kwargs):
        print("Wrapper's arguments:")
        if args:
            print("args->",args)
        elif kwargs:
            print("kwargs->",kwargs)
        func(*args, **kwargs)
    return wr

@decor 
def funcK(**kwargs):
	for k,v in kwargs.items():
		print(k,v)
funcK(a=97, b=98, c=99)

#-----------------------------------------------------
def decor(func):
    def wr(*args):
        print("About document-oriented databases:")      
        func(*args)
    return wr

class NoSQL(object):
    def __init__ (self):
        self.n = 'NoSQL databases'
        self.doc = 'document-oriented db'
        self.s = 'subclass'
        self.xml = 'xml databases'
        self.r = 'relational databases'
        self.t = 'tables'
        
    @decor
    def description(self, n='',doc='',s='',xml=''):
        print("One of the main categories of {0} is {1}.\nIts {2} is {3}."
              .format(self.n, self.doc, self.s, self.xml))
    @decor
    def description2(self, doc='', r='', t=''):
        print("The {0} are juxtopposed to {1} which store data in {2}."
             .format(self.doc, self.r, self.t))
        
no = NoSQL()
no.description()
no.description2()

#based on very helpful tutorial:
#https://gist.github.com/Zearin/2f40b7b9cfc51132851a
