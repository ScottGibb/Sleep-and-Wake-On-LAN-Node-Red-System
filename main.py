"""
Simple TCP Server Script that keeps a TCP Server running in order for NodeRed to connect and put PC into sleep mode
"""

import logging
import os
import socket
import sys
import time
import pidfile

# Desktop Credentials
HOST = "192.168.0.101"
PORT = 60000
PROJECT_PATH = (
    "C:/Users/smgib_161/Documents/Projects/Sleep-and-Wake-On-LAN-Node-Red-System/"
)
MAX_ERRORS = 5
# Logger Setup
logger = logging.getLogger("SOL_Logger")
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler(PROJECT_PATH + "SOL.log")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
fh.setFormatter(formatter)
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)

try:
    with pidfile.PIDFile():
        logger.info('Starting Sleep on LAN Script')
except pidfile.AlreadyRunningError:
    logger.error('Sleep on LAN Script already running, Aborting!')
    sys.exit(-1)

error_count = 0
while True:
    if error_count > MAX_ERRORS:
        logger.error(f'Sleep on LAN Script reached max error count {MAX_ERRORS}')
        logger.error("System Exiting")
        sys.exit(-2)
    try:
        while True:
            logger.info("Looping Round and creating new socket")
            # Create a new Socket
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                logger.info(f"Attempting to bind on port {PORT}")
                sock.bind((HOST, PORT))
                logger.info(f"Binded on port {PORT}")
                logger.info(f"Attempting to listen on port {PORT}")
                error_count = 0
                sock.listen()
                logger.info("Listening on Port 60000")
                conn, addr = sock.accept()
                logger.info("Accepted Connection")
                sockFile = conn.makefile()

                # Decode Message and perform selected operation
                with sockFile:
                    message = sockFile.readline()
                    logger.debug(message.strip())
                    message = message.strip()
                    strings = message.split(":")
                    if (strings[0]) == "state":
                        if (strings[1]) == "off":
                            logger.info("Closing socket")
                            sock.close()
                            logger.info("Turning PC off")
                            os.system("rundll32.exe powrprof.dll,SetSuspendState  0,1,0")
                            # os.system("shutdown /s /t 0")
                    else:
                        logger.info("Closing socket")
                        sock.close()

    except Exception as e:
        logger.error(e)
    logger.warning("Python code has reached end of script, the code will no logner talk to Node-Red")
    logger.info(f"Attempting to restart loop! Error Number: {error_count}")
    error_count = error_count+1
