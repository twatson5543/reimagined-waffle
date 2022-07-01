# Libraries
import os
import time
from datetime import datetime

# ======== Functions ========

class Tm:
    # //// Get Current Time
    def GetCurTime():
        now = datetime.now()
        current_time = now.strftime("%Y%m%d%H%M%S")
        return current_time
    # //// Parse Time to just last 2 digits (seconds)
    def ParseTime(time):
        timsplit = list(str(time))
        timemerge = "".join(timsplit[-2:])
        return timemerge
    # //// Check if Time is at '00'
    def ChkTime(curtime):
        if curtime == "00":
            return True
        else:
            return False



# //// Ping Command for Websites
def pingCom(site):
    output = os.system("timeout 2 ping -c 1 " + site)
    if output == 0:
        return True
    else:
        return False


# //// Sites being pinged
def PingSites(Ready):
    if Ready == True:
        # // Add Sites Here
        Site1 = pingCom("www.google.com")
        Site2 = pingCom("www.facebook.com")
        # // Add Any new sites to list
        SiteStatuses = [Site1, Site2]
        return SiteStatuses


# //// Create a list of False values, based on Length of original list.
def SiteLengthCreate(SiteList):
    Blanklist = []
    for i in SiteList:
        Blanklist.append(False)
    return Blanklist


# //// Parse through and get date for filename
def FileNameParse(date):
    Split = list(str(date))
    Cut = Split[:-6]
    Merged = "".join(Cut)
    FileName = "log_" + Merged + ".txt"
    return FileName


# //// Write and append to file
def FileWrite(filename, log):
    file = open(filename, "a")
    file.write(log)
    file.write('\n')
    file.close()


# //// If time is ready, print out the Status of the network to log.txt
def SitePrint(ready, SiteStatusList, CurTime):
    if ready == True:
        CompareList = SiteLengthCreate(SiteStatusList)
        FileName = FileNameParse(CurTime)
        if CompareList == SiteStatusList:
            log = "<date=" + str(CurTime) + "/>" + "<status=" + "Network Down" + "/>"
            FileWrite(FileName, log)
            print(log)
        else:
            log = "<date=" + str(CurTime) + "/>" + "<status=" + "Network Up" + "/>"
            FileWrite(FileName, log)
            print(log)



# ======== Main ========

def loop1():
    while True:
        FullTime = Tm.GetCurTime()
        CurrentTime = Tm.ParseTime(FullTime)
        Ready2Run = Tm.ChkTime(CurrentTime)
        SiteStatus = PingSites(Ready2Run)
        SitePrint(Ready2Run, SiteStatus, FullTime)

        if Ready2Run == True:
            time.sleep(1.5)
        time.sleep(0.03)


loop1()