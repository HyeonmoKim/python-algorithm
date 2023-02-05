'''
제한시간 : C/C++/Java/JS/Python(1초)| 메모리 제한 : 1024MB


회사에는 N개의 회의실이 있다. 수많은 팀이 모여 토론하고 업무를 처리하기 위해서는 회의실이 필수적이다.
내부망에 아주 간단한 회의실 예약 시스템이 있지만 편의성이 매우 떨어진다. 단순히 예약된 회의의 목록만 표시되기 때문에, 방 별로 비어 있는 시간이 언제인지를 확인하기가 힘든 것이다. 당신은 이를 직접 해결해 보기로 마음 먹었다.

회의실 이용 규칙은 다음과 같다:
회의실은 9시부터 18시까지만 사용 가능하다. 모든 회의의 시간은 이 안에 완전히 포함되어야 한다.
회의는 정확히 한 회의실을 연속한 일정 시간 동안만 점유한다. 즉 각 회의는 (회의실, 시작 시각, 종료 시각)의 정보로 나타낼 수 있다.
회의의 시작과 종료 시각은 시(時, hour) 단위로만 설정 가능하다. 같은 회의실을 사용하는 회의 시간은 서로 겹칠 수 없다. 여기서 겹친다는 것은, 두 회의 모두에 포함되는 시간이 1시간 이상 존재한다는 것을 의미한다. 예를 들어, 10시-12시의 회의와 11시-13시의 회의는 겹치는데, 11시-12시의 시간이 두 회의 모두에 포함되기 때문이다.
한 회의가 끝나는 시각에, 같은 회의실에서 다른 회의가 시작하는 것은 허용된다. 이 경우 두 회의가 겹치지 않기 때문이다.
길이가 0인 회의, 즉 시작 시각과 종료 시각이 동일한 회의는 예약된 바 없으며, 새롭게 잡을 수도 없다.
이미 예약된 M개의 회의에 대한 정보가 주어지면, 회의실별로 비어 있는 시간대를 정리해 출력하는 프로그램을 작성해 보자. 구체적인 형식은 아래의 을 참고하시오.


제약조건
1≤N≤50
1≤M≤100
회의실의 이름은 영문 알파벳 소문자로만 이루어져 있으며 길이는 1 이상 10 이하이다.
주어지는 모든 시각은 9 이상 18 이하이다.
회의의 시작 시각은 회의의 종료 시각을 1시간 이상 앞선다.


부분문제
(30점) N=1
(70점) 다른 제약 조건이 없다.


입력형식
첫째 줄에 회의실의 수와 예약된 회의의 수를 나타내는 정수 N과 M이 공백을 사이에 두고 주어진다.
이어 N개의 줄에는 각 회의실의 이름이 주어진다.
이어 M개의 줄에는 각 회의가 배정된 회의실의 이름 r과 시작 시각 s, 그리고 종료 시각 t가 공백을 사이에 두고 주어진다.


출력형식
각 회의실에 대한 정보를 회의실 이름의 오름차순으로 출력한다. 각 회의실에 대한 정보는 다음과 같다.

첫째 줄에는 { Room 회의실이름: } (중괄호 제외)을 출력한다.

둘째 줄에는 예약가능 시간을 출력한다.
예약 가능한 시간대의 개수를 n이라고 할 때, { n available: } (중괄호 제외)을 출력하고, 뒤따른 n개의 줄에 예약 가능한 시간대를 { 09-18 } (하이픈 한개, 중괄호 제외)형태로 출력해야 한다. 한 자리 수의 경우 앞에 0을 붙여 두 자리 수로 만들어야 함에 유의하라.
예약 가능한 시간이 없다면, Not available을 출력한다.

각 회의실에 대한 정보 사이에는 ----- (하이픈 다섯 개)로 구분선이 출력되어야 한다.

'''

import sys

n, m = list(map(int,input().split()))

rooms_lst=[]
rooms={}
reservations=[]

def algorithm(rooms, reservations):
    for room, st, end in reservations :
        for i in range(st,end):
            rooms[room].remove(i)
    rooms_lst.sort()
    for i in rooms_lst:
        print('Room '+ i+':')
        rooms[i]=list(rooms[i])
        available=[]
        st=rooms[i][0]
        end=st+1
        for j in range(len(rooms[i])) :
            if st==18 :
                break
            elif st<end and end==18 :
                pass
            elif (rooms[i][j+1])%18 - rooms[i][j] == 1:
                end += 1
                continue

            if st == 9 :
                st = '0'+str(st)
            else :
                st=str(st)
            available.append([st, str(end)])
            if j<len(rooms[i]):
                st = rooms[i][j + 1]
                end = st+1

        if len(available)==0 :
            print('Not available')
        else :
            print(len(available), 'available:')
            for a,b in available :
                print(a+'-'+b)

        if rooms_lst.index(i)+1 != len(rooms_lst) :
            print('-----')

for _ in range(n) :
    room=input()
    rooms_lst.append(room)
    rooms[room]={9,10,11,12,13,14,15,16,17,18}

for _ in range(m) :
    a,b,c = input().split()
    reservations.append([a,int(b),int(c)])

algorithm(rooms, reservations)
