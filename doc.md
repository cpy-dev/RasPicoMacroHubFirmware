# Keyboard mapping firmware

### Compatible with CircuitPython only
- It is required Adafruit's "adafruit_hid" library

# Installation
- simply copy the file and paste it into your device, together with the adafruit_hid library

# Usage
- "..." lets you write keyboard maps on microcontrollers (such as Raspberry Pi Pico)
- open your code.py file
- when starting, import the firmware's file and "board" module
```
from firmware import Keyboard, Keycode, LayerSwitch
import board
```

- instantiate a Keyboard object
  - give True (o leave blank) as parameter if you have a direct connection to each button on you keyboard
  - if you use a matrix structure, using diodes, pass False
```keyboard = Keyboard()```

- if you use matrix, set the diodes direction:
```
keyboard.direction(keyboard.RC) # if you use Row -> Col

keyboard.direction(keyboard.CD) # if you use Col -> Row
```

- define the pins using the "pins()" method
  - when using direct connection, pass a list containing all the pins you use
  - when using matrix, pass a matrix containing two tuples, the first containing the row pins, teh second containing the column pins

```
keyboard.pins((board.GP0, board.GP1, board.GP2, board.GP3)) # direction connection

keyboard.pins(((board.GP0, board.GP1), (board.GP2, board.GP3))) # matrix connection
```

- define your map by creating a tuple of functions:
  - for direct connection, every function will be assigned to the GPIO on the same index
  - for map connection, functions will be assigned to the index corresponding in the matrix position:
    - in RC the first index is the top left button, and the second index is the button on second row, first column
    - in CR the first index is the top left button, the second is in the first row, second column

```
map = (
  (keyboard.click((Key.S,), hold=(Key.CTRL,))),
  (keyboard.click((Key.R,), hold=(Key.GUI,))),
  (keyboard.click((Key.T,), hold=(Key.CTRL,))),
  (keyboard.click((Key.W,), hold=(Key.CTRL,))),
)

keyboard.setMap(map)
```

- if you want to create multiple layers, you must use the `LayerSwitch` class 
- when instantiating an object of that type, you must pass as parameter the index of the layer you want to switch
- if you configure multiple layers, it is required to modify the map accordingly to the number of layers
  - for each layer, a function must be specified for every button in the map


```
FIRST_LAYER = LayerSwitch(1)

map = (
  ( 
    keyboard.click((Key.S,), hold=(Key.CTRL,)), # Layer zero
    keyboard.click((Key.O,), hold=(Key.CTRL,))  # Layer one
  ),
  (
    keyboard.click((Key.R,), hold=(Key.GUI,)), # Layer zero
    keyboard.click((Key.GUI,))  # Layer one
  ),
  (
    keyboard.click((Key.T,), hold=(Key.CTRL,)), # Layer zero
    keyboard.click((Key.N,), hold=(Key.CTRL,))  # Layer one
  ),
  (
    FIRST_LAYER, FIRST_LAYER # Switch must be set on every layer
  )
)

keyboard.setMap(map)

```

- once done defining pins and map, simply call the run method

```
keyboard.run()
```