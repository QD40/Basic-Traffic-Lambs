import time

def red():
    print("Currently Active Light: Red")
    timer = 10
    while timer > 0:
        print("Time Left: ", timer)
        time.sleep(1)
        timer -= 1

def yellow():
    print("Currently Active Light: Yellow")
    timer = 3
    while timer > 0:
        print("Time Left: ", timer)
        time.sleep(1)
        timer -= 1

def green():
    print("Currently Active Light: Green")
    timer = 10
    while timer > 0:
        print("Time Left: ", timer)
        time.sleep(1)
        timer -= 1

while True:
    green()
    yellow()
    red()
    yellow()