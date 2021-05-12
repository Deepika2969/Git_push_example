my_message = "Sai ram, Please help me"
print(my_message)

# here my_message is a variable

#1) To convert the string to lower case we use lower() method.This can be accessed with the variable name.
print(my_message.lower())

#2) To convert the string to Upper case we use upper() method.This can be accessed with the variable name.
print(my_message.upper())

#3) To count the number of words or letters that are present in the string
#a) To count the particular word
print(my_message.count('Sai'))
#b) To count the particular letter
print(my_message.count('a'))

#To find if a particular string is present or not.
print(my_message.find('Please'))
#If present it will return thr index of the satrtinglette of the string

print(my_message.find('Deepika'))
#If th string is not present it returns -1

#myTrail
my_trial = 'Deepika is a good girl and a good boy'
print(my_trial.find('good'))
print(my_trial[13])

#If the word is repeated then it gives the first occurrence

message = 'Hello World'
print(message)

#replace method
message.replace('World','Deepika')
print(message)

