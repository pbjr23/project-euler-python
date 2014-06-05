from mathtools import alphabet_dictionary

def pr22(file):
    lookup = alphabet_dictionary()
    score = 0
    fin = open(file)
    list_names = eval("[" + fin.read() + "]") 
    list_names.sort()
    for name in range(len(list_names)):
        value = 0
        for letter in list_names[name]:
            value += lookup[letter.lower()]
        score += value * (name + 1)
    return score

print pr22('pr22.txt')
