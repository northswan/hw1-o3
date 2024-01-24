# Домашнее задание № 1
## Чтение и запись файл, первичная обработка

Задание посвящено работе с данными содержания озона в атмосфере Земли за несколько десятилетий.
Вам нужно проанализировать данные в формате [NetCDF](https://ru.wikipedia.org/wiki/NetCDF), нарисовать график и вывести статистическую информацию в файл формата [JSON](https://ru.wikipedia.org/wiki/JSON).
Программа должна быть представлена в файле `ozon.py`, график в файле `ozon.png` и выходные результаты в файле `ozon.json`. Файл с исходными данными в репозиторий класть ненужно.

**Дедлайн 08 февраля 2024 в 23:55**

Вы должны сделать следующее:
- Загрузить файл с данными: <https://d1qb6yzwaaq4he.cloudfront.net/protocols/o3field/msr2/MSR-2.nc> (524 МБ). Не кладите файл в репозиторий, он очень большой. Информацию о данных смотрите на сайте <http://www.temis.nl/protocols/O3global.php>. По временной шкале данные начинаются с января 1979 года.
- В файле `ozon.py` находится заготовка программы, принимающей в качестве аргументов командной строки географические долготу и широту в градусах. Например для Москвы:
  ```bash
  > python3 ozon.py 37.66 55.77
  37.66 55.77
  ```
  > Для задания аргументов командной строки в Spyder используйте меню "Запуск" -> "Настройки для файла..." (`Ctrl+F6`) -> "Опции командной строки"

  Нужно модифицировать код `ozon.py` таким образом, чтобы для заданных пользователем долготы и широты программа извлекала из файла `MSR-2.nc` требуемые данные и рассчитывала:

  * максимальное, минимальное и среднее содержание озона;
  * максимальное, минимальное и среднее содержание озона среди январей всех лет;
  * максимальное, минимальное и среднее содержание озона среди июлей всех лет.

  Рассчитанные метрики следует сохранить в файле `ozon.json` придерживаясь следующего примера формата:
  ```json
  {
    "coordinates": [37.66, 55.77],
    "jan": {
      "min": 293.0,
      "max": 382.0,
      "mean": 344.5
    },
    "jul": {
      "min": 297.0,
      "max": 344.0,
      "mean": 323.7
    },
    "all": {
      "min": 264.0,
      "max": 431.0,
      "mean": 333.4
    }
  }
  ```

  Одновременно с этим, для заданных пользователем долготы и широты программа должна сохранять файл `ozon.png` с одним графиком, на котором разными цветами приведены зависимости:

  * зависимость содержания озона от времени для всего доступного интревала;
  * зависимость содержания озона от времени для всех январей;
  * зависимость содержания озона от времени для всех июлей.

  Цвета и оформление графика остаются на ваше усмотрение, но график должен быть понятным (не забудьте подписать оси).

  Программа `ozon.py` должна корректно работать для любых географических координат, а не только для географических координат из примера.

- *Задание со звёздочкой (на бонусные баллы)*. Используйте пакет [geopy](https://pypi.org/project/geopy/), и модифицируйте программу `ozon.py` таким образом, чтобы она одновременно поддерживала два варианта задания аргументов командной строки:
  * координатный
    ```bash
    > python3 ozon.py 37.66 55.77
    ```
  * текстовый
    ```bash
    > python3 ozon.py "Europe/Moscow"
    ```
    В этом случае следует определить географические координаты для заданного названия с помощью пакета `geopy`.
