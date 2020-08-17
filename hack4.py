if __name__ == '__main__':
    N = int(input("Enter number of commands: "))
    list1 = []
    for i in range(N):
        givenCommand = input().split()
        commandName = givenCommand[0]
        args = givenCommand[1:]

        if commandName != "print":
            finalCommand = commandName + "(" + "," .join(args) + ")"
            eval("list1."+finalCommand)
        else:
            print(list1)