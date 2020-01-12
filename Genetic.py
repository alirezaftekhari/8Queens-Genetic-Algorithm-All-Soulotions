import random
def getHuristic(li):
    huristic = []
    for i in range(len(li)):
        j = i - 1
        huristic.append(0)
        while j >= 0:
            if li[i] == li[j] or (abs(li[i] - li[j]) == abs(i - j)):
                huristic[i] += 1
            j -= 1
        j = i + 1
        while j < len(li):
            if li[i] == li[j] or (abs(li[i] - li[j]) == abs(i - j)):
                huristic[i] += 1
            j += 1
    return huristic
def getFitness(li):
    clashes = 0
    for i in range(len(li) - 1):
        for j in range(i + 1, len(li)):
            if li[i] == li[j]:
                clashes += 1
    for i in range(len(li) - 1):
        for j in range(i + 1, len(li)):
            if abs(li[j] - li[i]) == abs(j - i):
                clashes += 1
    return 28 - clashes
def buildKid(li1, li2, crossOver):
    new = []
    for i in range(crossOver):
        new.append(li1[random.randint(0, 7)])
    for i in range(crossOver, 8):
        new.append(li2[random.randint(0, 7)])
    return new
def changeChilds(co):
    global father, mother, child1, child2, crossover
    crossover = co
    child1 = buildKid(father, mother, crossover)
    child2 = buildKid(mother, father, crossover)
def changeChromosome(li):
    global crossover, father, mother
    newchange = -1
    while newchange != 0:
        newchange = 0
        tmpli = li
        getHur = getHuristic(tmpli)
        index = getHur.index(max(getHur))
        maxFitness = getFitness(tmpli)
        for i in range(1, 9):
            tmpli[index] = i
            if getFitness(tmpli) > maxFitness:
                maxFitness = getFitness(tmpli)
                newchange = i
            tmpli = li
        if newchange == 0:
            for i in range(len(li) - 1):
                for j in range(i + 1, len(li)):
                    if li[i] == li[j]:
                        li[j] = random.randint(1, 8)
        else:
            li[index] = newchange

c = 0
all = []
while c < 92:
    crossover = 4
    father = []
    mother = []
    for i in range(8):
        father.append(random.randint(1, 8))
        mother.append(random.randint(1, 8))
    fitnessFather = getFitness(father)
    fitnessMother = getFitness(mother)
    while fitnessFather != 28 and fitnessMother != 28:
        changeChilds(crossover)
        changeChromosome(child1)
        changeChromosome(child2)
        fitnessFather = getFitness(child1)
        fitnessMother = getFitness(child2)
        father = child1
        mother = child2
        print(father)
        print(mother)
    if getFitness(father) == 28:
        if father not in all:
            all.append(father)
            c += 1
    else:
        if mother not in all:
            all.append(mother)
            c += 1
print(len(all))
print("**********All solutions**********")
for i in all:
    print(i)
print("*********************************")