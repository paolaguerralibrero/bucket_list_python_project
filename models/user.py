class User:

    def __init__(self, first_name, last_name, id = None):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id

    def __str__(self):
        return str(self.id) + " " + self.first_name + " " + self.last_name