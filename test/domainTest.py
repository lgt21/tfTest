# -*- coding: utf-8 -*-
# @Time    : 2017/10/25 11:56
# @Author  : lgt
# @Site    : 
# @File    : domainTest.py
# @Software: PyCharm


domains = '''
石家庄		sjz.okxueche.net
北京		bj.okxueche.net
郑州		zz.okxueche.net
洛阳		ly.okxueche.net
唐山		ts.okxueche.net
济南		jn.okxueche.net
大连		dl.okxueche.net
合肥		hf.okxueche.net
贵阳		gy.okxueche.net
无锡		gy.okxueche.net
潍坊		wf.okxueche.net
东莞		dg.okxueche.net
'''
sql = '''
INSERT INTO `coaches`.`web_domain_mapping` (
	`region`,
	`domain`,
	`regionId`
) SELECT
	'${city}',
	'${domain}',
	(
		SELECT
			regionId
		FROM
			RegionList
		WHERE
			city = '${city}'
		AND regionFlag = 1
	)
FROM
	DUAL
WHERE
	NOT EXISTS (
		SELECT
			id
		FROM
			web_domain_mapping
		WHERE
			domain = '${domain}'
	);
'''
domainList = domains.split("\n")
for i in range(len(domainList)):
    d = domainList[i]
    if d.strip():
        dc = d.split('\t')[0]
        dd = d.split('\t')[-1].split(".")[0]
        # print(sql.replace("${city}", dc).replace("${domain}", dd).replace("\n", " "))
        print("select * from web_domain_mapping where domain = '%s';" % dd)