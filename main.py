import urllib
import urllib2
import json


def get_response(inn):
    url = "https://egrul.nalog.ru/"
    data = urllib.urlencode({"query": inn})
    headers = {"Content-Type": "application/x-www-form-urlencoded"}

    request = urllib2.Request(url, data, headers)

    try:
        response = urllib2.urlopen(request)
        result = response.read()
        return result
    except urllib2.HTTPError as e:
        return "Ошибка HTTP: " + str(e.code)
    except urllib2.URLError:
        return "Ошибка сети"


def get_company_info(inn):
    url = "https://egrul.nalog.ru/"

    # Отправляем запрос с ИНН
    data = urllib.urlencode({"query": inn})
    headers = {"Content-Type": "application/x-www-form-urlencoded"}

    request = urllib2.Request(url, data, headers)
    response = urllib2.urlopen(request)
    result = json.loads(response.read())

    # Получаем task ID
    task_id = result.get("t")
    if not task_id:
        return "Не удалось получить task ID"



    # Запрашиваем результат по правильному URL
    result_url = "https://egrul.nalog.ru/search-result/" + task_id

    response = urllib2.urlopen(result_url)
    company_data = json.loads(response.read())

    return company_data


# 🔥 Введи ИНН компании:
inn = "110506802086"
data = get_company_info(inn)
print(json.dumps(data, indent=4, ensure_ascii=False))
