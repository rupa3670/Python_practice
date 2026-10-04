def total_cost(price_per_kg, kg):
    return price_per_kg * kg

def is_sweet(fruit):
    sweet_fruits = ["Mango","Litchi","Banana"]
    if fruit in sweet_fruits:
        return True
    else:
        return False
print("Cost of 2 kg mango:", total_cost (150,2), "Taka")
print("Is Mango sweet?", is_sweet("Mango"))  
print("Is Lemon sweet?", is_sweet("Lemon"))          
