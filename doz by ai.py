import random

def input_number():
    print("adady beyn 3 ta 100 vared konid")

    try:
        user_input = int(input("abad doz ra vared konid : "))
    except: 
        print("adad vorody ra check konid ")
        return False

    if user_input >= 3:
        return user_input
    else:
        print(" adady bozorg tar az 2 vared konid ")
        return False
andaze_doz = input_number()

adadb = [i for i in range(andaze_doz ** 2)]

def screen(n):
    counter_1 = 0
    counter_2 = 0
    for i in adadb:
        print(f"{i:>4}", end=" ")
        counter_1 += 1
        if counter_1 >= n:
            counter_2 += 1
            print()
            if counter_2 <= n - 1:
                print(end="")
            counter_1 = 0

def porbodanc(position):
    if type(position) != int:
        return False
    else:
        return True

whos_turn = "o"
def user_input():
    global whos_turn
    whos_turn = ch_x_or_o(whos_turn)
    desired_cell = int(input(f"adady beyn [0-{andaze_doz ** 2 - 1}] vared konid : "))
    return desired_cell, whos_turn

def porbodan(user_input, x_or_o):
    if porbodanc(adadb[user_input]):
        adadb[user_input] = x_or_o
    else:
        print("in khone pore ye adad dige vared konid")
        global whos_turn
        whos_turn = ch_x_or_o(whos_turn)
        input("Press enter to continue...")
    
def ch_x_or_o(x_or_o):
    if x_or_o == "x":
        return "o"
    elif x_or_o == "o":
        return "x"

def statusg():
    for i in adadb:
        if i != "x" and i != "o":
            return "not full"
    return "full"

def hbarande(n):
    halat = []

    counter1 = 0
    counter2 = n
    while counter2 <= n ** 2:
        result1 = list(range(counter1, counter2))
        halat.append(result1)
        counter1 += n
        counter2 += n

    counter1 = 0
    while counter1 < n:
        result1 = list(range(counter1, n ** 2, n))
        halat.append(result1)
        counter1 += 1
    
    counter1 = 0
    result1 = list(range(counter1, n ** 2, n + 1))
    halat.append(result1)
    
    result1 = list(range(n - 1, n ** 2 - 1, n - 1))
    halat.append(result1)
    
    return halat  

def check(list):
    check_variable = list[0]
    counter = 0
    for i in list:
        if check_variable == i:
            counter += 1
    if counter == len(list):
        return True
    else:
        return False

def help1(list):
    sample_list = [adadb[i] for i in list]
    return sample_list

def tashkhis_barande():
    for i in hbarande(andaze_doz):
        if check(help1(i)):
            if help1(i)[0] == "x":
                return "bakhty !"
            elif help1(i)[0] == "o":
                return "bordy !"
        else:
            continue
        
def barande_o(list):
    checkm = "o"
    counter = 0
    for i in list:
        if checkm == i:
            counter += 1
    if counter >= 2:
        return True
    else:
        return False
    
def barande_x(list):
    checkm = "x"
    counter = 0
    for i in list:
        if checkm == i:
            counter += 1
    if counter >= 2:
        return True
    else:
        return False

def ai():
    status = False
    for indexs in hbarande(andaze_doz):
        if barande_x(help1(indexs)):
            for i in indexs:
                if type(adadb[i]) == int:
                    adadb[i] = "x"
                    status = True
                    break
                else:
                    continue
            break
        else:
            continue
    if status == False:
        for indexs in hbarande(andaze_doz):
            if barande_o(help1(indexs)):
                for i in indexs:
                    if type(adadb[i]) == int:
                        adadb[i] = "x"
                        status = True
                        break
                    else:
                        continue
                break
            else:
                continue
    if status == False:
        while True:
            random_index = random.randint(0, andaze_doz ** 2 - 1)
            if porbodanc(adadb[random_index]):
                adadb[random_index] = "x"
                break       
            
def hazf_porshodeha():
    for i in range(len(adadb)):
        if type(adadb[i]) == int:
            adadb[i] = " "
    return adadb
    
while statusg() == "not full":
    screen(andaze_doz)
    print()
    print(f" Nobat {ch_x_or_o(whos_turn)}")
    if whos_turn == "x":
        is_invalid = True
        while is_invalid:
            try:
                user_Input = user_input()
                porbodan(user_Input[0], user_Input[1])
                is_invalid = False
            except:
                print("adad ro check kon")
                whos_turn = ch_x_or_o(whos_turn)
    else:
        is_invalid = True
        while is_invalid:
            try:
                ai()
                whos_turn = ch_x_or_o(whos_turn)
                is_invalid = False
            except:
                continue            
            
    if tashkhis_barande() == "bakhty !":
        hazf_porshodeha()
        screen(andaze_doz)
        print("bakhty")
        break
    elif tashkhis_barande() == "bordy !":
        hazf_porshodeha()
        screen(andaze_doz)
        print("bordy !")
        break
    else:
        continue

if tashkhis_barande() != "bakhty !" and tashkhis_barande() != "bordy !":
    screen(andaze_doz)
    print("mosavi")

