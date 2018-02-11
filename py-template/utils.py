import random

def generate_shortened_url():
    return ''.join(random.choice('0123456789ABCDEF') for i in range(7))
