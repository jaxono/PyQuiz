import tkinter as tk
import gameplay


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
		self.text.insert(tk.END, "Hi")									# Set text
		self.text.config(state=tk.DISABLED)								# Disable editing text by user
		self.text.pack(expand=True, fill=tk.BOTH)						# Grow text box to fill frame


# Function for creating the gui
class GUI:
	def __init__(self, game_play_data):
		# Create window
		self.main_window = tk.Tk()														# Create
		self.main_window.title("PyQuiz")												# Set title
		self.main_window_frame = tk.Frame(self.main_window, width=640, height=480)		# Set size
		self.main_window_frame.pack()
		self.main_window.resizable(False, False)										# Disable resizing/maximising

		# Create question text box
		self.question_text = TextBox(self.main_window_frame, 20, 20, 600, 100)

		# Create buttons
		self.buttons = [
			Button(self.main_window_frame, 20, 140, 186, 100, "Button 1", lambda: gameplay.click_answer(game_play_data, 0)),
			Button(self.main_window_frame, 226, 140, 186, 100, "Button 2", lambda: gameplay.click_answer(game_play_data, 1)),
			Button(self.main_window_frame, 432, 140, 186, 100, "Button 3", lambda: gameplay.click_answer(game_play_data, 2))
		]


if __name__ == "__main__":
	GUI()
