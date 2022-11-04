import requests
city = "Moscow,RU"
appid = "812556ece7acd4a4a8167b62bbba7b97"
res = requests.get("http://api.openweathermap.org/data/2.5/forecast",params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print("Прогноз погоды на неделю:")
for i in data['list']:
    print("Дата <", i['dt_txt'], "> \r\nТемпература <",i['main']['temp'], "> \r\nПогодные условия <",i['weather'][0]['description'], ">" "\r\nСкорость ветра <", i["wind"]["speed"],"> \r\nВидимость <",i["visibility"], ">")
    print("_____________________")
