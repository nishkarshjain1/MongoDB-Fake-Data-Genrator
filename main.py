import pymongo
import random
import string
class MyCrud:
    """CRUD operation class that involves all the crud operations"""
    def __init__(self):
        self.client = pymongo.MongoClient('mongodb://localhost:27017/')
        self.db  = self.client['mydatabase']
        self.collect = self.db["customers"]

    @staticmethod
    def random_name(size=5,char=string.ascii_lowercase):
        """This method is used to genrate random name """
        a = "".join(random.choice(char) for _ in range(size))
        return a.capitalize()

    @staticmethod
    def random_digit(size=2,digit=string.digits):
        a="".join(random.choice(digit) for _ in range(size))
        return int(a)

    def create(self,data):
        """This method is used to insert only one data at a time"""
        x = self.collect.insert_one(data)
        return x
    
    def create_many(self,data):
        """THis method is used to insert bulk data at a time"""
        x = self.collect.insert_many(data)
        return x
    
    def update(self,find,update):
        x = self.collect.update_one(find,update)
        return x


    def delete(self,data):
        x = self.collect.delete_one()
        return x        
    
    def show(self):
        arr = []
        for x in self.collect.find():
            print(x)

if __name__ == "__main__":
    a = []
    for i in range(10):
        a.append({'name':MyCrud.random_name(),'age':MyCrud.random_digit()})
    mycrud = MyCrud()

    data = mycrud.create_many(a)
    
        


    
    
