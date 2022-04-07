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
        if data >= 10000:
            data = str('{:.0e}'.format(data)).replace('e+0', 'e')
        data = str(data).replace('e-0', 'e-')
        pos = data.find('.')
        output = []
        if pos == -1:
            for element in data:
                if element in num:
                    #output.append(num[element])
                    self.i2cwrite(count[loc], num[element].to_bytes(1, 'big'))
                    loc += 1

        else:
            for element in data:
                if element in num:
                   output.append(num[element])
                   loc += 1
            output[pos-1] = output[pos-1]|0x80
            for i in range(4):
                self.i2cwrite(count[i], output[i].to_bytes(1,'big'))


    def reset(self):
        for i in count:
            self.i2cwrite(i, num[' '])

    #Dictionary and list to use
num = {' ':(b'\x00'),
        '0':(63),
        '1':(6),
        '2':(91),
        '3':(79),
        '4':(102),
        '5':(109),
        '6':(125),
        '7':(7),
        '8':(127),
        '9':(103),
        'E':(121),
        'e':(121),
        '-':(64)}

count = [0x34,0x35,0x36, 0x37]
