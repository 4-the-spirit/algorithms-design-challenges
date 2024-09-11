from collections import deque


class SafeArray(deque):
    def __init__(self, array, default):
        super().__init__(array)
        self.default = default

    def __len__(self):
        return super().__len__()

    def __getitem__(self, index):
        if index >= len(self) or index < (-1) * len(self):
            return self.default
        return super().__getitem__(index)

    def __setitem__(self, key, value):
        super().__setitem__(key, value)
