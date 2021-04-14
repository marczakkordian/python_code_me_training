graph = {'dom': ['szkoła', 'bar', 'kościół'], 'szkoła': ['dom', 'szpital'],
         'szpital': ['teatr', 'szkoła', 'kino', 'bar'], 'teatr': ['szpital', 'kina'],
         'kino': ['szpital', 'teatr', 'kościół'], 'kościół': ['bar', 'kino', 'dom'],
         'bar': ['dom', 'kościół', 'szpital'], }

for item in graph:
    print('----> krawędzie z', item)
    for e in graph[item]:
        print(item, '---', e)
