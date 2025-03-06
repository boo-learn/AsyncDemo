import time
import asyncio


async def async_task(n):
    print(f"Задача {n} началась")
    await asyncio.sleep(2)  # Имитация долгой операции
    print(f"Задача {n} завершилась")


async def main():
    # Запускаем три корутины асинхронно
    await asyncio.gather(async_task(1), async_task(2), async_task(3))
    print("Готово!")


# TODO: назовите все корутины в примере
# TODO: что будет, если в асинхронной async_task() использовать синхронный time.sleep(2)?

if __name__ == "__main__":
    asyncio.run(main())
