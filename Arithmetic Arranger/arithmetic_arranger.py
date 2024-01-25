def arithmetic_arranger(problems, show_answers=False):
  if len(problems) > 5:
      return "Error: Too many problems."

  valid_operators = {'+', '-'}
  operators = [problem.split()[1] for problem in problems]
  if set(operators) != valid_operators and len(set(operators)) != 2:
      return "Error: Operator must be '+' or '-'."

  numbers = [num for problem in problems for num in problem.split() if num.isdigit()]
  if not all(map(lambda x: len(x) < 5, numbers)):
      return "Error: Numbers cannot be more than four digits."

  formatted_problems = {'top_row': '', 'bottom_row': '', 'dashes': '', 'solutions': ''}
  for problem in problems:
      operand1, operator, operand2 = problem.split()
      width = max(len(operand1), len(operand2)) + 2

      formatted_problems['top_row'] += f"{operand1.rjust(width)}    "
      formatted_problems['bottom_row'] += f"{operator}{operand2.rjust(width - 1)}    "
      formatted_problems['dashes'] += "-" * width + "    "
      formatted_problems['solutions'] += str(eval(problem)).rjust(width) + "    "

  result = [formatted_problems['top_row'].rstrip(),
            formatted_problems['bottom_row'].rstrip(),
            formatted_problems['dashes'].rstrip()]

  if show_answers:
      result.append(formatted_problems['solutions'].rstrip())

  return '\n'.join(result)


# Example usage:
problems_list = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
result = arithmetic_arranger(problems_list, show_answers=True)
print(result)
