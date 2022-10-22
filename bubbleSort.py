# markdict={"Santos": 73, "Garcia": 85, "Abellar": 90, "Villamayor": 67, "Lee": 96}


dic = {"Santos": 73, "Garcia": 85, "Abellar": 90, "Villamayor": 67, "Lee": 96}
key = list(dic.keys())

for i in range ( len ( key ) - 1 ) :
    if  key [ i ] > key [ i + 1 ] :
        key [ i ] , key [ i + 1 ] =  key [ i + 1 ] , key [ i ]

print(key)
