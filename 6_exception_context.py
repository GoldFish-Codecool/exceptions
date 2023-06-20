import sys
import traceback

while True:
    try:
        value = int(input("Value: "))
    # except (KeyboardInterrupt, Exception):
    except (BaseException):
        print(f"TRACEBACK {traceback.format_exc()}")
        print("-----------------------------------------------")
        print(f"SYS {sys.exc_info()}")
        print("-----------------------------------------------")
