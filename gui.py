import tkinter as tk
import gameplay
import tkinter.messagebox as tk_mb


# Simplified class for a button
class Button:
	def __init__(self, parent: tk.Frame, x: int, y: int, width: int, height: int, text: str = "Default", click_event=lambda: print("Default")):
		self.text = tk.StringVar()
		self.text.set(text)
		self.button_frame = tk.Frame(parent, width=width, height=height)
		self.button_frame.place(x=x, y=y)
		self.button_frame.propagate(False)
		self.button = tk.Button(self.button_frame, textvariable=self.text, command=click_event)
		self.button.pack(expand=True, fill=tk.BOTH)


# Simplified class for a text box
class TextBox:
	def __init__(self, parent: tk.Frame, x: int, y: int, width: int, height: int, text: str = "Default"):
		self.frame = tk.Frame(parent, width=width, height=height)		# Set size
		self.frame.place(x=x, y=y)										# Set pos
		self.frame.propagate(False)										# Disable affecting parent size
		self.text = tk.Text(self.frame)									# Create
		self.text.insert(tk.END, "")									# Set text
		self.text.config(state=tk.DISABLED)								# Disable editing text by user
		self.text.pack(expand=True, fill=tk.BOTH)						# Grow text box to fill frame


# Function for creating the gui
class GUI:
	def __init__(self, game_play_data):
		# Create window
		self.main_window = tk.Tk()														# Create
		self.main_window.title("PyQuiz")												# Set title
		self.main_window_frame = tk.Frame(self.main_window, width=640, height=540)		# Set size
		self.main_window_frame.pack()
		self.main_window.resizable(False, False)										# Disable resizing/maximising

		# Create question text box
		self.question_text = TextBox(self.main_window_frame, 20, 20, 600, 100)

		# Create end note text box
		self.end_note_text = TextBox(self.main_window_frame, 20, 260, 600, 100)

		self.score_text = TextBox(self.main_window_frame, 20, 380, 600, 20)

		# Create buttons
		self.buttons = [
			Button(self.main_window_frame, 20, 140, 186, 100, "Button 1", lambda: gameplay.click_answer(game_play_data, 0)),
			Button(self.main_window_frame, 226, 140, 186, 100, "Button 2", lambda: gameplay.click_answer(game_play_data, 1)),
			Button(self.main_window_frame, 432, 140, 186, 100, "Button 3", lambda: gameplay.click_answer(game_play_data, 2))
		]

		self.restart_button = Button(self.main_window_frame, 20, 420, 290, 100, "Restart", lambda: game_play_data.reset_game())
		self.help_button = Button(self.main_window_frame, 330, 420, 290, 100, "Help", lambda: tk_mb.showinfo("Help", "Press one of the 3 questions below the question to select a question. If your question is correct you will gain a point else you will loose a life. If you loose 3 lives then it is game over and you will need to press the restart button."))


if __name__ == "__main__":
	GUI(0)
