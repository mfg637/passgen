import random
import tkinter

lowercase_letters = [chr(i) for i in range(ord('a'), ord('z')+1)]
uppercase_letters = [chr(i) for i in range(ord('A'), ord('Z')+1)]
digits = [chr(i) for i in range(ord('0'), ord('9')+1)]
special_characters = ['+', '-', '!', '@', '#', '$', '^', '&', '*', '(', ')', '[', ']', '{', '}']

password_characters = lowercase_letters + uppercase_letters + digits + special_characters

def strcmp(istr, tstr):
	if tstr in istr:
		return len(tstr)
	i=0
	max_closure = ""
	while (i<len(tstr)):
		j = 0
		while(j<len(istr)):
			if (istr[j]==tstr[i]):
				k=1
				closure_str = istr[j]
				equal = True
				while equal & (i+k<len(tstr)) & (j+k<len(istr)):
					equal = istr[j+k]==tstr[i+k]
					if equal:
						closure_str+=istr[j+k]
					k+=1
				if len(closure_str)>len(max_closure):
					max_closure = closure_str
			j+=1
		i+=1
	return len(max_closure)

class MainWindow:
	def __init__(self):
		self._root = tkinter.Tk()
		self._root.title("Password generator by mfg637")
		self._passlen_label = tkinter.Label(self._root, text="Password lenght: ")
		self._passlen_label.grid(row=0, column=0, sticky='e')
		self._passlen_field = tkinter.Entry(self._root)
		self._passlen_field.grid(row=0, column=1)
		self._passlen_field.insert(0, '16')
		self._similar_word_label = tkinter.Label(self._root, text="Similar to: ")
		self._similar_word_label.grid(row=1, column=0, sticky='e')
		self._similar_word_field = tkinter.Entry(self._root)
		self._similar_word_field.grid(row=1, column=1)
		self._similarity_len_label = tkinter.Label(self._root, text="Min similar chars: ")
		self._similarity_len_label.grid(row=2, column=0, sticky='e')
		self._similarity_len_field = tkinter.Entry(self._root)
		self._similarity_len_field.insert(0, '4')
		self._similarity_len_field.grid(row=2, column=1)
		self._generate_password_button = tkinter.Button(self._root, text="Generate new Password",
			command=self.generate_password)
		self._generate_password_button.grid(row=3, column=0, columnspan=2)
		self._password_caption_label = tkinter.Label(self._root, text="New password is:")
		self._password_caption_label.grid(row=4, column=0, sticky="w")
		self._password_label = tkinter.Label(self._root, text="No passwords generated")
		self._password_label.grid(row=5, column=0, columnspan=2)
		self._copy_pass_button = tkinter.Button(self._root, text="Copy password", command=self.copy_password)
		self._copy_pass_button.grid(row=6, column=0)
		self._root.mainloop()

	def generate_password(self):
		password_len = int(self._passlen_field.get())
		password = ''
		similar_word = self._similar_word_field.get()
		similar_chars = min(int(self._similarity_len_field.get()), len(similar_word))
		generate_similar_password = len(similar_word)>0
		for i in range(password_len):
			password += random.choice(password_characters)
		while (generate_similar_password):
			if strcmp(password.lower(), similar_word)>=similar_chars:
				generate_similar_password = False
			else:
				password = ""
				for i in range(password_len):
					password += random.choice(password_characters)
		self._password_label['text'] = password

	def copy_password(self):
		self._root.clipboard_clear()
		self._root.clipboard_append(self._password_label['text'])
		self._root.update()


window = MainWindow()