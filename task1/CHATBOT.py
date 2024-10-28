import tkinter as tk
from tkinter import scrolledtext

class SimpleChatbot:
    def __init__(self, master):
        self.master = master
        master.title("Simple Chatbot")

        self.chat_area = scrolledtext.ScrolledText(master, state='disabled', wrap='word', width=50, height=20)
        self.chat_area.grid(row=0, column=0, padx=10, pady=10)

        self.entry = tk.Entry(master, width=48)
        self.entry.grid(row=1, column=0, padx=10, pady=10)
        self.entry.bind("<Return>", self.send_message)

        self.send_button = tk.Button(master, text="Send", command=self.send_message)
        self.send_button.grid(row=1, column=1, padx=10)

    def send_message(self, event=None):
        user_input = self.entry.get()
        if user_input.strip() == "":
            return

        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, "You: " + user_input + "\n")
        self.chat_area.config(state='disabled')

        response = self.get_response(user_input)
        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, "Chatbot: " + response + "\n")
        self.chat_area.config(state='disabled')

        self.entry.delete(0, tk.END)

    def get_response(self, user_input):
        user_input = user_input.lower()

        if "hello" in user_input or "hi" in user_input:
            return "Hello! How can I assist you today?"
        elif "how are you" in user_input:
            return "I'm just a program, but I'm functioning as expected! How about you?"
        elif "your name" in user_input:
            return "I am a simple chatbot created to help you."
        elif "help" in user_input:
            return "Sure! What do you need help with?"
        elif "bye" in user_input or "exit" in user_input:
            return "Goodbye! Have a great day!"
        elif "weather" in user_input:
            return "I'm not able to check the weather, but I hope it's nice outside!"
        else:
            return "I'm sorry, I didn't understand that. Can you please rephrase?"

if __name__ == "__main__":
    root = tk.Tk()
    chatbot = SimpleChatbot(root)
    root.mainloop()
