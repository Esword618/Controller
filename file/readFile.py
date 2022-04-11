# -*- coding: utf-8 -*-

def GetInfo(filePath):
    start = False
    paramsList = []
    with open(filePath,"rb") as f:
        # 防止文件太大，用for迭代读取
        for i in f:
            i = i.decode().strip()
            if 'X-coord' in i:
                start = True
            if start:
                if "Number of" in i or i=='':
                    break
                paramList = i.replace("%","").split(",")
                paramList = [i.strip() for i in paramList]
                paramsList.append(paramList)
    labelList,paramsList = paramsList[0],paramsList[1:]
    InfoList = [dict(zip(labelList,paramList)) for paramList in paramsList]
    # 把一些字符数字参数转化为int类型，便于后续计算
    for i,dic in enumerate(InfoList):
        dic['X-coord'] = int(dic['X-coord'])
        dic['Y-coord'] = int(dic['Y-coord'])
        dic['wavelength'] = int(dic['wavelength'])
        InfoList[i] = dic
    return InfoList
path = './coordinates.txt'
InfoList = GetInfo(path)
# for i in InfoList:
    # print(i)

CoordinateList = [(InfoList[i]['X-coord']-InfoList[i-1]['X-coord'],InfoList[i]['Y-coord']-InfoList[i-1]['Y-coord']) for i in range(1,len(InfoList))]
for i,List in enumerate(CoordinateList):
    print(List,InfoList[i])
