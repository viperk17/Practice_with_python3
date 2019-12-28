# #script for monthly
# #script for day
# #script for week to pay the credit card bill
# import datetime
# import calendar
#
# balance = 5000
# interest_rate = 13* 0.1
# monthly_payment = 500
#
# #write script to payoff the credit card bill
# '''specify the dates'''
# today = datetime.date.today()   #today
#
# #how many days in each month
# days_in_current_month = calendar.monthrange(today.year, today.month)[1]
# # print(days_in_current_month)
#
# days_till_end_month = days_in_current_month - today.day
# # print(days_till_end_month)
# start_date = today + datetime.timedelta(days=days_till_end_month + 1)
# # print(start_date)
# end_date = start_date
#
# #how long will take to make the payment
# while balance > 0:
#     interest_charge = (interest_rate / 12) * balance
#     balance += interest_charge
#     balance -= monthly_payment
#
#     balance = round(balance, 2) #round to 3 decimal places
#     if balance < 0:
#         balance = 0
#         #or
#     # balance = 0 if balance < 0 else round(balance, 3)
#
#     # print(end_date, balance)
#
#     days_in_current_month = calendar.monthrange(end_date.year, end_date.month)[1]
#     end_date = end_date + datetime.timedelta(days=days_in_current_month)


import datetime
import calendar

balance = 10000
interest_rate = 13 * .01
monthly_payment = 1000

today = datetime.date.today()
days_in_current_month = calendar.monthrange(today.year, today.month)[1]
days_till_end_month = days_in_current_month - today.day

start_date = today + datetime.timedelta(days=days_till_end_month + 1)
end_date = start_date

while balance > 0:
    interest_charge = (interest_rate / 12) * balance
    balance += interest_charge
    balance -= monthly_payment

    balance = round(balance, 2)
    if balance < 0:
        balance = 0

    print(end_date, balance)

    days_in_current_month = calendar.monthrange(end_date.year, end_date.month)[1]
    end_date = end_date + datetime.timedelta(days=days_in_current_month)
