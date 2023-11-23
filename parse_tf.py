with open('pda.txt', 'r') as file :
    lines = file.readlines()

from_state = input("From State: ").upper()
to_state = input("To State: ").upper()

data = []
n = 1
for line in lines :
    if n < 8 :
        n += 1
        continue
    line = line.split()
    if line[0].upper() == from_state and line[3].upper() == to_state :
        push = line[4].split(",")
        to_push = ""
        for el in push :
            if el == "e" :
                to_push += "ε"
            else :
                to_push += f"{el} "
        output = f"{line[1]}, {line[2]} / {to_push}"
        data.append(output)

print("\n_____________________________\n")
for el in data :
    print(el)