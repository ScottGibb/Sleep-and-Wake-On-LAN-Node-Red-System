"""
Simple TCP Server Script that keeps a TCP Server running in order for NodeRed to connect and put PC into sleep mode
"""
import logging
import os
import socket

# Desktop Credentials
HOST = '192.168.0.101'
PORT = 60000
PROJECT_PATH = 'C:/Users/smgib_161/Documents/Projects/Sleep-and-Wake-On-LAN-Node-Red-System/'
#Logger Setup
logger = logging.getLogger('SOL_Logger')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler(PROJECT_PATH + "SOL.log")
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)

# Run Continuously
while True:
    logger.info("Looping Round and creating new socket")
    # Create a new Socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

        sock.bind((HOST, PORT))
        sock.listen()
        logger.info("Listening on Port 60000")
        conn, addr = sock.accept()
        logger.info("Accepted Connection")
        sockFile = conn.makefile()

        # Decode Message and perform selected operation
        with sockFile:
            message = sockFile.readline()
            logger.debug(message)
            message = message.strip()
            strings = message.split(':')
            if (strings[0]) == "state":
                if (strings[1]) == "off":
                    logger.info("Putting System to sleep")
                    os.system("rundll32.exe powrprof.dll,SetSuspendState  0,1,0")  # Puts PC in Sleep Mode
    logger.info("Closing socket")
    sock.close()
