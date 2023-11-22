with open('test2.html', 'r') as file :
    lines = file.readlines()
line_number = len(lines)
print("Syntax Error\n")
print(f"Error at line {line_number} : token [\033[33m a \033[0m]")