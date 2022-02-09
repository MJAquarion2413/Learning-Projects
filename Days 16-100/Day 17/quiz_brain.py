class QuizBrain:
    def __init__(self, question_list):
        self.quest_list = question_list
        self.quest_num = 0
        self.score = 0;

    def next_question(self):
        question = self.quest_list[self.quest_num]
        self.quest_num += 1
        ans = input(f"Q.{self.quest_num + 1}:{question.text} (True/False)")
        self.check_answer(ans, question.ans)

    def still_has_questions(self):
        return self.quest_num < len(self.quest_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.casefold() == correct_answer.casefold():
            print("You got it correct!")
            self.score += 1
        else:
            print("You were wrong :(")
        print(f"The correct answer is: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.quest_num}\n")
