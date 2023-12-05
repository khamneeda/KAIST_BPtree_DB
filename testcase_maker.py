import os
import random
from bptree import BPTree

def safe_mkdir(path):
    if not os.path.exists(path):
        os.mkdir(path)

def input_maker():
    safe_mkdir('input_gened')
    safe_mkdir('deletion')

    for i in range(30,60):
        insert_list = random.sample(range(1,31),10)

        f = open("input_gened/"+str(i)+".txt","w")
        d = open("deletion/"+str(i+30)+".txt","w")
        for j in range(10):
            f.write("Insert "+str(insert_list[j])+"\n")
            d.write("Insert "+str(insert_list[j])+"\n")
        insert_list.remove(random.choice(insert_list))
        for j in range(9):
            d.write("Delete "+str(insert_list[j])+"\n")
        f.close()
        d.close()

input_maker()