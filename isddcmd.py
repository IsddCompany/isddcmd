from os import system
import sys
import importlib

def_color = "0f"
console_color = def_color

if __name__ == "__main__":
    show_input_arrow = True
    default_input_arrow = "Leurc(sID1) _>"
    input_arrow = default_input_arrow

    ERRORLV = 0

inittext = """
ISDD cmd [Version 1.0.1.0]
(c) 1998` ISDD Company. All rights reserved.
"""

is_automation = len(sys.argv) > 1


#TODO: def set():
#       변수 세팅
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

def reload(outfile: list):
    global ERRORLV
    try:
        importlib.reload(importlib.import_module(outfile[1]))
    except ModuleNotFoundError:
        print(f"{outfile}을(를) 찾을수 없습니다.")
        ERRORLV = 1
    except:
        print(reload_help())
        ERRORLV = 1

def reload_help():
    return """
한번 불러온 외부파일은 다시 호출하면,
파일 내용이 바뀌어도 실행되는 내용은 바뀌지 않습니다.
이때 RELOAD를 사용하면 변경된 내용대로 ISDDCMD에 호출합니다.
(내부 명령어는 바뀌지 않습니다.)

RELOAD [OUTFILE]

  OUTFILE      외부파일의 이름을 지정합니다.

만약 OUTFILE이 외부파일이 아닐경우
RELOAD 명령은 ERRORLV을 1로 설정합니다.
    """



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

SAY [ON | OFF]
SAY [MESSAGE]
SAY INPSET [INPUT_ARROW | DEFAULT]

  ON | OFF      input_arrow가 보여지는지 여부를 정합니다.
  MESSAGE       출력할 문자열입니다.
  DEFAULT       input_arrow를 기본으로 (ISDDCMD가 실행되었을때)로 변경합니다.
  INPUT_ARROW   input_arrow를 INPUT_ARROW로 할당합니다.

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
RELOAD         외부 파일을 다시 불러옵니다.
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
