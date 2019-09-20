
dict_rum={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
def rum_sum(a,b):
    sum=0
    for i in list(a+b):
        if i in dict_rum:
            sum+=dict_rum[i]
    i= 0
    value=sorted(dict_rum.values(),reverse=True)
    rum_str=''
    while sum!=0:

        if sum // value[i]!=0:
            print(sum // value[i])
            sum-=value[i]
            for name, age in dict_rum.items():
                if age == value[i]:
                    rum_str+=name
        else:
            i+=1
    return rum_str

print(rum_sum('CI','MI'))
