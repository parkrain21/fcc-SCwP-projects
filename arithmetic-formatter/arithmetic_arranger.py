def arithmetic_arranger(problems, display=False):
# split the operands and operators
    str_problems = []
    for problem in problems:
        str_problems.append(problem.split())

# Error handling (not raising actual errors)
    if len(problems) > 5:
        return 'Error: Too many problems.'

    for str_problem in str_problems:
        if not str_problem[0].isdigit() or not str_problem[2].isdigit():
            return 'Error: Numbers must only contain digits.'
        elif str_problem[1] not in  ('+', '-'):
            return "Error: Operator must be '+' or '-'."
        elif len(str_problem[0]) > 4 or len(str_problem[2]) > 4:
            return 'Error: Numbers cannot be more than four digits.'

# main logic
    line_1 = ''
    line_2 = ''
    dashes = ''
    answer = ''

    for problem_i in range(len(str_problems)):
        a = str_problems[problem_i][0]
        b = str_problems[problem_i][2]
        operator = str_problems[problem_i][1]

        if operator == '+':
            ans = str(int(a) + int(b))
        elif operator == '-':
            ans = str(int(a) - int(b))

        max_operand_len = max(len(a), len(b))
        
        line_1 += a.rjust(max_operand_len + 2)
        line_2 += operator + b.rjust(max_operand_len + 1)
        dashes += '-' * (max_operand_len + 2)
        answer += ans.rjust(max_operand_len + 2)

        if problem_i != len(str_problems) - 1:
            line_1 += '    '
            line_2 += '    '
            dashes += '    '
            answer += '    '
    
    arranged_problems = line_1 + '\n' + line_2 + '\n' + dashes
    if display:
        return arranged_problems + '\n' + answer
    return arranged_problems