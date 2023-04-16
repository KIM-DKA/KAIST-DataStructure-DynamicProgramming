
class Father: 

    def __init__(self,strHometown):
        self.strHometown = strHometown
        print('Father class')

    def doFatherthing(self):
        print('Father do')

    def doRunning(self): 
        print('slow')
        

class Mother: 

    def __init__(self,strHometown): 
        self.strHometown = strHometown
        print('Mother class')

    def doMotherthind(self):
        print('Mother do')

class Child(Father, Mother):
    
    def __init__(self, strHometown):
        super(Child,self).__init__(strHometown)
        print('Child class')
    
    def doRunning(self):
        print('fast')


me = Child('seoul') 




