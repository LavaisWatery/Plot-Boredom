import json

class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.comments = set()
        self.data = {
            'name' : name,
            'age' : age,
        }

    def toStr(self):
        return self.name + ": " + self.age + "\n" + str(self.comments)

    def toJSON(self):
        return json.dumps(self.data)