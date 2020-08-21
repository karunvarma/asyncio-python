from concurrent.futures import Future
import threading
import time


'''

Event loops
-----------

In many asynchronous frame works coordination between different tasks
is managed by the EVENT LOOP

the idea behind an event loop is to continuously  monitor the status of
the various resources like network connections,DB queries  and trigger 
the corresponding call backs when a particular event takes place


Waiting for events to happen by continuously polling using a loop
 is commonly termed as busy-waiting.

'''



# simple non blocking example taken from packtpub

class Timer:

    def __init__(self,timeout):
        self.timeout = timeout
        self.start = time.time()

    def done(self):
        return time.time() - self.start > self.timeout
    
    def on_timer_done(self,callback):
        self.callback=callback
        
timer = Timer(2.0)
timer.on_timer_done(lambda: print("Timer is done!"))

while True:
    if timer.done():
        Timer.callback()
        break
    else:
        print("continue other work!!")


'''

the main restriction of an event loop is since the flow of execution
is managed by a continuosly running the loop, that it never uses bloc
-king calls. if we use any blocking statement(time.sleep) inside the 
loop it causes the call back dispatching get blocked untill call is done.



To avoid this, rather than using a blocking call, such as timer.sleep,
we let the event loop detect and execute the call back when the resource
is ready. By not blocking the execution flow

The event loop is free to monitor multiple resources in a concurrent way


The Python standard libraries include a very convenient event loop-based
concurrency framework, asyncio

'''




