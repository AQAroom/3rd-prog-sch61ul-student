#!/usr/bin/env python3
"""
Проверка структуры класса BankAccount через AST
Используется в GitHub Classroom
"""

import ast
import sys

def check_structure():
    """Проверяет структуру класса BankAccount"""
    try:
        with open('task.py', 'r', encoding='utf-8') as f:
            code = f.read()
    except FileNotFoundError:
        print("ERROR: Файл task.py не найден")
        return False
    
    try:
        tree = ast.parse(code)
    except SyntaxError as e:
        print(f"ERROR: Синтаксическая ошибка: {e}")
        return False
    
    # Находим класс BankAccount
    bank_class = None
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef) and node.name == 'BankAccount':
            bank_class = node
            break
    
    if not bank_class:
        print("ERROR: Класс BankAccount не найден")
        return False
    
    # Проверяем методы
    methods_found = []
    for item in bank_class.body:
        if isinstance(item, ast.FunctionDef):
            methods_found.append(item.name)
    
    required_methods = ["__init__", "add", "status", "withdraw"]
    for method in required_methods:
        if method not in methods_found:
            print(f"ERROR: Отсутствует метод {method}")
            return False
    
    # Находим __init__
    init_method = None
    for item in bank_class.body:
        if isinstance(item, ast.FunctionDef) and item.name == "__init__":
            init_method = item
            break
    
    if not init_method:
        print("ERROR: Метод __init__ не найден")
        return False
    
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
            return False
    
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
        return False
    
    print("SUCCESS: Все проверки структуры пройдены")
    return True

if __name__ == "__main__":
    sys.exit(0 if check_structure() else 1)
