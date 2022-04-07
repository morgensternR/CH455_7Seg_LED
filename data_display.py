import LedSeg_class as LED
import busio
import board
import time

i2c = busio.I2C(board.SCL, board.SDA)

seg = LED.Seg7(i2c)
seg.segset(b'\x41')
List = [x * 0.01 for x in range(0, 1000)]

for i in List:
    seg.readout(i)
    time.sleep(0.1)


