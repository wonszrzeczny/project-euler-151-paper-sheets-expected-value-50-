import copy
def expected(k,vals={(0,0,0,0,0):0,(1,0,0,0,0):1}):
    if k not in vals:
        vals[k]=0
        for i,num in enumerate(k):
            if num>0:
                next_k = list(copy.deepcopy(k))
                for j in range(0,i): next_k[j]+=1
                next_k[i]-=1
                vals[k]+=expected(tuple(next_k))/sum(k)*num
                if sum(k)==1: vals[k]+=1
    return vals[k]
print(expected((0,0,0,0,1)))