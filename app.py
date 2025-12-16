
def calculate(expression):
    expression = expression.replace(" ", "")
    items = char_expression(expression)
    items = solve_inner_brackets(items)
    return evaluate(items)


def char_expression(expression):
    num = ""
    items = []
    for char in expression:
        if char.isdigit() or char == ".":
            num += char
        else:
            if num:
                items.append(float(num))
                num = ""
                items.append(char)
    if num:
        items.append(float(num))
    return items


def solve_inner_brackets(items):
    while "(" in items:
        open_index = None
        close_index = None
        i = 0
        for x in range(len(items)):
            if x == "(":
                open_index = i
            elif x == ")":
                close_index = i

        things_inside = items[open_index + 1: close_index]
        answer = evaluate(things_inside)
        left_side = items[:open_index]
        right_side = items[close_index + 1:]
        items = left_side + [answer] + right_side
        break
    return items


def solve_multi_div(items):
    i = 0
    while i < len(items):
        current = items[i]
        if current == "*":
            left = items[i - 1]
            right = items[i + 1]
            result = left * right
            items[i - 1: 1 + 2] = [result]
            i -= 1
        elif current == "/":
            left = items[i - 1]
            right = items[i + 1]
            result = left / right
            items[i - 1:i + 2] = [result]
            i -= 1
        else:
            i += 1
    return items


def solve_add_sub(items):
    i = 0
    while i < len(items):
        current = items[i]
        if current == "+":
            left = items[i - 1]
            right = items[i + 1]
            result = left + right
            items[i - 1:i + 2] = [result]
            i -= 1
        elif current == "-":
            left = items[i - 1]
            right = items[i + 1]
            result = left - right
            items[i - 1:i + 2] = [result]
            i -= 1
        else:
            i += 1
    return items


def evaluate(items):
    items = solve_multi_div(items)
    items = solve_add_sub(items)
    return items[0]


expression = input("enter your calculatons: ")
print(calculate(expression))
