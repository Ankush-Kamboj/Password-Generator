import tkinter as tk
import tkinter.font as font
import random
import string

class PassGen:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("450x230")
        self.root.title("Password Generator")
        self.root.resizable("false", "false")
        self.root.config(bg = "White")

        self.max_len = tk.StringVar()
        self.pwd = tk.StringVar()
        
        heading1 = font.Font(family = "Helvetica", size = 26)
        heading2 = font.Font(family = "Helvetica", size = 16)

        passGenLabel = tk.Label(self.root, text = "PASSWORD GENERATOR", bg = "White")
        passGenLabel['font'] = heading1
        passGenLabel.pack()

        passLengthLabel = tk.Label(self.root, text = "Enter password length", bg = "White")
        passLengthLabel['font'] = heading2
        passLengthLabel.pack()

        passLengthEntry = tk.Entry(self.root, textvariable = self.max_len)
        passLengthEntry['font'] = heading2
        passLengthEntry.pack()

        self.passLengthError = tk.Label(self.root, text = "")
        self.passLengthError.pack()

        passEntry = tk.Entry(self.root, textvariable = self.pwd, state = "readonly")
        passEntry['font'] = heading2
        passEntry.pack()

        generateButton = tk.Button(self.root, text = "Generate", command = self.generate)
        generateButton['font'] = heading2
        generateButton.pack()

    def generate(self):
        flag = True
        self.passLengthError.config(text="")
        try:
            len = int(self.max_len.get())
        except:
            flag = False
            self.passLengthError.config(text = "*Please enter an Integer", fg="red")
            self.pwd.set("")
        
        if flag:
            if len > 5:
                password = self.passwordGenerator(len)
                self.pwd.set(password)
            else:
                self.passLengthError.config(text = "*Please enter an Integer greater than 5",fg="red")

    def passwordGenerator(self, max_len):
        lower_char = string.ascii_lowercase
        upper_char = string.ascii_uppercase
        symbols = string.punctuation
        digits = string.digits

        combined = lower_char + upper_char + symbols + digits

        # randomly selecting a char from each of the above
        rand_lower = random.choice(lower_char)
        rand_upper = random.choice(upper_char)
        rand_symbol = random.choice(symbols)
        rand_digit = random.choice(digits)

        temp_password = rand_lower + rand_upper + rand_symbol + rand_digit
        
        for i in range(max_len-4):
            temp_password = temp_password + random.choice(lower_char+upper_char)
            password = list(temp_password)
            random.shuffle(password)

        password = "".join(password)
        return password
        
    def showDialog(self):
        self.root.mainloop()


if __name__ == "__main__":
    PassGen().showDialog()