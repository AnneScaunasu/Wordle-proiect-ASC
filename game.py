import random

f = open("cuvinte.txt", 'r')
v = [x for x in f.readlines() if x != "\n"]
nr = random.randint(0, 11454)
CUVANT = list(v[nr])
del CUVANT[len(CUVANT) - 1]
cuv1 = []
k = 1
while cuv1 != CUVANT:
    ok = 0
    r = 1
    print(f"\033[3;37;40m Introduceti cuvantul de 5 litere(de tipar)")
    while r == 1:
        okk = 0
        cuv1 = list(input())
        cuv1.append("\n")
        if len(cuv1) != 6 or ("".join(cuv1) not in v):
            print(f'\033[3;37;40m Cuvantul dat nu este corect.Reintroduceti un cuvant.')
        else:
            for i in range(5):
                if not (cuv1[i] >= 'A' and cuv1[i] <= 'Z'):
                    print(f'\033[3;37;40m Cuvantul dat nu este corect.Reintroduceti un cuvant.')
                    okk = 1
                    break
            if okk == 0:
                r = 0
    for i in range(5):
        if CUVANT[i] == cuv1[i]:
            print(f"\033[3;32;40m {cuv1[i]}", end=' ')  # print("\033[1;32;40m Bright Green
            ok += 1
        elif cuv1[i] in CUVANT:
            print(f'\033[3;33;40m {cuv1[i]}', end=' ')
        else:
            print(f'\033[3;37;40m {cuv1[i]}', end=' ')
    print()
    if ok == 5:
        print(f"Ai gasit cuvantul in {k} incercari!")
        break
    k+=1
f.close()
