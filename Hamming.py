import random
import numpy as np
import pandas as pd

#df = pd.read_csv('sample.csv',name=['word','ascii'])

#def generate_random_ascii():
#    for i in range(0, 100):
#        make_str = list()
#        make_ascii = list()
#        make_hex list()
#        for j in range(0,4):
#            num = random.randint(97, 122)
#            make_str.append(str(chr(num)))
#        string = ''.join(make_str)
#        binary = bin(int.from_bytes(string.encode(),'big'))
#    return string, binary

df = pd.read_csv('sample.csv',names=['word','bin'])
array = list()
minNumber=100;
count = 0
def hamming(a,b):
    return len([i for i in filter(lambda x: x[0] != x[1], zip(a,b))])

for i in range(0,len(df.index)):
    for j in range(i+1,len(df.index)):
        hd = hamming(df.iloc[i,1], df.iloc[j,1])
        count += 1
        print(count,"(",df.iloc[i,0],df.iloc[j,0],")","hamming_distance:",hd)
        if minNumber > hd :
            minNumber = hd
print("min hamming distance",minNumber)

#for k in range(0,100):
#    string, binary = generate_random_ascii()
#    df.iloc[k,0] = string
#    df.iloc[k,1] = "0"+binary[2:]
#df.to_csv('sample.csv',header=False,index=False)



