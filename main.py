file_path = 'test.html'

with open(file_path, 'r', encoding='utf-8') as file:
    while True:
        char = file.read(1)
        if char == " " or char == "\n" :
            continue
        if not char :
            break
        print(char)