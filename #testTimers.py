#testTimers
import threading
import time



class ResettableTimer:
    def __init__(self, interval, callback):
        self.interval = interval
        self.callback = callback
        self.timer = None
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = True
        self.timer = threading.Timer(self.interval, self._callback_wrapper)
        self.timer.start()

    def _callback_wrapper(self):
        self.is_running = False
        self.callback()

    def start(self):
        if not self.is_running:
            self._run()

    def stop(self):
        if self.is_running:
            self.timer.cancel()
            self.is_running = False

    def reset(self):
        self.stop()
        self.start()
total =0
num =0
def left_on():
    global total
    total = total +1
def left_off():
    global total
    total = total +1
def right_on():
    global total
    total = total +1
def right_off():
    global total
    total = total +1

    
# Create a Timer object that expires after 1 second
l_on = ResettableTimer(1, left_on)
l_off = ResettableTimer(2, left_off)
r_on = ResettableTimer(1, right_on)
r_off = ResettableTimer(2, right_off)

l_on.start()
l_off.start()
r_on.start()
r_off.start()
while(num < 700):
        time.sleep(3)
        l_on.reset()
        l_off.reset()
        r_on.reset()
        r_off.reset()
        num+=1
        print(total)
l_on.stop()
l_off.stop()
r_on.stop()
r_off.stop()