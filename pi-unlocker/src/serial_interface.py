#!/usr/bin/env python3
import threading
import serial
import time

class SerialInterface(object):
    def __init__(self, port, baud, read_callback, timeOut=5):
        self._read_callback = read_callback
        self._lock = threading.RLock()

        try:
            self._ser = serial.Serial(port, baud, timeout=timeOut)
        except Exception as e:
            print('ERROR OPENING SERIAL PORT')
            print(e)
            raise

        thread = threading.Thread(target=self._read_from_port)
        thread.start()

    def send_unlock(self):
        with self._lock:
            self._ser.write('true')

    def send_failure(self):
        with self._lock:
            self._ser.write('false')

    def _read_from_port(self):
        time.sleep(2) # sleep on startup
        while True:
            with self._lock:
                reading = self._ser.readline()
            self._read_callback(reading)

