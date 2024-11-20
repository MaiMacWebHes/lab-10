# L103
# Mairi Weber-Hess, Aliza Litvak

# C — CPSC List

name_dict = {"Laneman":"Margaret", "DeYoung": "Lily", "Schuler":"Serenity", "Beck":"Olivia",
             "Hand":"Colleen", "Raycroft":"Anna", "Garcia Jimenez":"Victoria", "Gangwer":"Gwyneth",
             "Weber-Hess":"Mac", "Litvak":"Aliza", "Wyatt":"Elizabeth", "Taylor":"Rylee"}

last = sorted(name_dict)
first = sorted(name_dict.values())

index = 1
x = 1
y = 1
name_list = []
while index < len(first):
    for name in first:
        if name not in name_list:
            name_list.extend([first[x],last[y]])
            x += 1
            y += 1
            index += 1
        else:
            index += 1

def frequency_odds(x):
    d = dict()
    for name in x[1::2]:
        if name[0] not in d:
            d[name[0]] = 1
        else:
            d[name[0]] += 1
    return d

def frequency_evens(x):
    d = dict()
    for name in x[::2]:
        if name[0] not in d:
            d[name[0]] = 1
        else:
            d[name[0]] += 1
    return d

l = frequency_evens(name_list)
f = frequency_odds(name_list)
print(l)
print(f)