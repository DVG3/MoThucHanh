import json

with open("dat.txt","r",encoding="utf-8") as f:
    coquan_data = dict()
    coquan = ''
    for line in f:
        if line[0] == '@':
            coquan = ' '.join(line.split(' ')[2:]).strip('\n')
            print(coquan)
            coquan_data[coquan] = []
            line = line[2:]
            print(line)
            num = line.split(' ')[0][:-1]
            ans = ' '.join(line.split(' ')[1:]).strip('\n')
            print(ans, num)
            temp = {ans:num}
            coquan_data[coquan].append(temp)
            continue
        num = line.split(' ')[0][:-1]
        ans = ' '.join(line.split(' ')[1:]).strip('\n')
        print(ans, num)
        temp = {ans:num}
        coquan_data[coquan].append(temp)

coquan_data_text = json.dumps(coquan_data)
with open("dat.json","w",encoding="utf-8") as f:
    f.write(coquan_data_text)
        
