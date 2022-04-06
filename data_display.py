import LedSeg_class as LED
import busio
import board

i2c = busio.I2C(board.SCL, board.SDA)

data = 1e-5
seg = LED.Seg7(i2c)

seg.segset(b'\x41')
seg.readout(data)
