#!/usr/bin/env python3
"""
Проверка структуры класса BankAccount
Используется в GitHub Classroom
"""

import ast
import sys

def main():
    try:
        with open('task_Bank.py', 'r', encoding='utf-8') as f:
            code = f.read()
    except FileNotFoundError:
        print("ERROR: Файл task_Bank.py не найден")
        sys.exit(1)
    
    try:
        tree = ast.parse(code)
    except SyntaxError as e:
        print(f"ERROR: Синтаксическая ошибка: {e}")
        sys.exit(1)
    
    # Находим класс
    bank_class = None
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef) and node.name == 'BankAccount':
            bank_class = node
            break
    
    if not bank_class:
        print("ERROR: Класс BankAccount не найден")
        sys.exit(1)
    
    # Проверяем методы
    methods_found = []
    for item in bank_class.body:
        if isinstance(item, ast.FunctionDef):
            methods_found.append(item.name)
    
    required_methods = ["__init__", "add", "status", "withdraw"]
    for method in required_methods:
        if method not in methods_found:
            print(f"ERROR: Отсутствует метод {method}")
            sys.exit(1)
    
    # Находим __init__
    init_method = None
    for item in bank_class.body:
        if isinstance(item, ast.FunctionDef) and item.name == "__init__":
            init_method = item
            break
    
    if not init_method:
        print("ERROR: Метод __init__ не найден")
        sys.exit(1)
    
    # Проверяем атрибуты
    attributes_found = set()
    for node in ast.walk(init_method):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Attribute):
                    attributes_found.add(target.attr)
    
    required_attrs = ["account_number", "balance"]
    for attr in required_attrs:
        if attr not in attributes_found:
            print(f"ERROR: Отсутствует атрибут {attr}")
            sys.exit(1)
    
    # Проверяем вызов status()
    status_called = False
    for node in ast.walk(init_method):
        if (isinstance(node, ast.Call) and 
            isinstance(node.func, ast.Attribute) and 
            node.func.attr == "status"):
            status_called = True
            break
    
    if not status_called:
        print("ERROR: Метод status() не вызывается в __init__")
        sys.exit(1)
    
    print("SUCCESS: Все проверки структуры пройдены")
    sys.exit(0)

if __name__ == "__main__":
    main()
