import random
import time
import sys
import math
sys.setrecursionlimit(1000000)


class generator:
    tab = []
    max_wartosc = 2000000

    def losowe(self, rozmiar):
        self.tab = []
        for i in range(rozmiar):
            self.tab.append(random.randint(0, self.max_wartosc))

    def rosnące(self, rozmiar):
        self.tab = []
        for i in range(rozmiar):
            self.tab.append(i)

    def malejace(self, rozmiar):
        self.tab = []
        for i in range(rozmiar, 0, -1):
            self.tab.append(i)

    def stale(self,rozmiar):
        self.tab = []
        x = random.randint(0,self.max_wartosc)
        for i in range(rozmiar):
            self.tab.append(x)

    def aKsztaltne(self, rozmiar):
        self.tab = []
        j = 0
        for i in range(rozmiar//2):
            j += 1
            self.tab.append(i)
        if rozmiar %2 == 1:
            self.tab.append(j)
        for i in range(rozmiar//2):
            j -= 1
            self.tab.append(j)

def selectionSort(lista):
    for i in range(len(lista)-1):
        temp = lista[i]
        index = i
        for j in range(i, len(lista)):
            if temp > lista[j]:
                temp = lista[j]
                index = j
        if i != index:
            lista[index], lista[i] = lista[i], lista[index]
    return lista

def insertionSort(lista):
    for i in range(1, len(lista)):
        for j in range(i, 0, -1):
            if lista[j] < lista[j-1]:
                lista[j], lista[j-1] = lista[j-1], lista[j]
            else:
                break
    return lista

def quickSortRandom(lista):
    if len(lista) > 1:
        i = 0
        j = len(lista)-1
        x = lista[random.randint(0,j)]
        while True:
            while lista[i] < x:
                i += 1
            while lista[j] > x:
                j -= 1
            if i == j:
                return quickSortRandom(lista[:i])+[lista[i]]+quickSortRandom(lista[i+1:])
            elif i < j:
                lista[i], lista[j] = lista[j], lista[i]
                i += 1
                j -= 1
            elif i > j:
                return quickSortRandom(lista[:j+1])+quickSortRandom(lista[i:])
    else:
        return lista

def quickSortLeft(lista):
    if len(lista) > 1:
        i = 0
        j = len(lista)-1
        x = lista[0]
        while True:
            while lista[i] < x:
                i += 1
            while lista[j] > x:
                j -= 1
            if i == j:
                return quickSortLeft(lista[:i])+[lista[i]]+quickSortLeft(lista[i+1:])
            elif i < j:
                lista[i], lista[j] = lista[j], lista[i]
                i += 1
                j -= 1
            elif i > j:
                return quickSortLeft(lista[:j+1])+quickSortLeft(lista[i:])
    else:
        return lista

def skok(n):
    i = 1
    kroki = []
    while (3**i-1)/2 <= math.ceil(n/3):
        kroki.append(int((3**i-1)/2))
        i += 1
    return kroki[::-1]

def shellSort(lista):
    kroki = skok(len(lista))
    for i in kroki:
        for z in range(0, i):
            for j in range(z, len(lista),i):
                for k in range(j, z, -i):
                    if lista[k] < lista[k - i]:
                        lista[k], lista[k - i] = lista[k - i], lista[k]
                    else:
                        break
    return lista

def createHeap(lista):
    for i in range((len(lista)-1)//2, 0, -1):
        length=len(lista)
        j = i
        max_parent = (length-1)//2
        while j <= max_parent:
            child = j * 2
            if child > length:
                break
            if child + 1 < length and lista[child] < lista[child + 1]:
                child += 1
            if lista[j] < lista[child]:
                lista[j], lista[child] = lista[child], lista[j]
                j = child
            else:
                break
    return lista

def heapSort(lista):
    lista = createHeap([0]+lista)
    length = len(lista)
    k = 0
    for i in range(1,length-1):
        lista[1], lista[length-1-k] = lista[length-1-k], lista[1]
        k += 1
        j = 1
        while True:
            child = j*2
            if child > length-k:
                break
            if child+1 < length-k and lista[child] < lista[child+1]:
                child += 1
            if lista[j] < lista[child]:
                lista[j], lista[child] = lista[child], lista[j]
                j = child
            else:
                break
    return lista[1:]

tab = generator()
alg = ["selectionSort", "insertionSort", "shellSort", "heapSort", "quickSortRandom", "quickSortLeft"]
typ = ["losowe", "rosnące", "malejace","stale","aKsztaltne"]
rozmiar = {alg[0]:5000, alg[1]:5000, alg[2]:5000, alg[3]:50000, alg[4]:50000, alg[5]:50000}
file = open('wyniki.txt', 'w')
for i in alg:
    file.write("***"+i+"***\n")
    for j in typ:
        file.write(j+"\n")
        for k in range(rozmiar[i], rozmiar[i]*11, rozmiar[i]):
            try:
                getattr(tab, j)(k)
                start = time.time()
                globals()[i](tab.tab)
                koniec = time.time()-start
                file.write(str(k)+"\t"+str(koniec)+"\n")
                print(koniec)
            except Exception as error:
                file.write(str(k) + "\t---\n")
                break
file.close()