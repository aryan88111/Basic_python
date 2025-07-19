# def function_name(param1, param2:int ):
#     return param1+param2


# sum=function_name(12,33)
# print(sum)


# def printlist(listt):
#     for val in listt:
#         print(val)
        
        
# listt=[2,4,64,657,67,3,90,1,924,53,0] 

# printlist(listt)   

# def search(listt,key):
#      i=0
#      j=len(listt)-1
#      while i<j:
#         midIdx=(i+j)//2
#         if key==listt[midIdx]:
#            print(f"element {key} found at index {midIdx}")
#            return
#         elif key<listt[midIdx]:
#             j=midIdx-1
#         elif key>listt[midIdx]:
#             i=midIdx+1
#         else:
#             print("element not found")    

# listt.sort()   
# print(listt,"sorted list")        
# search(listt,90)            
           
 
# recursion


def show(n:int):
    if n<=0:
        return
    show(n-1)
    print(n)
    
    
show(7)  


def fact(n):
    if n==0 or n==1:
       return 1 
    faith= fact(n-1) 
    return faith *n

aa=fact(5)
print(aa)