from django.shortcuts import render
from .csv.auto_QA import *
from django.http import JsonResponse
import os
from py2neo import Graph

# Create your views here.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 项目绝对路径

def home(request):
    home1(request)
    return render(request, 'dance.html')
def home1(request):
    if request.POST.__contains__('name'):
        print(request.POST)
        str = request.POST['name']
        print(str)
        a = wenda(request, str)
        return JsonResponse(a, safe=False)
    else:
        return JsonResponse({'data': "null"}, safe=False)

def about(request):
    return render(request, 'about.html')
def index(request):
    return render(request, 'index.html')
def classes(request):
    return render(request, 'classes.html')
def contact(request):
    return render(request, 'contact.html')


def search(request):
    test_graph = Graph(
        "http://localhost:7474",
        username="neo4j",
        password="582460"
    )
    a = test_graph.run(
        "MATCH (a:person)- [b:manage] -> (c) RETURN a, b, c")
    return JsonResponse({'data': list(a)}, safe=False)



def wenda(request, search):
    # str = search.get("name")
    a = autoqa(search)
    print(a)
    return a


# 关系查询:实体1

def findRelationByEntity1(self,entity1):
    answer = self.graph.run("MATCH (n1:person {name:\""+entity1+"\"})- [rel] -> (n2) RETURN n1,rel,n2" ).data()
    return answer

# 关系查询：实体1+关系
def findOtherEntities(self, entity, relation):
    answer = self.graph.run("MATCH (n1:person {name:\"" + entity + "\"})-[rel:" + relation + "]->(n2) RETURN n1,rel,n2").data()
    return answer
# 关系查询 整个知识图谱体系
def zhishitupu(self):
    answer = self.graph.run("MATCH (n1:person)- [rel] -> (n2) RETURN n1,rel,n2 ").data()
    return answer
# 关系查询：实体2

def findRelationByEntity2(self, entity1):
    answer = self.graph.run("MATCH (n1)- [rel] -> (n2:major {name:\""+entity1+"\"}) RETURN n1,rel,n2" ).data()
    if (len(answer)==0):
        answer = self.graph.run("MATCH (n1)- [rel] -> (n2:level {name:\"" + entity1 + "\"}) RETURN n1,rel,n2").data()
        if (len(answer) == 0):
            answer = self.graph.run("MATCH (n1)- [rel] -> (n2:univer {name:\"" + entity1 + "\"}) RETURN n1,rel,n2").data()
    return answer
