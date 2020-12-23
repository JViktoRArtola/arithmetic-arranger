def arithmetic_arranger(problems, flag=True):
    if len(problems) > 5:
        return print("Error: Too many problems.")

    line_a = ''
    line_b = ''
    line_c = ''
    line_d = ''

    for i, problem in enumerate(problems):
        n1, op, n2 = problem.split()
        l1, l2 = len(n1), len(n2)

        if op not in ['+', '-']:
            return 'Error: Operator must be \'+\' or \'-\'.'
        if not (n1.isdigit() and n2.isdigit()):
            return 'Error: Numbers must only contain digits.'
        if l1 > 4 or l2 > 4:
            return 'Error: Numbers cannot be more than four digits.'

        space = max(l1, l2)
        result = int(n1) + int(n2) if op == '+' else int(n1) - int(n2)

        line_a = line_a + n1.rjust(space + 2)
        line_b = line_b + op + n2.rjust(space + 1)
        line_c = line_c + ''.rjust(space + 2, '-')
        line_d = line_d + str(result).rjust(space + 2)

        if i < len(problems) - 1:
            line_a += '    '
            line_b += '    '
            line_c += '    '
            line_d += '    '

    if flag:
        arranged_problems = line_a + '\n' + line_b + '\n' + line_c + '\n' + line_d
    else:
        arranged_problems = line_a + '\n' + line_b + '\n' + line_c
    return arranged_problems