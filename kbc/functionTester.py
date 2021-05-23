import random
def lifeline(ques):
	answerKey = ques['answer']
	keysBase = ['name', 'answer', 'money']
	newQues = {x:ques[x] for x in keysBase}
	for key, value in ques.items() :
		if str(answerKey) in key:
			newQues[key] = value
	newOption = 0

	while True:
		newOption = random.randint(1,4)
		if newOption != answerKey:
			break

	for key, value in ques.items() :
			if str(newOption) in key:
				newQues[key] = value
				break
	
	return newQues



test = {
            "name": " India's largest city by population",
            "option1": "Delhi",
            "option2": "Mumbai",
            "option3": "Pune",
            "option4": "Bangalore",
            "answer": 2,
            "money": 1000
        }

print(tryout(test))