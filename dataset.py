import csv
import pandas as pd

# 将head和tail的offset找到并存储
filename = '数据集1.csv'
header = ['sentence', 'relation', 'head', 'head_offset', 'tail', 'tail_offset']
all_list1 = [[1, 2, 3, 10, 11, 12], [4, 5, 6, 14, 15, 16], [7, 8, 9, 17, 18, 19]]
f = csv.reader(open(filename, 'r'))
head_list = []
tail_list = []
sentence_list = []
relation_list = []
head_offset_list = []
tail_offset_list = []
all_list = []
this_list = []
num = 0
new_list = []
for line in f:
    sentence = line[0]
    relation = line[1]
    head = line[2]
    tail = line[4]
    head_offset = sentence.find(head[0])
    tail_offset = sentence.find(tail[0])
    all_list.append(sentence)
    all_list.append(relation)
    all_list.append(head)
    all_list.append(head_offset)
    all_list.append(tail)
    all_list.append(tail_offset)

for i in range(6):
    all_list.pop(0)

for sub in all_list:
    this_list.append(sub)
    num = num + 1
    if num % 6 == 0:
        new_list.append(this_list)

        this_list = []

        continue
print(new_list)

new = pd.DataFrame(columns=header, data=new_list)
new.to_csv('D:/test2.csv')

