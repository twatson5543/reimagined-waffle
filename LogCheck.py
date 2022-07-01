# Libraries
import os


# ========== Functions ==========
class f1:
    # //// Current File Directory
    def FileDir():
        filepath = os.path.abspath(__file__)
        return filepath
    # //// Parse through abs path to get folder path instead of filepath
    def FileDirParse(FileDir):
        flist_1 = FileDir.split('/')
        flist_2 = flist_1[1:-1]
        flist_3 = []
        for i in flist_2:
            newitem = "/" + str(i)
            flist_3.append(newitem)
        flist_4 = "".join(flist_3) + "/"
        return flist_4
    # //// List Files in Directory that are log_ files.
    def FileList(Dirpath):
        list1 = sorted(os.listdir(Dirpath))
        print(list1)
        list2 = []
        for i in list1:
            if (i.find("log_") != -1):
                list2.append(i)
        return list2
# End f1


class f2:
    # //// Get Content from file
    def GetText(filepath):
        file1 = open(filepath, 'r')
        fileLines = file1.readlines()
        file1.close()
        fileLines2 = [i.replace("\n",'') for i in fileLines]
        return fileLines2
    # //// Get all Content from all files
    def GetListText(filepath):
        list1 = []
        for i in filepath:
            FileText = f2.GetText(i)
            list1.append(FileText)
        return list1
    # //// Parse through to make new list of content
    def ListParse(oglist):
        ilist = []
        for i in oglist:
            nlist = []
            for n in i:
                list1 = n.split('/>')
                list2 = list1[:-1]
                list3 = [o.replace('<date=', '') for o in list2]
                list4 = [o.replace('<status=', '') for o in list3]
                #print(list4)
                nlist.append(list4)
            ilist.append(nlist)
        #print(ilist)
        return ilist
# End f2


class f3:
    def calcNetTime(oglist):
        FullList = []
        for i in oglist:
            DailyTrueList = []
            for n in i:
                #print(n[1])
                if n[1] == 'Network Up':
                    DailyTrueList.append(True)
                else:
                    DailyTrueList.append(False)
            #print(DailyTrueList)
            FalseCount = str(DailyTrueList.count(False))
            FullList.append(FalseCount)
        return FullList
    def DateLogList(list):
        DateList = []
        for i in list:
            i2 = i.replace("log_","")
            i3 = i2.replace(".txt","")
            DateList.append(i3)
        print(DateList)
        return DateList
    def WriteLogList(lista, listb):
        WriteList = []
        for a,b in zip(lista,listb):
            compiled_list = "<LogDate=" + b + "/><NumOfMinutesDown=" + a + "/>"
            print(compiled_list)
            WriteList.append(compiled_list)
        return WriteList
# End f3


class f4:
    def WriteToFile(list):
        file = open('InternetDailyLogs.txt','w')
        for i in list:
            file.writelines(i + '\n')
        file.close()
# End f4


# ========== Main Run ==========
# // Get Log Files
absFilepath = f1.FileDir()
absDirPath = f1.FileDirParse(absFilepath)
LogFileList = f1.FileList(absDirPath)

# // Get Contents of Log Files
FileContentList = f2.GetListText(LogFileList)
ParsedContentList = f2.ListParse(FileContentList)

# // Get daily logs of Minutes Down
MinutesOffline = f3.calcNetTime(ParsedContentList)
LogDateList = f3.DateLogList(LogFileList)
WriteList = f3.WriteLogList(MinutesOffline,LogDateList)

# // Write Final Logs to file
f4.WriteToFile(WriteList)
