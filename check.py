def check_type_int(sum):
    try:
        sum = int(sum)
    except ValueError:
        print("Invalid data type")
        return ""
    if sum < 0:
        print("Invalid data type")
        return ""
    return sum
def check_num(num_account, num):
    if num_account >= num or num_account < 0:
        print("Invalid number")
        return False
    return True
