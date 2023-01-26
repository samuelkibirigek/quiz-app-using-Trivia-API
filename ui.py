from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_board = Label(text=f"Score:{self.quiz.score}", bg=THEME_COLOR, fg="white", font=("Arial", 15, "bold"))
        self.score_board.grid(row=0, column=1)

        self.canvas = Canvas(height=350, width=300)
        self.question_text = self.canvas.create_text(
            150,
            155,
            width=200,
            text=f"The quiz question",
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        check_image = PhotoImage(file="images/true.png")
        wrong_image = PhotoImage(file="images/false.png")

        self.true_button = Button(image=check_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)
        self.false_button = Button(image=wrong_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def give_feedback(self, check):
        if check:
            self.canvas.config(bg="green")
            self.canvas.update()
        else:
            self.canvas.config(bg="red")
            self.canvas.update()
        self.window.after(1000, self.get_next_question())
        self.score_board.config(text=f"Score: {self.quiz.score}")



