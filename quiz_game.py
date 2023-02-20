print("Welcome to my quiz: Are you smarter than a 5th grader?")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("How many continents are there? ")
if answer.lower() == "seven":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What line divides the earth around the middle? ")
if answer.lower() == "equator":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What country is closest to the Great Barrier Reef? ")
if answer.lower() == "australia":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("In what century are we living right now? ")
if answer == "21st century":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What is the name of the writing system used by Ancient Egyptians? ")
if answer == "hieroglyphics":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("At which timezone is the state of Montana? ")
if answer == "mountain standard time":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Who is famous for saying, 'I have a dream.'? ")
if answer == "martin luther king jr":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("In what country did the Olympics originate? ")
if answer == "greece":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score/8) * 100) + "%.")