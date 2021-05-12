nums = [1,5,3,2,4]

print(len(nums))
print(min(nums))
print(max(nums))
print(sum(nums))
#To create a List of courses.

courses = ['History','Math','Physics','CompSci']
print(len(courses))
# check this :print(max(courses))

# check this :print(min(courses))

#Accessing the elements of the List.

print(courses[1])
print(courses[-1])

#Slicing of List is similar to that of Strings

print(nums[2:4])
print(nums[:4])
print(nums[3:])
print(nums[0::3])

#Methods used in the List

## a)Append Method (This alters the original string)
courses.append('Art')
#courses.append('Art','Drawing') This is not possible as it will take only one argument)
print(courses)

##b)Insert Method (This alter the original String)
courses.insert(2,'Art')
print(courses)

##c)Extend method (This alters the original String)
courses_2 = ['Art','Education']
courses.extend(courses_2)
print(courses)

## Differnce between Insert and Extend method
courses.insert(4,courses_2)
print(courses)

# d) Remove method (This alters the original string)

courses.remove('Art')
print(courses)

# e) Pop method (This also alters the string)
alpha = ['a','b','c','d']
pop_Value = alpha.pop()
print(alpha)
print(pop_Value)