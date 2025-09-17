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