import json

FILE_PATH = "data/users.json"

def load_users():
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def save_users(users):
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(users, f, indent=4, ensure_ascii=False)

def find_user_by_username(username):
    users = load_users()
    for user in users:
        if user["username"] == username:
            return user
    return None

def update_user_health(username, health_data):
    users = load_users()
    for user in users:
        if user["username"] == username:
            user["health"] = health_data
            break
    save_users(users)
