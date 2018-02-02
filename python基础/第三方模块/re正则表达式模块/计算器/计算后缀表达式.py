# -*- coding: utf-8 -*-


operator = ["*","/","+","-"]
def calc_postfix(postfix_exp):
    stack = []
    for char in postfix_exp:
        if char not in operator:
            stack.append(char)
        else:
            op = char
            num1 = stack.pop()
            num2 = stack.pop()
            calc(op, num1, num2)


def calc(op, num1, num2):
    if not num1.isdigit() and not num2.isdigit():
        raise "num error"
    else:
        num1 = int(num1)
        num2 = int(num2)
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        if num2 == 0:
            raise "zeros error"
        else:
            return num1 / num2
    else:
        raise "op error"

