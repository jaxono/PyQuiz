import tkinter as tk


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


# Function for creating the gui
def gui():
	# Create window
	main_window = tk.Tk()													# Create
	main_window.title("PyQuiz")												# Set title
	main_window_frame = tk.Frame(main_window, width=640, height=480)		# Set size
	main_window_frame.pack()
	main_window.resizable(False, False)										# Disable resizing/maximising

	# Create text box inside its own frame so that we can set its size in pixels
	question_text_frame = tk.Frame(main_window_frame, width=600, height=100)		# Set size
	question_text_frame.place(x=20, y=20)											# Set pos
	question_text_frame.propagate(False)											# Disable affecting parent size
	question_text = tk.Text(question_text_frame)									# Create
	question_text.insert(tk.END, "Hi")												# Set text
	question_text.config(state=tk.DISABLED)											# Disable editing text by user
	question_text.pack(expand=True, fill=tk.BOTH)															# Grow text box to fill frame

	# Create buttons
	buttons = [
		Button(main_window_frame, 20, 140, 186, 100, "Button 1", lambda: print("Button 1")),
		Button(main_window_frame, 226, 140, 186, 100, "Button 2", lambda: print("Button 2")),
		Button(main_window_frame, 432, 140, 186, 100, "Button 3", lambda: print("Button 3"))
	]
	buttons[0].text.set("Hi")

	main_window.mainloop()


if __name__ == "__main__":
	gui()
