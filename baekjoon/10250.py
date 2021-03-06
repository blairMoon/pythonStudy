'''
ACM 호텔 매니저 지우는 손님이 도착하는 대로 빈 방을 배정하고 있다.
고객 설문조사에 따르면 손님들은 호텔 정문으로부터 걸어서 가장 짧은 거리에 있는 방을 선호한다고 한다. 
여러분은 지우를 도와 줄 프로그램을 작성하고자 한다.
즉 설문조사 결과 대로 호텔 정문으로부터 걷는 거리가 가장 짧도록 방을 배정하는 프로그램을 작성하고자 한다.

문제를 단순화하기 위해서 호텔은 직사각형 모양이라고 가정하자. 
각 층에 W 개의 방이 있는 H 층 건물이라고 가정하자 (1 ≤ H, W ≤ 99).
그리고 엘리베이터는 가장 왼쪽에 있다고 가정하자(그림 1 참고).
이런 형태의 호텔을 H × W 형태 호텔이라고 부른다. 호텔 정문은 일층 엘리베이터 바로 앞에 있는데, 
정문에서 엘리베이터까지의 거리는 무시한다.
또 모든 인접한 두 방 사이의 거리는 같은 거리(거리 1)라고 가정하고 호텔의 정면 쪽에만 방이 있다고 가정한다.
프로그램은 표준 입력에서 입력 데이터를 받는다. 
프로그램의 입력은 T 개의 테스트 데이터로 이루어져 있는데 T 는 입력의 맨 첫 줄에 주어진다.
 각 테스트 데이터는 한 행으로서 H, W, N, 세 정수를 포함하고 있으며 각각 호텔의 층 수, 각 층의 방 수, 몇 번째 손님인지를 나타낸다(1 ≤ H, W ≤ 99, 1 ≤ N ≤ H × W). 




'''
T = int(input())

for i in range(T):
    H, W, N = map(int,input().split())
    floor = N % H 
    room_number =  (N // H) + 1
    if floor == 0:
        floor = H
        room_number -= 1
    print(100 * floor + room_number )




