
# coding: utf-8

# In[ ]:


class Account:
    def __init__(self,name,bal):
        self.name = name
        self.bal = bal
    def deposit(self,amt):
        self.bal += amt
        self.displayBal()
    def withdraw(self,amt):
        if amt>self.bal:
            print("Balance Not Available")
            self.displayBal()
        else:
            self.bal -= amt
            self.displayBal()
    def displayBal(self):
        print("Available Balance is:",self.bal)
        
a = Account('Manash',1000)
a.displayBal()
a.deposit(50000)
a.withdraw(5000)


# In[7]:


from math import pi

class Cone:
    def __init__(self,height,radius):
        self.height = height
        self.radius = radius
        
    def volume(self):
        self.vol = (pi*(self.radius**2)*self.height)/3
        print("Volume is :",self.vol)
        
    def surface_area(self):
        self.sa = pi*self.radius*(self.radius+(self.height**2 + self.radius**2)**2)
        print('Surface Area is: ',self.sa)
        
c = Cone(3,5)
c.volume()
c.surface_area()

