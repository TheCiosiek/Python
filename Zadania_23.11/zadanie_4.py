import random
def roll_two_dice_times(n):
    cnt=0
    for i in range(n):
        roll_1=random.randint(1,6)
        roll_2=random.randint(1,6)
        if roll_1==roll_2:
            cnt+=1

    print(f"Rzucono {n} razy dwoma kostkami, te same wartości wypadły {cnt} razy.")
        

i=int(input("Ile razy rzucić kostką: "))
roll_two_dice_times(i)