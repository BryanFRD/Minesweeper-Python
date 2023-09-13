class Case:
  
  hasBomb: bool
  bombsAround: int
  isRevealed: bool
  isFlagged: bool
  
  def __init__(self, hasBomb: bool = False, bombsAround: int = 0, isRevealed: bool = False, isFlagged: bool = False) -> None:
    self.hasBomb = hasBomb
    self.bombsAround = bombsAround
    self.isRevealed = isRevealed
    self.isFlagged = isFlagged
    pass
  
  def __str__(self) -> str:
    if(self.isRevealed):
      if(self.hasBomb):
        return " B"
      else:
        return "  " if self.bombsAround == 0 else f" {self.bombsAround}"
    elif self.isFlagged:
      return " F"
    else:
      return "██"