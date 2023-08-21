choice_begin=(input("welcome to the quiz..Are you ready?"))
if choice_begin in ["yes,Yes"]:
    print("Lets Get Started!")
else:
    "break" 
score=0
#---------------------------------------------------------------------------------------------------------------------
choice1=(input("In which year was the python language developed? "))    #Question no1
if choice1=='1989':
    score+=5
    print("Correct :)")
else:
    print("Incorrect :(")
#---------------------------------------------------------------------------------------------------------------------
choice2=(input("Output for 4+3%5 is?"))                                 #Question no2
if choice2=='7':
    score+=5
    print("Correct :)")
else:
    print("Incorrect :(")
#---------------------------------------------------------------------------------------------------------------------
choice3=(input("Python supports the creation of anonymous functions at runtime, using a construct called?"))   #Question no3
if choice3 in ['lambda,Lambda']:
    score+=5
    print("Correct :)")
else:
    print("Incorrect :(")
#---------------------------------------------------------------------------------------------------------------------
choice4=(input("What is output of print(math.pow(3,2)?"))             #Question no4
if choice4=='9.0':
    score+=5
    print("Correct :)")
else:
    print("Incorrect :(")
#---------------------------------------------------------------------------------------------------------------------
choice5=(input("output for math.ceil(1.03)gives?"))                  #Question no5
if choice5=='2.0':
    score+=5
    print("Correct :)")
else:
    print("Incorrect :(")
#---------------------------------------------------------------------------------------------------------------------
choice6=(input("What is the return value of trunc()?"))              #Question no6
if choice6=='int':
    score+=5
    print("Correct :)")
else:
    print('Incorrect :(')
#---------------------------------------------------------------------------------------------------------------------
choice7=(input("output for 'z'+'xy'?"))                              #Question no7
if choice7=='zxy':
    score+=5
    print("Correct :)")
else:
    print("Incorrect :(")
#---------------------------------------------------------------------------------------------------------------------
choice8=(input("name a entry controlled loop"))                      #Question no7
if choice8 in ["for,while"]:
    score+=5
    print("Correct :)")
else:
    print("Incorrect :(")
#----------------------------------------------------------------------------------------------------------------------
choice9=(input("which statament is not executed if it has terminated loop?"))  #Question no8
if choice9=='break':
    score+=5
    print("Correct :)")
else:
    print("Incorrect:(")
#----------------------------------------------------------------------------------------------------------------------
choice10=(input("Which bus is unidirectional?"))                               #Question no8
if choice10 in ["Control bus, control bus, CONTROL BUS"]:
    score+=5
    print("Correct :)")
else:
    print("Incorrect :(")
print("Your score is",score)