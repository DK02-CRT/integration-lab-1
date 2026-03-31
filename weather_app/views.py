from django.shortcuts import render
import requests
weather_codes = {
    (0,): "czyste niebo",
    (1,): "głównie bezchmurnie",
    (2,): "częściowo pochmurno",
    (3,): "pochmurno",
    (45,): "mgła",
    (48,): "opadająca mgła szronowa",
    (51,): "mżawka lekka",
    (53,): "mżawka umiarkowana",
    (55,): "mżawka gęsta",
    (56,): "zamrażająca mżawka: lekka",
    (57,): "zamrażająca mżawka: gęsta intensywność",
    (61,): "deszcz słaby",
    (63,): "deszcz umiarkowany",
    (65,): "deszcz intensywny",
    (66,): "marznący deszcz: intensywność lekka",
    (67,): "marznący deszcz: intensywność ciężka",
    (71,): "opady śniegu: intensywność niewielka",
    (73,): "opady śniegu: intensywność umiarkowana",
    (75,): "opady śniegu: intensywność duża",
    (77,): "ziarna śniegu",
    (80,): "przelotne opady deszczu: słabe",
    (81,): "przelotne opady deszczu: umiarkowane",
    (82,): "przelotne opady deszczu: gwałtowne",
    (85,): "opady śniegu lekkie",
    (86,): "opady śniegu intensywne",
    (95,): "burza: Słaba lub umiarkowana",
    (96,): "burza z lekkim gradem",
    (99,): "burza z silnym gradem",
}
coordinates = {
    "Gowino": ("54.57", "18.20"),
    "Gdynia": ("54.52", "18.53"),
    "Warszawa": ("52.237", "21.017"),
    "Tokyo": ("35.65", "139.84")
}
def weather_view(request):
    place = "Gdynia"
    weather_url = (f"https://api.open-meteo.com/v1/forecast"
                   f"?latitude={coordinates[place][0]}&longitude={coordinates[place][1]}"
                   f"&hourly=temperature_2m,rain,weather_code,wind_speed_10m")
    response = requests.get(weather_url)
    data = response.json()
    temperature = data["hourly"]["temperature_2m"][0]
    wind = data["hourly"]["wind_speed_10m"][0]


    return render(request, "weather_app/weather.html", {
        "place": place,
        "temperature": temperature,
        "wind": wind
    })