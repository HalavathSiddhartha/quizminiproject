#quiz mini project:

print("WELCOME TO SHORT QUIZ")
ready = input("Are you ready? ")
if ready.lower() != "yes":
    quit()
print("OKAY let's play:)")  
score = 0
answer = input("Who is the father of Computer science? ")
if answer.upper() == "Charles Babbage":
    print('correct')
    score+=1
else:
    print("Incorrect")
answer = input("In a computer, most processing takes place in ? ")
if answer.upper() == "cpu":
    print('correct')
    score+=1
else:
    print("Incorrect")
answer = input("What converts an entire program into machine language? ")
if answer.upper() == "Compiler":
    print('correct')
    score+=1
else:
    print("Incorrect")
answer = input("IBM stands for? ")
if answer.upper() == "International Business Machines":
    print('correct')
    score+=1
else:
    print("Incorrect")
answer = input("XML stands for ? ")
if answer.upper() == "Extensible Markup Language":
    print('correct')
    score+=1
else:
    print("Incorrect")
answer = input("Full form of LAN? ")
if answer.upper() == "Local Area Network":
    print('correct')
    score+=1
else:
    print("Incorrect")
answer = input("Which is most common tool used to restrict access to computer system? ")
if answer.upper() == "Passwords":
    print('correct')
    score+=1
else:
    print("Incorrect")

answer = input("A DVD is an example of an ? ")
if answer.upper() == "Optical Disc":
    print('correct')
    score+=1
else:
    print("Incorrect")
answer = input("Unwanted repetitious messages, such as unsolicited bulk e-mail is known as ? ")
if answer.upper() == "Spam":
    print('correct')
    score+=1
else:
    print("Incorrect")
answer = input("What kind of memory is both static and non-volatile ? ")
if answer.upper() == "ROM":
    print('correct')
    score+=1
else:
    print("Incorrect")
print("Thank you for your Answers")
print("Your score is " + str(score) + " Your Percentage is " + str(score/100))