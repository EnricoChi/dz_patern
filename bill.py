class Bill:
    bill = {}

    @classmethod
    def create_bill(cls):
        print(f'************ Created new bill ************')
        return cls

    @classmethod
    def add_work(cls):
        work_type = input('Enter work type: ')
        work_type_price = input('Work price: ')
        return cls.bill.update({work_type: int(work_type_price)})

    @classmethod
    def get_total_price(cls):
        return sum(cls.bill.values())

    def get_bill(self):
        pass


class WorkType:
    pass
