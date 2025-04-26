def get_ans(arr, k):
    mydict=dict()
    for i in arr:
        if i in mydict.keys():
            mydict[i]+=1
        else:
            mydict[i]=1
    maxx=max(arr)
    arr2=[[] for _ in range(maxx+1)]
    for key, value in mydict.items():
        arr2[value].append(key)
    ans=list()
    # print(arr2)
    while k:
        for i in range(len(arr2)-1, -1, -1):
            if arr2[i]:
                if len(arr2[i])<=k:
                    ans.extend(arr2[i])
                    k-=len(arr2[i])
                else:
                    ans.extend(arr2[i][0:k])
                    k=0
                if k==0:
                    return ans
    return ans
                    
nums = [4, 4, 4, 6, 6, 5, 5, 5, 7]
k = 3
ans=get_ans(nums, k)
print(ans)
