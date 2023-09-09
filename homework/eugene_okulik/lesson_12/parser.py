with open('av.txt') as av_file:
    data = av_file.read()


lines = data.splitlines()
print(lines)

features = {}
new_category = True
current_categ = None
for line in lines:
    if not line:
        new_category = True
        current_categ = None
        continue
    if new_category:
        features[line] = []
        current_categ = line
        new_category = False
    else:
        features[current_categ].append(line)

print(features['Подушки'])
