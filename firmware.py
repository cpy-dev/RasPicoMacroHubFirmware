import board
import usb_hid
import digitalio
import analogio
from adafruit_hid.keybaord import Keyboard
from adafruit_hid.keycode import Keycode

class LayerSwitch:
    def __init__(self, layerIndex):
        self.layer = layerIndex

def write(string, hold=None):
    
        
class Keyboard:
    def __init__(self, direct=True):
        self.direct = direct
        self.rows = []
        self.cols = []
        self.pins = []
        self.map = []
        self.keyboard = Keyboard(usb_hid.devices)
        
    def pins(self, pins):
        if self.direct:
            self.pins = pins
        else:
            self.rows = pins[0]
            self.cols = pins[1]
            
    def setMap(self, map):
        self.map = map
        
    def run(self):
        while True:
            if self.direct:
                for index, button in enumerate(self.pin):
                    if button.value:
                        fnc = self.map[index]
                        fmc()
         
        
