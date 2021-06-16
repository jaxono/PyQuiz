from enum import Enum


# A class that is used to store a question
class Question:
	def __init__(self):
		self.correct_answer = 0
		self.question = ""
		self.answers = []


# States that the decoder can be in
class DecodeState(Enum):
	QUESTION = 0
	INCORRECT_ANSWER = 1
	CORRECT_ANSWER = 2


# Main decoder function
def decode_pqq(name: str):

	# A function to decide what should happen to the current string based on the decoder state
	def end_string():
		striped_current_string = current_string.strip()
		if decode_state == DecodeState.QUESTION:
			current_question.question = striped_current_string
		elif decode_state == DecodeState.CORRECT_ANSWER or decode_state == DecodeState.INCORRECT_ANSWER:
			current_question.answers.append(striped_current_string)
			if decode_state == DecodeState.CORRECT_ANSWER:
				current_question.correct_answer = len(current_question.answers) - 1

	# Open the file and load the content to a string
	file = open(name, "r", encoding="utf-8")
	file_text = file.read()
	file.close()

	# Init some vars
	current_question = Question()
	decode_state = DecodeState.QUESTION
	current_string = ""
	questions = []

	# The decoder loop
	for char in file_text:  # Step through all the chars in the file

		# If there is a newline char then we will append the current question to the question list
		if char == "\n":
			end_string()
			current_string = ""
			decode_state = DecodeState.QUESTION
			if len(current_question.answers) != 0:
				questions.append(current_question)
			current_question = Question()

		# A bar will start a incorrect answer
		elif char == "|":
			end_string()
			current_string = ""
			decode_state = DecodeState.INCORRECT_ANSWER

		# A asterisk will start a correct answer
		elif char == "*":
			end_string()
			current_string = ""
			decode_state = DecodeState.CORRECT_ANSWER

		# Any other char will append the current string
		else:
			current_string += char

	# return the list of questions at the end
	return questions


# Test function
def test_decode_pqq():
	questions = decode_pqq("test.pqq")
	for question in questions:
		print(question.question)
		for answer in question.answers:
			print(answer)
		print(question.correct_answer)


if __name__ == "__main__":
	test_decode_pqq()
