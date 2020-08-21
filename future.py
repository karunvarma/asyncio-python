from concurrent.futures import Future
import threading
import time


def network_request_async(number):

    # creating a future
    future=Future()

    # this is the respose we are getting from the network
    result={
        "success":True,
        "result":number**2
    }

    # creating a async call after 5 sec
    # after 5 sec we are setting the future result
    timer = threading.Timer(5.0, lambda: future.set_result(result))
    timer.start()

    # returning the future
    return future


def fetch_square(number):

    # making an async call which will return future 
    res_future=network_request_async(number)
    def on_done_future(future):
        response = future.result()
        if response["success"]:
            print("Result is :{}".format(response["result"]))

    # the call back will be called only after the future has result
    res_future.add_done_callback(on_done_future)


fetch_square(10)

for _ in range(5):
    time.sleep(2)
    print("doing work")

