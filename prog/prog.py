def valeur(char):
    val = 0
    if char == '':
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
    cpt = 0
    l = len(char)
    while cpt < l:
        if cpt < l - 1:
            if valeur(char[cpt+1]) > valeur(char[cpt]):
                total += valeur(char[cpt+1]) - valeur(char[cpt])
                cpt = cpt + 2
            else:
                total += valeur(char[cpt])
                cpt += 1

        else:
            total += valeur(char[cpt])
            cpt += 1

    return total

def calculatrice(operateur,char1,char2):
    if operateur == '-':
        return valeur_totale(char1) - valeur_totale(char2)
    if operateur == '+':
        return valeur_totale(char1) + valeur_totale(char2)
    if operateur == '*':
        return valeur_totale(char1) * valeur_totale(char2)
    if operateur == '/':
        if valeur_totale(char2) == 0:
            return "erreur"
        else:
            return valeur_totale(char1) / valeur_totale(char2)
