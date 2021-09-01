name = input("what is your name?: ")
birthday = input('what month were you born in?: ')
print(f'hello {name} {len(name)}')
if 'August' in birthday:
    print('happy birthday month!')

classes = input ('Please enter your classes seperated by a comma: ')
class_list = classes.split(', ')
for s in class_list:
    print(s)


