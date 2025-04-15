
# Інструкція з розгортання у production-середовищі

Цей документ містить детальні кроки для розгортання проєкту **trajectory_diplom** у робочому середовищі.


## 🖥️ 1. Вимоги до апаратного забезпечення

| Компонент           | Мінімальні вимоги             | Рекомендовано              |
|---------------------|-------------------------------|----------------------------|
| Архітектура         | x86_64                        | x86_64                     |
| CPU                 | 1 ядро                        | 2+ ядра                    |
| RAM                 | 1 ГБ                          | 2 ГБ                       |
| Дисковий простір    | 200 МБ                        | 500 МБ                     |
| OS                  | Ubuntu 20.04+ / Windows 10+   | Ubuntu Server 22.04 LTS   |


## 2. Необхідне програмне забезпечення

- Python 3.11+
- pip
- virtualenv (опціонально)
- Git
- Systemd або Supervisor (менеджер процесів)
- nginx (опціонально, для веб-інтерфейсу/API)



## 3. Налаштування мережі

- Вхідні: порт 22 (SSH), 80/443 (якщо потрібен веб-доступ)
- Вихід в Інтернет для доступу до PyPI
- Статична IP або домен



## 4. Конфігурація серверів

```bash
sudo adduser trajectory_user
sudo usermod -aG sudo trajectory_user
ssh-copy-id trajectory_user@your.server.ip

git clone https://github.com/alina12111/trajectory_diplom.git
cd trajectory_diplom

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```


## 🗄️ 5. Налаштування СУБД

Проєкт не потребує БД. Якщо додаватиметься — використовуйте PostgreSQL або SQLite, додайте `.env`.



## 6. Розгортання коду

```bash
nohup python3 trajectory.py > logs/output.log 2>&1 &
```

або через systemd:

```ini
# /etc/systemd/system/trajectory.service
[Unit]
Description=Trajectory Calculation Service
After=network.target

[Service]
User=trajectory_user
WorkingDirectory=/home/trajectory_user/trajectory_diplom
ExecStart=/home/trajectory_user/trajectory_diplom/venv/bin/python3 trajectory.py
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl daemon-reexec
sudo systemctl enable trajectory
sudo systemctl start trajectory
```



## ✅ 7. Перевірка працездатності

- `tail -f logs/output.log`
- Графік будується при введенні параметрів
- Немає помилок у логах
- API або GUI працює (якщо реалізовано)



🔐 **Безпека:** користуйтеся `.env`, обмежуйте доступ, не зберігайте паролі у відкритому коді.

