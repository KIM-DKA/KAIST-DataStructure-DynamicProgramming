
from time import ctime 

class MyHome: 
    def __init__(self,roof_color): 
        self.roof_color = roof_color 
    
    def print_home_color(self): 
        print(f'my home color is {self.roof_color}')

    def __del__(self): 
        print('delete pacakges')