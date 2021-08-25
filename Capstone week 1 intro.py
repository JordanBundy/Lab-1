print('Hello capstone')
# variables
school = 'MCTC'
gpa = 3.7
students_in_class = 22
# if statements
if gpa == 4:
    print ('WOW!')
elif gpa > 3:
    print('Awesome!')
else:
    print('Cool!')

#lists
schools = ['MCTC', 'DCTC', 'North Henneipn Tech']
if 'MCTC' in schools:
    print('MCTC is on the list')
    schools.sort()
    print(schools)
    schools.append('Century college')
    schools.reverse() # returns none
    print(schools)
# strings
class_name = 'software dev capstone'
print(class_name.upper())
print(len(class_name))
print(class_name.split())
print(class_name.split('o'))
if "capstone" in class_name:
    print('this must be the capstone')
#loops
for x in range(10):
    print(x)
for s in schools:
    print(s.upper())
for letter in school:
    print(letter * 10)
data = [0] * 10
print(data)
#while loops
name = input('Enter your name  ')

while not name:
    print('please enter atleast one character')
    name = input('Enter your name  ')
#true and false and none
start_of_semester = True
Winter = False
if Winter:
    print('Brr!')
else: 
    print("its not winter")
#dictionaries
class_codes = {2905: 'Capstone', 2560: 'Web', 2545: 'Java'}
for code in class_codes:
    print(code)
    print(class_codes[code])
for code, name in class_codes.items():
    print('The class code is ' + str(code) + ' and the name is " + name')
for code, name in class_codes.items():
    print(f'The class code is  {code} and the name is {name}')
#slicing strings, lists   
schools = ['MCTC', 'DCTC', 'North Henneipn Tech']
first_two = schools[:2]
print(first_two)
last_school = schools[-1]
last_two_schools = schools[-2:]
school_name = "minneapolis community technical college"
city = school_name[:11]
print (city)
#file io
#with open("Data.txt"):
