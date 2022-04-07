import LedSeg_class as LED
import busio
import board

i2c = busio.I2C(board.SCL, board.SDA)

data = 9999+1
seg = LED.Seg7(i2c)

seg.segset(b'\x41')
#seg.i2cwrite(0x34, b'\x86')
seg.readout(data)
