size = int(input())
keys = [None] * size
values = [None] * size
def hash_(key, size):
    if type(key)==int:
        return key%size
    elif type(key)==str:
        sum_=0
        for i in key:
            sum_+=ord(i)
        return sum_%size
def rehash(hashed, size):
    #hashed=hash_(key, size)
    return (hashed+1)%size
    
def put(keys, values, key, data):   # you may add more params   
    
    count=0
    global size
   
    
    for i in keys:
        if not(i==None):
            count+=1
   # print(keys,'keys')
    print(len(keys),'abc')
    if count>=int((2/3)*(len(keys))):
        

        keys, values= resize(keys, values)
        
    hashed=hash_(key, size)
    if keys[hashed]==None:
        keys[hashed]=key
        values[hashed]=data
    else:
        while keys[hashed]!=None:
            hashed=rehash(hashed,size)
        keys[hashed]=key
        values[hashed]=data
        

def get(keys, values, key):   # you may add more params
    hashed=hash_(key, size)
    if keys[hashed]==key:
        return values[hashed]
    else:
        while keys[hashed]!=key:
            hashed=rehash(hashed,size)
        return values[hashed]

def resize(keys, values):    # you may add more params
    global size
    size = size * 3
    n_keys = [None] * size
    n_values=[None]* size
    
    # appendlist=[None]*(((len(keys))*3)-size)
    
    # keys=keys+appendlist
    # values=values+appendlist
    
       
    print(size,'size')
    for i in range(len(keys)) :
        if not(keys[i]==None):
            key=keys[i]
            data=values[i]
            # hashed=hash_(key, size)
            put(n_keys, n_values, key, data)
    keys = n_keys
    values=n_values
    return keys,values
    print(keys, values,'keys and values')

num = int(input())   # number of items to be added to the hash table
for i in range(num):
    val = input().split(" ")
    key = (val[0])
    val = (val[1])
    put(keys, values, key, val)
    
for i in range(num):
    key = (input())
    print(get(keys, values, key))