discountList = []
m = 0
def dfs(arr,cnt):
    global m
    discount = [10,20,30,40]
    if cnt == m:
        discountList.append(arr)
        return
    for elem in discount:
        dfs(arr+[elem],cnt+1)
def solution(users, emoticons):
    global m
    m = len(emoticons)
    dfs([],0)
    maxSignup, maxUsersTotalPrice= 0,0
    for emoticonDiscountList in discountList:
        signup, usersTotalPrice= 0,0
        for d,emoticonplus in users:
            totalPrice = 0
            for emoticonDiscount,emoticonPrice in zip(emoticonDiscountList,emoticons):
                if d <= emoticonDiscount:
                    totalPrice += (emoticonPrice*(100-emoticonDiscount)//100)
            if totalPrice >= emoticonplus:
                signup+=1
                totalPrice = 0
            usersTotalPrice+=totalPrice
        if maxSignup < signup:
            maxSignup = signup
            maxUsersTotalPrice = usersTotalPrice
        elif maxSignup == signup:
            maxUsersTotalPrice = max(usersTotalPrice,maxUsersTotalPrice)
    return [maxSignup,maxUsersTotalPrice]