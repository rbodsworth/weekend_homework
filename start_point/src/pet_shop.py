# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(shop):
    return shop ["name"]

def get_total_cash(total):
    return total["admin"]["total_cash"]

def add_or_remove_cash(shop, sale):
    shop ["admin"]["total_cash"] += sale 

def get_pets_sold(shop):
    return shop ["admin"]["pets_sold"]

def increase_pets_sold(sale, pets):
    sale["admin"]["pets_sold"] += pets

def get_stock_count(shop):
    return len(shop["pets"])

def get_pets_by_breed(shop, breed):
    pets = []
    for pet in shop ["pets"]:
        if pet ["breed"] == breed:
            pets.append(pets)

    return pets 

def find_pet_by_name(shop, name):
    for pet in shop ["pets"]:
        if pet ["name"] == name:
            return pet 

def remove_pet_by_name(shop, name):
    dictionary_key = 0 
    for pet in shop ["pets"]:
        if pet ["name"] == name:
            shop ["pets"].pop(dictionary_key)
        dictionary_key += 1 

def add_pet_to_stock(shop, new_pet):
        shop ["pets"].append(new_pet)

def get_customer_cash(customer):
        return customer["cash"]

def remove_customer_cash(customer, amount):
    customer ["cash"] -= amount

def get_customer_pet_count(customer):
    return len(customer["pets"])
    
def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)

