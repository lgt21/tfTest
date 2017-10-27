# -*- coding: utf-8 -*-
# @Time    : 2017/10/27 15:57
# @Author  : lgt
# @Site    : 
# @File    : tuitionTest.py
# @Software: PyCharm

regionIds = '''
340111	429
340121	430
340122	663317
340123	431
340103	432
340104	433
340102	434
'''

exRegionId = '520113'
exCountryId = '636'

sqls = '''
INSERT INTO `coaches`.`Coaches_tuition_chargeDetail` (`regionId`, `countyId`, `title`, `content`, `price`, `createTime`, `retakeprice`, `typeFlag`) VALUES ('520113', '636', '理论培训费', '市驾驶理科培训中心', '20', '1509088230', '0', '0');
INSERT INTO `coaches`.`Coaches_tuition_chargeDetail` (`regionId`, `countyId`, `title`, `content`, `price`, `createTime`, `retakeprice`, `typeFlag`) VALUES ('520113', '636', '考试费', '市交警支队车管所', '570', '1509088242', '0', '0');
INSERT INTO `coaches`.`Coaches_tuition_chargeDetail` (`regionId`, `countyId`, `title`, `content`, `price`, `createTime`, `retakeprice`, `typeFlag`) VALUES ('520113', '636', '体检费', '市交警支队车管所', '20', '1509088247', '0', '0');
INSERT INTO `coaches`.`Coaches_tuition_chargeDetail` (`regionId`, `countyId`, `title`, `content`, `price`, `createTime`, `retakeprice`, `typeFlag`) VALUES ('520113', '636', '驾校管理费', '市驾驶培训公司', '1700', NULL, '0', '0');
INSERT INTO `coaches`.`Coaches_tuition_chargeDetail` (`regionId`, `countyId`, `title`, `content`, `price`, `createTime`, `retakeprice`, `typeFlag`) VALUES ('520113', '636', 'IC卡费', '市驾驶理科培训中心', '80', NULL, '0', '0');
'''

regionList = regionIds.split("\n")
sqlList = sqls.replace(exRegionId, "%s").replace(exCountryId, "%s").split("\n")

for i in range(len(regionList)):
    r = regionList[i].strip()
    if(r):
        rr = r.split("	")[0]
        rc = r.split("	")[-1]
        if(rr != exRegionId):
            print("DELETE FROM Coaches_tuition_chargeDetail where regionId = '%s';" % rr)
            for j in range(len(sqlList)):
                s = sqlList[j].strip()
                if(s):
                    print(s % (rr, rc))