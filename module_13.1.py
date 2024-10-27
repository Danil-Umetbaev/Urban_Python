import asyncio

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнование')
    for number in range(1, 6):
        print(f'Силач {name} поднял {number}')
        await asyncio.sleep(1/power)
    print(f'Силач {name} закончил соревнование')

async def start_tournament():
    print("ДА НАЧНЁТСЯ СОРЕВНОВАНИЕ")
    task1 = asyncio.create_task(start_strongman('Ruki-bazuki', 1))
    task2 = asyncio.create_task(start_strongman('Ahiles', 5))
    task3 = asyncio.create_task(start_strongman('Zeus', 100))
    await task1
    await task2
    await task3
    print("Соревнование закончилось")

asyncio.run(start_tournament())
