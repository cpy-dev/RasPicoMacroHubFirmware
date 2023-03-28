import digitalio
import analogio
import board
import usb_hid
from adafruit_hid.mouse import Mouse
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard import Keycode as K
import time

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

led.value = True
time.sleep(0.1)
led.value = False
time.sleep(0.1)
led.value = True

############# BASE OBJACTS DEFINITION ############
# porcoddio non toccare questi codici #
def initButton(gpio):
    button = digitalio.DigitalInOut(gpio)
    button.direction = digitalio.Direction.INPUT
    button.pull = digitalio.Pull.DOWN
    return button

# mouse and keyboard instance for initialisation
mouse = Mouse(usb_hid.devices)
keyboard = Keyboard(usb_hid.devices)

# initialisation of joystick axes
xaxis = analogio.AnalogIn(board.A1)
yaxis = analogio.AnalogIn(board.A0)

# initialisation of joystick related buttons
joyStickLeft = initButton(board.GP20)
joyStickRight = initButton(board.GP21)
joyStickIntegrated = initButton(board.GP22)

# initialisation of precision mouse keys
right = initButton(board.GP13)
left = initButton(board.GP15)
moveUp = initButton(board.GP14)
moveLeft = initButton(board.GP16)
moveDown = initButton(board.GP17)
moveRight = initButton(board.GP18)

# initialisation of macropad keys
macro11 = initButton(board.GP0)
macro12 = initButton(board.GP1)
macro13 = initButton(board.GP2)
macro14 = initButton(board.GP3)

macro21 = initButton(board.GP4)
macro22 = initButton(board.GP5)
macro23 = initButton(board.GP6)
macro24 = initButton(board.GP7)

macro31 = initButton(board.GP8)
macro32 = initButton(board.GP9)
macro33 = initButton(board.GP10)
macro34 = initButton(board.GP11)

# conversion function for joystick value
def fix(value):
    return value * 10 / 65535 - 5
    
# association table from ascii to keycodes
keys = {
    ' ' : lambda : [keyboard.press(K.SPACE), keyboard.release(K.SPACE)],
    '!' : lambda : [keyboard.press(K.SHIFT), keyboard.press(K.ONE), keyboard.release(K.ONE), keyboard.release(K.SHIFT)],
    '"' : lambda : [keyboard.press(K.SHIFT), keyboard.press(K.TWO), keyboard.release(K.TWO), keyboard.release(K.SHIFT)],
    '#' : lambda : [keyboard.press(K.RIGHT_ALT), keyboard.press(K.QUOTE), keyboard.release(K.QUOTE), keyboard.release(K.RIGHT_ALT)],
    '$' : lambda : [keyboard.press(K.SHIFT), keyboard.press(K.FOUR), keyboard.release(K.FOUR), keyboard.release(K.SHIFT)],
    '%' : lambda : [keyboard.press(K.SHIFT), keyboard.press(K.FIVE), keyboard.release(K.FIVE), keyboard.release(K.SHIFT)],
    '&' : lambda : [keyboard.press(K.SHIFT), keyboard.press(K.SIX), keyboard.release(K.SIX), keyboard.release(K.SHIFT)],
    "'" : lambda : [keyboard.press(K.MINUS), keyboard.release(K.MINUS)],
    '(' : lambda : [keyboard.press(K.SHIFT), keyboard.press(K.EIGHT), keyboard.release(K.EIGHT), keyboard.release(K.SHIFT)],
    ')' : lambda : [keyboard.press(K.SHIFT), keyboard.press(K.NINE), keyboard.release(K.NINE), keyboard.release(K.SHIFT)],
    '*' : lambda : [keyboard.press(K.SHIFT), keyboard.press(K.RIGHT_BRACKET), keyboard.release(K.RIGHT_BRACKET), keyboard.release(K.SHIFT)],
    '+' : lambda : [keyboard.press(K.RIGHT_BRACKET), keyboard.release(K.RIGHT_BRACKET)],
    ',' : lambda : [keyboard.press(K.COMMA), keyboard.release(K.COMMA)],
    '-' : lambda : [keyboard.press(K.FORWARD_SLASH), keyboard.release(K.FORWARD_SLASH)],
    '.' : lambda : [keyboard.press(K.PERIOD), keyboard.release(K.PERIOD)],
    '/' : lambda : [keyboard.press(K.SHIFT), keyboard.press(K.SEVEN), keyboard.release(K.SEVEN), keyboard.release(K.SHIFT)],
    '0' : lambda : [keyboard.press(K.ZERO), keyboard.release(K.ZERO)],
    '1' : lambda : [keyboard.press(K.ONE), keyboard.release(K.ONE)],
    '2' : lambda : [keyboard.press(K.TWO), keyboard.release(K.TWO)],
    '3' : lambda : [keyboard.press(K.THREE), keyboard.release(K.THREE)],
    '4' : lambda : [keyboard.press(K.FOUR), keyboard.release(K.FOUR)],
    '5' : lambda : [keyboard.press(K.FIVE), keyboard.release(K.FIVE)],
    '6' : lambda : [keyboard.press(K.SIX), keyboard.release(K.SIX)],
    '7' : lambda : [keyboard.press(K.SEVEN), keyboard.release(K.SEVEN)],
    '8' : lambda : [keyboard.press(K.EIGHT), keyboard.release(K.EIGHT)],
    '9' : lambda : [keyboard.press(K.NINE), keyboard.release(K.NINE)],
    ':' : lambda : [keyboard.press(K.SHIFT), keyboard.press(K.PERIOD), keyboard.release(K.PERIOD), keyboard.release(K.SHIFT)],
    ';' : lambda : [keyboard.press(K.SHIFT), keyboard.press(K.COMMA), keyboard.release(K.COMMA), keyboard.release(K.SHIFT)],
    '<' : lambda : [keyboard.press(K.SHIFT), keyboard.press(K.COMMA), keyboard.release(K.COMMA), keyboard.release(K.SHIFT)],
    '=' : lambda : [keyboard.press(K.ZERO), keyboard.release(K.ZERO)],
    '>' : lambda : [keyboard.press(K.SHIFT), keyboard.press(K.DOT), keyboard.release(K.DOT), keyboard.release(K.SHIFT)],
    '?' : lambda : [keyboard.press(K.SHIFT), keyboard.press(K.MINUS), keyboard.release(K.MINUS), keyboard.release(K.SHIFT)],
    '@' : lambda : [keyboard.press(K.RIGHT_ALT), keyboard.press(K.SEMICOLON), keyboard.release(K.SEMICOLON), keyboard.release(K.RIGHT_ALT)],
    'A' : lambda : [keyboard.press(K.SHIFT), keyboard.press(K.A), keyboard.release(K.A), keyboard.release(K.SHIFT)],
    'B' : lambda : [keyboard.press(K.SHIFT), keyboard.press(K.B), keyboard.release(K.B), keyboard.release(K.SHIFT)],
    'C' : lambda : [keyboard.press(K.SHIFT), keyboard.press(K.C), keyboard.release(K.C), keyboard.release(K.SHIFT)],
    'D' : lambda : [keyboard.press(K.SHIFT), keyboard.press(K.D), keyboard.release(K.D), keyboard.release(K.SHIFT)],
    'E' : lambda : [keyboard.press(K.SHIFT), keyboard.press(K.E), keyboard.release(K.E), keyboard.release(K.SHIFT)],
    'F' : lambda : [keyboard.press(K.SHIFT), keyboard.press(K.F), keyboard.release(K.F), keyboard.release(K.SHIFT)],
    'G' : lambda : [keyboard.press(K.SHIFT), keyboard.press(K.G), keyboard.release(K.G), keyboard.release(K.SHIFT)],
    'H' : lambda : [keyboard.press(K.SHIFT), keyboard.press(K.H), keyboard.release(K.H), keyboard.release(K.SHIFT)],
    'I' : lambda : [keyboard.press(K.SHIFT), keyboard.press(K.I), keyboard.release(K.I), keyboard.release(K.SHIFT)],
    'J' : lambda : [keyboard.press(K.SHIFT), keyboard.press(K.J), keyboard.release(K.J), keyboard.release(K.SHIFT)],
    'K' : lambda : [keyboard.press(K.SHIFT), keyboard.press(K.K), keyboard.release(K.K), keyboard.release(K.SHIFT)],
    'L' : lambda : [keyboard.press(K.SHIFT), keyboard.press(K.L), keyboard.release(K.L), keyboard.release(K.SHIFT)],
    'M' : lambda : [keyboard.press(K.SHIFT), keyboard.press(K.M), keyboard.release(K.M), keyboard.release(K.SHIFT)],
    'N' : lambda : [keyboard.press(K.SHIFT), keyboard.press(K.N), keyboard.release(K.N), keyboard.release(K.SHIFT)],
    'O' : lambda : [keyboard.press(K.SHIFT), keyboard.press(K.O), keyboard.release(K.O), keyboard.release(K.SHIFT)],
    'P' : lambda : [keyboard.press(K.SHIFT), keyboard.press(K.P), keyboard.release(K.P), keyboard.release(K.SHIFT)],
    'Q' : lambda : [keyboard.press(K.SHIFT), keyboard.press(K.Q), keyboard.release(K.Q), keyboard.release(K.SHIFT)],
    'R' : lambda : [keyboard.press(K.SHIFT), keyboard.press(K.R), keyboard.release(K.R), keyboard.release(K.SHIFT)],
    'S' : lambda : [keyboard.press(K.SHIFT), keyboard.press(K.S), keyboard.release(K.S), keyboard.release(K.SHIFT)],
    'T' : lambda : [keyboard.press(K.SHIFT), keyboard.press(K.T), keyboard.release(K.T), keyboard.release(K.SHIFT)],
    'U' : lambda : [keyboard.press(K.SHIFT), keyboard.press(K.U), keyboard.release(K.U), keyboard.release(K.SHIFT)],
    'V' : lambda : [keyboard.press(K.SHIFT), keyboard.press(K.V), keyboard.release(K.V), keyboard.release(K.SHIFT)],
    'W' : lambda : [keyboard.press(K.SHIFT), keyboard.press(K.W), keyboard.release(K.W), keyboard.release(K.SHIFT)],
    'X' : lambda : [keyboard.press(K.SHIFT), keyboard.press(K.X), keyboard.release(K.X), keyboard.release(K.SHIFT)],
    'Y' : lambda : [keyboard.press(K.SHIFT), keyboard.press(K.Y), keyboard.release(K.Y), keyboard.release(K.SHIFT)],
    'Z' : lambda : [keyboard.press(K.SHIFT), keyboard.press(K.Z), keyboard.release(K.Z), keyboard.release(K.SHIFT)],
    '[' : lambda : [keyboard.press(K.RIGHT_ALT), keyboard.press(K.LEFT_BRACKET), keyboard.release(K.LEFT_BRACKET), keyboard.release(K.RIGHT_ALT)],
    '\\': lambda : [keyboard.press(K.GRAVE), keyboard.release(K.GRAVE)],
    ']' : lambda : [keyboard.press(K.RIGHT_BRACKET), keyboard.release(K.RIGHT_BRACKET)],
    '^' : lambda : [keyboard.press(K.SHIFT), keyboard.press(K.SIX), keyboard.release(K.SIX), keyboard.release(K.SHIFT)],
    '_' : lambda : [keyboard.press(K.SHIFT), keyboard.press(K.FORWARD_SLASH), keyboard.release(K.FORWARD_SLASH), keyboard.release(K.SHIFT)],
    '`' : lambda : [keyboard.press(K.GRAVE), keyboard.release(K.GRAVE)],
    'a' : lambda : [keyboard.press(K.A), keyboard.release(K.A)],
    'b' : lambda : [keyboard.press(K.B), keyboard.release(K.B)],
    'c' : lambda : [keyboard.press(K.C), keyboard.release(K.C)],
    'd' : lambda : [keyboard.press(K.D), keyboard.release(K.D)],
    'e' : lambda : [keyboard.press(K.E), keyboard.release(K.E)],
    'f' : lambda : [keyboard.press(K.F), keyboard.release(K.F)],
    'g' : lambda : [keyboard.press(K.G), keyboard.release(K.G)],
    'h' : lambda : [keyboard.press(K.H), keyboard.release(K.H)],
    'i' : lambda : [keyboard.press(K.I), keyboard.release(K.I)],
    'j' : lambda : [keyboard.press(K.J), keyboard.release(K.J)],
    'k' : lambda : [keyboard.press(K.K), keyboard.release(K.K)],
    'l' : lambda : [keyboard.press(K.L), keyboard.release(K.L)],
    'm' : lambda : [keyboard.press(K.M), keyboard.release(K.M)],
    'n' : lambda : [keyboard.press(K.N), keyboard.release(K.N)],
    'o' : lambda : [keyboard.press(K.O), keyboard.release(K.O)],
    'p' : lambda : [keyboard.press(K.P), keyboard.release(K.P)],
    'q' : lambda : [keyboard.press(K.Q), keyboard.release(K.Q)],
    'r' : lambda : [keyboard.press(K.R), keyboard.release(K.R)],
    's' : lambda : [keyboard.press(K.S), keyboard.release(K.S)],
    't' : lambda : [keyboard.press(K.T), keyboard.release(K.T)],
    'u' : lambda : [keyboard.press(K.U), keyboard.release(K.U)],
    'v' : lambda : [keyboard.press(K.V), keyboard.release(K.V)],
    'w' : lambda : [keyboard.press(K.W), keyboard.release(K.W)],
    'x' : lambda : [keyboard.press(K.X), keyboard.release(K.X)],
    'y' : lambda : [keyboard.press(K.Y), keyboard.release(K.Y)],
    'z' : lambda : [keyboard.press(K.Z), keyboard.release(K.Z)],
    '{' : lambda : [keyboard.press(K.RIGHT_ALT), keyboard.press(K.SHIFT), keyboard.press(K.LEFT_BRACKET), keyboard.release(K.LEFT_BRACKET), keyboard.release(K.SHIFT), keyboard.release(K.RIGHT_ALT)],
    '|' : lambda : [keyboard.press(K.SHIFT), keyboard.press(K.GRAVE), keyboard.release(K.GRAVE), keyboard.release(K.SHIFT)],
    '}' : lambda : [keyboard.press(K.RIGHT_ALT), keyboard.press(K.SHIFT), keyboard.press(K.RIGHT_BRACKET), keyboard.release(K.RIGHT_BRACKET), keyboard.release(K.SHIFT), keyboard.release(K.RIGHT_ALT)],
    '~' : lambda : [keyboard.press(K.SHIFT), keyboard.press(K.GRAVE), keyboard.release(K.GRAVE), keyboard.release(K.SHIFT)],
}

# write function for directly writing string with optional hold keys
def write(string, hold=None):
    if hold is not None:
        if isinstance(hold, tuple):
            for holding in hold:
                keyboard.press(holding)
        else:
            keyboard.press(hold)
                          
    for char in string:
        if char in keys.keys():
            (keys[char])()

    if hold is not None:
        if isinstance(hold, tuple):
            for holding in hold:
                keyboard.release(holding)
        else:
            keyboard.release(hold)

# click function for keycode(s) and optional hold keys
def click(keycodes, hold=None):
    if hold is not None:
        if isinstance(hold, tuple):
            for holding in hold:
                keyboard.press(holding)
        else:
            keyboard.press(hold)
            
    if isinstance(keys, tuple):
        for key in keycodes:
            try:
                keyboard.press(key)
                keyboard.release(key)
            except: pass
    else:
        try:
            keyboard.press(keys)
            keyboard.release(keys)
        except: pass
        
    if hold is not None:
        if isinstance(hold, tuple):
            for holding in hold:
                keyboard.release(holding)
        else:
            keyboard.release(hold)


############ CUSTOM DEFINITION ########
# da qua si può iniziare a scrivere cagate #

jsStep = 3          # step di movimento del joystick
precisionStep = 2   # step di movimento del mouse di precisione

# class definition for click only keys
class Action:
    def __init__(self, device, onClick):
        self.device = device
        self.onClick = onClick
        
# class definition for press and hold keys
class LayerAction:
    def __init__(self, device, onPress, onRelease):
        self.device = device
        self.onPress = onPress
        self.onRelease = onRelease
        self.active = False

class Layer:
    def __init__(self, device, index):
        self.device = device
        self.index = index
        self.active = False

def sequentialLayer():
    global layer
    if layer < 2:
        layer += 2
    else:
        layer = 0
        
# mouse map
mouseMap = (
    LayerAction(left, lambda : [mouse.press(mouse.LEFT_BUTTON)], lambda: [mouse.release(mouse.LEFT_BUTTON)]),
    LayerAction(right, lambda : [mouse.press(mouse.RIGHT_BUTTON)], lambda : [mouse.release(mouse.RIGHT_BUTTON)]),
    Action(moveUp, lambda : [mouse.move(0, -precisionStep)]),
    Action(moveDown, lambda : [mouse.move(0, precisionStep)]),
    Action(moveLeft, lambda : [mouse.move(-precisionStep, 0)]),
    Action(moveRight, lambda : [mouse.move(precisionStep, 0)]),
    LayerAction(joyStickLeft, lambda : [mouse.press(mouse.LEFT_BUTTON)], lambda : [mouse.release(mouse.LEFT_BUTTON)]),
    LayerAction(joyStickRight, lambda : [mouse.press(mouse.RIGHT_BUTTON)], lambda : [mouse.release(mouse.RIGHT_BUTTON)]),
    LayerAction(joyStickIntegrated, lambda : [mouse.press(mouse.MIDDLE_BUTTON)], lambda : [mouse.release(mouse.MIDDLE_BUTTON)]),
)


macroMap = (
    (
        Action(macro11, lambda : [write('/')]),
        Action(macro11, lambda : [click(K.Q, hold=K.SHIFT)])
    ),
    (
        Action(macro12, lambda : [click(K.X, hold=K.CONTROL)]),
        Action(macro12, lambda : [click(K.W, hold=K-SHIFT)])
    ),
    (
        Action(macro13, lambda : [click(K.C, hold=K.CONTROL)]),
        Action(macro13, lambda : [click(K.E, hold=K.SHIFT)])
    ),
    (
        Action(macro14, lambda : [click(K.V, hold=K.CONTROL)]),
        Action(macro14, lambda : [write('Treni & F1')])
    ),
    
    (
        Action(macro21, lambda : [click(K.S, hold=K.CONTROL)]),
        Action(macro21, lambda : [click(K.ONE, hold=K.SHIFT)])
    ),
    (
        Action(macro22, lambda : [click(K.A, hold=K.CONTROL)]),
        Action(macro22, lambda : [click(K.TWO, hold=K.SHIFT)])
    ),
    (
        Action(macro23, lambda : [click(K.LEFT_ARROW, hold=K.ALT)]),
        Action(macro23, lambda : [click(K.ONE, hold=K.WINDOWS)])
    ),
    (
        Action(macro24, lambda : [click(K.RIGHT_ARROW, hold=K.ALT)]),
        Action(macro24, lambda : [click(K.TWO, hold=K.WINDOWS)])
    ),
    
    (
        Action(macro31, lambda : [click(K.D, hold=K.WINDOWS)]),
        Action(macro31, lambda : [click(K.THREE, hold=K.SHIFT)])
    ),
    (
        Action(macro32, lambda : [click(K.O, hold=K.CONTROL)]),
        Action(macro32, lambda : [click(K.FOUR, hold=K.SHIFT)])
    ),
    (
        Action(macro33, lambda : [click(K.N, hold=K.CONTROL)]),
        Action(macro33, lambda : [click(K.E, hold=K.WINDOWS)])
    ),
    (
        Layer(macro34, 1),
        Layer(macro34, 1)
    ),
)

if __name__ == '__main__':
    layer = 0
    lastLayer = 0
    while True:
        for action in macroMap:
            if isinstance(action[layer], Action):
                if action[layer].device.value:
                    action[layer].onClick()
                    time.sleep(0.2)

            else:
                if action[layer].device.value:
                    if not action[layer].active:
                        lastLayer = layer
                        layer = action[layer].index
                        action[layer].active = True
                
                else:
                    layer = lastLayer
                    action[layer].active = False

        
        for action in mouseMap:
            if isinstance(action, Action):
                if action.device.value:
                    action.onClick()
            
            else:
                if action.device.value:
                    if not action.active:
                        action.onPress()
                        action.active = True

                else:
                    if action.active:
                        action.onRelease()
                        action.active = False
        
        x = round(fix(xaxis.value))
        if x != 0 and not x % 2:
            
            if x < 0:
                x += 1
            
            elif x > 0:
                x -= 1
                
        y = round(fix(yaxis.value))
        if y != 0 and not y % 2:
            
            if y < 0:
                y += 1
            
            elif y > 0:
                y -= 1
            
        if x or y:
            mouse.move(jsStep * -x, jsStep * -y)
