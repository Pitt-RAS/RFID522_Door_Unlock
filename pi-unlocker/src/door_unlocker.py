#!/usr/bin/env python3

from serial_interface import SerialInterface

class DoorUnlocker(object):
    def __init__(self, port, baud):
        self._serial_interface = serial_in = SerialInterface(port, baud, serial_callback)

    def _serial_callback(self, data):
        print(data)
        if data == 'yay':
            self._serial_interface.send_unlock()
        else:
            self._serial_interface.send_failure()

if __name__ == '__main__':
    port = '/dev/cu.usbserial-A505026C'
    baud = 9600

    door_unlocker = DoorUnlocker(port, baud)
