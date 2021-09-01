""" A quiz program containing several different topics with no limit to qeuestions to be answered/ added, keeping track of your score. Telling you if you're wrong. """
def main():
    total_score = 0
    artDictionary = {'Who painted the Mono Lisa?' : 'Leonardo Da Vinci', 'What precious stone is used to make the artist\'s pigment ultramarine?' : 'Lapiz lazuli' , 'Anish Kapoor\'s bean-shaped Cloud Gate scuplture is a landmark of which city?' : 'Chicago' ,
    'Which kid\'s TV characters are named after Renaissance artists?' : ' Teenage mutant ninja turtles' , 'The graphite in an artist\'s pencil is made of what chemical element?' : 'Carbon'}
    spaceDictionary = {'Which planet is closest to the sun?' : 'mercury' , 'Which planet spins in the opposite direction to all the others in the solar system?' : 'Venus' , 
    'How many moons does Mars have?' : '2' , ' What was the first human-made object to leave the solar system?' : 'Voyager 1' , 'When an asteroid enters the Earth\'s atmosphere and burns up, it is known as what?' : 'Meteor'}
    topics = ['art', 'space']
    print(topics)
    topic = input('Which of these topics would you like to quiz yourself on? Enter it here: ')
    while topic not in topics :
        topic = input('Please enter art or space.')
    else:

        if topic == 'art':

            for i in artDictionary:
                print(i)
                answer = input('Enter your answer: ')
                if answer == artDictionary[i]:
                    print('Correct')
                    total_score += 1
                else:
                    print('Wrong')

            print('End of quiz!')
            print(f'Your total score on {topic} questions is {total_score} out of {len(artDictionary)}.')

            if total_score == len(artDictionary):
                print('You got all the answers correct!')


        elif topic == 'space':
            
            for i in spaceDictionary:
                print(i)
                answer = input('Enter your answer: ')
                if answer == spaceDictionary[i]:
                    print('Correct')
                    total_score += 1
                else:
                    ('Wrong')

            print('End of quiz!')
            print(f'Your total score on {topic} questions is {total_score} out of {len(spaceDictionary)}.')

            if total_score == len(spaceDictionary):
                print('You got all the answers correct!')

main()

