import tkinter as tk
import random 

class RockPaperScissorsApp:
    def __init__(self,master):
        self.master =master
        master.title("Rock Paper Scissors Game")
        master.geometry("420x420")
        master.configure(bg= "#e5d4f1")

        self.options = ["Rock","Paper","Scissors"]
        self.user_score = 0
        self.cpu_score = 0

        self.header = tk.Label(master, text="let's play rock Paper Scissors", font=("Calibri",16,"italic","bold"),bg= "#f0e8a8", fg= "#105bd4")
        self.header.pack(pady = 10)

        self.button_frame = tk.Frame(master, bg= "#fcf6bd")
        self.button_frame.pack(pady=15)

        self.rock_btn = tk.Button(self.button_frame, text = "Rock", width=12, command=lambda: self.play_game("Rock"))
        self.paper_btn = tk.Button(self.button_frame, text = "Paper", width=12, command=lambda: self.play_game("Paper"))
        self.scissors_btn = tk.Button(self.button_frame, text = "Scissors", width=12, command=lambda: self.play_game("Scissors"))

        self.rock_btn.grid(row=0, column=0, padx=10)
        self.paper_btn.grid(row=0, column=1, padx=10)
        self.scissors_btn.grid(row=0, column=2, padx=10)

         #display choice
        self.choice_info = tk.Label(master, text="", font=("Calibri",12,),bg= "#fcf6bd")
        self.choice_info.pack(pady=10)

        #result
        self.result_text = tk.Label(master, text="", font=("Calibri",14,"bold"),bg= "#f09273")
        self.result_text.pack(pady=5)

        #score
        self.score_text = tk.Label(master, text="User: 0 | CPU: 0", font=("Calibri",12,),bg= "#fcf6bd")
        self.score_text.pack(pady=10)

        #Resert button
        self.reset_btn = tk.Button(master, text="Reset Game", command=self.reset_game)
        self.reset_btn.pack(pady=10)

    def play_game(self, user_choice):
        cpu_choice = random.choice(self.options)
        self.choice_info.config(text=f"You: {user_choice} | Computer: {cpu_choice}")

          #outcome
        if user_choice == cpu_choice:
            outcome= "It's a Tie!"
        elif(user_choice == "Rock" and cpu_choice == "Scissors") or \
            (user_choice == "Paper" and cpu_choice == "Rock") or \
            (user_choice == "Scissors" and cpu_choice == "Paper"):
            outcome = "You Win!"
            self.user_score += 1
        else:
            outcome = "You Lose!"
            self.cpu_score += 1
        
        self.result_text.config(text=outcome)
        self.score_text.config(text=f"User: {self.user_score} | CPU: {self.cpu_score}")

    def reset_game(self):
        self.user_score = 0
        self.cpu_score = 0
        self.choice_info.config(text="")
        self.result_text.config(text="")
        self.score_text.config(text="User: 0 | CPU: 0")

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsApp(root)
    root.mainloop()
        
    
        


        
        
