with open('tf.txt', 'r') as file :
    lines = file.readlines()

from_state = input("From State: ").upper()
to_state = input("To State: ").upper()


data = []
for line in lines :
    line = line.split()
    if line[0].upper() == from_state and line[3].upper() == to_state :
        push = line[4].split(",")
        to_push = ""
        for el in push :
            if el == "e" :
                to_push += "ε "
            else :
                to_push += f"{el} "
        output = f"δ( {line[0]}, {line[1]}, {line[2]} ) =" + " {" + f"( {line[3]}, {to_push})" + "}"
        data.append(output)

print("\n_____________________________\n")
for el in data :
    print(el)