import asyncio
import random


async def my_coroutine(n):
    """Простая корутина, имитирующая выполнение задачи."""
    print(f"Корутина {n} началась")
    delay = random.uniform(1, 4)
    await asyncio.sleep(delay)  # Имитация долгой операции
    print(f"Корутина {n} завершилась")
    return f"Результат {n} за {delay} секунд"


async def main():
    """Пример использования asyncio.as_completed()."""
    tasks = [asyncio.create_task(my_coroutine(i)) for i in range(4)]
    for completed_task in asyncio.as_completed(tasks):
        result = await completed_task
        print(f"Получен результат: {result}")


# Корутины выполняются асинхронно, результаты доступны сразу, по завершению каждой корутины.
if __name__ == "__main__":
    asyncio.run(main())
