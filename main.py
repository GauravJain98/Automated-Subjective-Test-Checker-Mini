from worker import train,evaluate
from data_set import *

class Question():
    def __init__(self, data_set,marks):
        self.data_set = data_set
        self.marks = marks

Q = Question(data_set = data_set,marks = 10)

train(Q.data_set)


if __name__ == "__main__"
while True:
    ans = str(input("Enter answer to evaluate or 0 to exit \n"))
    if ans == "0":
        break
    print("Marks {} Out of {}".format(evaluate(Q.marks,ans) ,Q.marks))