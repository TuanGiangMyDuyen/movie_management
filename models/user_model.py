from models.json_model import JSONHandler

class User:
    def __init__(self, userInfo):
        self.userInfo = userInfo

    def get_user(self, role):
        json_handler = JSONHandler("users.json")
        users = json_handler.read_json()
        if not users:
            users = {'users': []}
            json_handler.write_json(users)
        for user in users[role]:
            if user["username"] == self.userInfo['username']:
                return user

    @staticmethod
    def get_user_by_email(email):
        json_handler = JSONHandler("users.json")
        users = json_handler.read_json()
        for user in users["users"]:
            if user["email"] == email:
                return user

    def save_user(self, role):
        json_handler = JSONHandler("users.json")
        users = json_handler.read_json()
        users[role].append(self.userInfo)
        json_handler.write_json(users)

    @staticmethod
    def change_pass(role, newUser):
        json_handler = JSONHandler("users.json")
        users = json_handler.read_json()
        for user in users[role]:
            if user['username'] == newUser['username']:
                user['password'] = newUser['password']
        json_handler.write_json(users)