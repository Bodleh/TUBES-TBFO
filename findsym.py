with open('tf.txt', 'r') as file:
    lines = file.readlines()

data = []
for line in lines :
        line = line.split()
        data.append(line[2])

data = list(set(data))

output = ""
for el in data :
    output += f"{el} "

print(output)