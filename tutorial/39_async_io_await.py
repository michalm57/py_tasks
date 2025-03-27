import asyncio
import time

async def brewCoffe():
    print("Start brewCoffee()")
    await asyncio.sleep(3)
    print("End brewCoffee()")
    return "Coffe ready"

async def toastBagel():
    print("toastBagel()")
    await asyncio.sleep(2)
    print("End toastBagel")
    return "Bagel toasted"

async def main():
    start_time = time.time()
    
    # result_coffee = brewCoffe()
    # result_bagel = toastBagel()
    
    # batch = asyncio.gather(brewCoffe(), toastBagel())
    # result_coffee, result_bagel = await batch
    
    coffee_task = asyncio.create_task(brewCoffe())
    toast_task = asyncio.create_task(toastBagel())
    
    result_coffee = await coffee_task
    result_bagel = await coffee_task

    end_time = time.time()
    elapsed_time = end_time - start_time
    
    print(f"Result of brewCoffee: {result_coffee}")
    print(f"Result of toastBagel: {result_bagel}")
    print(f"Total execution time: {elapsed_time}")
    
if __name__ == "__main__":
    asyncio.run(main())