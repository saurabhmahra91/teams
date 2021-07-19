import asyncio
# ---------------------------------------------

async def main():
    print("A")
    await asyncio.sleep(1)
    print("B")

async def other_func():
    print("1")
    await asyncio.sleep(2)
    print("2")

asyncio.run(main())

# what we want tp achieve is that 
# call main()
# print A
# call the other function
# print the other function call
# print 1
# while the other function is sleeping, get back to the main function
# execute remaining part of main while other function is sleeping say
# execute print B earlier if the other func was still sleeping
# once the other func's sleep has been completed, do the remaining part of this function, namely
# print 2
# below is how do we achive the same
#--------------------------------------------PG1


# ----------------------------------------------
# Implementation 1
async def main():
    print("A")
    task = asyncio.create_task(other_func())
    print("B")

async def other_func():
    print("1")
    await asyncio.sleep(2)
    print("2")

asyncio.run(main())

# prints A
# calls other function
# prints 1
# other function is sleeping, get back to original function
# prints B 
# main function ended, so program is completed other func gets only half completed
# ----------------------------------------------------PG2


# ----------------------------------------------
# Implementation 2
async def main():
    print("A")
    task = asyncio.create_task(other_func())
    print("B")
    await task

async def other_func():
    print("1")
    await asyncio.sleep(2)
    print("2")

asyncio.run(main())

# prints A
# calls other function
# prints 1
# other function is sleeping, get back to original function
# prints B 
# now we are awaiting for the other func to complete
# other func prints 2
# await completed 
# main func ended -> program finished
# ----------------------------------------------------PG3



# -------------------------------------------------------
# how can one do synchronus programming in asynchronus function 
# async def main():
#     print("A")
#     await other_func()
#     print("B")

# async def other_func():
#     print("1")
#     await asyncio.sleep(2)
#     print("2")

# asyncio.run(main())
# --------------------------------------------------------PG4