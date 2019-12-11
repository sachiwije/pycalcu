def compute(expression):
    values = expression.split(' ')
    num0 = float(values[0])
    operator = values[1]
    num1 = float(values[2])
    if operator == '+':
        return num0 + num1
    else:
        print('unknown operator!')
        return None
