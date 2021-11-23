import random
def roll_dice_times(n,dots,rolls):
    cnt=0
    for i in range(n):
        if random.randint(1,6) == dots:
            cnt+=1
    if cnt>=rolls:
        return True
    else:
        return False

i=int(input("Ile razy rzucić kostką: "))
j=int(input("Jaka wartość oczekiwana: "))
k=int(input("Ile razy musi wypaść: "))
isTrue=roll_dice_times(i,j,k)
confirmation="nie "
if isTrue:
    confirmation=""
print(f"Rzucono {i} razy kostką, oczekiwana wartość ({j}) {confirmation}wypadła przynajmniej {k} razy.")

