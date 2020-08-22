import asyncio,random
from threading import current_thread
from threading import Thread


async def do_something(sleep_for):
    print(" event loop running in  {0} = {1}  will sleep for {2}".format
    (
            current_thread().getName(),
            asyncio.get_event_loop().is_running(),
            sleep_for
    ))

    await asyncio.sleep(sleep_for)

def launch_event_loops():

    # get a new event loop
    loop = asyncio.new_event_loop()


    # set the event loop for the current thread
    asyncio.set_event_loop(loop)


    # running the co routine in the event loops and its a blocking call
    loop.run_until_complete(
        do_something(random.randint(1,5))
    )


    # closing the event loop
    loop.close()







t1=Thread(target=launch_event_loops)
t2=Thread(target=launch_event_loops)

t1.start()
t2.start()

print("Is event loop running in thread {0} = {1}\n".format(current_thread().getName(),
                                                         asyncio.get_event_loop().is_running()))
 
