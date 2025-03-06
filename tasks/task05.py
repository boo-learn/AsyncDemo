# TODO: Создайте корутину, которая ждет 5 секунд.
#  Запустите ее как задачу и отмените ее через 2 секунды.

import asyncio

async def long_task():
    print("Задача началась")
    await asyncio.sleep(5)
    print("Задача завершилась")

async def main():
    task = asyncio.create_task(long_task())
    await asyncio.sleep(2)
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("Задача была отменена")

asyncio.run(main())