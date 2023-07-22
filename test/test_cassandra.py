from cassandra.cluster import Cluster

cluster = Cluster(['localhost'])
session = cluster.connect()

print(session.execute("SELECT release_version FROM system.local").one())
rows = session.execute("SELECT * FROM news.test")
for r in rows:
    for i in range(len(r)):
        print(r[i], end='\t')
    print()