# -*- coding: utf-8 -*- 
import requests

import csv
from stanfordcorenlp import StanfordCoreNLP

final =""
def autoqa(seq):
    global final

    nlp_ch = StanfordCoreNLP(r'C:\Users\dell\Documents\stanford-corenlp-4.1.0', lang='zh')
    def search(url):
        global final
        response=requests.get(url)
        anse=response.json()
        if(anse['data']=={}):
            ans=0
        else :
            ans=1
            for li in anse['data']['avp']:
                final += li[0]+":"+li[1]+"\n"
        return ans
    final=""
    arm=[]
    a_p_arm=[]
    a_s_arm=[]
    p_arm=[]
    per=[]
    p_ran=[]
    pre_arm=[]
    ran=[]
    s_arm=[]
    with open(r'D:\PythonProject\gc2020002\KnowledgeGraph\csv\army.csv',encoding="utf-8") as f:
        army= csv.reader(f)
        next(army)
        for row in army:
            arm.append(row)

    with open(r"D:\PythonProject\gc2020002\KnowledgeGraph\csv\army_pre_army.csv",encoding="utf-8") as f:
        army_pre_army = csv.reader(f)
        next(army_pre_army)
        for row in army_pre_army:
            a_p_arm.append(row)
    with open(r"D:\PythonProject\gc2020002\KnowledgeGraph\csv\army_sub_army.csv",encoding="utf-8") as f:
        army_sub_army = csv.reader(f)
        next(army_sub_army)
        for row in army_sub_army:
            a_s_arm.append(row)
    with open(r"D:\PythonProject\gc2020002\KnowledgeGraph\csv\person_army.csv",encoding="utf-8") as f:
        person_army = csv.reader(f)
        next(person_army)
        for row in person_army:
            p_arm.append(row)
    with open(r"D:\PythonProject\gc2020002\KnowledgeGraph\csv\person.csv",encoding="utf-8") as f:
        person = csv.reader(f)
        next(person)
        for row in person:
            per.append(row)
    with open(r"D:\PythonProject\gc2020002\KnowledgeGraph\csv\person_rank.csv",encoding="utf-8") as f:
        person_rank = csv.reader(f)
        next(person_rank)
        for row in person_rank:
            p_ran.append(row)
    with open(r"D:\PythonProject\gc2020002\KnowledgeGraph\csv\pre_army.csv",encoding="utf-8") as f:
        pre_army = csv.reader(f)
        next(pre_army)
        for row in pre_army:
            pre_arm.append(row)
    with open(r"D:\PythonProject\gc2020002\KnowledgeGraph\csv\rank.csv",encoding="utf-8") as f:
        rank = csv.reader(f)
        next(rank)
        for row in rank:
            ran.append(row)
    with open(r"D:\PythonProject\gc2020002\KnowledgeGraph\csv\sub_army.csv",encoding="utf-8") as f:
        sub_army = csv.reader(f)
        next(sub_army)
        for row in sub_army:
            s_arm.append(row)
    s1=""
    s2=0

    shiti1=0#0找不到1人名2队伍名
    shiti2=0#0不知道问啥1人在哪个部队2职务3曾用名
    shiti2=['所属','属于','率领','所在','统帅','加入']
    shiti3=['职位','职务','军衔','官职']
    shiti4=['过去','从前','之前','以前','曾用名','前身']
    shiti5=['下属','管辖']
    for row in arm:
        if row[1] in seq:
            s1=row[1]
            s2=row[0]
            shiti1=2
    for row in per:
        if row[1] in seq:
            s1=row[1]
            s2=row[0]
            shiti1=1

    for shiti in shiti2 :
        if shiti in seq:
            shiti2=1
    for shiti in shiti3 :
        if shiti in seq:
            shiti2=2
    for shiti in shiti4 :
        if shiti in seq:
            shiti2=3
    for shiti in shiti5 :
        if shiti in seq:
            shiti2=4
    ans=0

    if(shiti1==1 and shiti2==1):
        ans=1
        a_num=0
        for row in p_arm:
            if(row[1]==s2):
                a_num=row[1]
        if(a_num==0):
            ans=0
        else:
            last_a=""
            for row in arm:
                if(a_num==row[0]):
                    last_a=row[1]
        if(last_a==""):
            ans=0
        else:
            final=s1+"所在的部队名字是"+last_a
    if(shiti1==1 and shiti2==2):
        ans=1
        a_num=0
        for row in p_ran:
            if(row[1]==s2):
                a_num=row[1]
        if(a_num==0):
            ans=0
        else:
            last_a=""
            for row in ran:
                if(a_num==row[0]):
                    last_a=row[1]
        if(last_a==""):
            ans=0
        else:
            final+=s1+"的军衔是"+last_a
    if(shiti1==2 and shiti2==3):
        ans=1
        a_num=0
        for row in a_p_arm:
            if(row[1]==s2):
                a_num=row[1]
        if(a_num==0):
            ans=0
        else:
            last_a=""
            for row in pre_arm:
                if(a_num==row[0]):
                    last_a=row[1]

        if(last_a==""):
            ans=0
        else:
            final+=s1+"的前身是"+last_a
    if(shiti1==2 and shiti2==4):
        ans=1
        a_num=[]
        for row in a_s_arm:
            if(row[0]==s2):
                a_num.append(row[1])
        if(a_num==[]):
            ans=0
        else:
            last_a=[]
            for row in arm:
                if(row[0] in a_num):
                    last_a.append(row[1])

        if(last_a==""):
            ans=0
        else:
            final=s1+"的下属部队有"
            for li in last_a:
                final+=li+" "
            final+="\n"
    if(ans==0):
        url="https://api.ownthink.com/kg/knowledge?entity="+seq
        ans=search(url)
    if(ans==0):

        nr=0
        tem=""

        res=nlp_ch.pos_tag(seq)
        for li in res:
            if( li[1]=="PRP"):
                url="https://api.ownthink.com/kg/knowledge?entity="+li[1]

                tem=""
                nr=0
                ans=search(url)
            elif( li[1]=="NR" or li[1]=="NN"):
                tem=tem+li[0]
                nr=1
            else:
                if(nr==1):
                    url="https://api.ownthink.com/kg/knowledge?entity="+tem

                    ans=search(url)
                    tem=""
                    nr=0
        if(nr==1):
            url="https://api.ownthink.com/kg/knowledge?entity="+tem

            ans=search(url)



    if(ans==0):

        final="抱歉，暂时无法回答您的提问"
    return final
