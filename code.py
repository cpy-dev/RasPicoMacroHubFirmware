import digitalio
import analogio
import board
import usb_hid
from adafruit_hid.mouse import Mouse
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard import Keycode as K

############# BASE OBJACTS DEFINITION ############
# porcoddio non toccare questi codici #

mouse = Mouse(usb_hid.devices)
keyboard = Keyboard(usb_hid.devices)

xaxis = analogio.AnalogIn(board.GPA0)
yaxis = analogio.AnalogIn(board.GPA1)

joyStickLeft = digitalio.DigitalInOut(board.GP20)
joyStickLeft.direction = digitalio.Direction.INPUT
joyStickLeft.pull = digitalio.Pull.DOWN

joyStickRight = digitalio.DigitalInOut(board.GP21)
joyStickRight.direction = digitalio.Direction.INPUT
joyStickRight.pull = digitalio.Pull.DOWN

joyStickIntegrated = digitalio.DigitalInOut(board.GP22)
joyStickIntegrated.direction = digitalio.Direction.INPUT
joyStickIntegrated.pull = digitalio.Pull.DOWN

right = digitalio.DigitalInOut(board.GP13)
right.direction = digitalio.Direction.INPUT
right.pull = digitalio.Pull.DOWN

left = digitalio.DigitalInOut(board.GP15)
left.direction = digitalio.Direction.INPUT
left.pull = digitalio.Pull.DOWN

moveUp = digitalio.DigitalInOut(board.GP14)
moveUp.direction = digitalio.Direction.INPUT
moveUp.pull = digitalio.Pull.DOWN

moveLeft = digitalio.DigitalInOut(board.GP16)
moveLeft.direction = digitalio.Direction.INPUT
moveLeft.pull = digitalio.Pull.DOWN

moveDown = digitalio.DigitalInOut(board.GP17)
moveDown.direction = digitalio.Direction.INPUT
moveDown.pull = digitalio.Pull.DOWN

moveRight = digitalio.DigitalInOut(board.GP18)
moveRight.direction = digitalio.Direction.INPUT
moveRight.pull = digitalio.Pull.DOWN

macro11 = digitalio.DigitalInOut(board.GP0)
macro11.direction = digitalio.Direction.INPUT
macro11.pull = digitalio.Pull.DOWN

macro12 = digitalio.DigitalInOut(board.GP1)
macro12.direction = digitalio.Direction.INPUT
macro12.pull = digitalio.Pull.DOWN

macro13 = digitalio.DigitalInOut(board.GP2)
macro13.direction = digitalio.Direction.INPUT
macro13.pull = digitalio.Pull.DOWN

macro14 = digitalio.DigitalInOut(board.GP3)
macro14.direction = digitalio.Direction.INPUT
macro14.pull = digitalio.Pull.DOWN

macro21 = digitalio.DigitalInOut(board.GP4)
macro21.direction = digitalio.Direction.INPUT
macro21.pull = digitalio.Pull.DOWN

macro22 = digitalio.DigitalInOut(board.GP5)
macro22.direction = digitalio.Direction.INPUT
macro22.pull = digitalio.Pull.DOWN

macro23 = digitalio.DigitalInOut(board.GP6)
macro23.direction = digitalio.Direction.INPUT
macro23.pull = digitalio.Pull.DOWN

macro24 = digitalio.DigitalInOut(board.GP7)
macro24.direction = digitalio.Direction.INPUT
macro24.pull = digitalio.Pull.DOWN

macro31 = digitalio.DigitalInOut(board.GP8)
macro31.direction = digitalio.Direction.INPUT
macro31.pull = digitalio.Pull.DOWN

macro32 = digitalio.DigitalInOut(board.GP9)
macro32.direction = digitalio.Direction.INPUT
macro32.pull = digitalio.Pull.DOWN

macro33 = digitalio.DigitalInOut(board.GP10)
macro33.direction = digitalio.Direction.INPUT
macro33.pull = digitalio.Pull.DOWN

macro34 = digitalio.DigitalInOut(board.GP11)
macro34.direction = digitalio.Direction.INPUT
macro34.pull = digitalio.Pull.DOWN

def fix(value):
    value * 10 / 65535 - 5

keys = {
    ' ' : lambda : [keyboard.press(K.SPACE), keyboard.release(K.SPACE)],
    '!' : lambda : [keyboard.press(K.SHIFT), keyboard.press(K.ONE), keyboard.release(K.ONE), keyboard.release(K.SHIFT)],
    '"' : lambda : [keyboard.press(K.SHIFT), keyboard.press(K.QUOTE), keyboard.release(K.QUOTE), keyboard.release(K.SHIFT)],
    '#' : lambda : [keyboard.press(K.SHIFT), keyboard.press(K.THREE), keyboard.release(K.THREE), keyboard.release(K.SHIFT)],
    '$' : lambda : [keyboard.press(K.SHIFT), keyboard.press(K.FOUR), keyboard.release(K.FOUR), keyboard.release(K.SHIFT)],
    '%' : lambda : [keyboard.press(K.SHIFT), keyboard.press(K.FIVE), keyboard.release(K.FIVE), keyboard.release(K.SHIFT)],
    '&' : lambda : [keyboard.press(K.SHIFT), keyboard.press(K.SEVEN), keyboard.release(K.SEVEN), keyboard.release(K.SHIFT)],
    "'" : lambda : [keyboard.press(K.QUOTE), keyboard.release(K.QUOTE)],
    '(' : lambda : [keyboard.press(K.SHIFT), keyboard.press(K.NINE), keyboard.release(K.NINE), keyboard.release(K.SHIFT)],
    ')' : lambda : [keyboard.press(K.SHIFT), keyboard.press(K.ZERO), keyboard.release(K.ZERO), keyboard.release(K.SHIFT)],
    '*' : lambda : [keyboard.press(K.SHIFT), keyboard.press(K.EIGHT), keyboard.release(K.EIGHT), keyboard.release(K.SHIFT)],
    '+' : lambda : [keyboard.press(K.SHIFT), keyboard.press(K.EQUALS), keyboard.release(K.EQUALS), keyboard.release(K.SHIFT)],
    ',' : lambda : [keyboard.press(K.COMMA), keyboard.release(K.COMMA)],
    '-' : lambda : [keyboard.press(K.MINUS), keyboard.release(K.MINUS)],
    '.' : lambda : [keyboard.press(K.DOT), keyboard.release(K.DOT)],
    '/' : lambda : [keyboard.press(K.FORWARD_SLASH), keyboard.release(K.FORWARD_SLASH)],
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
    ':' : lambda : [keyboard.press(K.SHIFT), keyboard.press(K.SEMICOLON), keyboard.release(K.SEMICOLON), keyboard.release(K.SHIFT)],
    ';' : lambda : [keyboard.press(K.SEMICOLON), keyboard.release(K.SEMICOLON)],
    '<' : lambda : [keyboard.press(K.SHIFT), keyboard.press(K.COMMA), keyboard.release(K.COMMA), keyboard.release(K.SHIFT)],
    '=' : lambda : [keyboard.press(K.EQUALS), keyboard.release(K.EQUALS)],
    '>' : lambda : [keyboard.press(K.SHIFT), keyboard.press(K.DOT), keyboard.release(K.DOT), keyboard.release(K.SHIFT)],
    '?' : lambda : [keyboard.press(K.SHIFT), keyboard.press(K.FORWARDSLASH), keyboard.release(K.FORWARDSLASH), keyboard.release(K.SHIFT)],
    '@' : lambda : [keyboard.press(K.SHIFT), keyboard.press(K.TWO), keyboard.release(K.TWO), keyboard.release(K.SHIFT)],
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
    '[' : lambda : [keyboard.press(K.LEFT_BRACKET), keyboard.release(K.LEFT_BRACKET)],
    '\\' : lambda : [keyboard.press(K.BACKSLASH), keyboard.release(K.BACKSLASH)],
    ']' : lambda : [keyboard.press(K.RIGHT_BRACKET), keyboard.release(K.RIGHT_BRACKET)],
    '^' : lambda : [keyboard.press(K.SHIFT), keyboard.press(K.SIX), keyboard.release(K.SIX), keyboard.release(K.SHIFT)],
    '_' : lambda : [keyboard.press(K.SHIFT), keyboard.press(K.MINUS), keyboard.release(K.MINUS), keyboard.release(K.SHIFT)],
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
    '{' : lambda : [keyboard.press(K.SHIFT), keyboard.press(K.LEFT_BRACKET), keyboard.release(K.LEFT_BRACKET), keyboard.release(K.SHIFT)],
    '|' : lambda : [keyboard.press(K.SHIFT), keyboard.press(K.BACKSLASH), keyboard.release(K.BACKSLASH), keyboard.release(K.SHIFT)],
    '}' : lambda : [keyboard.press(K.SHIFT), keyboard.press(K.RIGHT_BRACKET), keyboard.release(K.RIGHT_BRACKET), keyboard.release(K.SHIFT)],
    '~' : lambda : [keyboard.press(K.SHIFT), keyboard.press(K.GRAVE), keyboard.release(K.GRAVE), keyboard.release(K.SHIFT)],
}

def write(string, hold=None):
    if hold is not None:
        for holding in hold:
            keyboard.press(holding)

    for char in string:
        if char in keys.keys():
            (keys[char])()

    if hold is not None:
        for holding in hold:
            keyboard.release(holding)

def click(keycodes, hold=None):
    if hold is not None:
        for holding in hold:
            keyboard.press(holding)

    for key in keycodes:
        try:
            keyboard.press(key)
            keyboard.release(key)
        except:
            pass

    if hold is not None:
        for holding in hold:
            keyboard.release(holding)

############ CUSTOM DEFINITION ########
# da qua si può iniziare a scrivere cagate #

jsStep = 2          # step di movimento del joystick
precisionStep = 4   # step di movimento del mouse di precisione

class Action:
    def __init__(self, device, onClick):
        self.device = device
        self.onClick = onClick
        
class LayerAction:
    def __init__(self, device, onPress, onRelease):
        self.device = device
        self.onPress = onPress
        self.onRelease = onRelease
        self.active = False

map = [
    LayerAction(left, lambda : [mouse.press(mouse.LEFT_BUTTON)], lambda: [mouse.release(mouse.LEFT_BUTTON)]),
    LayerAction(right, lambda : [mouse.press(mouse.RIGHT_BUTTON)], lambda : [mouse.release(mouse.RIGHT_BUTTON)]),
    Action(moveUp, lambda : [mouse.move(0, -precisionStep)]),
    Action(moveDown, lambda : [mouse.move(0, precisionStep)]),
    Action(moveLeft, lambda : [mouse.move(-precisionStep, 0)]),
    Action(moveRight, lambda : [mouse.move(precisionStep, 0)]),
    LayerAction(joyStickLeft, lambda : [mouse.press(mouse.RIGHT_BUTTON)], lambda : [mouse.release(mouse.RIGHT_BUTTON)]),
    LayerAction(joyStickRight, lambda : [mouse.press(mouse.MIDDLE_BUTTON)], lambda : [mouse.release(mouse.MIDDLE_BUTTON)]),
    LayerAction(joyStickIntegrated, lambda : [mouse.press(mouse.LEFT_BUTTON)], mouse.release(mouse.LEFT_BUTTON)),
    Action(macro11, lambda: []),
    Action(macro12, lambda: []),
    Action(macro13, lambda: []),
    Action(macro14, lambda: []),
    Action(macro21, lambda: []),
    Action(macro22, lambda: []),
    Action(macro23, lambda: []),
    Action(macro24, lambda: []),
    Action(macro31, lambda: []),
    Action(macro32, lambda: []),
    Action(macro33, lambda: []),
    Action(macro34, lambda: []),
]

if __name__ == '__main__':
    while True:
        for action in map:
            if isinstance(action, Action):
                if action.device.value:
                    action.onPress()
            
            else:
                if action.device.value and not action.value:
                    action.onPress()
                    action.value = True
                
                else:
                    if action.value:
                        action.onRelease()
                        action.value = False
                        
        x = round(fix(xaxis))
        y = round(fix(yaxis))

        if x or y:
            mouse.move(jsStep * x, jsStep * y)
