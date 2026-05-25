# it can store only immutable ele(unique) 
# .but it is mutable data type,unordered type,
# idx se access nhi kar skte ,no idxing,no update,can insert ele.


# st=set()
# st1={}
# print(st)
# print(type(st))
# print(type(st1))


# st2=(1,2,3,3,4,5,'hello',4,6)
# print(st2)

# st=(1,2,3,3,4,5,'hello',4,6,[4,5,6])
# for i in st:
#     print(i,end="")

# remove ->agar ele present hoga toh error through karega.
# st={1,2,3,1,2,3,'hello',3,4,(4,5,6,3)}
# st.remove(30)
# print(st)


# discard->agar ele present hoga toh error through nhi karega
# st={1,2,3,1,2,3,'hello',3,4,(4,5,6,3)}
# st.discard(30)
# print(st)

# del st
# print(st)

# append ki jgh add use hoga 
# extend ki jgh update
# st={1,2,3,1,2,3,'hello',3,4,(4,5,6,3)}
# st.add((20,5,6))
# st.add(20)
# st.update((50,76,99))
# print(st)



# list[] add nhi hogi ,tuple() ho sakta hai
# st={1,2,3,4,5}
# st.add((2,3,5))
# print(st)
# st.update([50,2,3])
# print(st)

# s={1,2,3,4,5}
# s1={3,4,5,6,7,8}
# print("union",s|s1)
# print("intersection",s&s1)
# print("difference",s-s1)
# print("symmetric difference",s^s1)



# assig ques

# s1={1,2,3,4,5}
# s2={4,5,6,7,8}
# print("intersection",s1&s2)

# s1={10,20,30,40}
# s2={30,40,50,60}
# print("symmetric difference",s1^s2)

# s1={1,2,3}
# s2={1,2,3,4,5}
# for i in range(len(s1)):
#     if i in s2:
#         print("true")
#     else:
#         print("false")


s1={2,4,6}
s2={1,3,5}
st=set()
print("union",s1|s2)
