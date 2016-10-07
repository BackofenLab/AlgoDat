class PriorityQueueItem:

    """Provides a handle for a queue item.

    This handle can be used to remove or
    update the queue item.
    """
    
    def __init__(self, key, value, index):
        self.key = key;
        self.value = value;
        self.index = index;
