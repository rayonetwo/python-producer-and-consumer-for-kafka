import string
import random

user_ids = list(range(1, 10))
recipient_ids = list(range(1, 10))

def create_message() -> dict:
    random_user = random.choice(user_ids)
    random_recipient = random.choice(recipient_ids)

    # Create a random message
    random_message = ''.join(random.choice(string.ascii_letters) for i in range(32))

    return {
        'user_id': random_user,
        'recipient_id': random_recipient,
        'message': random_message
    }
