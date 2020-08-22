import asyncio
from asyncio import Future
 
 
async def bar(future):
    print("bar will sleep for 3 seconds")
    await asyncio.sleep(3)
    print("bar resolving the future")
    future.done()
    future.set_result("future is resolved")
    print("--------------------------------")
 
 
async def foo(future):
    print("foo will await the future")
    await future
    print("foo finds the future resolved")
 
 
async def main():
    future = Future()
    results = await asyncio.gather(foo(future), bar(future))
 
 
if __name__ == "__main__":
    asyncio.run(main())
    print("main exiting")
