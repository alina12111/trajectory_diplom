
# 📦 Інструкція з розгортання у production-середовищі

Цей документ містить кроки для початкового розгортання проєкту **trajectory_diplom** на сервері.

## 1. Вимоги
- **ОС:** Ubuntu 20.04+ / Windows 10+
- **CPU:** 1+ ядро
- **RAM:** 1+ ГБ
- **Диск:** 200+ МБ

## 2. ПЗ
- Python 3.11+, pip, virtualenv
- Git, systemd

## 3. Розгортання
```bash
git clone https://github.com/alina12111/trajectory_diplom.git
cd trajectory_diplom
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
nohup python3 trajectory.py > logs/output.log 2>&1 &
```

## 4. Перевірка
- `tail -f logs/output.log`
- Очікується побудова графіка без помилок
