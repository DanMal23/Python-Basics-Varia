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
    print ('My favourate : ', ', '.join(arr))
            
distro('ArcoLinux', 'Fedora29', 'SilverBlue', 'Ubuntu')

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
