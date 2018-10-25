from worker import train,evaluate
from data_set import data_sets

class Question():
    def __init__(self, data_set,marks,text):
        self.text = text
        self.data_set = data_set
        self.marks = marks
        self.phrases = []

    def setPhrases(self,phrases):
        self.phrases = phrases

    def getPhrases(self,phrases):
        return self.phrases

markses = [10,5]

question = []
questions = ["What is republic day?","What is Engineering?"]
for i in range(len(markses)):
    Q = Question(data_set = data_sets[i],marks = markses[i],text=questions[i])
    train(Q)
    question.append(Q)

Q = ""


if __name__ == "__main__":
    while True:
        i = int(input("Enter Question number \n"))
        ans = str(input("Enter answer to evaluate or 0 to exit \n"))
        if(i ==1):
            print("Marks {} Out of {}".format(evaluate(question[0],ans) ,question[0].marks)) 
        if(i==2):    
            print("Marks {} Out of {}".format(evaluate(question[1],ans) ,question[1].marks)) 
        if ans == "0":
            break
