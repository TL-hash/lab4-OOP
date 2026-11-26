class Table:
    def __init__(self, l=1, w=1, h=1):
        self.length = l
        self.width = w
        self.height = h

class KitchenTable(Table):
    places = 4

    def set_places(self, p):
        self.places = p

k = KitchenTable()
k.places = 6
