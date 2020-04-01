from STP import *


def main():

    s = STP(0,0)
    s.readFromFile()
    best = 99999
    sum = 0
    for i in range (10):
        print ("introduceti parametrii ")
        Tmax = int(input("Tmax = "))
        Tmin = float(input("Tmin = "))
        alpha = float(input("alpha = "))
        maxIter = int(input("maxIter ="))
        fit = s.simAnn(Tmax, Tmin, alpha, maxIter)
        sum = sum + fit
        if ( fit > best):
            best = fit

    avg = sum/10

    g101 = open("results101.txt", "a")
    g101.write("best: ")
    g101.write(str(best))
    g101.write("  ")
    g101.write("avg: ")
    g101.write(str(avg))

if __name__ == '__main__':
    main()
