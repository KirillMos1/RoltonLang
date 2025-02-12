import sys

vars_list = {}

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
                print("\033[35mError 121 - Var not found\033[0m")
                return
        returned += str(arg) + " "
    print(returned)

def inputing(text, var):
    vars_list[var] = ["str", input(text)]

def typing(var):
    if var not in vars_list.keys():
        print("\033[35mError 121 - Var not found\033[0m")
    else:
        print(f"type {vars_list[var][0]}")

# def go_in_if(doings):
#     for doing in doings:
#         intepriter(doing)

def runner(com):
    global ifer_res, ifer, repeater, list_reps
    if "(" in com and ")" in com:
        func = com.split("(")[0]
        match func:
            case "print":
                args = com.split("(")[1].replace(")", "").split(", ")
                if args[0]:
                    printer(args)
                else:
                    print()
            case "type":
                var = com.split("(")[1].replace(")", "")
                typing(var)
            case "input":
                args = com.split("(")[1].replace(")", "").split(", ")
                if len(args) < 2:
                    print("\033[35mError 111 - invalid syntax\033[0m")
                    return
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
                                print("\033[35mError 121 - Var not found\033[0m")
                                return
            case "exit":
                raise SystemExit()
    elif com == "}":
        if ifer:
            ifer = False
            return
        elif repeater:
            repeater = False
            return
        else:
            print("\033[35mError 111 - invalid syntax\033[0m")
    elif "if" in com:
        if "{" in com:
            ifer = True
            usl = com.replace("if ", "").replace(" {", "")
            if "==" in usl:
                el1 = usl.replace(" == ", "")[0]
                el2 = usl.replace(" == ", "")[1]
                if "\"" in el1:
                    el1 = rl1.replace("\"", "")
                    tp1 = "str"
                else:
                    if el1.isdigit():
                        tp1 = "int"
                    else:
                        if el1 in vars_list.keys():
                            el1n = vars_list[el1][1]
                            tp1 = vars_list[el1][0]
                            el1 = el1n
                        else:
                            print("\033[35mError 121 - Var not found\033[0m")
                            ifer = False
                            return
                if "\"" in el2:
                    el2 = rl1.replace("\"", "")
                    tp2 = "str"
                else:
                    if el2.isdigit():
                        tp2 = "int"
                    else:
                        if el2 in vars_list.keys():
                            el2n = vars_list[el2][1]
                            tp2 = vars_list[el2][0]
                            el2 = el2n
                        else:
                            print("\033[35mError 121 - Var not found\033[0m")
                            ifer = False
                            return
                if tp1 != tp2:
                    ifer_res = False
                    ifer = True; return 
                else:
                    ifer_res = eval(f"{el1} == {el2}")
                    ifer = True; return 
        else:
            print("\033[35mError 113 - don`t find open symbol for body\033[0m")
            ifer = False
            return
    elif "repeats" in com:
        if "{" in com:
            repeats = com.replace("repeats", "").replace(" {", "")
            if not repeats:
                print("\033[35mError 111 - invalid syntax\033[0m")
                ifer = False
                return
            repeater = True
            list_reps.append(repeats)
        else:
            print("\033[35mError 111 - invalid syntax\033[0m")
            return
    elif "=" in com:
        coms = com.split("=")
        coms[0] = coms[0].strip()
        if coms[0].startswith("1") or coms[0].startswith("2") or coms[0].startswith("3") or coms[0].startswith("4") or coms[0].startswith("5") or coms[0].startswith("6") or coms[0].startswith("7") or coms[0].startswith("8") or coms[0].startswith("9"):
            print("\033[35mError 112 - invalid var name\033[0m")
            ifer = False
            return
        else:
            if coms[1][1:].isdigit():
                vars_list[coms[0]] = ["int", coms[1][1:]]
            else:
                if "\"" in coms[1]:
                    vars_list[coms[0]] = ["str", coms[1][1:].replace("\"", "")]
                else:
                    if coms[1][1:] in vars_list.keys():
                        vars_list[coms[0]] = [vars_list[coms[1][1:]][0], vars_list[coms[1][1:]][1]]
                    else:
                        print("\033[35mError 121 - Var not found\033[0m")
                        ifer = False
                        return
    elif com == "":
        return
    else:
        print("\033[35mError 111 - invalid syntax\033[0m")
        return

def run_reps(lister):
    repeatings = lister[0]
    lister.pop(0)
    for i in range(int(repeatings[1:])):
        for com in lister:
            runner(com)

def run_if(doings):
    for doing in doings:
        runner(doing)

repeater = False
ifer = False
ifer_res = None
list_ifer = []
list_reps = []

def intepriter(fase = "std"):
    global list_ifer, ifer, repeater, list_reps
    if ifer:
        fase = "if"
    if repeater:
        fase = "repeats"
    if fase == "if":
        com = input("... ")
        if com == "}":
            if ifer_res:
                ifer = False
                list_ifer = []
                run_if(list_ifer)
                return
            else:
                return
        else:
            list_ifer.append(com)
    elif fase == "repeats":
        com = input("... ")
        if com == "}":
            run_reps(list_reps)
            repeater = False
            list_reps = []
            return
        else:
            list_reps.append(com)
    else:
        com = input(">>> ")
        runner(com)

def run_file(path):
    file_get = open(path, "r", encoding = "utf-8")
    for line in file_get.read().split("\n"):
        runner(line)

try:
    filename = sys.argv[1]
    if ".rolton" not in filename:
        print("\033[35mError 241 - file don`t have extension \".rolton\"\033[0m")
        runner("exit()")
    if "\\" not in filename:
        if "/" not in filename:
            print(f"{filename}")
            print("\033[35mError 242 - enter the absolute path to the file\033[0m")
            runner("exit()")
    else:
        run_file(filename)
        runner("exit()")
except SystemExit:
    runner("exit()")
except FileNotFoundError:
    print("\033[35mError 243 - file not found\033[0m")
    runner("exit()")
except:
    pass

def start():
    print("-"*50, "\n" + "|" + " "*19 + "RoltonLang", " "*18 + "|", "\n" + "-"*50)
    while True:
        intepriter()

start()
