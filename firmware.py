import board
import usb_hid
import digitalio
import analogio
from adafruit_hid.keybaord import Keyboard
from adafruit_hid.keycode import Keycode as K
import time

class LayerSwitch:
    def __init__(self, layerIndex):
        self.layer = layerIndex

class __Key:    
    C = K.C
    M = K.M
    A = K.A
    B = K.B
    D = K.D
    E = K.E
    F = K.F
    G = K.G
    H = K.H
    I = K.I
    J = K.J
    K = K.K
    L = K.L
    N = K.N
    O = K.O
    P = K.P
    Q = K.Q
    R = K.R
    S = K.S
    T = K.T
    U = K.U
    V = K.V
    W = K.W
    X = K.X
    Y = K.Y
    Z = K.Z
    ONE = K.ONE
    TWO = K.TWO
    THREE = K.THREE
    FOUR = K.FOUR
    FIVE = K.FIVE
    SIX = K.SIX
    SEVEN = K.SEVEN
    EIGHT = K.EIGHT
    NINE = K.NINE
    ZERO = K.ZERO
    ENTER = K.ENTER
    RETURN = K.RETURN
    ESCAPE = K.ESCAPE
    BACKSPACE = K.BACKSPACE
    TAB = K.TAB
    SPACEBAR = K.SPACEBAR
    SPACE = K.SPACE
    MINUS = K.MINUS
    EQUALS = K.EQUALS
    LEFT_BRACKET = K.LEFT_BRACKET
    RIGHT_BRACKET = K.RIGHT_BRACKET
    BACKSLASH = K.BACKSLASH
    POUND = K.POUND
    SEMICOLON = K.SEMICOLON
    QUOTE = K.QUOTE
    GRAVE_ACCENT = K.GRAVE_ACCENT
    COMMA = K.COMMA
    PERIOD = K.PERIOD
    FORWARD_SLASH = K.FORWARD_SLASH
    CAPS_LOCK = K.CAPS_LOCK
    F1 = K.F1
    F2 = K.F2
    F3 = K.F3
    F4 = K.F4
    F5 = K.F5
    F6 = K.F6
    F7 = K.F7
    F8 = K.F8
    F9 = K.F9
    F10 = K.F10
    F11 = K.F11
    F12 = K.F12
    PRINT_SCREEN = K.PRINT_SCREEN
    SCROLL_LOCK = K.SCROLL_LOCK
    PAUSE = K.PAUSE
    INSERT = K.INSERT
    HOME = K.HOME
    PAGE_UP = K.PAGE_UP
    DELETE = K.DELETE
    END = K.END
    PAGE_DOWN = K.PAGE_DOWN
    RIGHT_ARROW = K.RIGHT_ARROW
    LEFT_ARROW = K.LEFT_ARROW
    DOWN_ARROW = K.DOWN_ARROW
    UP_ARROW = K.UP_ARROW
    KEYPAD_NUMLOCK = K.KEYPAD_NUMLOCK
    KEYPAD_FORWARD_SLASH = K.KEYPAD_FORWARD_SLASH
    KEYPAD_ASTERISK = K.KEYPAD_ASTERISK
    KEYPAD_MINUS = K.KEYPAD_MINUS
    KEYPAD_PLUS = K.KEYPAD_PLUS
    KEYPAD_ENTER = K.KEYPAD_ENTER
    KEYPAD_ONE = K.KEYPAD_ONE
    KEYPAD_TWO = K.KEYPAD_TWO
    KEYPAD_THREE = K.KEYPAD_THREE
    KEYPAD_FOUR = K.KEYPAD_FOUR
    KEYPAD_FIVE = K.KEYPAD_FIVE
    KEYPAD_SIX = K.KEYPAD_SIX
    KEYPAD_SEVEN = K.KEYPAD_SEVEN
    KEYPAD_EIGHT = K.KEYPAD_EIGHT
    KEYPAD_NINE = K.KEYPAD_NINE
    KEYPAD_ZERO = K.KEYPAD_ZERO
    KEYPAD_PERIOD = K.KEYPAD_PERIOD
    KEYPAD_BACKSLASH = K.KEYPAD_BACKSLASH
    APPLICATION = K.APPLICATION
    POWER = K.POWER
    KEYPAD_EQUALS = K.KEYPAD_EQUALS
    F13 = K.F13
    F14 = K.F14
    F15 = K.F15
    F16 = K.F16
    F17 = K.F17
    F18 = K.F18
    F19 = K.F19
    F20 = K.F20
    F21 = K.F21
    F22 = K.F22
    F23 = K.F23
    F24 = K.F24
    LEFT_CONTROL = K.LEFT_CONTROL
    CONTROL = K.CONTROL
    LEFT_SHIFT = K.LEFT_SHIFT
    SHIFT = K.SHIFT
    LEFT_ALT = K.LEFT_ALT
    ALT = K.ALT
    OPTION = K.OPTION
    LEFT_GUI = K.LEFT_GUI
    GUI = K.GUI
    WINDOWS = K.WINDOWS
    COMMAND = K.COMMAND
    RIGHT_CONTROL = K.RIGHT_CONTROL
    RIGHT_SHIFT = K.RIGHT_SHIFT
    RIGHT_ALT = K.RIGHT_ALT
    RIGHT_GUI = K.RIGHT_GUI
    
    def __init__(self):
        pass

Key = __Key()
    
chars = {
    ' ' : lambda : (keyboard)[keyboard.press(K.SPACE), keyboard.release(K.SPACE)],
    '!' : lambda : (keyboard)[keyboard.press(K.SHIFT), keyboard.press(K.ONE), keyboard.release(K.ONE), keyboard.release(K.SHIFT)],
    '"' : lambda : (keyboard)[keyboard.press(K.SHIFT), keyboard.press(K.QUOTE), keyboard.release(K.QUOTE), keyboard.release(K.SHIFT)],
    '#' : lambda : (keyboard)[keyboard.press(K.SHIFT), keyboard.press(K.THREE), keyboard.release(K.THREE), keyboard.release(K.SHIFT)],
    '$' : lambda : (keyboard)[keyboard.press(K.SHIFT), keyboard.press(K.FOUR), keyboard.release(K.FOUR), keyboard.release(K.SHIFT)],
    '%' : lambda : (keyboard)[keyboard.press(K.SHIFT), keyboard.press(K.FIVE), keyboard.release(K.FIVE), keyboard.release(K.SHIFT)],
    '&' : lambda : (keyboard)[keyboard.press(K.SHIFT), keyboard.press(K.SEVEN), keyboard.release(K.SEVEN), keyboard.release(K.SHIFT)],
    "'" : lambda : (keyboard)[keyboard.press(K.QUOTE), keyboard.release(K.QUOTE)],
    '(' : lambda : (keyboard)[keyboard.press(K.SHIFT), keyboard.press(K.NINE), keyboard.release(K.NINE), keyboard.release(K.SHIFT)],
    ')' : lambda : (keyboard)[keyboard.press(K.SHIFT), keyboard.press(K.ZERO), keyboard.release(K.ZERO), keyboard.release(K.SHIFT)],
    '*' : lambda : (keyboard)[keyboard.press(K.SHIFT), keyboard.press(K.EIGHT), keyboard.release(K.EIGHT), keyboard.release(K.SHIFT)],
    '+' : lambda : (keyboard)[keyboard.press(K.SHIFT), keyboard.press(K.EQUALS), keyboard.release(K.EQUALS), keyboard.release(K.SHIFT)],
    ',' : lambda : (keyboard)[keyboard.press(K.COMMA), keyboard.release(K.COMMA)],
    '-' : lambda : (keyboard)[keyboard.press(K.MINUS), keyboard.release(K.MINUS)],
    '.' : lambda : (keyboard)[keyboard.press(K.DOT), keyboard.release(K.DOT)],
    '/' : lambda : (keyboard)[keyboard.press(K.FORWARD_SLASH), keyboard.release(K.FORWARD_SLASH)],
    '0' : lambda : (keyboard)[keyboard.press(K.ZERO), keyboard.release(K.ZERO)],
    '1' : lambda : (keyboard)[keyboard.press(K.ONE), keyboard.release(K.ONE)],
    '2' : lambda : (keyboard)[keyboard.press(K.TWO), keyboard.release(K.TWO)],
    '3' : lambda : (keyboard)[keyboard.press(K.THREE), keyboard.release(K.THREE)],
    '4' : lambda : (keyboard)[keyboard.press(K.FOUR), keyboard.release(K.FOUR)],
    '5' : lambda : (keyboard)[keyboard.press(K.FIVE), keyboard.release(K.FIVE)],
    '6' : lambda : (keyboard)[keyboard.press(K.SIX), keyboard.release(K.SIX)],
    '7' : lambda : (keyboard)[keyboard.press(K.SEVEN), keyboard.release(K.SEVEN)],
    '8' : lambda : (keyboard)[keyboard.press(K.EIGHT), keyboard.release(K.EIGHT)],
    '9' : lambda : (keyboard)[keyboard.press(K.NINE), keyboard.release(K.NINE)],
    ':' : lambda : (keyboard)[keyboard.press(K.SHIFT), keyboard.press(K.SEMICOLON), keyboard.release(K.SEMICOLON), keyboard.release(K.SHIFT)],
    ';' : lambda : (keyboard)[keyboard.press(K.SEMICOLON), keyboard.release(K.SEMICOLON)],
    '<' : lambda : (keyboard)[keyboard.press(K.SHIFT), keyboard.press(K.COMMA), keyboard.release(K.COMMA), keyboard.release(K.SHIFT)],
    '=' : lambda : (keyboard)[keyboard.press(K.EQUALS), keyboard.release(K.EQUALS)],
    '>' : lambda : (keyboard)[keyboard.press(K.SHIFT), keyboard.press(K.DOT), keyboard.release(K.DOT), keyboard.release(K.SHIFT)],
    '?' : lambda : (keyboard)[keyboard.press(K.SHIFT), keyboard.press(K.FORWARDSLASH), keyboard.release(K.FORWARDSLASH), keyboard.release(K.SHIFT)],
    '@' : lambda : (keyboard)[keyboard.press(K.SHIFT), keyboard.press(K.TWO), keyboard.release(K.TWO), keyboard.release(K.SHIFT)],
    'A' : lambda : (keyboard)[keyboard.press(K.SHIFT), keyboard.press(K.A), keyboard.release(K.A), keyboard.release(K.SHIFT)],
    'B' : lambda : (keyboard)[keyboard.press(K.SHIFT), keyboard.press(K.B), keyboard.release(K.B), keyboard.release(K.SHIFT)],
    'C' : lambda : (keyboard)[keyboard.press(K.SHIFT), keyboard.press(K.C), keyboard.release(K.C), keyboard.release(K.SHIFT)],
    'D' : lambda : (keyboard)[keyboard.press(K.SHIFT), keyboard.press(K.D), keyboard.release(K.D), keyboard.release(K.SHIFT)],
    'E' : lambda : (keyboard)[keyboard.press(K.SHIFT), keyboard.press(K.E), keyboard.release(K.E), keyboard.release(K.SHIFT)],
    'F' : lambda : (keyboard)[keyboard.press(K.SHIFT), keyboard.press(K.F), keyboard.release(K.F), keyboard.release(K.SHIFT)],
    'G' : lambda : (keyboard)[keyboard.press(K.SHIFT), keyboard.press(K.G), keyboard.release(K.G), keyboard.release(K.SHIFT)],
    'H' : lambda : (keyboard)[keyboard.press(K.SHIFT), keyboard.press(K.H), keyboard.release(K.H), keyboard.release(K.SHIFT)],
    'I' : lambda : (keyboard)[keyboard.press(K.SHIFT), keyboard.press(K.I), keyboard.release(K.I), keyboard.release(K.SHIFT)],
    'J' : lambda : (keyboard)[keyboard.press(K.SHIFT), keyboard.press(K.J), keyboard.release(K.J), keyboard.release(K.SHIFT)],
    'K' : lambda : (keyboard)[keyboard.press(K.SHIFT), keyboard.press(K.K), keyboard.release(K.K), keyboard.release(K.SHIFT)],
    'L' : lambda : (keyboard)[keyboard.press(K.SHIFT), keyboard.press(K.L), keyboard.release(K.L), keyboard.release(K.SHIFT)],
    'M' : lambda : (keyboard)[keyboard.press(K.SHIFT), keyboard.press(K.M), keyboard.release(K.M), keyboard.release(K.SHIFT)],
    'N' : lambda : (keyboard)[keyboard.press(K.SHIFT), keyboard.press(K.N), keyboard.release(K.N), keyboard.release(K.SHIFT)],
    'O' : lambda : (keyboard)[keyboard.press(K.SHIFT), keyboard.press(K.O), keyboard.release(K.O), keyboard.release(K.SHIFT)],
    'P' : lambda : (keyboard)[keyboard.press(K.SHIFT), keyboard.press(K.P), keyboard.release(K.P), keyboard.release(K.SHIFT)],
    'Q' : lambda : (keyboard)[keyboard.press(K.SHIFT), keyboard.press(K.Q), keyboard.release(K.Q), keyboard.release(K.SHIFT)],
    'R' : lambda : (keyboard)[keyboard.press(K.SHIFT), keyboard.press(K.R), keyboard.release(K.R), keyboard.release(K.SHIFT)],
    'S' : lambda : (keyboard)[keyboard.press(K.SHIFT), keyboard.press(K.S), keyboard.release(K.S), keyboard.release(K.SHIFT)],
    'T' : lambda : (keyboard)[keyboard.press(K.SHIFT), keyboard.press(K.T), keyboard.release(K.T), keyboard.release(K.SHIFT)],
    'U' : lambda : (keyboard)[keyboard.press(K.SHIFT), keyboard.press(K.U), keyboard.release(K.U), keyboard.release(K.SHIFT)],
    'V' : lambda : (keyboard)[keyboard.press(K.SHIFT), keyboard.press(K.V), keyboard.release(K.V), keyboard.release(K.SHIFT)],
    'W' : lambda : (keyboard)[keyboard.press(K.SHIFT), keyboard.press(K.W), keyboard.release(K.W), keyboard.release(K.SHIFT)],
    'X' : lambda : (keyboard)[keyboard.press(K.SHIFT), keyboard.press(K.X), keyboard.release(K.X), keyboard.release(K.SHIFT)],
    'Y' : lambda : (keyboard)[keyboard.press(K.SHIFT), keyboard.press(K.Y), keyboard.release(K.Y), keyboard.release(K.SHIFT)],
    'Z' : lambda : (keyboard)[keyboard.press(K.SHIFT), keyboard.press(K.Z), keyboard.release(K.Z), keyboard.release(K.SHIFT)],
    '[' : lambda : (keyboard)[keyboard.press(K.LEFT_BRACKET), keyboard.release(K.LEFT_BRACKET)],
    '\\' : lambda : (keyboard)[keyboard.press(K.BACKSLASH), keyboard.release(K.BACKSLASH)],
    ']' : lambda : (keyboard)[keyboard.press(K.RIGHT_BRACKET), keyboard.release(K.RIGHT_BRACKET)],
    '^' : lambda : (keyboard)[keyboard.press(K.SHIFT), keyboard.press(K.SIX), keyboard.release(K.SIX), keyboard.release(K.SHIFT)],
    '_' : lambda : (keyboard)[keyboard.press(K.SHIFT), keyboard.press(K.MINUS), keyboard.release(K.MINUS), keyboard.release(K.SHIFT)],
    '`' : lambda : (keyboard)[keyboard.press(K.GRAVE), keyboard.release(K.GRAVE)],
    'a' : lambda : (keyboard)[keyboard.press(K.A), keyboard.release(K.A)],
    'b' : lambda : (keyboard)[keyboard.press(K.B), keyboard.release(K.B)],
    'c' : lambda : (keyboard)[keyboard.press(K.C), keyboard.release(K.C)],
    'd' : lambda : (keyboard)[keyboard.press(K.D), keyboard.release(K.D)],
    'e' : lambda : (keyboard)[keyboard.press(K.E), keyboard.release(K.E)],
    'f' : lambda : (keyboard)[keyboard.press(K.F), keyboard.release(K.F)],
    'g' : lambda : (keyboard)[keyboard.press(K.G), keyboard.release(K.G)],
    'h' : lambda : (keyboard)[keyboard.press(K.H), keyboard.release(K.H)],
    'i' : lambda : (keyboard)[keyboard.press(K.I), keyboard.release(K.I)],
    'j' : lambda : (keyboard)[keyboard.press(K.J), keyboard.release(K.J)],
    'k' : lambda : (keyboard)[keyboard.press(K.K), keyboard.release(K.K)],
    'l' : lambda : (keyboard)[keyboard.press(K.L), keyboard.release(K.L)],
    'm' : lambda : (keyboard)[keyboard.press(K.M), keyboard.release(K.M)],
    'n' : lambda : (keyboard)[keyboard.press(K.N), keyboard.release(K.N)],
    'o' : lambda : (keyboard)[keyboard.press(K.O), keyboard.release(K.O)],
    'p' : lambda : (keyboard)[keyboard.press(K.P), keyboard.release(K.P)],
    'q' : lambda : (keyboard)[keyboard.press(K.Q), keyboard.release(K.Q)],
    'r' : lambda : (keyboard)[keyboard.press(K.R), keyboard.release(K.R)],
    's' : lambda : (keyboard)[keyboard.press(K.S), keyboard.release(K.S)],
    't' : lambda : (keyboard)[keyboard.press(K.T), keyboard.release(K.T)],
    'u' : lambda : (keyboard)[keyboard.press(K.U), keyboard.release(K.U)],
    'v' : lambda : (keyboard)[keyboard.press(K.V), keyboard.release(K.V)],
    'w' : lambda : (keyboard)[keyboard.press(K.W), keyboard.release(K.W)],
    'x' : lambda : (keyboard)[keyboard.press(K.X), keyboard.release(K.X)],
    'y' : lambda : (keyboard)[keyboard.press(K.Y), keyboard.release(K.Y)],
    'z' : lambda : (keyboard)[keyboard.press(K.Z), keyboard.release(K.Z)],
    '{' : lambda : (keyboard)[keyboard.press(K.SHIFT), keyboard.press(K.LEFT_BRACKET), keyboard.release(K.LEFT_BRACKET), keyboard.release(K.SHIFT)],
    '|' : lambda : (keyboard)[keyboard.press(K.SHIFT), keyboard.press(K.BACKSLASH), keyboard.release(K.BACKSLASH), keyboard.release(K.SHIFT)],
    '}' : lambda : (keyboard)[keyboard.press(K.SHIFT), keyboard.press(K.RIGHT_BRACKET), keyboard.release(K.RIGHT_BRACKET), keyboard.release(K.SHIFT)],
    '~' : lambda : (keyboard)[keyboard.press(K.SHIFT), keyboard.press(K.GRAVE), keyboard.release(K.GRAVE), keyboard.release(K.SHIFT)]
}
        
class Keyboard:
    RC = 1
    CR = 2
    def __init__(self, direct=True):
        self.direct = direct
        
        self.rows = ()
        self.cols = ()
        
        self.pins = ()
        self.map = ()
        
        self.keyboard = Keyboard(usb_hid.devices)
        self.direction = None
        
    def setDirection(self, direction):
        self.direction = direction
        
    def pins(self, pins):
        if self.direct:
            self.pins = pins
        
        else:
            self.rows = pins[0]
            self.cols = pins[1]
            
    def setMap(self, map):
        self.map = map
    
    def click(self, keys, hold=None):
        if hold is not None:
            for holding in hold:
                self.keyboard.press(holding)
                
        for key in keys:
            try:
                self.keyboard.press(key)
                self.keyboard.release(key)

            except:
                pass

        if hold is not None:
            for holding in hold:
                self.keyboard.release(holding)
        
    def write(self, string, hold=None):
        if hold is not None:
            for holding in hold:
                self.keyboard.press(holding)
                
        for char in string:
            if char in chars:
                char(self.keyboard)
        
        if hold is not None:
            for holding in hold:
                self.keyboard.release(holding)
    
    def run(self):
        layer = 0
        lastAction = None
        lastTime = time.time()
        
        while True:
            if self.direct:
                
                for index, button in enumerate(self.pin):
                    if isinstance(self.map[index], LayerSwitch):
                        
                        if button.value:
                            layer = button.layer
                        
                        else:
                            layer = 0
                    
                    else:
                        if button.value:
                            fnc = self.map[index] if not layer else (self.map[index])[layer]
                    
                            if fnc == lastAction and time.time() - lastTime < 0.01:
                                continue
                            
                            if isinstance(fnc, str):
                                self.write(fnc)
                            
                            elif isinstance(fnc, K):
                                self.click(fnc)
                            
                            else:
                                try: fnc()
                                except: pass
                            
                            lastAction = fnc
                            lastTime = time.time()
                                
            elif self.direction == self.RC:
                index = 0
                
                for row in self.rows:
                    row.value = True
                    
                    for col in self.cols:
                        if col.value:
                            fnc = self.map[index] if not layer else (self.map[index])[layer]
                            
                            if fnc == lastAction and time.time() - lastTime < 0.01:
                                continue
                            
                            if isinstance(fnc, str):
                                self.write(fnc)
                            
                            elif isinstance(fnc, K):
                                self.click(fnc)
                            
                            else:
                                try: fnc()
                                except: pass
                            
                            lastAction = fnc
                            lastTime = time.time()
                        
                        index += 1
                    row.value = False
                    
            elif self.direction == self.CR:
                index = 0
                
                for col in self.cols:
                    col.value = True
                    
                    for row in self.rows:
                        if row.value:
                            fnc = self.map[index] if not layer else (self.map[index])[layer]
                            
                            if fnc == lastAction and time.time() - lastTime < 0.01:
                                continue
                            
                            if isinstance(fnc, str):
                                self.write(fnc)
                            
                            elif isinstance(fnc, K):
                                self.click(fnc)
                            
                            else:
                                try: fnc()
                                except: pass
                            
                            lastAction = fnc
                            lastTime = time.time()
                        
                        index += 1
                    col.value = False
