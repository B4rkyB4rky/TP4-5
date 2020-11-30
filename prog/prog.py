def valeur(char):
    val = 0
    if char == 'I':
        val += 1
    if char == 'V':
        val += 5
    if char == 'X':
        val += 10
    if char == 'L':
        val += 50
    if char == 'C':
        val += 100
    if char == 'D':
        val += 500
    if char == 'M':
        val += 1000

    return val

def valeur_totale(char):
    total = 0
    for i in range(0, len(char)):
        if i != len(char)-1:
            if valeur(char[i + 1]) > valeur(char[i]):
                total += (valeur(char[i+1]) - valeur(char[i]))


        total += valeur(char[i])


    return total
