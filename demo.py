import random as rn

hint_word = []

def getUniqueNumber(encode_answer):
	value = 0
	while(True):
		randNumber = rn.randint(0, len(encode_answer) - 1)
		if (randNumber not in hint_word):
			value = randNumber
			break
	return value


def getHint(encode_answer):
	hint = ""
	rang = rn.randint(1, len(encode_answer)/2)
	answer_word = encode_answer
	answer_splitted_word = list(answer_word)
	hint_word_length = len(encode_answer) - 1
	hint_splitted_word = ("_" * hint_word_length).split("_")
	print(hint_splitted_word)
	print(answer_word)
	print(answer_splitted_word)	
	for i in range(0, len(hint_splitted_word)):
		hint_splitted_word[i] = "_"

	for i in range(0, rang):
		unique_value = getUniqueNumber(encode_answer)
		hint_word.append(unique_value)
		for n in hint_word:
			hint_splitted_word[n] = answer_splitted_word[n]	

	for i in hint_splitted_word:
		hint = hint + i
    
	return hint
	
print(getHint("come"))