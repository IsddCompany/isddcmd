import os
import json
import urllib.request as requesturl

#아직 사용 안하므

def on_help():
    return """
현재 버전을 표시하거나 최신버전과 비교합니다.
VERSION(또는 VER) [-ch | -cmd]
    
    인수없음        ISDDCMD의 버전을 확인합니다.
    -ch            ISDDCMD의 릴리즈된 최신버전과 비교합니다.
    -cmd           cmd의 버전을 표시합니다.
    """


## def on_trigger(_input: list):
#    if '-cmd' in _input:
#        os.system('VER')
#    if '-ch' in _input:
#        a = requesturl('https://raw.githubusercontent.com/IsddCompany/isdddatas/isddcmd/isddcmd.json')

def on_trigger(input:list):
    return