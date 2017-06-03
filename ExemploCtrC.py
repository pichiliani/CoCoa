import signal
import time
import sys




def handler(signum, frame):
    print('Here you go')
    sys.exit(0)

signal.signal(signal.SIGINT, handler)

time.sleep(10) # Press Ctrl+c here