from os import system

show_input_arrow = True
default_input_arrow = "Leurc(sID1) _>"
input_arrow = default_input_arrow

inittext = """
ISDD cmd [Version 0.1.0.0]
(c) 1998 ISDD Company. All rights reserved.
"""

system("title ISDD cmd")
print(inittext)


def command_input(input_: list):
    try:
        exec(f"{input_[0]}(input_)")
    except NameError:
        print(f"'{input_[0]}'이(가) 내부 또는 외부 명령, 실행할 수 있는 프로그램, 또는 파이썬 파일이 아닌것 같습니다.")
    except SyntaxError:
        print("구문이 잘못되었습니다.")
    print()


def start(file: list):
    return

def cmd(self):
    system("title cmd")
    system("cmd")

def isddcmd(self):
    system("py isddcmd.py")



def say(n: list):
    global input_arrow
    if len(n) < 2:
        print(f'입력 화살표가 '
              f'{f"기본 화살표({default_input_arrow})로 되어있습니다." if default_input_arrow == input_arrow else f"{input_arrow}로 되어있습니다."}'
              )
    elif n[1] == 'inpset':
        if n[2] == 'default':
            input_arrow = default_input_arrow
        else:
            input_arrow = n[2]
    else:
        inp = str(n[1])
        if inp[0] == '$':
            try:
                print(exec(inp[1:]))
            finally:
                return
        else:
            if inp.startswith('"') and inp.endswith('"') or inp.startswith("'") and inp.endswith("'"):
                inp = inp[1:-1]
            print(inp)
    return n


while True:

    input_text = input(input_arrow if show_input_arrow else "").split(" ")
    command_input(input_text)
