** start of main.py **

def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    top_row = []
    bottom_row = []
    line_row = []
    answer_row = []

    for prob in problems:
        pieces = prob.split()
        if len(pieces) != 3:
            return "Error: Invalid format."

        num1 = pieces[0]
        op = pieces[1]
        num2 = pieces[2]

        if op != '+' and op != '-':
            return "Error: Operator must be '+' or '-'."

        if not num1.isdigit() or not num2.isdigit():
            return "Error: Numbers must only contain digits."

        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        maxlen = max(len(num1), len(num2)) + 2
        top = num1.rjust(maxlen)
        bottom = op + ' ' + num2.rjust(maxlen - 2)
        line = '-' * maxlen

        top_row.append(top)
        bottom_row.append(bottom)
        line_row.append(line)

        if show_answers:
            if op == '+':
                result = int(num1) + int(num2)
            else:
                result = int(num1) - int(num2)
            answer_row.append(str(result).rjust(maxlen))

    arranged = '    '.join(top_row) + '\n' + '    '.join(bottom_row) + '\n' + '    '.join(line_row)

    if show_answers:
        arranged += '\n' + '    '.join(answer_row)

    return arranged

** end of main.py **

