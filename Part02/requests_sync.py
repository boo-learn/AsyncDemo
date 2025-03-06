import requests #  pip install requests
import time


def fetch(url):
    """Синхронно получает содержимое URL."""
    response = requests.get(url)
    return response.text


def main(urls):
    """Главная функция для выполнения синхронных запросов."""
    results = []
    for url in urls:
        results.append(fetch(url))
    return results


if __name__ == "__main__":
    urls = [
        "https://www.python.org",
        "https://www.example.com",
        "https://www.google.com",
    ]

    start_time = time.time()
    results = main(urls)
    end_time = time.time()

    for result in results:
        print(f"Получено {len(result)} байт")

    print(f"Время выполнения: {end_time - start_time:.2f} секунд")
