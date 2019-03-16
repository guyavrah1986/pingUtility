import ping3

def initPinger(ipAddress,
                numOfSecBetweenInterval=60,
                totalDurationInMinutes=60):
    print("initPinger - start")


    print("initPinger - end")

def runPing(ipAddress):
    ret = ping3.ping(ipAddress, timeout=1)
    if ret == "None":
        return ("ping fail")
    else:
        return ("ping success")