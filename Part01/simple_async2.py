import time
import asyncio


async def async_task(n, delay):
    print(f"Задача {n} началась")
    await asyncio.sleep(delay)  # Имитация долгой операции
    print(f"Задача {n} завершилась")


async def main():
    # Запускаем три корутины асинхронно
    await asyncio.gather(async_task(1, 2), async_task(2, 1), async_task(3, 1.5))
    print("Готово!")


if __name__ == "__main__":
    asyncio.run(main())
