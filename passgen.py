import random
import tkinter

lowercase_letters = [chr(i) for i in range(ord('a'), ord('z')+1)]
uppercase_letters = [chr(i) for i in range(ord('A'), ord('Z')+1)]
digits = [chr(i) for i in range(ord('0'), ord('9')+1)]
special_characters = ['+', '-', '!', '@', '#', '$', '^', '&', '*', '(', ')', '[', ']', '{', '}']

password_characters = lowercase_letters + uppercase_letters + digits + special_characters

class MainWindow:
	def __init__(self):
		self._root = tkinter.Tk()
		self._root.title("Password generator by mfg637")
		self._passlen_label = tkinter.Label(self._root, text="Password lenght: ")
		self._passlen_label.grid(row=0, column=0)
		self._passlen_field = tkinter.Entry(self._root)
		self._passlen_field.grid(row=0, column=1)
		self._passlen_field.insert(0, '16')
		self._generate_password_button = tkinter.Button(self._root, text="Generate new Password",
			command=self.generate_password)
		self._generate_password_button.grid(row=1, column=0, columnspan=2)
		self._password_caption_label = tkinter.Label(self._root, text="New password is:")
		self._password_caption_label.grid(row=2, column=0, sticky="w")
		self._password_label = tkinter.Label(self._root, text="No passwords generated")
		self._password_label.grid(row=3, column=0, columnspan=2)
		self._copy_pass_button = tkinter.Button(self._root, text="Copy password", command=self.copy_password)
		self._copy_pass_button.grid(row=4, column=0)
		self._root.mainloop()

	def generate_password(self):
		password_len = int(self._passlen_field.get())
		password = ''
		for i in range(password_len):
			password += random.choice(password_characters)
		self._password_label['text'] = password

	def copy_password(self):
		self._root.clipboard_clear()
		self._root.clipboard_append(self._password_label['text'])
		self._root.update()


window = MainWindow()