# functions.py
def add(x, y):
    return x + y

def get_user_full_name(user_data):
    first_name = user_data.get("first_name", "")
    last_name = user_data.get("last_name", "")
    return f"{first_name} {last_name}".strip()

def divide(a, b):
    if b == 0:
        raise ValueError("Деление на ноль невозможно")
    return a / b


# ==================== ЗАДАЧА 1 ====================
def is_valid_password(password: str) -> bool:
    """Проверяет, соответствует ли пароль минимальным требованиям по длине."""
    return len(password) >= 8


# ==================== ЗАДАЧА 2 ====================
def get_age_group(age: int) -> str:
    """
    Возвращает возрастную группу по возрасту.
    - До 13 лет: "ребенок"
    - От 13 до 18 лет: "подросток"
    - Старше 18 лет: "взрослый"
    """
    if age < 13:
        return "ребенок"
    elif 13 <= age < 18:
        return "подросток"
    else:
        return "взрослый"


# ==================== ЗАДАЧА 3 ====================
def calculate_cart_total(cart_items: list[dict]) -> float:
    """Рассчитывает общую стоимость товаров в корзине."""
    total_cost = 0.0
    for item in cart_items:
        total_cost += item["price"] * item["quantity"]
    return total_cost


# ==================== ЗАДАЧА 4 ====================
def get_value_from_dict(data_dict: dict, key: str):
    """Возвращает значение из словаря по ключу."""
    return data_dict[key]


# ==================== ЗАДАЧА 5 ====================
class InsufficientFundsError(Exception):
    """Исключение, вызываемое при нехватке средств."""
    pass


class Wallet:
    def __init__(self, initial_balance: float = 0.0):
        if initial_balance < 0:
            raise ValueError("Начальный баланс не может быть отрицательным.")
        self.balance = initial_balance

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть положительной.")
        self.balance += amount

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной.")
        if amount > self.balance:
            raise InsufficientFundsError("Недостаточно средств на счете.")
        self.balance -= amount