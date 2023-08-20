start_str = 'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, dignissim vitae libero'
spec_sim = ".,:;!_*-+()/#¤%&) "
list_start_str = list(start_str)
list_new_str = []
d = len(list_start_str)
for i in range(len(list_start_str)):
    list_new_str.append(list_start_str[i])
    if i != len(list_start_str) - 1:
        if list_start_str[i] not in spec_sim and list_start_str[i+1] in spec_sim:
            list_new_str.append('ing')
    else:
        break
new_str = ''.join(list_new_str)
print(new_str)