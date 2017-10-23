def mergesort(num,low,high):
    if (low == high):
        return
    mid = (low + high)/2;

    mergesort(num,low,mid)
    mergesort(num,mid+1,high)

    i = low
    j = mid + 1
    temp = [0]*(high+1)
    for k in range(low,high+1):
        if(i == mid + 1):
            temp[k] = num[j]
            j = j+1
        elif(j == high + 1):
            temp[k] = num[i]
            i = i+1
        elif(num[i] < num[j]):
            temp[k] = num[i]
            i = i+1
        else:
            temp[k] = num[j]
            j = j+1
    for k in range(low,high+1):
        num[k] = temp[k]

    return num

num = [2,3,5,5,8,1]
print mergesort(num,0,len(num)-1)
