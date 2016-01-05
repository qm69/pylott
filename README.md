## pylott Состоит из двух блоков `scrapper` и `tabler`
#### scrapper.py
  - идет в папку `modules`
  - перебирает каждую подпапку `if not dr.startswith('__')`
  - в ней запускает файл `main.py`
  - в файл `main.py` запускается функция `main()`
    который можно запустить вручную из Sublime

## To-do
#### tabler.py
  - [ ] описать функционал 'termtable.py' в 'README.md'
  - [ ] decima добавить номера к повторам шаров

#### modules
  - [x] New York время тиража не добавляет
  - [ ] Автоматически выводить название лотереи
  - [ ] Belgium Pick 3 пропускает тиражи
  - [ ] California не добавляет время тиража
  - [ ] 'librs >> printer >> print_save()' добавить дату
  - [ ] Belgium >> main.py >> 'Up to date' don't work

#### scraper.py

Lottery Data 
====================================================
Нью-Йорк
  - Numbers » 10:00 [20:24] & 02:00 [15:35] (МарафрнБет)
    "nylottery.ny.gov/wps/portal/Home/Lottery/Home/Daily+Games/NUMBERS"
  - Win 4   » 19:20 [20:24] & 02:30 [15:35]
    "nylottery.ny.gov/wps/portal/Home/Lottery/Home/Daily+Games/WIN+4"

==================  Done  =======================
Украина
  - Тройка » 19:30 GMT 20:00 [23:00 +3:00]
    "lottery.com.ua/uk/lottery/loto3/results.htm"
  - Кено   » 19:30 GMT 20:00 [23:00 +3:00]
    "lottery.com.ua/uk/lottery/loto3/results.htm"
Бельгия
  - Pick 3 » 19:45 [~21:30] aka "lotteryextreme.com/belgium"
    "nationale-loterij.be/nl/onze-spelen/pick-3/resultaten"
  - Keno » 19:45 [~21:30]
    "nationale-loterij.be/nl/onze-spelen/keno/resultaten"
Зеландия
  - Play 3 » 18:00 GMT +12 08:30 [<09:30]
    "mylotto.co.nz/index.php/play3/results/"
Флорида
  - Cash 3 » 20:29 [!21:30] & 02:31 [03:57]
    "flalottery.com/cash3.do"
  - Play 4 » 20:30 [21:30] & 02:29 [03:57]
    "Smth link"
Калифорния Pacific Time -8/-7
  - Daily 3 » 21:45 [<00:36] & 04:30 [07:30] 1:00pm and 6:30pm 
    "http://www.calottery.com/play/draw-games/daily-3"
  - Daily 4 » 04:30 [07:30]
    "calottery.com/play/draw-games/daily-4"
==================  МарафрнБет  =======================
Онтарио
  - Pick 3 » 20:55 & 01:55 (МарафрнБет)
    ???"lotterycanada.com/ontario-pick-3"