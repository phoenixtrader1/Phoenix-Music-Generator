users = {
    "user1": {"balance": 10},
    "user2": {"balance": 5},
}

def get_balance(username):
    return users.get(username, {"balance": 0})["balance"]

def spend_token(username, amount=1):
    if username in users and users[username]["balance"] >= amount:
        users[username]["balance"] -= amount
        return True
    return False

def add_tokens(username, amount):
    if username in users:
        users[username]["balance"] += amount
    else:
        users[username] = {"balance": amount}
