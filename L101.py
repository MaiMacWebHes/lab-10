# L101
# Mac Weber-Hess, Aliza Litvak

# A – Write the get method yourself

mydict = {"un" : 1, "deux" : 2, "trois": 3, "quatre" : 4, "cinq" : 5, "six" : 6}

def my_get_method(d,g):
    if g in d:
        print(d[g])
    else:
        # print("dne")
        print(0)

my_get_method(mydict,"deux")

print(mydict.get("deux",0))