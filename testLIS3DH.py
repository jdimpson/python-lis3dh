#!/usr/bin/python

from LIS3DH import LIS3DH
from time import sleep


def clickcallback(channel):
    # interrupt handler callback
    print("Interrupt detected")
    click = sensor.getClick()
    print("Click detected (0x%2X)" % (click))
    if (click & 0x10):
        print(" single click")
    if (click & 0x20):
        print(" double click")


if __name__ == '__main__':
    testADC=True
    sensor = LIS3DH(debug=True,enableADC=testADC)
    sensor.setRange(LIS3DH.RANGE_2G)
    sensor.setClick(LIS3DH.CLK_DOUBLE, 200, mycallback=clickcallback)
    # second accelerometer
    # s2 = LIS3DH(address=0x19, debug=True)

    print("Starting stream")
    while True:

        x = sensor.getX()
        y = sensor.getY()
        z = sensor.getZ()
        if testADC:
            a = sensor.getChan1()
            b = sensor.getChan2()
            c = sensor.getChan3()

            print("\rX: %.6f\tY: %.6f\tZ: %.6f\t1: %.6f\t2: %.6f\t3: %.6f" % (x, y, z, a, b, c))
        else:
            print("\rX: %.6f\tY: %.6f\tZ: %.6f" % (x, y, z))
        sleep(0.1)

    # click sensor if polling & not using interrupt
    #        click = sensor.getClick()
    #        if (click & 0x30) :
    #            print "Click detected (0x%2X)" % (click)
    #            if (click & 0x10): print " single click"
#            if (click & 0x20): print " double click"
