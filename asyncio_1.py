import asyncio,time

'''
8/22/2020
The asyncio framework - python high performance

'''

# simple example

# loop = asyncio.get_event_loop()

# def callback():
#     print("hello world")
#     loop.stop()
    

# loop.call_later(5.0,callback)

# starting the loop
# loop.run_forever()


'''
one of the main problems with call backs is that they require us to break 
the program execution into small functions that will be invoked only 
when certain event takes place



Coroutines:
its a natural way to break up the program execution into chunks
you may think coroutine as function that can be stopped and resumed


'''

#--------------------------------------------------
# The below two codes behave similar

# def range_generators(n):
#     i=0
#     while i < n:
#         print("Generating Value {}".format(i))
#         yield i
#         i+=1


# generator = range_generators(3)
# print(generator)
# print(next(generator))




# async def hello():
#     print("hello world")

# coro=hello()


# loop=asyncio.get_event_loop()
# loop.run_until_complete(coro)

#-----------------------------------------


# async def wait_and_print(msg):
#     await asyncio.sleep(1)
#     print("Message: ",msg)
# loop.run_until_complete(wait_and_print("Hello world"))

loop=asyncio.get_event_loop()


# asynchronous network call
async def network_request(number):
    await asyncio.sleep(10.0)
    return {
        "success":True,
        "result":number**2
    }

async def fetch_square(number):
    response = await network_request(number)
    if response["success"]:
        print("Result is: {}".format(response["result"]))

# loop.run_until_complete(fetch_square(2))


'''
Running tasks using run_until_complete is 5n for testing and debugging

program will be started with loop.run_forever most of the times,
and we will need to submit our tasks while the loop is already running.

'''

asyncio.ensure_future(fetch_square(2))
asyncio.ensure_future(fetch_square(3))
asyncio.ensure_future(fetch_square(4))

# loop.run_forever()
