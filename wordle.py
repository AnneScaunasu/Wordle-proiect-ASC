f = open("cuvinte.txt", 'r')
g = open("solutii.text", 'w')
v = [list(x) for x in f.readlines() if x != "\n"]

# programul intern

import math

for x in v:
    del x[len(x) - 1]
fr1 = {}
fr2 = {}
fr3 = {}
fr4 = {}
fr5 = {}
frl = {}
for x in range(26):
    fr1[chr(65 + x)] = 0
for x in v:
    fr1[x[0]] += 1
# print(f"Prima pozitie:\n{fr1}")

for x in range(26):
    fr2[chr(65 + x)] = 0
for x in v:
    fr2[x[1]] += 1
# print(f"A doua pozitie:\n{fr2}")

for x in range(26):
    fr3[chr(65 + x)] = 0
for x in v:
    fr3[x[2]] += 1
# print(f"A treia pozitie:\n{fr3}")

for x in range(26):
    fr4[chr(65 + x)] = 0
for x in v:
    fr4[x[3]] += 1
# print(f"A patra pozitie:\n{fr4}")

for x in range(26):
    fr5[chr(65 + x)] = 0
for x in v:
    fr5[x[4]] += 1
# print(f"A cincea pozitie:\n{fr5}")

for x in range(26):
    frl[chr(65 + x)] = 0
for x in v:
    for i in range(5):
        frl[x[i]] += 1
# print(f"Frecventa literelor in dictionarul dat este:\n{frl}")


pr = {}
for x in range(26):
    pr[chr(65 + x)] = 0
for x in frl:
    pr[x] = frl[x] / (len(v) * 5)
# print(f"Probabilitatea ca fiecare litera din alfabet sa apara in fisier este:\n{pr}")


pr_cuv = {}
for x in v:
    pr_cuv["".join(x)] = fr1[x[0]] / len(v)
    pr_cuv["".join(x)] += fr2[x[1]] / len(v)
    pr_cuv["".join(x)] += fr3[x[2]] / len(v)
    pr_cuv["".join(x)] += fr4[x[3]] / len(v)
    pr_cuv["".join(x)] += fr5[x[4]] / len(v)
    pr_cuv["".join(x)] /= 5

# rezolvare

nr = 0
x=list(input())
nr_ok = 0
corect = ["_", "_", "_", "_", "_"]
in_cuv0 = []
in_cuv1 = []
in_cuv2 = []
in_cuv3 = []
in_cuv4 = []
not_in_cuv = set()
j=0
while True:
    if j == 0:
        CUVANT = ['C', 'A', 'R', 'E', 'I']
    elif j == 1:
        CUVANT = ['S', 'O', 'T', 'U', 'L']
    else:
        for i in sorted(pr_cuv, key=pr_cuv.get, reverse=True):
            ok1 = 0
            ok2 = 0
            ok3 = 0
            for k in range(5):
                if i[k] not in not_in_cuv:
                    ok1 += 1
            for k in range(len(in_cuv0)):
                if (in_cuv0[k] in i) and i[0] != in_cuv0[k]:
                    ok2 += 1
            for k in range(len(in_cuv1)):
                if (in_cuv1[k] in i) and i[1] != in_cuv1[k]:
                    ok2 += 1
            for k in range(len(in_cuv2)):
                if (in_cuv2[k] in i) and i[2] != in_cuv2[k]:
                    ok2 += 1
            for k in range(len(in_cuv3)):
                if (in_cuv3[k] in i) and i[3] != in_cuv3[k]:
                    ok2 += 1
            for k in range(len(in_cuv4)):
                if (in_cuv4[k] in i) and i[4] != in_cuv4[k]:
                    ok2 += 1
            for k in range(5):
                if corect[k] == '_' or corect[k] == i[k]:
                    ok3 += 1
            if ok1 == 5 and ok2 == nr_ok and ok3 == 5:
                l = []
                l.extend(i)
                CUVANT = l
                break
    print(str("".join(CUVANT)),end="")
    if CUVANT == x:
        print(f" ({j + 1} incercari)\n")
        break
    print(" -> ",end="")
    for i in range(5):
        if CUVANT[i] == x[i]:
            corect[i] = CUVANT[i]
        elif CUVANT[i] in x:
            nr_ok += 1
            if i==0:
                in_cuv0.append(CUVANT[i])
            elif i==1:
                in_cuv1.append(CUVANT[i])
            elif i==2:
                in_cuv2.append(CUVANT[i])
            elif i==3:
                in_cuv3.append(CUVANT[i])
            elif i==4:
                in_cuv4.append(CUVANT[i])
        else:
            not_in_cuv.add(CUVANT[i])
    j+=1
for x in v:
    nr_ok = 0
    g.write("\n")
    corect = ["_", "_", "_", "_", "_"]
    in_cuv0 = []
    in_cuv1 = []
    in_cuv2 = []
    in_cuv3 = []
    in_cuv4 = []
    not_in_cuv = set()
    g.write(str("".join(x)))
    g.write(': ')
    j=0
    while True:
        if j == 0:
            CUVANT = ['C', 'A', 'R', 'E', 'I']
        elif j == 1:
            CUVANT = ['S', 'O', 'T', 'U', 'L']
        else:
            for i in sorted(pr_cuv, key=pr_cuv.get, reverse=True):
                ok1 = 0
                ok2 = 0
                ok3 = 0
                for k in range(5):
                    if i[k] not in not_in_cuv:
                        ok1 += 1
                for k in range(len(in_cuv0)):
                    if (in_cuv0[k] in i) and i[0] != in_cuv0[k]:
                        ok2 += 1
                for k in range(len(in_cuv1)):
                    if (in_cuv1[k] in i) and i[1] != in_cuv1[k]:
                        ok2 += 1
                for k in range(len(in_cuv2)):
                    if (in_cuv2[k] in i) and i[2] != in_cuv2[k]:
                        ok2 += 1
                for k in range(len(in_cuv3)):
                    if (in_cuv3[k] in i) and i[3] != in_cuv3[k]:
                        ok2 += 1
                for k in range(len(in_cuv4)):
                    if (in_cuv4[k] in i) and i[4] != in_cuv4[k]:
                        ok2 += 1
                for k in range(5):
                    if corect[k] == '_' or corect[k] == i[k]:
                        ok3 += 1
                if ok1 == 5 and ok2 == nr_ok and ok3 == 5:
                    l = []
                    l.extend(i)
                    CUVANT = l
                    break
        g.write(str("".join(CUVANT)))
        if CUVANT == x:
            nr = nr+j+1
            g.write(f" ({j + 1} incercari)\n")
            break
        g.write(" -> ")
        for i in range(5):
            if CUVANT[i] == x[i]:
                corect[i] = CUVANT[i]
            elif CUVANT[i] in x:
                nr_ok += 1
                if i==0:
                    in_cuv0.append(CUVANT[i])
                elif i==1:
                    in_cuv1.append(CUVANT[i])
                elif i==2:
                    in_cuv2.append(CUVANT[i])
                elif i==3:
                    in_cuv3.append(CUVANT[i])
                elif i==4:
                    in_cuv4.append(CUVANT[i])
            else:
                not_in_cuv.add(CUVANT[i])
        j+=1
nr /= len(v)
g.write(f"Programul face aproximativ {nr:.2f} incercari pentru a gasi un cuvant")
f.close()
g.close()
