import json
import math
import tkinter as tk
from tkinter import messagebox

import bcrypt  # type: ignore
import numpy as np  # type: ignore
import matplotlib.pyplot as plt  # type: ignore

from logger_config import logger

# Функція для перевірки коректності email

def is_valid_email(email):
    """
    Перевіряє правильність формату email.

    Args:
        email (str): Адреса електронної пошти.

    Returns:
        bool: True, якщо адреса має символ '@' та '.', інакше False.
    """
    return "@" in email and "." in email

# Функція для хешування пароля

def hash_password(password):
    """
    Генерує захищений хеш пароля за допомогою алгоритму bcrypt.

    Args:
        password (str): Пароль у відкритому вигляді.

    Returns:
        bytes: Захешований пароль у форматі bytes.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

# Симуляція бази даних
users_db = {}

# Функція для розрахунку траєкторії

def calculate_trajectory(_, angle, height):
    """
    Виконує розрахунок балістичної траєкторії вертикального спуску літального апарату
    в атмосфері Землі за заданим кутом та висотою.

    Args:
        angle (float): Кут нахилу траєкторії в градусах.
        height (float): Початкова висота (м).

    Returns:
        dict: Словник з початковою швидкістю, часом польоту та горизонтальною відстанню.
    """
    g = 9.81
    angle_rad = math.radians(angle)
    initial_velocity = math.sqrt(2 * g * height)
    time_of_flight = (2 * initial_velocity * math.sin(angle_rad)) / g
    horizontal_distance = initial_velocity * math.cos(angle_rad) * time_of_flight

    results = {
        "initial_velocity": initial_velocity,
        "time_of_flight": time_of_flight,
        "horizontal_distance": horizontal_distance
    }
    with open("trajectory_results.json", "w", encoding="utf-8") as file:
        json.dump(results, file, indent=4)

    return results

# Функція для візуалізації траєкторії

def plot_trajectory():
    """
    Зчитує результати з JSON-файлу та візуалізує траєкторію польоту на графіку.
    """
    with open("trajectory_results.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    g = 9.81
    v = data["initial_velocity"]
    angle = 45
    angle_rad = np.radians(angle)

    t = np.linspace(0, data["time_of_flight"], num=500)
    x = v * np.cos(angle_rad) * t
    y = x * np.tan(angle_rad) - (g * x**2) / (2 * v**2 * np.cos(angle_rad)**2)

    plt.plot(x, y)
    plt.title("Траєкторія польоту")
    plt.xlabel("Горизонтальна відстань (м)")
    plt.ylabel("Висота (м)")
    plt.grid()
    plt.show()

# Інтерфейс

def open_calculation_window():
    """
    Відкриває нове вікно для введення параметрів і обчислення траєкторії.
    """
    calc_window = tk.Toplevel(root)
    calc_window.title("Розрахунок траєкторії")

    tk.Label(calc_window, text="Маса апарату (кг):").grid(row=0, column=0, padx=5, pady=5)
    mass_entry = tk.Entry(calc_window)
    mass_entry.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(calc_window, text="Кут спуску (°):").grid(row=1, column=0, padx=5, pady=5)
    angle_entry = tk.Entry(calc_window)
    angle_entry.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(calc_window, text="Висота (м):").grid(row=2, column=0, padx=5, pady=5)
    height_entry = tk.Entry(calc_window)
    height_entry.grid(row=2, column=1, padx=5, pady=5)

    def calculate():
        try:
            mass = float(mass_entry.get())
            angle = float(angle_entry.get())
            height = float(height_entry.get())
            results = calculate_trajectory(mass, angle, height)
            messagebox.showinfo("Результати", f"Швидкість: {results['initial_velocity']:.2f} м/с\n"
                                              f"Час польоту: {results['time_of_flight']:.2f} с\n"
                                              f"Дальність: {results['horizontal_distance']:.2f} м")
        except ValueError:
            messagebox.showerror("Помилка", "Введіть коректні значення!")

    tk.Button(calc_window, text="Розрахувати", command=calculate).grid(row=3, column=0, padx=5, pady=5)
    tk.Button(calc_window, text="Побудувати графік", command=plot_trajectory).grid(row=3, column=1, padx=5, pady=5)


def open_registration_window():
    """
    Відкриває вікно реєстрації користувача з полями для email та пароля.
    """
    registration_window = tk.Toplevel(root)
    registration_window.title("Реєстрація")
    registration_window.geometry("300x200")
    registration_window.grab_set()
    registration_window.transient(root)

    tk.Label(registration_window, text="Email:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
    email_entry = tk.Entry(registration_window, width=25)
    email_entry.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(registration_window, text="Password:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
    password_entry = tk.Entry(registration_window, width=25, show="*")
    password_entry.grid(row=1, column=1, padx=10, pady=10)

    tk.Label(registration_window, text="Confirm Password:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
    confirm_password_entry = tk.Entry(registration_window, width=25, show="*")
    confirm_password_entry.grid(row=2, column=1, padx=10, pady=10)

    def register_user():
        email = email_entry.get()
        password = password_entry.get()
        confirm_password = confirm_password_entry.get()

        if not is_valid_email(email):
            messagebox.showerror("Помилка", "Некоректний email!")
            return

        if email in users_db:
            messagebox.showerror("Помилка", "Користувач із таким email вже зареєстрований!")
            return

        if len(password) < 8 or not any(char.isupper() for char in password) or not any(char.isdigit() for char in password):
            messagebox.showerror("Помилка", "Пароль має бути не менше 8 символів з великою літерою та цифрою!")
            return

        if password != confirm_password:
            messagebox.showerror("Помилка", "Паролі не співпадають!")
            return

        hashed_password = hash_password(password).decode('utf-8')
        users_db[email] = hashed_password

    try:
        with open("users_db.json", "r", encoding="utf-8") as file:
            json.dump(users_db, file)
        messagebox.showinfo("Успіх", "Реєстрація успішна!")
        registration_window.destroy()
        calc_button.config(state="normal")
    except (IOError, ValueError) as e:
        messagebox.showerror("Помилка", f"Не вдалося зберегти дані: {e}")

    tk.Button(registration_window, text="Register", command=register_user).grid(row=3, column=0, columnspan=2, pady=10)
    tk.Button(registration_window, text="Cancel", command=registration_window.destroy).grid(row=4, column=0, columnspan=2, pady=5)

    registration_window.update_idletasks()
    x = (registration_window.winfo_screenwidth() - registration_window.winfo_reqwidth()) // 2
    y = (registration_window.winfo_screenheight() - registration_window.winfo_reqheight()) // 2
    registration_window.geometry(f"+{x}+{y}")

# Основне вікно
root = tk.Tk()
root.title("Система моделювання")

tk.Button(root, text="Реєстрація", command=open_registration_window).pack(pady=10)
calc_button = tk.Button(root, text="Розрахунок траєкторії", command=open_calculation_window, state="disabled")
calc_button.pack(pady=10)

root.mainloop()
