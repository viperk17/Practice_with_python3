# list1 = [2, 5, 'June']
# list1.insert(1, 1)
# print(list1)
#
# # list1.remove(1)
# # print(list1)
#
# list1.append(['alpha','echo'])
# print(list1)
#
# list1.extend(['alpha','brao','charlie'])
# print(list1)
#
# # lst = list1.sort()
# # print(lst)
#
# # list1.pop(-1)
# # print(list1)
#
# list1.reverse()
# print(list1)
#
#
# courses = ['English','Math','Physics','CS']
# print(len(courses))
# try:
#     print(courses[4])
# except:
#     print("Not in range")
#
# courses.append('Art')
# print(courses)
#
# courses.insert(1,'Chemistry')
# print(courses)
#
# courses2 = ['Hindi','Education']
# courses.append(courses2)
# print(courses)
#
# courses.extend(courses2)
# print(courses)
#
# courses.remove(courses2)
# print(courses)
#
# courses.pop()
# print(courses)
#
# courses.reverse()
# print(courses)
#
# courses.sort(reverse=True)
# print(courses, "Using Reverse")
#
# # Sorting without using .sort()
#  
#

# # while courses:
# #     min = courses[0]    # arbitrary in list
# #     for x in courses:
# #         if x > min:
# #             min = x
# #     new_list.append(min)
# #     courses.remove(min)
# print(new_list)
# ################## sorting end ####################################
#
# sorted_courses = sorted(courses)
# print(sorted_courses)
#
# # find the index of element
# print(courses.index("English"))
#
# # for course in courses:
# #     print(course)
#
# for index, course in enumerate(courses, start=101):
#     print(index, course)
#
# # join the elements of the list
# course_str = ' <-> '.join(courses)
# print(course_str)
#
# # to reverse the change, split values
# n_list = course_str.split(" <-> ")
# print(course_str)
# print(n_list)


# # Working with Tuples
# tuple1 = ('History','Math','Physics','Java')
# tuple2 = tuple1

# print(tuple1)
# print(tuple2)
# try:
#     tuple1[0] = 'Art'
# except Exception as e:
#     print(e)


# Working with Sets
# cs_courses = {'History','Math','Physics','CS','Math'}
# art_courses = {'History','Math','Art','Design'}
 
# print(cs_courses.union(art_courses))
