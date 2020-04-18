from City import *
import math
import random

class TSP:

    def __init__(self, n, dist):
        self.n = n
        self.dist = [[]]
        self.cities = []

    def eucliadinanDistance(self, a, b):
        return round (math.sqrt( (b.getX()-a.getX())*(b.getX()-a.getX()) + (b.getY()-a.getY())*(b.getY()-a.getY()) ), 2)

    def printResults(self):
        g = open("results.txt", "w")
        for i in range (self.n):
            for j in range (self.n):
                g.write(str(self.dist[i][j]))
                g.write(" ")
            g.write("\n")
        #g.write(self.dist)

    def calculateDistances(self):
        self.dist = [[0 for j in range(self.n+1)] for i in range(self.n+1)]
        for i in range (self.n):
            for j in range (i+1, self.n-1):
                self.dist[i+1][j+1] = self.eucliadinanDistance(self.cities[i], self.cities[j])
                self.dist[j + 1][i + 1] = self.eucliadinanDistance(self.cities[i], self.cities[j])
        #for checking distances
        #self.printResults()

    def readFromFile(self):
        #f = open ("lessValues.txt", "r")
        f = open("values.txt", "r")
        buffer = 0
        for i in range (6):
            buffer = f.readline()

        self.n = 0
        for buffer in f:
            elements = buffer.split()
            if ( len(elements) == 3 ):
                self.cities.append( City(elements[0], elements[1], elements[2]))
                self.n = self.n + 1


        #for city in self.cities:
           # print(city.getCity())

        #print(self.n)

        self.calculateDistances()

    def generateSolution(self):
        c = []
        for i in range (1, self.n+1):
            c.append(i)
        random.shuffle(c)
        return c

    def fitness(self, tour):
        fit = 0
        print("ruta este ", tour)
        for i in range (0, self.n-1):
            fit = fit + self.dist[tour[i]][tour[i+1]]
        fit = fit + self.dist[tour[self.n - 1]][tour[0]]
        return fit

    def vecinAleator(self, c):
        x = random.randint(0, int(self.n) - 1)
        y = random.randint(0, int(self.n) - 1)
        #different values
        while (x == y):
            x = random.randint(0, int(self.n) - 1)
            y = random.randint(0, int(self.n) - 1)
        #print (" index ", x, " ", y)
        c[x], c[y] = c[y], c[x]
        return c


    def simAnn(self, Tmax, Tmin, alpha, maxIter):

        #set initial temp, considering Tmax
        temp = Tmax
        c = self.generateSolution()
        print (self.fitness(c))

        while ( temp > Tmin):
            k = 1
            x = self.vecinAleator(c[:])
            #print ("vecinul este ", x)
            #print(self.fitness(x))
            #print (x)
            delta = int(self.fitness(x) - self.fitness(c))
            if (delta < 0):
                c = x
            else:
                if ( random.random() < math.exp( -delta/temp) ):
                    c = x

            while (k < maxIter):
                x = self.vecinAleator(c[:])
                delta = int(self.fitness(x) - self.fitness(c))
                if (delta < 0):
                    c = x
                else:
                    if (random.random() < math.exp(-delta / temp)):
                        c = x
                k = k + 1

            #cool system
            temp = alpha * temp
        g101 = open("results101.txt", "a")

        g101.write("parametrii: Tmax=")
        g101.write(str(Tmax))
        g101.write(", Tmin=")
        g101.write(str(Tmin))
        g101.write(", alpha=")
        g101.write(str(alpha))
        g101.write(", maxIter=")
        g101.write(str(maxIter))
        g101.write(" ruta: ")
        g101.write(str(c))

        g101.write(" fitness = ")
        g101.write(str(self.fitness(c)))
        g101.write("\n")
        #print("fitness ", self.fitness(c))
        return self.fitness(c)




