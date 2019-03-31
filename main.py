from worker import train, evaluate
from data_set import final_dataset


# class Question():
#     def __init__(self, data_set, marks, text):
#         self.text = text
#         self.data_set = data_set
#         self.marks = marks
#         self.phrases = []

#     def setPhrases(self, phrases):
#         self.phrases = self.phrases + phrases

#     def getPhrases(self):
#         return self.phrases

# # markses = [10,5]


# question = []
# # questions = ["What is republic day?","What is Engineering?"]
# for i in range(len(final_dataset)):
#     Q = Question(data_set=final_dataset[i]["data"], marks=final_dataset[i]
#                  ['max_marks'], text=final_dataset[i]['question'])
#     train(Q)
#     question.append(Q)
# Q = ""


if __name__ == "__main__":
    val = 0
    no = len(final_dataset[0]['data']['test'])
    for ans in final_dataset[0]['data']['test']:
        eva = evaluate(ans[0])
        val += pow(((eva-ans[1])/ans[1]), 2)/no
        print("{} {}".format(eva, ans[1]))
    print(1-pow(val, .5))
