from py2neo import Graph,Node,Relationship

test_graph = Graph(
    "http://localhost:7474",
    username="neo4j",
    password="582460"
)
a = test_graph.run("MATCH (a:person {person_name:'杨靖宇'})-[b:manage]->(c:army {army_name:'东北人民革命军第一军'}  )   RETURN a,b,c")
print(list(a))