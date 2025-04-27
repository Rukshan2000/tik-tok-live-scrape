from threading import Lock
from collections import defaultdict

# Data storage
comments = []
recent_gifts = []
gifter_coins = defaultdict(int)
gifter_avatars = {}
data_lock = Lock()

def reset_data():
    """Clear all data structures."""
    with data_lock:
        comments.clear()
        recent_gifts.clear()
        gifter_coins.clear()
        gifter_avatars.clear()