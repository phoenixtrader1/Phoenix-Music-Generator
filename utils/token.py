from users.wallet import spend_token, get_balance

def use_token(username, amount=1):
    if spend_token(username, amount):
        return True, f"{amount} token(s) spent. Remaining balance: {get_balance(username)}"
    return False, "Insufficient tokens."
