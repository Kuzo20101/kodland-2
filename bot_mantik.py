import random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password

def yazi_tura():
    cevap = random.randint(2)
    if cevap == 1:
        print("yazı")
    else:
        print("tura")
