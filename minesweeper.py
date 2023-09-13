from InputType import InputType
from Grid import Grid

grid: Grid

def ask_for_input(prompt: str, type: InputType, error: str = "Mauvaise entrée"):
  condition, format = type()
  ipt = input(prompt)
  
  if(condition(ipt) is None):
    print(error)
    return ask_for_input(prompt, type, error)
  
  return format(ipt)

while(True):
  if not ask_for_input("Do you wawnt to play ? (y/n): ", InputType.PLAY):
    break
  
  grid = Grid(20, 10, 5)
  
  while(True):
    grid.prompt()
    
    x, y, reveal = ask_for_input("Enter coordinates (ex: b7 r|f)", InputType.GRID)
    case = grid.get_case(x, y)
    
    if(case is None):
      print(f"Not within grid, grid size: {grid.width}x-{grid.height}y")
      continue
    
    grid.reveal(x, y, reveal)
    
    if(case.hasBomb):
      grid.prompt()
      print("You've found a bomb !")
      break