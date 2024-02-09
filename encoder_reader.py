import micropython
import pyb
import utime
class Encoder:
    """! 
    This class implements a motor driver for an ME405 kit. 
    """

    def __init__ (self, pin1, pin2, timer):
        """! 
        Creates a motor driver by initializing GPIO
        pins, setting up timer channels to read encoder values.
        @param en_pin (There will be several parameters)
        """
        self.pin1 = pin1
        self.pin2 = pin2
        self.timer = timer
        self.ch1 = self.timer.channel(1, pyb.Timer.ENC_AB, pin=self.pin1)
        self.ch2 = self.timer.channel(2, pyb.Timer.ENC_AB, pin=self.pin2)
        print("Creating encoder")
        self.timer.counter(0)
        self.pos = self.timer.counter()

    def read(self):
        """!
        This method sets the duty cycle to be sent
        to the motor to the given level. Positive values
        cause torque in one direction, negative values
        in the opposite direction.
        @param level A signed integer holding the duty
               cycle of the voltage sent to the motor 
        """
        AR = 65535
        new_count = self.timer.counter()
        prev_count = self.pos()
        delta = new_count-prev_count
        overflow = (AR+1)/2
        if delta >= overflow:
            delta -= overflow
        elif delta <= -overflow:
            delta += overflow
        else
            pass
        self.pos += delta
        return self.pos
        
    
    def zero(self):
        self.timer.counter(0)
        self.pos = self.timer.counter()

if __name__ == "__main__":
    pin1 = pyb.Pin(pyb.Pin.board.PC6, pyb.Pin.IN)
    pin2 = pyb.Pin(pyb.Pin.board.PC7, pyb.Pin.IN)
    timer = pyb.Timer(8, freq=20000)
    encoder = Encoder(pin1, pin2, timer)
    while(True):
        print(encoder.read())
        utime.sleep_ms(100)
    


