# Keyboard mapping firmware

### Compatible with CircuitPython only
- It is required Adafruit's "adafruit_hid" library

# Installation
- simply copy the file and paste it into your device

# Usage
- "..." lets you write keyboard maps on microcontrollers (such as Rasppberry Pi Pico)
- open your code.py file
- when starting, import the firmware's file and "board" module
```
from firmware import Keyboard, Keycode
import board
```

- instantiate a Keyboard object
  - give True (o leave blank) as paramter if you have a direct connection to each button on you keyboard
  - if you use a matrix structure, using diodes, pass False
```keyboard = Keyboard()```

- if you use matrix, set the diodes direction:
```
keyboard.direction(keyboard.RC) # if you use Row -> Col

keyboard.direction(keyboard.CD) # if you use Col -> Row
```

- define the pins using the "pins()" methos
  - when using direct connection, pass a list containing all the pins you use
  - when using matrix, pass a matrix containing two tuples, the first containing the row pins, teh second containing the column pins

```
keyboard.pins([board.GP0, board.GP1, board.GP2, board.GP3]) # direction connection

keyboard.pins([(board.GP0, board.GP1), (board.GP2, board.GP3)]) # matrix connection
```

- define your map by creating a list of functions:
  - for direct connection, every function will be assigned to the GPIO on tha same index
  - for map connection, 
