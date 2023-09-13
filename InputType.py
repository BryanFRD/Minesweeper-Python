from enum import Enum
import re

class InputTypeCondition(Enum):
  PLAY_CONDITION = lambda value: re.fullmatch("(y|n)", value)
  GRID_CONDITION = lambda value: re.fullmatch("([a-zA-Z])(\d{1,})\s(r|f)", value)

class InputTypeFormat(Enum):
  PLAY_FORMAT = lambda value: value[0] == "y"
  GRID_FORMAT = lambda value: [ord(value[0].lower()) - ord('a'), int(value[1]), value[3] == "f"]

class InputType(Enum):
  PLAY = lambda: [InputTypeCondition.PLAY_CONDITION, InputTypeFormat.PLAY_FORMAT]
  GRID = lambda: [InputTypeCondition.GRID_CONDITION, InputTypeFormat.GRID_FORMAT]
 
