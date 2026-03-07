# nums=[71,56,72,23,29]

# min=30
# max=100
# for num in nums:
#     if num<min:
#         min= num
#     # print(f"In this iteration value of min is: {min}")
#     if num>max:
#         max=num
#     # print(f"In this iteration value of max is: {max}")

# print(min,max)


    
# name="Abdullah"

# # for char in name:
# # print(name[::2])


# def fact(n):
#     if n==0:
#         return 0
    
#     elif n==1:
#         return 1
    
#     else:
#         return n*fact(n-1) # 4 *fact(3) [3 * fact(2)]

# print(fact(4))

class User:
    users=45
    def __init__(self,id,name):
        self.id=id
        self.name=name
        
    @classmethod
    def info(self):
        self.users=6
        # print(f"The user id is {self.id}, name is {self.name} and total no of users are: {self.users}")
        print(self.users)


u1=User(1,"ali")
u1.info()

print(User.users)