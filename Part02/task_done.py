import asyncio


async def my_coroutine(n):
    await asyncio.sleep(1)
    print(f"Корутина {n} завершилась")
    return f"Результат {n}"


async def main():
    task = asyncio.create_task(my_coroutine(1))
    print(f"Задача выполнена до await: {task.done()}")  # False
    await task
    print(f"Задача выполнена после await: {task.done()}")  # True


# Проверка выполнена ли задача
asyncio.run(main())
