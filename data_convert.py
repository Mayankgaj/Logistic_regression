def data_convert(data):
    """
    data : give input as list only
    return : data converted into one hot encodeing
    """
    final_data = data[:6]
    for i in range(2,3):
        if data[-i] == 2:
            final_data.insert(0,1)
            final_data.insert(1,0)
            final_data.insert(2,0)
            final_data.insert(3,0)
            final_data.insert(4,0)
        elif data[-i] == 3:
            final_data.insert(0,0)
            final_data.insert(1,1)
            final_data.insert(2,0)
            final_data.insert(3,0)
            final_data.insert(4,0)
        elif data[-i] == 4:
            final_data.insert(0,0)
            final_data.insert(1,0)
            final_data.insert(2,1)
            final_data.insert(3,0)
            final_data.insert(4,0)
        elif data[-i] == 5:
            final_data.insert(0,0)
            final_data.insert(1,0)
            final_data.insert(2,0)
            final_data.insert(3,1)
            final_data.insert(4,0)
        elif data[-i] == 6:
            final_data.insert(0,0)
            final_data.insert(1,0)
            final_data.insert(2,0)
            final_data.insert(3,0)
            final_data.insert(4,1)
        else:
            final_data.insert(0,0)
            final_data.insert(1,0)
            final_data.insert(2,0)
            final_data.insert(3,0)
            final_data.insert(4,0)
    for i in range(1,2):
        if data[-i] == 2:
            final_data.insert(5,1)
            final_data.insert(6,0)
            final_data.insert(7,0)
            final_data.insert(8,0)
            final_data.insert(9,0)
        elif data[-i] == 3:
            final_data.insert(5,0)
            final_data.insert(6,1)
            final_data.insert(7,0)
            final_data.insert(8,0)
            final_data.insert(9,0)
        elif data[-i] == 4:
            final_data.insert(5,0)
            final_data.insert(6,0)
            final_data.insert(7,1)
            final_data.insert(8,0)
            final_data.insert(9,0)
        elif data[-i] == 5:
            final_data.insert(5,0)
            final_data.insert(6,0)
            final_data.insert(7,0)
            final_data.insert(8,1)
            final_data.insert(9,0)
        elif data[-i] == 6:
            final_data.insert(5,0)
            final_data.insert(6,0)
            final_data.insert(7,0)
            final_data.insert(8,0)
            final_data.insert(9,1)
        else:
            final_data.insert(5,0)
            final_data.insert(6,0)
            final_data.insert(7,0)
            final_data.insert(8,0)
            final_data.insert(9,0)

        del final_data[10:12]
        return final_data