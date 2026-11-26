# Deadline Planner
Учебный проект: планировщик приоритизации задач по срокам. Python 3.10+, без сторонних библиотек.

```bash
python planner.py add "Подготовить отчёт" 2026-12-01 --priority 3
python planner.py list
python planner.py done 1
python -m unittest discover -s tests -v
```
Незавершённые задачи идут первыми, затем по возрастанию срока, убыванию приоритета (3 — высокий) и ID. Просроченные отмечаются OVERDUE. Данные локально в tasks.json.
