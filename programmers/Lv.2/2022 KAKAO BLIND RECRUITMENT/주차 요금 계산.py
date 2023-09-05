import math
def feeCal(fees, time):
    if time <= fees[0]:
        return fees[1]
    else:
        return fees[1]+ (math.ceil((time-fees[0])/fees[2])*fees[3])
    
def timeCal(info):
    totalTime = 0
    ehours, eminutes = 23, 59
    if len(info)%2 !=0:
        info.append('23:59 OUT')
    INTime, OUTTime = 0 , 0
    for i in info:
        time, state = i.split()
        hours, minutes = time.split(':')        
        totalTime += int(hours)*60 + int(minutes) if state=='OUT' else -1 * (int(hours)*60 + int(minutes))
    return totalTime
    
def solution(fees, records):        
    result = []
    answer = []
    carsInfo = {}
    for record in records:
        info, carNum, state= record.split()
        if carsInfo.get(carNum,False):
            carsInfo[carNum].append(' '.join([info,state]))
        else:
            carsInfo[carNum] = [' '.join([info,state])]
    for key, values in carsInfo.items():
        result.append([key,feeCal(fees,timeCal(values))])
    result.sort()
    for carNum,res in result:
        answer.append(res)
    return answer