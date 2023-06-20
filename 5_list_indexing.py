my_list = [3, 5, 8, 9]

repeat_it = True

while repeat_it:
    try:
        index = int(input("index: "))
        print(my_list[index])
        repeat_it = False
    except Exception as ex:
        # print(f"{type(ex)}: {ex}")
        pass
