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


# some properties


# lst = [3,4,5,6,7,8,9]
# lst.reverse()
# print(lst)


# lst= [3,44,56,62,2,8,12]
# # # original lst me change karega 
# # lst.sort()
# # lst.sort(reverse=True)
# # print(lst)

# lst1=[2,3,1,4,8,15,69,23]
# # original lst me change nhi hota h 
# lst1=sorted(lst)
# print(lst1)
# print(lst)

# Q.1 WAP to print to 


# lst1=[2,4,6,8,3,5,8,9]
# n=len(lst1)

# if n%2==0:
#     first_half = lst1[n//2]
#     second_half = lst1[n//2]

#     print("first half:",first_half)
#     print("second half:", second_half)
#     # sum=len(lst1(n//2))

# else:

#     print("list divide nhi ho sakti ")


# lst1=[2,4,6,8,3,5,8,9]
# print(lst1)
# n=lst1[0]*lst1[-1]
# lst1.insert(3,n)
# print(lst1)

# lst=[[23,45,76],[45,3,12],[3,5,20]]
# for i in lst:
#     print("first : ",i[0],"last : ",i[-1])

# lst=[[1,2,4,5],[3,5,4,3],[4,5,3,2]]
# sum=0
# for i in lst:
#     print(max(i))
#     sum+=max(i)

# print(sum)

# lst=[[1,2,4,5],[3,5,4,3],[4,5,3,2]]
# total=0
# for i in lst:
#     s=sum(i)
#     print(s)
#     total+=s
     
# print("total : ",total)


# lst=[2,4,5,6,7,8,9,55]
# lst1=[i for i in lst if i%2==0]
# print(lst1)


# lst1=[]
# for i in lst:
#     if i%2==0:
#         lst1.append(i)
# print(lst1)



# lst=[2,4,5,6,7,8,9,55]
# lst1=[i for i in lst if i%2!=0]
# print(lst1)

# for i in range(1,21):
#     if i%2!=0:
#         print(i)


# lst=[2,4,5,6,7,8,9,55]
# for i in lst:
#     if i%2==0:
#         print("even")
#     else:
#         print("odd")

# lst1=["even" if i%2==0 else "odd" for i in lst]
# print(lst1)
    
       
# lst=[2,4,5,6,7,8,9,55]
# for i in lst:
#     print(i*i)

# lst1=[i*i for i in lst]
# print(lst1)


lst=[i if i%2==0 for i in range(1,20)]
print(lst)