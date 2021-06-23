import gui
import decode_pqq
import tkinter as tk
import random


# A class that contains some variables from the gameplay function so that they can be shared across functions
class GamePlayData:
	gui: any

	def __init__(self):
		# Init vars
		self.game_over = 0
		self.score = 0
		self.lives = 3
		self.correct_answer = 0
		self.question_num = -1
		# Load questions
		self.questions = decode_pqq.decode_pqq("questions.pqq")

	def reset_game(self):
		self.game_over = 0
		self.score = 0
		self.lives = 3
		self.correct_answer = 0
		new_question(self)

		self.gui.score_text.text.config(state=tk.NORMAL)
		self.gui.score_text.text.delete(1.0, tk.END)
		self.gui.score_text.text.config(state=tk.DISABLED)


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
	# Update correctness, score and lives remaining
	correctness = "Incorrect"
	if not game_play_data.game_over:
		if button_num == game_play_data.questions[game_play_data.question_num].correct_answer:
			game_play_data.score += 1
			correctness = "Correct"
		else:
			game_play_data.lives -= 1
	if game_play_data.lives < 0 or game_play_data.game_over:
		game_play_data.game_over = 1
		game_play_data.lives = 0
		correctness = "Game Over"
		for x in range(3):
			game_play_data.gui.buttons[x].state = tk.DISABLED

	# Update end note box
	game_play_data.gui.end_note_text.text.config(state=tk.NORMAL)
	game_play_data.gui.end_note_text.text.delete(1.0, tk.END)
	if game_play_data.question_num != -1:
		game_play_data.gui.end_note_text.text.insert(tk.END, game_play_data.questions[game_play_data.question_num].end_note)
	else:
		game_play_data.gui.end_note_text.text.insert(tk.END, "")
	game_play_data.gui.end_note_text.text.config(state=tk.DISABLED)

	# Update scoreboard
	game_play_data.gui.score_text.text.config(state=tk.NORMAL)
	game_play_data.gui.score_text.text.delete(1.0, tk.END)
	game_play_data.gui.score_text.text.insert(tk.END, "{}, Score: {}, Lives: {}".format(correctness, game_play_data.score, game_play_data.lives))
	game_play_data.gui.score_text.text.config(state=tk.DISABLED)
	
	# Get a new question
	if not game_play_data.game_over:
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
