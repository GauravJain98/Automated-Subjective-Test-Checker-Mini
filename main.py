from worker import train,evaluate
from data_set import *

class Question():
    def __init__(self, data_set,marks):
        self.data_set = data_set
        self.marks = marks
        self.phrases = []

    def setPhrases(phrases):
        self.phrases = phrases

    def getPhrases(phrases):
        return self.phrases

Q1 = Question(data_set_1 = data_set,marks = 10)
Q2 = Question(data_set_2 = data_set,marks = 5)

train(Q1)
train(Q2)


if __name__ == "__main__"
    while True:
        i = int(input("Enter Question number"))
        ans = str(input("Enter answer to evaluate or 0 to exit \n"))
        switch(i):
            case 1:print("Marks {} Out of {}".format(evaluate(Q1.marks,ans) ,Q1.marks)) break
            case 2:print("Marks {} Out of {}".format(evaluate(Q2.marks,ans) ,Q2.marks)) break
        if ans == "0":
            break
