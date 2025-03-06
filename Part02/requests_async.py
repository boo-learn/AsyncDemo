import asyncio
import aiohttp
import time


async def fetch(session, url):
    """Асинхронно получает содержимое URL."""
    response = await session.get(url)
    try:
        return await response.text()
    finally:
        response.close()


async def main(urls):
    """Главная функция для выполнения асинхронных запросов."""
    session = aiohttp.ClientSession()
    try:
        tasks = [fetch(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        return results
    finally:
        await session.close()


if __name__ == "__main__":
    urls = [
        "https://www.python.org",
        "https://www.example.com",
        "https://www.google.com",
    ]

    start_time = time.time()
    results = asyncio.run(main(urls))
    end_time = time.time()

    for result in results:
        print(f"Получено {len(result)} байт")

    print(f"Время выполнения: {end_time - start_time:.2f} секунд")
