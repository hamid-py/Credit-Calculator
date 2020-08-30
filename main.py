import math
import sys


def interest(interest):
    if interest.isdigit():
        interest = int(interest)
    else:
        interest = float(interest)
    i = interest / 1200
    return i


def differentiated_payment(p, n, i):
    i = interest(i)
    p = int(p)
    n = int(n)
    overpayment_list = []
    for m in range(1, n + 1):
        d = (p / n) + i * (p - ((p * (m - 1)) / n))
        print(f'Month {m}: payment is {math.ceil(d)}')
        overpayment_list.append(math.ceil(d))
    print(f'Overpayment = {math.ceil(sum(overpayment_list) - p)}')


def annuity_payment(p, n, i):
    credit = int(p)
    number_of_period = int(n)
    i = interest(i)
    A = credit * ((i * ((1 + i) ** number_of_period)) / (((1 + i) ** number_of_period) - 1))
    print(f'Your monthly payment = {math.ceil(A)}!')
    print(f'Overpayment = {math.ceil(A) * number_of_period - credit}')


def cal_number_of_month_payment(p, a, i):
    try:
        credit = int(p)
        monthly_payment = int(a)
        i = interest(i)
        month_number = math.log(monthly_payment / (monthly_payment - (i * credit)), 1 + i)
        if math.ceil(month_number) == 1:
            print(f"It will take {math.ceil(month_number)} month to repay the credit!")
        elif math.ceil(month_number) < 12:
            print(f"It will take {math.ceil(month_number)} months to repay the credit!")
        elif math.ceil(month_number) == 12:
            print(f"It will take 1 year to repay the credit!")
        elif math.ceil(month_number) >= 12 and math.ceil(month_number) % 12 != 0:
            print(f"It will take {math.ceil(month_number) // 12} years and {math.ceil(month_number) % 12} months to "
                  f"repay the "
                  f"credit!")
        elif math.ceil(month_number) >= 12 and math.ceil(month_number) % 12 == 0:
            print(f"It will take {math.ceil(month_number) // 12} years to repay the credit!")
            print(f'Overpayment = {math.ceil(month_number) * monthly_payment - credit}')
    except ValueError:
        print('please enter digit')


def credit_principal(A, n, i):
    if A.isdigit():
        A = int(A)
    else:
        A = float(A)
    n = int(n)
    i = interest(i)
    P = (A / (((i * ((1 + i) ** n)) / (((1 + i) ** n) - 1))))
    print(f'Your credit principal = {math.floor(P)}!')
    print(f'Overpayment = {n * A - math.floor(P)}')


def what_to_do():
    print("What do you want to calculate?",
          "type 'n' for number of monthly payments,",
          "type 'a' for annuity monthly payment amount,",
          "type 'p' for credit principal:", sep='\n')
    return input()


# what_to_do = what_to_do()
# try:
#     if what_to_do == 'n':
#         cal_number_of_month_payment()
#     elif what_to_do == 'a':
#         annuity_payment()
#     elif what_to_do == 'p':
#         credit_principal()
#     else:
#         raise ValueError
# except ValueError:
#     print(f'{what_to_do} is not an option')

# differentiated_payment(500000, 8, '7.8')
try:
    args = sys.argv
    if len(args) != 5:
        raise ValueError
    else:
        args_dict = {}
        args.pop(0)
        for i in args:
            args_dict[i.split('=')[0]] = i.split('=')[1]
        if args_dict['--type'] == 'diff':
            if '--principal' in args_dict and '--periods' in args_dict and '--interest' in args_dict:
                differentiated_payment(args_dict['--principal'], args_dict['--periods'], args_dict['--interest'])
            else:
                raise ValueError
        elif args_dict['--type'] == 'annuity':
            if '--principal' in args_dict and '--periods' in args_dict and '--interest' in args_dict:
                annuity_payment(args_dict['--principal'], args_dict['--periods'], args_dict['--interest'])
            elif '--payment' in args_dict and '--periods' in args_dict and '--interest' in args_dict:
                credit_principal(args_dict['--payment'], args_dict['--periods'], args_dict['--interest'])
            elif '--principal' in args_dict and '--payment' in args_dict and '--interest' in args_dict:
                cal_number_of_month_payment(args_dict['--principal'], args_dict['--payment'], args_dict['--interest'])

except ValueError:
    print('Incorrect parameters')
