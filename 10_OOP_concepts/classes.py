import datetime as t


class Customer:
    def __init__(self, name, lastname, email):
        self.name = name
        self.lastname = lastname
        self.email = email

    def register(self):
        days = len(self.name) + len(self.lastname)
        today = t.datetime.now()
        register_at = today + t.timedelta(days)
        return register_at.strftime('%Y-%m-%d')


if __name__ == '__main__':
    user = Customer('Jon', 'Snow', 'jon@example.com')
    print(user.register())
