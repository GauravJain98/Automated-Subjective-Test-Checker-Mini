from worker import train,evaluate
from data_set import dataset

class Question():
    def __init__(self, data_set,marks,text):
        self.text = text
        self.data_set = data_set
        self.marks = marks
        self.phrases = []

    def setPhrases(self,phrases):
        self.phrases = self.phrases + phrases

    def getPhrases(self):
        return self.phrases

# markses = [10,5]

question = []
# questions = ["What is republic day?","What is Engineering?"]
for i in range(len(dataset)):
    Q = Question(data_set = dataset[i]["data"],marks = dataset[i]['max_marks'],text=dataset[i]['question'])
    train(Q)
    question.append(Q)
Q = ""


if __name__ == "__main__":
    for ans in dataset[0]['data']['test']:
        print(format(evaluate(question[0],ans)))