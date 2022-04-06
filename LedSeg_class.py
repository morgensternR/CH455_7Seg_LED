#7 Segment display
class Seg7:
    def __init__(self, i2c = None ):
        if i2c == None:
            i2c = busio.I2C(board.SCL1, board.SDA1)
        self.i2c = i2c

    def i2cwrite(self, addr, cmd):
        try:
            self.i2c.try_lock()
            self.i2c.writeto(addr, cmd)
            self.i2c.unlock()
        except:
            print("err line 14")
            self.i2c.unlock()

    def segset(self, cmd):
        try:
            if type(cmd) != bytes:
                print("Error command must be in bytes\n")
                print("0[INTENS][7SEG][SLEEP]0[ENA]B\n")
                print("0 000 0 0 0 0")
                return
            self.i2cwrite(0x24, cmd)
        except:
            print("err line 26")
            self.i2c.unlock()

    def readout(self, data):
        self.reset()
        loc = 0
        data = str(data).replace('e-0', 'e-')
        for element in data:
            if element in num:
                self.i2cwrite(count[loc] , num[element])
                loc += 1
    def reset(self):
        for i in count:
            self.i2cwrite(i, num[' '])
    #Dictionary and list to use
num = {' ':(b'\x00'),
        '0':(b'\x3f'),
        '1':(b'\x06'),
        '2':(b'\x5b'),
        '3':(b'\x4f'),
        '4':(b'\x66'),
        '5':(b'\x6d'),
        '6':(b'\x7d'),
        '7':(b'\x07'),
        '8':(b'\x7f'),
        '9':(b'\x67'),
        'E':(b'\x79'),
        'e':(b'\x79'),
        '.':(b'\x80'),
        '-': (b'\x40')}

count = [0x34,0x35,0x36, 0x37]
