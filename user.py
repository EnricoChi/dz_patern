class UserInterface:
    def get_full_name(self):
        pass


class User(UserInterface):

    def __init__(self, name, group):
        self.name = name
        self.group = group

    @classmethod
    def create_user(cls, name, group):
        try:
            user = getattr(cls, f'_create_{group}')(name, group)
            print(f'************ Created new {group} {name} ************')
            return user
        except AttributeError:
            print(f'++++++++++++ Wrong group ++++++++++++')

    @staticmethod
    def _create_worker(name, group):
        return Booker(name, group)

    @staticmethod
    def _create_booker(name, group):
        return Worker(name, group)


class Booker(User):

    def pay_bill(self):
        pass


class Worker(User):

    def create_bill(self):
        pass

    def confirm_pay(self):
        pass
