import random
import tkinter

class MainWindow:
	def __init__(self):
		self._root = tkinter.Tk()
		self._passlen_label = tkinter.Label(self._root, text="Password lenght: ")
		self._passlen_label.grid(row=0, column=0)
		self._passlen_field = tkinter.Entry(self._root)
		self._passlen_field.grid(row=0, column=1)
		self._generate_password_button = tkinter.Button(self._root, text="Generate new Password")
		self._generate_password_button.grid(row=1, column=0, columnspan=2)
		self._password_caption_label = tkinter.Label(self._root, text="New password is:")
		self._password_caption_label.grid(row=2, column=0, sticky="w")
		self._password_label = tkinter.Label(self._root, text="No passwords generated")
		self._password_label.grid(row=3, column=0, columnspan=2)
		self._copy_pass_button = tkinter.Button(self._root, text="Copy password")
		self._copy_pass_button.grid(row=4, column=0)
		self._root.mainloop()


window = MainWindow()