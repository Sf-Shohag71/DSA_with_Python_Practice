commands = ["insert 0 5", "insert 1 10", "insert 0 6", "print", "remove 6", "append 9", "append 1", "sort", "print", "pop", "reverse", "print"]
my_list = []

for command in commands:
    name, *arr = command.split()
    arr = list(map(int, arr))

    match name:
        case "insert":
            my_list.insert(arr[0], arr[1])
        case "print":
            print(my_list)
        case "remove":
            my_list.remove(arr[0])
        case "append":
            my_list.append(arr[0])
        case "sort":
            my_list.sort()
        case "pop":
            my_list.pop()
        case "reverse":
            my_list.reverse()