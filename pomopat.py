import time
import os

FOCUS_TIME = 25
REST_TIME = 5
REST_LONG_TIME = 10
MINUTES = 60

def focus_time(minutes=1):
    message=f"Focus {minutes} minutes."
    os.system("say " + message)
    for i in range(1,minutes+1):
        print(f"Focus: {i} minutes")
        time.sleep(MINUTES * 1)

def rest_time(minutes=1,loops=1):
    if loops == 4:
        minutes = minutes + REST_LONG_TIME

    message=f"Take a rest {minutes} minutes."
    os.system("say " + message)
    
    for i in range(1, minutes+1):
        print(f"Rest: {i} minutes")
        time.sleep(MINUTES * 1)

def main():
  for loop in range(1,5):
      focus_time(FOCUS_TIME)
      rest_time(minutes=REST_TIME,loops=loop)


if __name__ == '__main__':
    os.system("say Hi, I'm pomo pat, I'm working only on Mac")
    while True:
        main()