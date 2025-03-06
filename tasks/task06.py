# TODO: Напишите асинхронную программу, которая отправляет HTTP-запросы к трём различным веб-сайтам:
#  "https://www.yandex.com", "https://www.google.com" и "https://www.python.org".
#  Как только от одного из сайтов будет получен ответ,
#  необходимо отменить выполнение запросов к остальным сайтам
#  и вывести время, затраченное на получение первого ответа.

import asyncio
import aiohttp
import time


async def fetch(session, url, task):
    """Асинхронно получает содержимое URL."""
    try:
        start_time = time.time()
        response = await session.get(url)
        try:
            await response.text()  # Получаем содержимое, чтобы вызвать ответ
            end_time = time.time()
            return url, end_time - start_time
        finally:
            response.close()
    except asyncio.CancelledError:
        return None, None


async def main():
    """Главная функция для выполнения асинхронных запросов."""
    urls = [
        "https://www.yandex.com",
        "https://www.google.com",
        "https://www.python.org",
    ]

    session = aiohttp.ClientSession()
    try:
        tasks = [asyncio.create_task(fetch(session, url, task)) for url, task in zip(urls, range(len(urls)))]

        done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

        for task in pending:
            task.cancel()

        first_result = done.pop().result()

        if first_result[0]:
            print(f"Первый ответ получен от {first_result[0]} за {first_result[1]:.2f} секунд")
        else:
            print("Все задачи были отменены до получения ответа")
    finally:
        await session.close()


if __name__ == "__main__":
    asyncio.run(main())
