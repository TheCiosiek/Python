def menu():
    dt.load_products()
    while dt.auth[0]==True:
        #option = options()
        #TODO
        if option == 1:
            #add_product()
            #TODO
            pass
        elif option == 2:
            #del_product()
            #TODO
            pass
        elif option == 3:
            #change_product()
            #TODO
            pass
        elif option == 4:
            return
        elif option == 6:
            dt.auth=False, "user"
        elif option == 7:
            dt.auth = None, "user"

def options():
    #TODO
    pass

def add_product():
    #TODO
    pass

def del_product():
    #TODO
    pass

def change_product():
    #TODO
    pass