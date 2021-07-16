import time
import logging

def main():
    print('from inside the mina of logger mount volume')
    logging.basicConfig(filename="app_logs/my_logs.log", level=logging.DEBUG)

    start_time = time.time()
    logging.debug("Program starts running at %d", start_time)


main()