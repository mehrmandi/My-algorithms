import pandas as pd
import re


data_question = pd.read_csv(r"C:\Users\USER\Desktop\quera\Files\data\qoura_questions.csv")
data_shereno = pd.read_csv(r"C:\Users\USER\Desktop\quera\Files\data\shereno.csv")
data_stopwords = open(r"C:\Users\USER\Desktop\quera\Files\data\stopwords.txt", encoding="utf8")


digit_question = data_question["question"].str.count(r'\d')

digit_shereno = data_shereno["Poem"].str.count(r'\d')

file = data_stopwords.readlines()
stopwords_line = [line.rstrip('\n') for line in file]

question_en = []

for index, row in data_question.iterrows():
    question = row['question'].split(" ")
    for word in question:
        numbers = re.findall(r"^(?=.*\b(?=\S*[a-zA-Z])(?=\S*[0-9]))", word)
        if word not in numbers:
            question_en.append(word)



question_set = set(question_en)


wanted = []

for wnt in stopwords_line:
    wnt = wnt.encode('utf-8')
    wanted.append(wnt)

poem_en = []

for index, row in data_shereno.iterrows():
    poem = row['Poem'].encode('utf-8')
    poem_en.append(poem)

word = []
for i in wanted:
    for j in poem_en:
        if i in j:
            word.append(i)





print(len(question_set))

print(sum(digit_question), sum(digit_shereno))


print(len(set(word)))

