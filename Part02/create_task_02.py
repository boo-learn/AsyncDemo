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
    # Создание задач
    task1 = asyncio.create_task(my_coroutine(1))
    task2 = asyncio.create_task(my_coroutine(2))
    task3 = asyncio.create_task(my_coroutine(3))

    # Ожидание завершения задач и сбор результатов
    results = await asyncio.gather(task1, task2, task3)
    print("Результаты:", results)


# Корутины выполняются асинхронно, но результаты будут получены только когда все корутины отработают.
if __name__ == "__main__":
    asyncio.run(main())
