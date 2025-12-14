#!/usr/bin/env python3
"""
Проверка структуры класса BankAccount
Используется в GitHub Classroom
"""

import ast
import sys

def check_bank_account_structure(filename):
    """Проверяет структуру класса BankAccount с помощью AST"""
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        tree = ast.parse(content)
        
        # Счетчики для баллов
        points = 0
        max_points = 5
        findings = []
        
        # Ищем класс BankAccount
        bank_class = None
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef) and node.name == 'BankAccount':
                bank_class = node
                break
        
        if not bank_class:
            findings.append("❌ Класс BankAccount не найден")
            return 0, max_points, findings
        
        findings.append("✅ Класс BankAccount найден")
        
        # Проверяем методы класса
        methods = []
        for node in ast.walk(bank_class):
            if isinstance(node, ast.FunctionDef):
                methods.append(node.name)
        
        required_methods = ['__init__', 'add', 'status', 'withdraw']
        missing_methods = []
        
        for method in required_methods:
            if method in methods:
                findings.append(f"✅ Метод {method}() найден")
                points += 1
            else:
                findings.append(f"❌ Метод {method}() отсутствует")
                missing_methods.append(method)
        
        # Проверяем наличие переменных экземпляра в __init__
        init_found = False
        for node in ast.walk(bank_class):
            if isinstance(node, ast.FunctionDef) and node.name == '__init__':
                init_found = True
                # Ищем присваивания self.balance и self.account_number
                has_balance = False
                has_account_number = False
                has_status_call = False
                
                for subnode in ast.walk(node):
                    # Проверяем присваивание self.balance
                    if (isinstance(subnode, ast.Assign) and
                        isinstance(subnode.targets[0], ast.Attribute) and
                        isinstance(subnode.targets[0].value, ast.Name) and
                        subnode.targets[0].value.id == 'self' and
                        subnode.targets[0].attr == 'balance'):
                        has_balance = True
                    
                    # Проверяем присваивание self.account_number
                    if (isinstance(subnode, ast.Assign) and
                        isinstance(subnode.targets[0], ast.Attribute) and
                        isinstance(subnode.targets[0].value, ast.Name) and
                        subnode.targets[0].value.id == 'self' and
                        subnode.targets[0].attr == 'account_number'):
                        has_account_number = True
                    
                    # Проверяем вызов self.status()
                    if (isinstance(subnode, ast.Expr) and
                        isinstance(subnode.value, ast.Call) and
                        isinstance(subnode.value.func, ast.Attribute) and
                        isinstance(subnode.value.func.value, ast.Name) and
                        subnode.value.func.value.id == 'self' and
                        subnode.value.func.attr == 'status'):
                        has_status_call = True
                
                if has_balance:
                    findings.append("✅ Переменная self.balance найдена в __init__()")
                    points += 0.5
                else:
                    findings.append("❌ Переменная self.balance не найдена в __init__()")
                
                if has_account_number:
                    findings.append("✅ Переменная self.account_number найдена в __init__()")
                    points += 0.5
                else:
                    findings.append("❌ Переменная self.account_number не найдена в __init__()")
                
                if has_status_call:
                    findings.append("✅ Вызов self.status() найден в __init__()")
                    points += 1
                else:
                    findings.append("❌ Вызов self.status() не найден в __init__()")
                
                break
        
        if not init_found:
            findings.append("❌ Метод __init__() не найден (хотя должен быть)")
        
        return points, max_points, findings
        
    except Exception as e:
        findings = [f"❌ Ошибка при анализе AST: {str(e)}"]
        return 0, 5, findings

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Использование: python check_structure.py <filename>")
        sys.exit(1)
    
    filename = sys.argv[1]
    points, max_points, findings = check_bank_account_structure(filename)
    
    # Выводим результаты
    for finding in findings:
        print(finding)
    
    print(f"\nБаллы за структуру: {points}/{max_points}")
    
    # Сохраняем баллы в файл для GitHub Actions
    with open("ast_results.txt", "w") as f:
        f.write(f"points={points}\n")
        f.write(f"max_points={max_points}\n")
        f.write("findings=" + "|".join(findings) + "\n")
