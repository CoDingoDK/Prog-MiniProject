class Menu:
    def __init__(self):
        self.highlight = None
        self.layout = {}
    def addMenuItem(self, name):
        self.layout.__setitem__(name, {})

    def addSubMenuItem(self, parent, name, action):
        temp = self.layout.__getitem__(parent)
        temp.__setitem__(name, action)

