def dateUmwandeln(date:str)->str:
    data = []
    if date[4] == ".":
        data.append(date[3])
        data.append(date[2])
        data.append(date[0])
        data.append(date[1])
        data.append(date[4])
        for i in range(5, 9):
            data.append(date[i])
        return "".join(data)


    data.append(date[3])
    data.append(date[4])
    data.append(date[2])
    data.append(date[0])
    data.append(date[1])
    data.append(date[5])
    for i in range(6,10):
        data.append(date[i])

    return "".join(data)


