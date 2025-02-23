import sys

vars_list = {} # name : [type, value]

def printer(args):
    returned = ""
    for arg in args:
        if ",/." in arg:
            arg = arg.replace(",/.", ", ").replace("\"", "")
        elif ",/." not in arg:
            if arg in vars_list.keys():
                if vars_list[arg][0] == "list":
                    arg = vars_list[arg][1]
                else:
                    arg = vars_list[arg][1]
                    if arg.startswith(" "):
                        arg = arg.replace(" ", "", 1)
            elif "\"" in arg:
                arg = arg.replace("\"", "")
            else:
                if arg.isdigit():
                    pass
                else:
                    print("\033[35mError 121 - Var not found\033[0m\a")
                    return
        returned += str(arg) + " "
    print(returned)

def inputing(text, var):
    vars_list[var] = ["str", input(text)]

def typing(var):
    if var not in vars_list.keys():
        print("\033[35mError 121 - Var not found\033[0m\a")
    else:
        print(f"type {vars_list[var][0]}")

# def go_in_if(doings):
#     for doing in doings:
#         intepriter(doing)

def runner(com, line = "None", where_run = "intepriter"):
    global ifer_res, ifer, repeater, list_reps, infer
    if "(" in com and ")" in com:
        if com[-1] != ")":
            print(f"\033[35mAn error was occuped!\nLine {line} from '{where_run}'\nError 111 - invalid syntax\033[0m\a")
            return
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
                    print(f"\033[35mAn error was occuped!\nLine {line} from '{where_run}'\nError 111 - invalid syntax\033[0m\a")
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
                                print(f"\033[35mAn error was occuped!\nLine {line} from '{where_run}'\nError 121 - Var not found\033[0m\a")
                                return
            case "exit":
                raise SystemExit()
            case "pomidor":
                print("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠻⣶⡆⠀⠿⠀⣶⠒⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣴⠾⠛⢹⣶⡤⢶⣿⡟⠶⠦⠄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣶⣤⣤⣤⣤⣴⠂⠸⠋⢀⣄⡉⠓⠀⠲⣶⣾⣿⣷⣄⠀⠀⠀⠀
⠀⠀⠀⢀⣾⡿⠋⠁⣠⣤⣿⡟⢀⣠⣾⣿⣿⣿⣷⣶⣤⣼⣿⣿⣿⣿⣆⠀⠀⠀
⠀⠀⠀⣾⡟⠀⣰⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀
⠀⠀⢸⡿⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀
⠀⠀⢸⡇⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀
⠀⠀⢸⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀
⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀
⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀
⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠉⠛⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
            case "expr":
                args = com.split("(")[1][:-1].split(", ")
            case _:
                print(f"\033[35mAn error was occuped!\nLine {line} from '{where_run}'\nError 111 - invalid syntax\033[0m\a")
    elif com == "}":
        if ifer:
            ifer = False
            return
        elif repeater:
            repeater = False
            return
        else:
            print(f"\033[35mAn error was occuped!\nLine {line} from '{where_run}'\nError 111 - invalid syntax\033[0m\a")
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
                            print(f"\033[35mAn error was occuped!\nLine {line} from '{where_run}'\nError 121 - Var not found\033[0m\a")
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
                            print(f"\033[35mAn error was occuped!\nLine {line} from '{where_run}'\nError 121 - Var not found\033[0m\a")
                            ifer = False
                            return
                if tp1 != tp2:
                    ifer_res = False
                    ifer = True; return 
                else:
                    ifer_res = eval(f"{el1} == {el2}")
                    ifer = True; return 
        else:
            print(f"\033[35mAn error was occuped!\nLine {line} from '{where_run}'\nError 113 - don`t find open symbol for body\033[0m\a")
            ifer = False
            return
    elif "repeats" in com:
        if "{" in com:
            repeats = com.replace("repeats", "").replace(" {", "")
            if not repeats:
                print(f"\033[35mAn error was occuped!\nLine {line} from '{where_run}'\nError 111 - invalid syntax\033[0m\a")
                ifer = False
                return
            repeater = True
            list_reps.append(repeats)
        else:
            print(f"\033[35mAn error was occuped!\nLine {line} from '{where_run}'\nError 111 - invalid syntax\033[0m\a")
            return
    elif "=" in com:
        coms = com.split("=")
        coms[0] = coms[0].strip()
        if coms[0][:1].isdigit() or not coms[0].isascii():
            print(f"\033[35mAn error was occuped!\nLine {line} from '{where_run}'\nError 112 - invalid var name\033[0m\a")
            ifer = False
            return
        else:
            if "[" in coms[1]: # список
                if coms[1][-1] == "]":
                    elements = coms[1].replace("[", "", 1)[0:-1].split(", ")
                    elements_ended = []
                    for el in elements:
                        if "\"" in el:
                            elements_ended.append(el.replace("\"", "")[1:] if el.replace("\"", "")[0] == " " else el.replace("\"", ""))
                        else:
                            if el.isdigit():
                                elements_ended.append(el)
                            else:
                                if el in vars_list.keys():
                                    el = vars_list[el][1]
                                    elements_ended.append(el)
                                else:
                                    print(f"\033[35mAn error was occuped!\nLine {line} from '{where_run}'\nError 121 - var not found\033[0m\a")
                                    return
                    vars_list[coms[0]] = ["list", elements_ended]
                else:
                    print(f"\033[35mAn error was occuped!\nLine {line} from '{where_run}'\nError 111 - invalid syntax\033[0m\a")
                    return
            elif coms[1][1:].isdigit():
                vars_list[coms[0]] = ["int", coms[1][1:]]
            # if "("
            else:
                if "\"" in coms[1]:
                    vars_list[coms[0]] = ["str", coms[1][1:].replace("\"", "")]
                else:
                    if coms[1][1:] in vars_list.keys():
                        vars_list[coms[0]] = [vars_list[coms[1][1:]][0], vars_list[coms[1][1:]][1]]
                    else:
                        print(f"\033[35mAn error was occuped!\nLine {line} from '{where_run}'\nError 121 - Var not found\033[0m\a")
                        ifer = False
                        return
    elif "inf" in com:
        if "{" in com:
            if len(com) == 5:
                infer = True
            else:
                print(f"\033[35mAn error was occuped!\nLine {line} from '{where_run}'\nError 111 - invalid syntax\033[0m\a")
                return
        else:
            print(f"\033[35mAn error was occuped!\nLine {line} from '{where_run}'\nError 111 - invalid syntax\033[0m\a")
            return
    elif com == "":
        return
    else:
        print(f"\033[35mAn error was occuped!\nLine {line} from '{where_run}'\nError 111 - invalid syntax\033[0m\a")
        return

def run_inf(doings):
    if "stop" not in doings:
        while True:
            for do in doings:
                runner(do)
    else:
        status = "dfr"
        while status != "stop":
            for do in doings:
                if do == "stop":
                    status = "stop"
                    break
                else:
                    runner(do)

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
infer = False
list_ifer = []
list_reps = []
list_infer = []

def intepriter(fase = "std"):
    global list_ifer, ifer, repeater, list_reps, list_infer, infer
    if ifer:
        fase = "if"
    if repeater:
        fase = "repeats"
    if infer:
        fase = "inf"
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
    elif fase == "inf":
        com = input("... ")
        if com == "}":
            run_inf(list_infer)
            infer = False
            list_infer = []
            return
        else:
            list_infer.append(com)
    else:
        com = input(">>> ")
        runner(com)

def run_file(path):
    file_get = open(path, "r", encoding = "utf-8")
    i = 1
    for line in file_get.read().split("\n"):
        runner(line, i, path)

try:
    filename = rf"{sys.argv[1]}"
    if ".rolton" not in filename:
        print("\033[35mError 241 - file don`t have extension \".rolton\"\033[0m\a")
        print("Press Enter to exit")
        input()
        runner("exit()")
    if "\\" not in filename:
        if "/" not in filename:
            print(f"{filename}")
            print("\033[35mError 242 - enter the absolute path to the file\033[0m\a")
            input()
            runner("exit()")
    else:
        run_file(filename)
        input()
        runner("exit()")
except SystemExit:
    runner("exit()")
except FileNotFoundError:
    input()
    print("\033[35mError 243 - file not found\033[0m\a")
    runner("exit()")
except Exception as e:
    pass

def start():
    print("-"*50, "\n" + "|" + " "*19 + "RoltonLang", " "*18 + "|", "\n" + "-"*50)
    while True:
        intepriter()

start()
