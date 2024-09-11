import isddcmd as main
from os import system

def on_help():
    return """

콘솔의 기본 전경색과 배경색을 설정합니다.

COLOR [attr]

  attr        콘솔 출력의 색 특성을 지정합니다.

색 특성은 두 자리의 16진수로 지정됩니다. 첫째 자리는
배경색에 해당하고 둘째 자리는 전경색에 해당합니다.

    0 = 검은색       8 = 회색
    1 = 파란색        9 = 연한 파란색
    2 = 녹색       A = 연한 녹색
    3 = 청록색        B = 연한 청록색
    4 = 빨간색         C = 연한 빨간색
    5 = 자주색      D = 연한 자주색
    6 = 노란색      E = 연한 노란색
    7 = 흰색       F = 밝은 흰색

인수가 지정되지 않으면 이 명령은 콘솔에 적용된 현재 지정 색을 알려줍니다.

전경색과 배경을 같게 지정하여 COLOR 명령을 실행하려고 할 경우
COLOR 명령은 ERRORLV을 1로
설정합니다.

예를 들면 "COLOR fc"는 밝은 흰색 위에 연한 빨간색을 생성합니다.
    """


def on_trigger(x__):
    if len(x__) <= 1:
        print(f"현재 콘솔 색은 {main.console_color}입니다")
    else:
        if len(str(x__[1])) <= 1:
            main.ERRORLV = 1
            print(on_help())
        elif x__[1] == 'def':
            main.console_color = main.def_color
            print(f"콘솔 색이 기본색인{main.def_color}로 설정되었습니다.")
        else:
            if str(x__[1])[0] == str(x__[1])[1]:
                main.ERRORLV = 1
                print(on_help())
            else:
                try:
                    int(str(x__[1]), 16)
                    main.console_color = str(x__[1])[:2]
                    system(f"color {main.console_color}")
                except ValueError:
                    main.ERRORLV = 1
                    print(on_help())