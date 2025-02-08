vars_list = {"system" : ["str", "RoltonLang"]}

def printer(args):
    returned = ""
    for arg in args:
        if ",/." in arg:
            arg = arg.replace(",/.", ", ").replace("\"", "")
        elif ",/." not in arg:
            if arg in vars_list.keys():
                arg = vars_list[arg][1]
                if arg.startswith(" "):
                    arg = arg.replace(" ", "", 1)
            elif "\"" in arg:
                arg = arg.replace("\"", "")
            else:
                print("Error 121 - Var not found")
                return
        returned += str(arg) + " "
    print(returned)

def inputing(text, var):
    vars_list[var] = ["str", input(text)]

def typing(var):
    if var not in vars_list.keys():
        print("Error 121 - Var not found")
    else:
        print(f"type {vars_list[var][0]}")

def intepriter():
    com = input(">>> ")
    if "(" in com and ")" in com:
        func = com.split("(")[0]
        match func:
            case "print":
                args = com.split("(")[1].replace(")", "").split(", ")
                printer(args)
            case "type":
                var = com.split("(")[1].replace(")", "")
                typing(var)
            case "input":
                args = com.split("(")[1].replace(")", "").split(", ")
                if len(args) < 2:
                    print("Error 111 - invalid syntax")
                else:
                    if "\"" in args[0]:
                        inputing(args[0].replace("\"", ""), args[1])
                    else:
                        if args[0].isdigit():
                            inputing(args[0], args[1])
                        else:
                            if args[0] in vars_list.keys():
                                args[0] = vars_list[args[0]][1]
                                inputing(args[0], args[1])
                            else:
                                print("Error 121 - Var not found")

    elif "=" in com:
        coms = com.split("=")
        coms[0] = coms[0].strip()
        if coms[0].startswith("1") or coms[0].startswith("2") or coms[0].startswith("3") or coms[0].startswith("4") or coms[0].startswith("5") or coms[0].startswith("6") or coms[0].startswith("7") or coms[0].startswith("8") or coms[0].startswith("9"):
            print("Error 112 - invalid var name")
        else:
            if coms[1][1:].isdigit():
                vars_list[coms[0]] = ["int", coms[1][1:]]
            else:
                vars_list[coms[0]] = ["str", coms[1][1:]]
    else:
        print("Error 111 - invalid syntax")

print("RoltonLang ")
while True:
    intepriter()
