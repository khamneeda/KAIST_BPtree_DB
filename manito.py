import random

manito = ['홍석','재현','지윤','경욱','성종','유민','치혁','진호','하연']
suho = ['영철','광수','상철','영식','영수','영숙','정숙','순자','옥순']
random.shuffle(suho)
random.shuffle(manito)

print("수호천사   -->   마니또")
for i in range(9):
    print(suho[i],"      -->    ",manito[i])
print("현숙       -->     해준")

suho.append("현숙")
print("\n\n수호천사 리스트: ", suho)

####배분한 사람 리스트
suho.remove('')+