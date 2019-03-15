'''
Created on 15.03.2019

@author: synatree
'''

from PyTrinamic.connections.serial_tmcl_interface import serial_tmcl_interface
import zerorpc
    
class zerorpc_serial_bridge(serial_tmcl_interface):
    server = None
    def __init__(self, comPort, baudrate=115200, bindString="tcp://127.0.0.1:4242"):
        super(comPort,baudrate)
        
        if not self.server:
            self.server = zerorpc.Server(self)
            self.server.bind(bindString)
            self.server.run()