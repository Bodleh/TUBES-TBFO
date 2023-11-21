# Check if pda is valid
def check_pda_validity(pda) :
    print()

# PDA FILE FORMAT MUST BE TRUE
def parse_pda(pda_path: str) -> dict :
    pda = {
        'states' : [],
        'input_symbols' : [],
        'stack_symbols' : [],
        'start_state' : 0,
        'start_stack_symbol' : 0,
        'final_states' : [],
        'pda_type' : 'E',
        'tf' : {}
    }

    with open(pda_path, 'r',) as file :
        lines = file.readlines()
    
    new_lines = []
    for line in lines :
        line = line.split()
        new_lines.append(line)

    count = 1
    for line in new_lines :
        if count == 1 :
            pda['states'] = line
            for states in pda['states'] :
                pda['tf'][states] = []
        elif count == 2 :
            pda['input_symbols'] = line
        elif count == 3 :
            pda['stack_symbols'] = line
        elif count == 4 :
            pda['start_state'] = line[0]
        elif count == 5 :
            pda['start_stack_symbol'] = line[0]
        elif count == 6 :
            pda['final_states'] = line
        elif count == 7 :
            pda['pda_type'] = line[0]
        elif count >= 8 :
            pda['tf'][line[0]].append({
                'input' : line[1],
                'pop' : line[2],
                'next_state' : line[3],
                'push' : line[4].split(',')
            })
        count += 1
    
    for states in pda['states'] :
        if pda['tf'][states] == [] :
            del pda['tf'][states]

    return pda



# Process tokens into PDA
def process(pda, tokens) :
    current_state = pda['start_state']
    stack = [pda['start_stack_symbol']]
    pda_type = pda['pda_type']
    valid = True
    cur_token = ""
    for token in tokens :
        cur_token = token
        #### for DEBUGGING
        # print(f"STACK: {stack}")
        # print(f"Current State : {current_state}") 
        ####

        success = False
        
        for transition in pda['tf'][current_state] :
            if token == transition['input'] :
                if stack[-1] == transition['pop'] :
                    current_state = transition['next_state']
                    stack.pop()
                    to_push = transition['push'][::-1]
                    for symbol in to_push :
                        if symbol != 'e' :
                            stack.append(symbol)
                    success = True
                    break
        
        if not success :
            valid = False
            break
    
    #### for DEBUGGING
    # print(f"STACK: {stack}")
    # print(f"Current State : {current_state}")
    ####

    if not valid :
        print(f"Current State: {current_state}")
        print(f"Current Token: {cur_token}")
        print(f"Current Top Stack: {stack[-1]}")
        print("Syntax Error")
    else :
        if pda_type == 'F' and current_state in pda['final_states'] :
            print("Accepted")
        elif pda_type == 'E' and stack == [pda['start_stack_symbol']] :
            print("Accepted")
        else :
            print("Syntax Error")


# Print PDA information for debugging
def printPDA(pda) :
    print(f"             States : {pda['states']}")
    print(f"      Input symbols : {pda['input_symbols']}")
    print(f"      Stack symbols : {pda['stack_symbols']}")
    print(f"        Start state : {pda['start_state']}")
    print(f" Start stack symbol : {pda['start_stack_symbol']}")
    print(f"       Final states : {pda['final_states']}")
    print(f"           PDA type : {pda['pda_type']}")
    print("TRANSITION FUNCTION :")
    for key, value in pda['tf'].items() :
        print(f">> State : {key}")
        for el in value :
            print(el)
