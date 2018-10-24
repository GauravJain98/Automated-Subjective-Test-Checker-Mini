from worker import train,evaluate

class Question():
    def __init__(self, data_set,marks):
        self.data_set = data_set
        self.marks = marks

Q = Question(data_set = ["This is a nice project we will do awesome things. The author is Gaurav Jain and he was a great man","This is a nice project we will do awesome things and Gaurav Jain"],marks = 10)

train(Q.data_set)

while True:
    ans = str(input("Enter answer to evaluate or 0 to exit \n"))
    if ans == "0":
        break
    print("Marks " + str(evaluate(Q.marks,ans)) + "Out of "+Q.marks)