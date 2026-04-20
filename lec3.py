
# reverse num


# num=int(input("enter num : "))
# print(num)
# rev=0
# while num>0:
#     dig=num%10
#     rev=rev*10+dig
#     num//=10
# print(rev)


# narcissistic num

# n=int(input("enter num : "))
# temp=n
# c=0

# while temp>0:
#     c+=1
#     temp//=10

# temp=n
# ans=0

# while temp>0:
#     r=temp%10
#     ans=ans+r**c
#     temp//=10


#     if ans == n:
#         print("armstrong / narcissistic num")
#     else :
#         print("not armstrong num")


# functions

# def factor(n):

#     for i in range(1,n+1):
#         if n%i==0:
#             print(i,end=" ")
        
#         n=int(input("enter the num : "))
#         factor(5)
    

# def factor_even(n):

#     if n % 2 == 0:
#         num = 1
#         for i in range(1, n + 1):
#             num = num * i
#         print("num is even", num)

#     else:
#         print("num is odd")


# n = int(input("enter the num: "))
# factor_even(n)


# def factor_even(n):

#     if n % 2 != 0:
#         num = 1
#         for i in range(1, n + 1):
#             num = num * i
#         print("num is odd", num)

#     else:
#         print("num is even")


# n = int(input("enter the num: "))
# factor_even(n)

#create list
# lst=[8,10,12,13,15,9]
# for i in range(len(lst)):
#  if lst[i]%2==0:
#     lst[i]-=5
#  else:
#     lst[i]+=5
# print(lst)


# lst=[8,10,12,13,15,9]
# max=-1
# for i in range(len(lst)):
#     if lst[i]>max:
#         max=lst[i]

# print(max)
       
# lst=[8,10,12,13,15,9]
# max=-1
# sl=-1
# for i in range(len(lst)):
#     if lst[i]>max:
#        sl=max
#        max=lst[i]
#     elif lst[i]>sl:
#         sl=lst[i]
       
# print(sl)


# lst=[8,10,12,13,15,9]
# lst.append("hello")
# lst.append([3,5,4,6,7,8])
# lst.insert(3,35)
# lst.insert(-3,88)
# lst.extend([2,5,8,7,78])
# print(lst)
# print(lst[-1][3])
       
# lst=[8,10,12,13,15,9]
# del lst[4]
# x=lst.pop(3)
# lst.remove(9)
# print(lst)
# print(x)

