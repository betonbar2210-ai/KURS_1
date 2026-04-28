from datetime import datetime
def greeting(date_time):
    date = datetime.fromisoformat(date_time)
    time_now = int(date.strftime('%H'))
    print(time_now)
    if 6 <= time_now < 12:
        return "Доброе утро"
    elif 12 <= time_now < 18:
        return "Добрый день"
    elif 18 <= time_now < 23:
        return "Добрый вечер"
    else:
        return "Доброй ночи"
date_time = '2026-04-27 00:51:00.177445'
w = greeting(date_time)
if __name__ == '__main__':
    print(w)