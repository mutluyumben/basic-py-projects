class quizBrain():
    
    def __init__(self, q_list):
        
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
    
    def question_queue(self):
        
        current_position = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_position.text}  (True / False): ")
        self.check_answer(user_answer, current_position.answer)

    def still_cont(self):
        if self.question_number >= len(self.question_list):
            return False
        else: 
            return True
        
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it")
            self.score += 1
        else: 
            print("WRONG")
        print(f"Your current score is {self.score}/{self.question_number}")
        print(f"Correct answer was: {correct_answer}\n")

