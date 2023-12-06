import os
import random
from bptree import BPTree

def safe_mkdir(path):
    if not os.path.exists(path):
        os.mkdir(path)

def input_maker():
    safe_mkdir('input_10')

    for i in range(1,200):
        insert_list = random.sample(range(1,31),10)
        f = open("input_10/"+str(i)+".txt","w")
        for j in range(10):
            f.write("Insert "+str(insert_list[j])+"\n")
        insert_list.remove(random.choice(insert_list))
        for j in range(9):
            f.write("Delete "+str(insert_list[j])+"\n")
        f.close()

#input_maker()
safe_mkdir('output_10')
fname = 1
while os.path.exists(f'input_10/{fname}.txt'):
    # if fname != 211:
    #     fname += 1
    #     continue
    insert_keys, delete_keys = [], []
    input_f = open(f'input_10/{fname}.txt')
    input_s = input_f.read().splitlines()
    for line in input_s:
        if line.startswith('Insert '):
            val = int(line[len('Insert '):])
            insert_keys.append(val)
        elif line.startswith('Delete '):
            val = int(line[len('Delete '):])
            delete_keys.append(val)
    tree = BPTree()
    output = tree.show(insert_keys, delete_keys)
    output_f = open(f'output_10/{fname}.txt', 'w')
    output_f.write(output)
    answer_f = open(f'answer_10/{fname}.txt')
    answer = answer_f.read()
    if output == answer:
        print(f'Test {fname} Correct')
    else:
        print(f'Incorrect For Test {fname}')
        #exit()
    fname += 1