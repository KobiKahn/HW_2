import random
import math
# HW2

#### TO RUN A CODE JUST CHANGE THE VARIABLE TO TRUE

#1

num1 = False
if num1:
    for num in range(0,10):
        print('Kobi Kahn')
        if num == 9:
            print('done')

# 2

num2 = False

if num2:
    for num in range(0,20):
        print('Red Gold')
        print('')

# 3

num3 = False

if num3:
    for num in range(2,101):
        if num % 2 == 0:
            print(num)

# 4

num4 = False

num = 0
if num4:
    while num <= 98:
        num += 2
        print(num)

# 5

num5 = False

blast_off = False
num = 10
if num5:
    while blast_off == False:
        print(num)
        num -= 1
        if num < 0:
            print('BLAST OFF!!!!!')
            blast_off = True

# 6

num6 = False

if num6:
    print(random.randint(1,10))

# 7

num7 = False

if num7:
    print(round(random.uniform(1,10),1))

# 8
num8 = False

def player_nums():
    zero = 0
    pos = 0
    neg = 0
    sum = 0
    nums = input('Type 7 numbers with a space in between\n ENTRY: ')
    nums = nums.split()
    for num in range(7):
        sum += int(nums[num])
        if int(nums[num]) > 0:
            pos += 1
        elif int(nums[num]) < 0:
            neg += 1
        else:
            zero += 1


    print(f'sum: {sum}')
    print(f'Zero: {zero}')
    print(f'Positive: {pos}')
    print(f'Negative: {neg}')

if num8:
    player_nums()

# 9
num9 = False

n_list = [0, 1]


heads = 0
tails = 0

if num9:
    for num in range(50):
        random_int = random.choice(n_list)
        if random_int == 0:
            heads += 1
            print('Heads')
        else:
            tails += 1
            print('Tails')
    print(f'Heads: {heads}\nTails: {tails}')





