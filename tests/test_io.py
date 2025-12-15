#!/usr/bin/env python3
"""
Тестовый скрипт для BankAccount
Используется в GitHub Classroom
"""

import sys

def check_io():
    # Импортируем класс из файла студента
    from task import BankAccount
    
    # Читаем входные данные
    data = sys.stdin.read().strip().split()
    # data = [input(), input()]
    if len(data) != 2:
        return
    
    try:
        # Преобразуем в числа
        initial_balance = int(data[0])
        operation = int(data[1])
        
        # Создаем счет
        account = BankAccount("test_account", initial_balance)
        
        # Выполняем операцию
        if operation >= 0:
            account.add(operation)
        else:
            account.withdraw(-operation)
        
        # Выводим итоговый баланс
        account.status()
        
    except (ValueError, TypeError):
        # Неправильные типы данных
        pass
    except Exception:
        # Любая другая ошибка
        pass

if __name__ == "__main__":
    check_io()
