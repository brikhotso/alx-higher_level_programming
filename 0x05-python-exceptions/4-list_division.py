def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            result = 0
            print("Division by 0")
        except TypeError:
            result = 0
            print("Wrong type")
        except IndexError:
            result = 0
            print("Out of range")
        finally:
            result_list.append(result)

    return result_list