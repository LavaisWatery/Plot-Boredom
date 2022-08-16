class MenuSelection:

    selected = False

    def __init__(self, st, func):
        self.func = func
        self.st = st

    def iter(self):
        while self.selected:
            if not self.func():
                self.selected = False
                break
    
    def str(self):
        return self.st

    def select(self):
        self.selected = True
        self.iter()