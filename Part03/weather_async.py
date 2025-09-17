import httpx
from fastapi import FastAPI, HTTPException

app = FastAPI()

WEATHER_API_URL = "https://api.weatherapi.com/v1/current.json"
WEATHER_API_KEY = "3f8bdfd3640f403288b223052250603"  # Замените на свой API-ключ


async def get_weather(city: str):
    """Получает данные о погоде из внешнего API."""
    params = {"key": WEATHER_API_KEY, "q": city}
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(WEATHER_API_URL, params=params)
            response.raise_for_status()  # Вызывает исключение для кодов ошибок 4xx и 5xx
            return response.json()
        except httpx.HTTPError as e:
            raise HTTPException(status_code=e.response.status_code if e.response is not None else 500, detail=str(e)) #Транслируем код ошибки внешнего API и сообщение


@app.get("/weather/{city}")
async def read_weather(city: str):
    """Маршрут для получения погоды по названию города."""
    weather_data = await get_weather(city)
    return weather_data


# TODO-1: сервис api.weatherapi.com отправляет слишком много данных.
#  измените код weather_async.py, так чтобы наше API возвращало JSON только с ключами:
#  "name" "region" "country" "temp_c" "feelslike_c"
#  используйте модель Pydantic для конвертации данных

# TODO-2: доработайте код так, чтобы при запросе на несуществующий город, ваше API возвращало 404


# TODO-3: сервис https://www.cbr-xml-daily.ru/daily_json.js (не требует api-key)
#  возвращает курсы валют на текущую дату
#  создайте handler для proxy-api, который будет возвращать только курс ЕВРО с параметрами:
#  "CharCode" "Name" "Value"