import pickle as pk
import numpy as np
from operator import itemgetter


filename = 'filepath'
polys = []
decomp = []


def makeArray(string, leng=9):
    string = string[1:-1]
    char_array = string.split(',')
    int_array = np.asarray(list(map(int, char_array)), 'float')
    int_array = np.pad(int_array, (0, leng - len(int_array)))
    return int_array

with open(filename, 'rb') as file:
    for line in file:
        gcd = int(line[-3])
        line = str(line, 'utf-8')
        line = line.strip()
        line = line[1:-6]
        index = line.find('}')
        poly = makeArray(line[0:index+1])
        poly = poly / gcd
        polys.append(poly)
        line = line[index+3:]
        factors = []
        while len(line) > 0:
            index = line.find('}')
            factor = makeArray(line[0:index+1])
            factors.append(factor)
            line = line[index+3:]
        for i in range(9):
            factors = sorted(factors, key=itemgetter(i), reverse=True)
        factors = np.concatenate(factors)
        decomp.append(factors)

with open('decomps.pkl', 'wb') as file:
    pk.dump(polys, file)

with open('polys.pkl', 'wb') as file:
    pk.dump(decomp, file)
