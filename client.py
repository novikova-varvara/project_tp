class Client:
    def __init__(self):
        self.name = None
        self.surname = None
        self.passport = None
        self.address = None
        self.num = None
        self.flag = False
        self.limit = 5000

    def builder(self, num):
        return Client.Builder(self, num)

    def modifier(self, num):
        return Client.Builder(self, num)

    def check_flag(self):
        if self.passport != None and self.address != None:
            self.flag = True
        return self.flag

    class Builder:
        def __init__(self, client, num):
            self.client = client
            self.client.num = num

        def set_name(self, name):
            self.client.name = name
            return self

        def set_surname(self, surname):
            self.client.surname = surname
            return self

        def set_passport(self, passport):
            self.client.passport = passport
            return self

        def set_address(self, address):
            self.client.address = address
            return self

        def build(self):
            return self.client