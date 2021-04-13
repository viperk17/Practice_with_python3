import datetime
import math

# current_weight =220
# goal_weight =180
# avg_lbs_week = 2
#
# start_date = datetime.date.today()
# end_date = start_date
#
# while current_weight > goal_weight:
#     end_date += datetime.timedelta(days=7)
#     current_weight -= avg_lbs_week
#
# print(end_date)
# #pirnt no of weeks to complete the task
# print(f'reached goal in {(end_date - start_date).days // 7} weeks')
#


'''to reach a goal'''
goal_subs = 150000
current_subs = 85000
subs_to_go = goal_subs - current_subs

avg_subs_day = 200
days_to_go = math.ceil(subs_to_go / avg_subs_day)  # ciel will round up the value

today = datetime.date.today()

print('No of days to go : ', today + datetime.timedelta(days=days_to_go))
