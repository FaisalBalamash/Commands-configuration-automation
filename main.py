def printConf(ID):
    last = last_digit(int(ID))
    test_list = []
    for i in range(1, 5):
        lines = f'Switch{i} Configuration:\nenable\nconf t\nip default-gateway 192.170.{last + 4 + i}.1\n'.split(
            '\n')
        test_list.append("------------------------------------------------------------------")
        for line in lines:
            test_list.append(line)
        for j in range(2, 16):
            lines = f'\nPC{j - 1} Configuration:\nenable\nconf t\ninterface f0/0\nip address 192.170.{last + 4 + i}.{j} 255.255.255.0\n'.split(
                '\n')
            for line in lines:
                test_list.append(line)
    return test_list


def last_digit(num):
    return num - (10 * int(num / 10))


if __name__ == '__main__':
    while True:
        ID = input("Please Enter your ID: ")
        if len(ID) == 7 and ID.isnumeric():
            file = open('Commands.txt', 'w')
            for i in range(len(printConf(ID))):
                file.writelines(str(printConf(ID)[i]) + "\n")

            file.close()
            print("Commands are printed in Commands.txt")
            exit(1)
        else:
            print("incorrect ID")
