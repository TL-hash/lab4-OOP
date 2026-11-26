# Python program showing
# abstract base class work
# class through subclassing

import abc


class parent:
    def geeks(self):
        pass

class child(parent):
    def geeks(self):
        print("child class")

print(issubclass(child, parent))
print(issubclass(child(), parent))


