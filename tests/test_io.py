#!/usr/bin/env python3
"""
Тестовый скрипт для BankAccount
Используется в GitHub Classroom
"""

import sys

def main():
    # Импортируем класс
    try:
        from task import BankAccount
    except ImportError:
        sys.exit(1)
    
    # Читаем входные данные
    data = sys.stdin.read().strip().split()
    if len(data) != 2:
        sys.exit(1)
    
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
        sys.exit(1)
    except Exception:
        sys.exit(1)

if __name__ == "__main__":
    main()
