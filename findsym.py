with open('pda.txt', 'r') as file:
    lines = file.readlines()

data = []
n = 1
for line in lines :
        if n < 8 :
             n += 1
             continue
        line = line.split()
        data.append(line[2])

data = list(set(data))

output = ""
for el in data :
    output += f"{el}, "
print(len(data))

print(output)