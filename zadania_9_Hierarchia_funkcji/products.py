def menu():
    dt.load_products()
    while dt.auth[0]==True:
        option = options()
        if option == 1:
            change_product()
        elif option == 2:
            add_product()
        elif option == 4:
            return
        elif option == 6:
            dt.auth=False, "user"
        elif option == 7:
            dt.auth = None, "user"