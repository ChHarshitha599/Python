class Exam:
    pass_marks = 22
    tot_questions = 50

    def __init__(self,name):
        self.name = name

    def start_exam(self,exam_started):
        self.exam_started = exam_started
        print("Exam started for ",self.name)

    def submit_exam(self,correct_answers):
        if not self.exam_started:
            print("Exam has not yet started")
        self.correct_answers = correct_answers
        self.exam_submitted = True
        print("Exam submitted for ",self.name)
        self.calculate_score()

    def calculate_score(self):
        if self.exam_submitted == False:
            print("Exam not submitted yet!")
            return
        score = 0
        score += self.correct_answers
        print("Score:",score)
        if score >= Exam.pass_marks:
            print("PASS")
        else:
            print("FAIL")

    @classmethod
    def update_pass_marks(cls, new_pass_marks):
        if new_pass_marks >= 0 and new_pass_marks <= Exam.tot_questions:
            cls.pass_marks = new_pass_marks
            print("Updated pass marks to:", cls.pass_marks)
        else:
            print("Invalid pass marks")

e1 = Exam("Maths")
e1.start_exam(True)
e1.submit_exam(30)
Exam.update_pass_marks(10)
