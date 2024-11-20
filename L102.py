# L102
# Mairi Weber-Hess, Aliza Litvak
from email.policy import default

# B – CPSC dictionary

name_dict = {"Laneman":"Margaret", "DeYoung": "Lily", "Schuler":"Serenity", "Beck":"Olivia",
             "Hand":"Colleen", "Raycroft":"Anna", "Garcia Jimenez":"Victoria", "Gangwer":"Gwyneth",
             "Weber-Hess":"Mac", "Litvak":"Aliza", "Wyatt":"Elizabeth", "Taylor":"Rylee"}

def classmates(mydict):
    d = dict()
    for lastname in mydict:
        if mydict[lastname] not in d:
            d[mydict[lastname]] = 1
        else:
            d[mydict[lastname]] += 1
    return d

classmates = classmates(name_dict)

def inverse_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse

frequency = inverse_dict(classmates)
print(frequency)

def frequency(mydict):
    def classmates(mydict):
        d = dict()
        for lastname in mydict:
            if mydict[lastname] not in d:
                d[mydict[lastname]] = 1
            else:
                d[mydict[lastname]] += 1
        return d
    mydict = classmates(mydict)

    def inverse_dict(d):
        inverse = dict()
        for key in d:
            val = d[key]
            if val not in inverse:
                inverse[val] = [key]
            else:
                inverse[val].append(key)
        return inverse
    result = inverse_dict(mydict)
    print(result)

frequency(name_dict)