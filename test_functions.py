#test_function.py
import pytest
from functions import add, get_user_full_name

@pytest.fixture
def sample_user_data(): 
    return {
"first_name": "Jane",
"last_name": "Doe",
"email": "jane.doe@example.com"
}
def test_get_user_full_name_with_fixture(sample_user_data):
    assert get_user_full_name(sample_user_data) == "Jane Doe"
def test_user_has_email_with_fixture(sample_user_data):
    assert "email" in sample_user_data

test_cases = [
(1, 2, 3), # Обычное сложение
(-1, -1, -2), # Сложение отрицательных чисел
(5, 0, 5), # Сложение с нулем
(-1, 1, 0), # Противоположные числа
(3.5, 2.5, 6.0) # Сложение чисел с плавающей точкой
]

@pytest.mark.parametrize("a, b, exoected", test_cases)
def test_add_parametrized(a, b, expected):
        assert add(a, b) == expected
        
@pytest.mark.parametrize("a, b, expected", test_cases)
def test_add_parametrized(a, b, expected):
        assert add(a, b) == expected

from functions import divide

def test_divide_by_zero_raises_error():
    with pytest.raises(ValueError):
        divide(10, 0)

@pytest.mark.skip(reason="Эта функция еще в разработке")
def test_new_feature():
# Код теста для новой, еще не готовой функции
    assert False

from functions import add
def test_add():
    assert add(2,3)== 5
    assert add(-1,1)==0
    assert add(10,-5)==5

@pytest.mark.xfail(reason="Известный баг с точностью float, тикет #123")
def test_float_precision_bug():
    assert (0.1 + 0.2) == 0.3 # Этот тест упадет из-за особенностей float


from functions import (
    is_valid_password,
    get_age_group,
    calculate_cart_total,
    get_value_from_dict,
    Wallet,
    InsufficientFundsError,
)


# ==================== ЗАДАЧА 1 ====================
def test_password_valid():
    assert is_valid_password("password123") == True

def test_password_too_short():
    assert is_valid_password("123") == False

def test_password_boundary():
    assert is_valid_password("12345678") == True  # ровно 8 символов
    assert is_valid_password("1234567") == False   # 7 символов


# ==================== ЗАДАЧА 2 ====================
@pytest.mark.parametrize("age, expected", [
    (10, "ребенок"),
    (12, "ребенок"),
    (13, "подросток"),
    (17, "подросток"),
    (18, "взрослый"),
    (25, "взрослый"),
])
def test_get_age_group(age, expected):
    assert get_age_group(age) == expected


# ==================== ЗАДАЧА 3 ====================
@pytest.fixture
def sample_cart():
    return [
        {"name": "apple", "price": 1.5, "quantity": 2},
        {"name": "banana", "price": 2.0, "quantity": 3},
        {"name": "orange", "price": 0.8, "quantity": 5},
    ]

def test_calculate_cart_total(sample_cart):
    # (1.5 * 2) + (2.0 * 3) + (0.8 * 5) = 3 + 6 + 4 = 13
    assert calculate_cart_total(sample_cart) == 13.0

def test_cart_contains_item(sample_cart):
    # Проверим, что в корзине есть товар "banana"
    item_names = [item["name"] for item in sample_cart]
    assert "banana" in item_names


# ==================== ЗАДАЧА 4 ====================
def test_get_value_success():
    data = {"a": 1, "b": 2}
    assert get_value_from_dict(data, "a") == 1

def test_get_value_key_error():
    data = {"a": 1}
    with pytest.raises(KeyError):
        get_value_from_dict(data, "b")


# ==================== ЗАДАЧА 5 ====================
@pytest.fixture
def wallet():
    return Wallet(initial_balance=20.0)

def test_deposit(wallet):
    wallet.deposit(10.0)
    assert wallet.balance == 30.0

def test_withdraw(wallet):
    wallet.withdraw(5.0)
    assert wallet.balance == 15.0

def test_withdraw_insufficient_funds(wallet):
    with pytest.raises(InsufficientFundsError):
        wallet.withdraw(100.0)

@pytest.mark.parametrize("method_name, args, expected_exception", [
    ("__init__", [-10.0], ValueError),
    ("deposit", [0.0], ValueError),
    ("deposit", [-5.0], ValueError),
    ("withdraw", [0.0], ValueError),
    ("withdraw", [-5.0], ValueError),
])
def test_value_error_on_invalid_input(method_name, args, expected_exception):
    if method_name == "__init__":
        with pytest.raises(expected_exception):
            Wallet(*args)
    else:
        wallet = Wallet()
        method = getattr(wallet, method_name)
        with pytest.raises(expected_exception):
            method(*args)

            