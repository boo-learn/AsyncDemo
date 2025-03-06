import asyncio


async def hello():
    print("Привет!")
    await asyncio.sleep(2)  # иди дальше, я посплю 2 секунды
    print("Пока!")


# Корутина - не сама функция, а то, что возвращается функция с await
print(type(hello()))
