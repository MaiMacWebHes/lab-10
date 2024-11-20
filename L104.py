# L104
# Mairi Weber-Hess, Aliza Litvak

red = {"flour" : 1.5, "sugar" : 0.5, "eggs" : 3, "baking powder" : 2, "baking soda" : 1, "red food dye" : 10 , "cocoa powder" : 1.5}
lemon = {"flour" : 2, "sugar" : 0.5, "eggs" : 3, "baking powder" : 2, "baking soda" : 1, "lemon juice" : 1 , "lemon zest" : 3}

def recipe_compare(x,y):
    for key in x:
        if key in y:
            print(key)

recipe_compare(red,lemon)
