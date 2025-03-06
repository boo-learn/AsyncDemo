import asyncio


async def my_coroutine(n):
    await asyncio.sleep(1)
    print(f"Корутина {n} завершилась")
    return f"Результат {n}"


async def main():
    task = asyncio.create_task(my_coroutine(1))
    task.cancel()
    print(f"Задача отменена: {task.cancelled()}")  # True
    try:
        await task
    except asyncio.CancelledError:
        print("Задача была отменена")


# Отмена задачи
asyncio.run(main())
