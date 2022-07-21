# 문제 source : 같은 숫자는 싫어
# https://school.programmers.co.kr/learn/courses/30/lessons/12906?language=python3

def solution(arr):
    stack = [arr[0]]
    for num in arr[1:]:
        if stack[-1] != num:
            stack.append(num)
    return stack
