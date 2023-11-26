from datetime import datetime
class User:
    def __init__(self, name):
        self.name = name
        self.access = set()
        self.change_of_history = []
        self.access_type = ("read", "write", "remove")

    def grant_access(self, access_type):
        self.access.add(access_type)
        self.change_of_history.append(datetime.now())
        print(f"Access '{access_type}' was granted to {self.name}.")

    def remove_access(self, access_type):
        self.access.remove(access_type)
        self.change_of_history.append(datetime.now())
        print(f"Acess '{access_type}' was removed from {self.name}.")

    def get_first_change_of_history(self):
        if self.change_of_history:
            return self.access, self.change_of_history[0]
        else:
            return None

    def get_change_of_history(self):
        return self.access, self.change_of_history

user1 = User("Marta Martova")
user1.grant_access("write")
user1.grant_access("read")
user1.remove_access("write")
print(user1.get_change_of_history())

user2 = User("Peter Petrovic")
user2.grant_access("write")
user2.grant_access("read")
user2.grant_access("erase")
user2.remove_access("write")

print(user2.get_change_of_history())
print(user1.get_first_change_of_history())