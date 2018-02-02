# -*- coding: utf-8 -*-

operator_precedence = { #这里指的是在栈中优先级
    '(' : 0,
    ')' : 0,
    '+' : 1,
    '-' : 1,
    '*' : 2,
    '/' : 2
}


def convert_infix_to_postfix(infix_list):
    postfix_list = []
    operator_stack = []
    for char in infix_list:
        if char not in operator_precedence:
            postfix_list.append(char)
        else:
            if char == '(':
                operator_stack.append(char) #入栈
            elif char == ')':
                while operator_stack[-1] != "(":
                    postfix_list.append(operator_stack.pop())
                operator_stack.pop() #弹出“（”
            elif not operator_stack:# 空栈，无论如何都要入栈
                operator_stack.append(char)
            elif operator_precedence[operator_stack[-1]] < operator_precedence[char]:
                operator_stack.append(char)
            else: #优先级小于和等于栈顶的
                while operator_stack:
                    if operator_stack[-1] == "(":
                        break
                    postfix_list.append(operator_stack.pop())
                operator_stack.append(char)

    while operator_stack:
        postfix_list.append(operator_stack.pop())

    return postfix_list


if __name__ == "__main__":
    infix_expression = "a + b * c + (d * e + f) * g".replace(" ", "")
    print(infix_expression)
    post = convert_infix_to_postfix(infix_expression)
    print("".join(post))


