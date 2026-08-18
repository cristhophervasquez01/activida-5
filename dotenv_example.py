from dotenv import load_dotenv
import os

load_dotenv()


user_name = os.getenv("USER_NAME")
user_password = os.getenv("USER_PASSWORD")

print (user_name)
print (user_password)
