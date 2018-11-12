from user import User
from bill import Bill


user_name = input('Enter you name: ')
user_group = input('worker/booker? ')
user = User.create_user(user_name, user_group)

if user_group == 'worker':
    new_bill = Bill.create_bill()
    while True:
        new_bill.add_work()
        more = input('Add more works/Get total price: [1/2] ')
        if more == '2':
            print(f'************ Total price: {new_bill.get_total_price()} ************')
            break
        continue



