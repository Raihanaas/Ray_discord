import random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password

def coinflip():
    num = random.randint(1,2)
    if num == 1:
        return "Heads"
    else:
        return "Tails"
    
def roll_dice():
    return "the dice is", random.randint(1,6)

def double_letter (str):
    result = ''
    for letter in str:
        result += letter * 2
    return result


def secret_function (a, b):
    # Tulis kode Kamu di sini!
    return str(a) + str(b)


print(double_letter("Hello"))
print(secret_function(1, 2))
print(secret_function("Hello, ", "world!"))