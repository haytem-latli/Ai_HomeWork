# from operator import index
import array

# BF = ["pommes", "eufs", "poires", "abricots", "farine", "beurre", "sucre", "sel"]
# BR_action = ["pate", "tarte sucrees", "tarte aux", "tarte abricots", "tarte poires", "tarte cerises"]
# BR_premisse = [["farine", "beurre"], ["pommes", "sucre"], ["sucrees", "pate"], ["abricots", "pate"], ["poires", "pate"],
#                ["cerises", "pate"]]
BF = []
BR_action = []
BR_premisse = []
LR = []


def index(p, table):
    i = 0
    while i < len(table):
        if p == table[i]:
            return i
        i = i + 1
    return None


def Bc(bf, br_action, br_premisse, but):
    if bf.__contains__(but):
        print("le but courant est prouve")
    else:
        if not br_action.__contains__(but):
            print("impossible de prouve le but courant ")
        else:
            i = index(but, br_action)
            x = br_premisse[i]
            j = 0
            while j < len(x):
                if bf.__contains__(x[j]):
                    print("condition : " + x[j] + " -> vérifiées")
                    br_premisse[i].pop(j)
                    j -= 1
                else:
                    if br_action.__contains__(x[j]):
                        print("Sous but : " + x[j])
                        Bc(bf, br_action, br_premisse, x[j])
                    else:
                        print("Sous but : " + x[j] + " impossible de prouve")
                        print("impossible de prouve le but courant ")
                        break
                j += 1
                if len(x) == 0:
                    bf.append(but)
                    print("le but courant est prouve")
                    break


def Fc(bf, br_action, br_premisse, but, regle):
    if but is None:
        i = 0
        while i < len(br_premisse) and i <= regle - 1:
            x = br_premisse[i]
            b = True
            for c in x:
                if not bf.__contains__(c):
                    b = False
                    break
            if b:
                bf.append(br_action[i])
                print(bf)
                print("la Regle" + (i + 1).__str__() + " est applicable")
            else:
                print("la Regle " + (i + 1).__str__() + " n'est pas applicable")
            i += 1
    else:
        i = 0
        while i < len(br_premisse):
            x = br_premisse[i]
            b = True
            for c in x:
                if not bf.__contains__(c):
                    b = False
                    break
            if b:
                bf.append(br_action[i])
                if br_action[i].__eq__(but):
                    print("le but est vérifier")
                    break
            else:
                print("la Regle " + (i + 1).__str__() + " n'est pas applicable")
            i += 1
        if i == len(br_premisse):
            print("le but n'est pas vérifier")


print("entrer Votre Base de Connaissance")
print("1- Base de faits : (entrez 'finie' quand vous avez fini)")
b = True
while b:
    F = input()
    if not F.__contains__(" "):
        if not F.__eq__("finie"):
            BF.append(F)
        else:
            b = False
    else:
        print("Erreur d'entrée")

print("2- Base de regles : (entrez 'finie' quand vous avez fini)")
b = True
j = 0
while b:
    F = input()
    i = 2
    x = []
    A = ""
    if not F.__eq__("finie"):
        T = F.split()
        if T[0].__eq__("Si") and not T[1].__eq__("Alors") and not T[1].__eq__("et"):
            x.append(T[1])
            while i < len(T):
                if T[i].__eq__("Alors"):
                    if not i == len(T) - 1:
                        A = T[i + 1]
                    else:
                        print("Erreur d'entrée")
                        break
                else:
                    if T[i].__eq__("et"):
                        if T[i + 1] is not None and not T[i + 1].__eq__("et"):
                            x.append(T[i + 1])
                        else:
                            print("Erreur d'entrée")
                            break
                i += 1
                if i == len(T):
                    LR.append(F)
                    BR_action.append(A)
                    BR_premisse.append(x)
                    j += 1
        else:
            print("Erreur d'entrée")
    else:
        b = False

while True:
    print("1-verifier une regle")
    print("2-verifier un but")
    print("3-quittez")
    choix = input()
    if choix == "1":
        i = 0
        for x in LR:
            print("R" + (i + 1).__str__() + " : " + x)
            i += 1
        print("choisis une regle")
        rule = input()
        Fc(BF, BR_action, BR_premisse, None, int(rule))
    else:
        if choix == "2":
            print("choisis une but")
            but = input()
            print("1-chaînage Avant")
            print("2-chaînage Arrière")
            print("choisis une method")
            method = input()
            if method == "1":
                Fc(BF, BR_action, BR_premisse, but, "")
            else:
                if method == "2":
                    Bc(BF, BR_action, BR_premisse, but)
                else:
                    print("Erreur d'entrée")
        else:
            if choix == "3":
                break
            else:
                print("Erreur d'entrée")
