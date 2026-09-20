import hashlib
users = {}
ADMIN_KEY = "273978245748557525877249758282457454854758457475294875284572"
import json

users = {}

def save_users():
    with open("users.json", "w") as file:
        json.dump(users, file, indent=4)


def load_users():
    global users
    try:
        with open("users.json", "r") as file:
            users = json.load(file)
    except FileNotFoundError:
        users = {}
class Signup(): 
    def __init__(self,username,password):
        self.username=username
        self.password=password 
    def weak_password(self):
        if len(self.password) < 8:
            raise ValueError("Password is too short! 🌸")
        return "Password accepted ✅"
    def add_users(self):
       if self.username in users:
        raise ValueError("Username already exists! ❌")
       if self.weak_password():
            users[self.username] = self.password
            return "User added successfully ✅"

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()
class Admin(Signup):
    def __init__(self, username, password, admin_key):
        self.username=username
        self.password=password
        super().__init__(username, password)
        if admin_key != ADMIN_KEY:
            raise ValueError("You are not allowed to be admin ❌")

    def show_users(self):
        for username in users:
            print(username)
     
user1 = Signup("Amitis", "python123")
user2= Signup("gin","66677788")
admin = Admin('BOSS','667676767','273978245748557525877249758282457454854758457475294875284572')
try:
    user1.add_users()
    user2.add_users()

    
    admin.show_users()

except ValueError as error:
    print(error)
