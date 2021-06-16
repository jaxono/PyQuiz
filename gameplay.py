import gui
import decode_pqq
import tkinter as tk
import random


# A class that contains some variables from the gameplay function so that they can be shared across functions
class GamePlayData:
	def __init__(self):
		# Init vars
		self.score = 0
		self.lives = 42069
		self.correct_answer = 0
		self.gui = 0
		self.question_num = 0
		# Load questions
		self.questions = decode_pqq.decode_pqq("test.pqq")


# Function that will change the current question to another question and will change the gui interface elements to that of the question.
def new_question(game_play_data):
	# Get a new question id and make sure that it is not the same as the last one
	question_id = game_play_data.question_num
	while question_id == game_play_data.question_num:
		question_id = random.randint(0, len(game_play_data.questions) - 1)
	game_play_data.question_num = question_id

	# Update the question box
	game_play_data.gui.question_text.text.config(state=tk.NORMAL)
	game_play_data.gui.question_text.text.delete(1.0, tk.END)
	game_play_data.gui.question_text.text.insert(tk.END, game_play_data.questions[question_id].question)
	game_play_data.gui.question_text.text.config(state=tk.DISABLED)

	# Update the button texts
	for x in range(3):
		game_play_data.gui.buttons[x].text.set(game_play_data.questions[question_id].answers[x])


# Function to call when a button is clicked
def click_answer(game_play_data, button_num: int):
	# Print/update correctness, score and lives remaining
	print("")
	if button_num == game_play_data.questions[game_play_data.question_num].correct_answer:
		game_play_data.score += 1
		print("Correct")
	else:
		game_play_data.lives -= 1
		print("Incorrect")
	print("Score: {}, Lives: {}".format(game_play_data.score, game_play_data.lives))
	
	# Get a new question
	new_question(game_play_data)


# The initial function that sets up the game state
def gameplay():
	game_play_data = GamePlayData()						# Init gameplay var
	game_play_data.gui = gui.GUI(game_play_data)		# Create GUI
	new_question(game_play_data)						# Show first question
	game_play_data.gui.main_window.mainloop()			# Run the main loop until the program ends


# Entrypoint
if __name__ == "__main__":
	gameplay()
