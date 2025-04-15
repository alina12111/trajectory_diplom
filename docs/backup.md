
# 💾 Інструкція з резервного копіювання

Проєкт не використовує базу даних, але можна резервувати:

## 1. Копіювання всього каталогу
```bash
tar -czf trajectory_backup_$(date +%F).tar.gz trajectory_diplom
```

## 2. Копіювання тільки конфігів та логів
```bash
tar -czf configs_logs_backup.tar.gz trajectory_diplom/config.py trajectory_diplom/logs/
```

## 3. Автоматизація (опційно)
Додайте cron-джобу:
```bash
crontab -e
```

І додайте:
```
0 2 * * * tar -czf /home/backups/trajectory_backup_$(date +\%F).tar.gz /home/trajectory_user/trajectory_diplom
```
