test_count = int(input())
for _ in range(test_count):
    x = 0
    y=0
    command_line = input()
    for command in command_line:
        if command == ">":
            x = x+1
        elif command == "<":
            x = x-1
        elif command =="^":
            y=y+1
        elif command == "v":
            y=y-1
    print (x ,y)
