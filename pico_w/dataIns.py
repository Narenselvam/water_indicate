import time

class Payload:
    def __init__(self,distance):
        self.distance=distance
        now = time.localtime()
        self.formatted_time = "{}-{}-{}  {}:{}".format(now[1], now[2], now[0], now[3], now[4])

  
    def insert(self):
        documentToAdd = {"device": "MyPico",
                        "readings": self.distance,
                        "time":self.formatted_time
                        }
        Payload = {
                "dataSource": "Cluster0",
                "database": "weatherdata",
                "collection": "datas",
                "document": documentToAdd,
                }
        return Payload
    