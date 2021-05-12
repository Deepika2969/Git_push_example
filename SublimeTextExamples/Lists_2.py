# a) Reverse method (This also alters the original string)

courses = ['History','Math','Physics','CompSci']

courses.reverse()
print(courses)

nums = [1,2,3,4]
nums.reverse()
print(nums)

# Sort method (This also alters the original list)
#By default Sort method sorts in asscending order

nums_1 = [1,5,3,6]
nums_1.sort() # To print in ascending order(ny default)
print(nums_1)

nums_2 = [10,5,3,19,20]
nums_2.sort(reverse=True) #To print is descending order
print(nums_2)

courses.sort()
print(courses)

#Using Sorted Function(This doesnot alter the original string)

sorted_List = sorted(courses)
print(sorted_List)

# index method (This returns the location of a particular item in the list)
exam = ['Deepika','Abhi','Ramu','Bhumi']
print(exam.index('Abhi'))

# in Keyword to check if a particular elemant is existing in the list or not
print('Abhi' in exam)
print(5 in nums_2)
print('Akshay' in exam)


#To conver the list to a string
exam_2 = ['Deepika','Abhi','Ramu','Bhumi']
exam_2_Str = ', '.join(exam_2)
print(exam_2_Str)

#To conver the string back to List.
print(exam_2_Str.split(', '))

# None Type

num = [5,6, 9,3,2,1]
new_num = num.sort() #this method doesnot return sorted List instead alters the original list.
print(new_num) # prints teh NONE object.
print(type(new_num))

new_num = num # assigning Sorted original list to new_List
print(new_num)