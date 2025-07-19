# from dotenv import load_dotenv, dotenv_values
# from pathlib import Path
# import os

# dotenv_path = Path(__file__).parent / ".env"
# # load_dotenv(dotenv_path)
# load_dotenv()
# config = dotenv_values(dotenv_path)

# port = int(os.getenv("PORT", 4000))  # if PORT not in .env, use 4000

# if port == 4000:
#     print("⚠️ Using default port")
# else:
#     print(f"🚀 Using custom port {port}")

# secret_key = os.getenv("SECRET_KEY")
# db_name = config.get("DB_NAME")

# print(f"port : {port}")
# print(f"secretKey : {secret_key}")
# print(f"databaseName: {db_name}")


# class Student:
#     college = "IIT"

#     @classmethod
#     def change_college(cls, name):
#         cls.college = name

# class BTechStudent(Student):
#     pass

# BTechStudent.change_college("NIT")

# print(Student.college)         # 👉 IIT
# print(BTechStudent.college)    # 👉 NIT ✅



class User:
    total_user_count=0
    firstName=None
    lastName=None
    def __init__(self,firstName,lastName):
        self.firstName=firstName
        self.lastName=lastName
       
        User.total_user_count+=1
        
    @property
    def full_name(cls):
     return cls.firstName + " " + cls.lastName
    
    @classmethod
    def get_user_count(cls):
     return cls.total_user_count
 
    @staticmethod
    def is_valid_name(name):
     if(name.isalpha()):
        return True
     else:
       return False



print(User.get_user_count())     # 0

u1 = User("Aryan", "Gautam")
print(u1.full_name)              # Aryan Gautam

print(User.get_user_count())     # 1

print(User.is_valid_name("Aryan"))   # True
print(User.is_valid_name("Aryan123")) # False
