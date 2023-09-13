from Case import Case
from random import random

class Grid:
  
  width: int
  height: int
  grid: list = list()
  
  def __init__(self, width: int, height: int, bombs: int) -> None:
    self.width = width
    self.height = height
    
    self.generate(bombs)
    
    pass
  
  def generate(self, bombs: int) -> None:
    self.grid = list()
    for x in range(0, self.width):
      self.grid.append(list())
      for y in range(0, self.height):
        self.grid[x].append(Case())
    
    for bomb in range(0, bombs):
      x = int(random() * self.width)
      y = int(random() * self.height)
      case = self.get_case(x, y)
      
      if(case.hasBomb):
        bomb -= 1
        continue
      
      case.hasBomb = True
      for xx in range(-1, 2):
        for yy in range(-1, 2):
          if(self.is_within(x+xx, x+yy)):
            self.get_case(x+xx, y+yy).bombsAround += 1
      
  def get_case(self, x: int, y: int) -> Case|None:
    if(self.is_within(x, y)):
      return self.grid[x][y]
    
    return None
  
  def is_within(self, x: int, y: int) -> bool:
    return self.width > x and x >= 0 and self.height > y and y >= 0
  
  def reveal(self, x: int, y: int, flag: bool = False):
    case = self.get_case(x, y)
    
    if(case is None or case.isRevealed):
      return
    
    if(flag):
      case.isFlagged = not case.isFlagged
    elif not case.isFlagged:
      case.isRevealed = True
    
    if(case.bombsAround > 0 or flag or case.isFlagged):
      return
    
    for i in range(-1, 2, 1):
      self.reveal(x+i, y)
      self.reveal(x, y+i)
    
  
  def prompt(self) -> None:
    prompt = ""
    for j in range(-1, self.height):
      for i in range(-1, self.width):
        if j == -1 and i > -1:
          prompt += f" {chr(ord('a') + i)}"
        elif i == -1 and j > -1:
          prompt += "{0:2}".format(j)
        elif i + j == -2:
          prompt += "  "
        else:
          prompt += str(self.get_case(i, j))
      prompt += "\n"
    prompt += "\n"
    print(prompt)