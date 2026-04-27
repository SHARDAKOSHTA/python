# lst=["red","orange","green","blue","while"]
# lst1=["black","yellow","green","blue"]
# ans1=[]
# ans2=[]
# for i in lst:
#     if i not in lst1:
#         ans1.append(i)
# print(ans1)

# for i in lst1:
#     if i not in lst:
#         ans2.append(i)
# print(ans2)

# lst=[0,0,1,2,3,4,4,5,6,6,7,8,9,4,4]
# temp=[lst[0]]
# ans=[]
# for i in range(len(lst)):
#     if lst[i]==lst[i-1]:
#         temp.append(lst[i])
#     else:
#         ans.append(temp)
#         temp=[lst[i]]

# print(ans)


lst=[0,0,1,2,3,4,4,5,6,6,7,8,9,4,4]
temp=[0]
for i in lst:
     if i!=temp[-1]:
       temp.append(i)

print(temp)