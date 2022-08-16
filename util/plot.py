import json
from queue import Empty

class Plot:
    global fetchData

    def __init__(self, name, **data):
        self.name = name

        if data is not None and len(data):
            self.plotX = data['plotX']
            self.plotY = data['plotY']
            fetchData(self)
        else:
            self.plotX = []
            self.plotY = []
            fetchData(self)

    def toStr(self):
        return self.name + ": " + "\n" + str(self.data)

    def fetchData(self):
        self.data = {
            'name' : self.name,
            'plotX' : self.plotX,
            'plotY' : self.plotY
        }

    def toJSON(self):
        fetchData(self)
        return json.dumps(self.data)