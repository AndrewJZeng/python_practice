import random

   # The quiz data. Keys are states and values are their capitals.
capitals = {"Is Start smart?": "No", "What is the meaning of life":"The answer is 42",
"What is 1+1":"I think you would like to know what 1+1 is","Are pandas cute?":"No",
"Is Amy chubby?":"No","Who is Amy's most powerful twin?":"Cow","Which came first the chicken or the egg?":"The poop",
"What does the fox say?":"Ring-ding-ding-ding-ding-ding","Is disney collector programs stuipid?":"Yes",
"What is the best type of video that you can watch, excluding gameplay?":"YouTube Poops"}

for quizNum in range(35):
    quizFile = open('capitalsquiz%s.txt' % (quizNum + 1), 'w')
    answerKeyFile = open('capitalsquiz_answers%s.txt' % (quizNum + 1), 'w')
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + 'Random questions quiz (Form %s)' % (quizNum + 1))
    quizFile.write('\n\n')
    states = list(capitals.keys())
    random.shuffle(states)
for questionNum in range(10):

# Get right and wrong answers.
    correctAnswer = capitals[states[questionNum]]
    wrongAnswers = list(capitals.values())
    del wrongAnswers[wrongAnswers.index(correctAnswer)]
    wrongAnswers = random.sample(wrongAnswers, 3)
    answerOptions = wrongAnswers + [correctAnswer]
    random.shuffle(answerOptions)
    quizFile.write('%s. %s?\n' % (questionNum + 1,states[questionNum]))
    for i in range(4):
        quizFile.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i]))
    quizFile.write('\n')
    answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
quizFile.close()
answerKeyFile.close()