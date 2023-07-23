# r'': 백슬래시를 사용하는 특수 문자를 그대로 사용하고 싶을 때
# (예) 파일 경로
# f'': 문자열 포매팅
# (예) f'알고리즘 {site} 문제 {n}개 해결'
import re
a=input()
b=input()

prog=re.compile(b)
answer = re.findall(prog,a)
print(len(answer))
