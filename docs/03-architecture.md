# 3. Архитектура
CLI argparse -> операции над задачами -> сортировка order -> JSON load/save. Сущность Task: id, title, deadline, priority, done. Запись через временный файл и замену. Ключ сортировки: (done, deadline, -priority, id). ISO-даты сравниваются лексикографически.
