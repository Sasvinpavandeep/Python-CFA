#Python quiz game

question =("what musical instrument that has six strings ? ",
           "what is the famous music in piano? ",
           "what is the most famous musical instrument?",
           "what can a drum do?",
           "what is the most classical musical instrument?",)

options =(("A.guitar","B.piano","C.drum","D.saxophone"),
         ("A.Fur elise beethoven","B.Happy birthday song","C.jingle bell","D.twinkle star"),
         ("A.saxophone","B.bass","C.drum","D.guitar"),
         ("A.drum","B.flute","C.Electric guitar","D.triangle"),
         ("A.violin","B.piano","C.cello","D.double bass"))

answers = ("A", "A","D","A","C")
guesses = {}
score = 0
question_num = 0

for question in question: 
    print("---------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input ("Enter(A, B, C, D ): ").upper()
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1
    print("----------------------")
    print("       RESULTS        ")
    print("----------------------")

    print("guesses: ", end="")
    for guess in guesses:
        print(guess, end=" ")
    print()    

    score = int(score / len(question) * 100)
    print(f"Your score is: {score}%")