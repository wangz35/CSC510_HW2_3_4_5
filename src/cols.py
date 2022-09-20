import re
from src.num import Num
from src.sym import Sym

class Cols:
    def __init__(self, names):
        self.names = names
        self.all = []
        self.x =[]
        self.y = []
        self.klass = None
    
        for idx, name in enumerate(names): 
                    col = name[0].isupper() and Num(idx, name) or Sym(idx, name)  
                    self.all.append(col)
                    if name[-1] != ':':
                        self.y.append(col) if name[-1] == '-' or name[-1] == '+' else self.x.append(col)
                        if name[-1] == '!':
                            self.klass = col


