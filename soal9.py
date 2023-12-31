list1 = ["Bagas", "Dimas", "Bagas", "Bagas", "Indra", "Gilang", "Gilang", "Hana", "Fajar", "Fajar"]
list2 = ["Bagas", "Dimas", "Fajar", "Bagas", "Indra", "Gilang", "Gilang", "Bagas", "Fajar", "Fajar"]
list3 = ["Aisyah" , "Bagas", "Dewi", "Dimas", "Eka", "Fajar", "Gilang" , "Hana", "Indra", "Jihan"] 

def makeDictionary(L):
    D = {}
    for i in L:
        if i not in D:
            D[i] = 1
        else:
            D[i] += 1
    return D

dict1 = makeDictionary(list1)
dict2 = makeDictionary(list2)
dict3 = makeDictionary(list3)

dict1 = dict(sorted(dict1.items(), key=lambda item:item[1], reverse=True))
dict2 = dict(sorted(dict2.items(), key=lambda item:item[1], reverse=True))
dict3 = dict(sorted(dict3.items(), key=lambda item:item[1], reverse=True))

person1 = [ k for k,v in dict1.items() if v == list(dict1.values())[0] and v > 1]
person2 = [ k for k,v in dict2.items() if v == list(dict2.values())[0] and v > 1]
person3 = [ k for k,v in dict3.items() if v == list(dict3.values())[0] and v > 1]

person = [person1, person2,person3]

for p in person:
    if len(p) == 1:
        print(p[0], "Nackal")
    elif len(p) == 2:
        print(f"{p[0]} dan {p[1]} Nackal")
    elif len(p) == 3:
        print(f"{p[0]}, {p[1]}, dan {p[2]} Nackal")
    else:
        print("Semuanya anak baik")
        