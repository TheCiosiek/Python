import os
def get_values():
    while True:
        try:
            values=input("Wpisz wartości oddzielone spacją.\n")
            if not values:
                raise ValueError
        except:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Nie wprowadzono żanej liczby, spróbuj jeszcze raz")
        else:
            break
    values=values.split()
    return values

def values_to_int(values):
    str_in_values=0
    while True:
        if str_in_values:
            values=get_values()
        try:
            for i in range (0, len(values)):
                values[i]=int(values[i])
        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            str_in_values=1
            print("Wprowadzono znak, a nie liczbę. Spróbuj jeszcze raz.")
        else:
            str_in_values=0
            break
    return values

def get_max(list):
    max=list[0]
    for i in list:
        if i>max:
            max=i
    return max

def get_sum(list):
    sum=0
    for i in list:
        sum+=i
    return sum

def get_min(list):
    min=list[0]
    for i in list:
        if i<min:
            min=i
    return min

def points_list(points):
    list=get_values()
    list=values_to_int(list)
    points[0]=get_sum(list)
    points[1]=get_max(list)
    points[2]=get_min(list)
    return points



    
again=1
while again==1:
    os.system('cls' if os.name == 'nt' else 'clear')
    points=[0]*3
    points=points_list(points)
    print(points)
    again=int(input('(1) Powtórzyć\n(0) Wyjść\nTwoja decyzja: '))