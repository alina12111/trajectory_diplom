
# 🔄 Інструкція з оновлення системи

Цей документ описує оновлення проєкту у production.

## 1. Підключення до сервера
```bash
ssh trajectory_user@your.server.ip
```

## 2. Зупинити сервіс (якщо запущено через systemd)
```bash
sudo systemctl stop trajectory
```

## 3. Оновлення коду
```bash
cd trajectory_diplom
git pull origin main
source venv/bin/activate
pip install -r requirements.txt
```

## 4. Перезапуск
```bash
sudo systemctl start trajectory
```

## 5. Перевірка логів
```bash
journalctl -u trajectory.service -f
```
