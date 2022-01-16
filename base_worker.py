



def delete(counter, file_name):

    file = open(file_name, mode="r", encoding="UTF-8")
    lines = file.readlines()
    file.close()

    file = open(file_name, mode="w", encoding="UTF-8")
    for i in range(len(lines)):
        if i != counter-1:
            file.write(lines[i])
    file.close()


def add(ID, name, file_name):
    flag = True
    file = open(file_name, mode="r", encoding="UTF-8")
    lines = file.readlines()
    for line in lines:
        if int(line.split(',')[0]) == int(ID):
            flag = False
            file.close()
    if flag:
        file.close()
        file = open(file_name, mode="a", encoding="UTF-8")
        file.write(str(ID) + ',' + str(name) + '\n')
        file.close()
    return flag


def getIDs(file_name):
    ret_arr = []
    file = open(str(file_name), mode="r", encoding="UTF-8")
    lines = file.readlines()
    for ID in lines:
        ret_arr.append(ID.split(',')[0])
    return ret_arr


def getNames(file_name):
    final_message = ""
    file = open(str(file_name), mode="r", encoding="UTF-8")
    lines = file.readlines()
    counter = 1
    for line in lines:
        final_message = final_message + str(counter) + '. ' + str(line.split(',')[1])
        counter+=1
    return final_message


def getAll():
    final_message = ""
    file_names = ["Base\\Group1.txt", "Base\\Group2.txt", "Base\\Group3.txt", "Base\\Group4.txt"]
    names = ["*Заказчики*", "*Группа 2*", "*Группа 3*", "*Группа 4*"]
    counter = 0
    for name in file_names:
        final_message = final_message + str(names[counter]) + '\n'
        counter += 1
        file = open(str(name), mode="r", encoding="UTF-8")
        lines = file.readlines()
        for line in lines:
            final_message = final_message + str(line)
    return final_message


