from os import system
import sys
import importlib

show_input_arrow = True
default_input_arrow = "Leurc(sID1) _>"
input_arrow = default_input_arrow
console_color = "0f"
ERRORLV = 0

inittext = """
ISDD cmd [Version 1.0.0.0]
(c) 1998` ISDD Company. All rights reserved.
"""

is_automation = len(sys.argv) > 1


def command_input(input_: list):
    if input_[0] == "exit":
        exit()
    elif input_[0] == "help":
        print(cmd_help())
    else:
        try:
            if len(input_) > 1:
                if input_[1] == "/?":
                    try:
                        exec(f"print({input_[0]}_help())")
                    except NameError:
                        try:
                            print(importlib.import_module(input_[0]).on_help())
                        except ModuleNotFoundError:
                            print(f"{input_[0]}의 도움알을 찾을수 없습니다.")
                    return
                else:
                    exec(f"{input_[0]}(input_)")
            else:
                try:
                    exec(f"{input_[0]}(input_)")
                except TypeError:
                    eval(input_[0])

        except NameError:
            try:
                a = importlib.import_module(input_[0])
                a.on_trigger(input_)
            except ModuleNotFoundError:
                print(f"{input_[0]}이(가) 내부 또는 외부 명령, 실행할 수 있는 프로그램, 또는 파이썬 파일이 아닌것 같습니다.")

        except SyntaxError:
            print("구문이 잘못되었습니다.")
    print()


def start(file: list):
    return


def cmd(title: list):
    system(f"title {'cmd' if len(title) < 2 else title[1]}")
    system("cmd")


def isddcmd(*args):
    system("py isddcmd.py")


def say(n: list):
    global input_arrow
    global show_input_arrow
    if len(n) < 2:

        print(f'입력 화살표가 '
              f'{"기본 화살표(" + default_input_arrow + ")로 되어있습니다." if default_input_arrow == input_arrow else input_arrow + "로 되어있습니다."}')
    elif n[1] == 'inpset':

        if len(n) > 2 and n[2] == 'default':
            input_arrow = default_input_arrow
        elif len(n) > 2:
            input_arrow = n[2]
        else:
            print("입력 화살표 설정값이 잘못되었습니다.")
    elif n[1] == 'on':
        show_input_arrow = True
    elif n[1] == 'off':
        show_input_arrow = False

    else:
        inp = str(n[1])
        if (inp.startswith('"') and inp.endswith('"')) or (inp.startswith("'") and inp.endswith("'")):
            inp = inp[1:-1]
            print(inp)
        else:
            print(inp)
    return n


def say_help():
    return """
메시지를 표시하거나 명령 줄을 설정하거나 켜거나 끕니다.
ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
SAY [ON | OFF]
SAY [message]
SAY [INPSET] [input_arrow | DEFAULT]
ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
input_arrow는 무조건 소문자로 바뀝니다.
현재 명령줄 설정을 표시하려면 매개 변수 없이 SAY를 입력하십시오.
"""


def cmd_help():
    return """
특정 명령어에 대한 자세한 내용이 필요하면 명령어 뒤에 /?를 입력하세요.

SAY            메시지를 표시하거나 명령 줄을 설정하거나 켜거나 끕니다.
EXIT           ISDDCMD를 종료합니다.
HELP           이 도움알을 표시합니다.
COLOR          콘솔 색을 바꿉니다.
    """


if __name__ == "__main__":
    system("title ISDD cmd")
    print(inittext)
    if not is_automation:

        while True:
            input_massage = []
            input_text = str(input(input_arrow if show_input_arrow else "")).lower().split(" ")
            for i in input_text:
                if i.startswith('$'):
                    try:
                        input_massage.append(eval(i[1:]))
                    except NameError:
                        input_massage.append(i[1:])
                    except Exception as e:
                        print(f"오류가 발생했습니다: {e}")
                else:
                    input_massage.append(i)
            command_input(input_massage)

    else:
        command_input("say byJjoon".split(" "))
