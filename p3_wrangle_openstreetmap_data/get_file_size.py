import os

toronto_canada_osm = '/Users/Jianyu/Desktop/OpenStreet/toronto_canada.osm'
toronto_db = '/Users/Jianyu/Desktop/OpenStreet/OpenStreetMap.db'
nodes_csv = '/Users/Jianyu/Desktop/OpenStreet/nodes.csv'
nodes_tags_csv = '/Users/Jianyu/Desktop/OpenStreet/nodes_tags.csv'
ways_csv = '/Users/Jianyu/Desktop/OpenStreet/ways.csv'
ways_nodes_csv = '/Users/Jianyu/Desktop/OpenStreet/ways_nodes.csv'
ways_tags_csv = '/Users/Jianyu/Desktop/OpenStreet/ways_tags.csv'

print 'File Sizes:'
print 'toronto_canada.osm:', os.path.getsize(toronto_canada_osm) / float(1024*1024*1024), 'GB'
print 'toronto.db:', os.path.getsize(toronto_db) / float(1024*1024), 'MB'
print 'nodes.csv:', os.path.getsize(nodes_csv) / float(1024*1024), 'MB'
print 'nodes_tags.csv:', os.path.getsize(nodes_tags_csv) / float(1024*1024), 'MB'
print 'ways.csv:', os.path.getsize(ways_csv) / float(1024*1024), 'MB'
print 'ways_nodes.csv:', os.path.getsize(ways_nodes_csv) / float(1024*1024), 'MB'
print 'ways_tags.csv:', os.path.getsize(ways_tags_csv) / float(1024*1024), 'MB'
