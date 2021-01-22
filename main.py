'''
 # Functia care trece prin cuvant
def verificare(tranzitii, start, final, sir):
    stare = start;
    for i in sir:
        stare = tranzitii[stare][i]
    return str(stare) in final

ok = True
d = {} # Un dictionar
n = int(input("Stari : "))
q = int(input("Starea initiala : "))
f = str(input("Starea finala : "))
f = f.split() # S-ar putea sa fie mai multe stari finale
for i in range(1, n + 1):
    x = str(input()) # Citim de la starea 0, x reprezinta legatura, iar y starea in care se ajunge, sigur trebuie sa fie cel putin o legatura
    y = int(input())
    d[i] = {x : y}
    while ok == True:
        x = str(input())
        if x == '-1': #Citim restul, ca sa trecem la urmatoarea stare introducem -1
            break
        y = int(input())
        d[i].update({x : y}) # Updatam dictionarul, care este ceva de genul d = {0 : {'a' : 1, 'b' : 0}, 1 : {'a' : 1, 'b' : 2}....}
s = str(input("Sir : "))
print(verificare(d, q, f, s))


'''
nfin = []  # Lista pentru stari nefinale
fin = []  # Lista pentru stari finale
ok = True
d = {}  # Un dictionar
n = int(input("Stari : "))
q = int(input("Starea initiala : "))
f = str(input("Starea finala : "))
f = f.split()  # S-ar putea sa fie mai multe stari finale
fi = []
for i in range(1, n + 1):
    if str(i) in f:
        fin.append(i)
    else:
        nfin.append(i)
for i in range(1, n + 1):
    x = str(input())
    y = int(input())
    d[i] = {x: y}
    while ok == True:
        x = str(input())
        if x == '-1':  # Citim restul, ca sa trecem la urmatoarea stare introducem -1
            break
        y = int(input())
        d[i].update({x: y})  # Updatam dictionarul, care este ceva de genul d = {0 : {'a' : 1, 'b' : 0}, 1 : {'a' : 1, 'b' : 2}....}
s = []  # O lista ce va contine doua liste, una cu starile finale, alta cu starile nefinale
s.append(fin)
s.append(nfin)
ok = 1
while ok == 1:
    ok = 0
    i = 0
    while i < len(s):  # Luam pe rand fiecare lista din lista s
        j = 0
        while j < (len(s[i]) - 1):
            jj = j + 1
            while jj < len(s[i]):
                a = d[s[i][j]]['a']
                b = d[s[i][j]]['b']
                aa = d[s[i][jj]]['a']
                bb = d[s[i][jj]]['b']
                for poz in range(len(s)):  # Aflam pozitiile unde duc starile in functie de 0 sau 1
                    if a in s[poz]:
                        apoz = poz
                    if b in s[poz]:
                        bpoz = poz
                    if aa in s[poz]:
                        aapoz = poz
                    if bb in s[poz]:
                        bbpoz = poz
                if apoz != aapoz or bpoz != bbpoz:  # Daca nu se mai afla in aceeasi lista, stergem elementul si cream o noua lista cu el
                    s.append([s[i][jj]])
                    s[i].remove(s[i][jj])
                    ok = 1
                jj += 1
            j += 1
        i += 1
ns = []  # Vector cu stari
for i in range(len(s)):
    ch = ""
    for j in range(len(s[i])):
        ch += str(s[i][j]);
    ns.append(ch)
dn = {}  # Dictionarul final
for i in range(len(s)):
    for j in range(len(s[i])):
        p = d[s[i][j]]['a']
        pp = d[s[i][j]]['b']
        for j in ns:
            if str(p) in j:
                valoare1 = j
                break
        for j in ns:
            if str(pp) in j:
                valoare2 = j
                break
        dn[ns[i]] = {'a': valoare1}
        dn[ns[i]].update({'b': valoare2})
for i in range(len(ns)):
    if dn[ns[i]]['a'] == ns[i] and dn[ns[i]]['b'] == ns[i]:
        del dn[ns[i]]
print(dn)
