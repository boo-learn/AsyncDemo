import time


def sync_task(n):
    print(f"Задача {n} началась")
    time.sleep(2)  # Имитация долгой операции
    print(f"Задача {n} завершилась")


def sync_main():
    for i in range(3):
        sync_task(i)


start_time = time.time()
sync_main()
end_time = time.time()
print(f"Синхронное выполнение заняло: {end_time - start_time:.2f} секунд")
