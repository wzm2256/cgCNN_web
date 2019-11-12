import re

file_name = 'index.html'
new_file_name = 'index_hef.html'

f = open(file_name)
f_new = open(new_file_name,'w')
for line in f:
    # if not 'src=' in line:
    #     f_new.write(line)
    #     continue
    
    m=re.search(r'src="(.*)" w', line)
    if m == None:
        f_new.write(line)
        continue
    src = m.group(1)

    m=re.split(r'<img(.*)/>', line)
    pre = m[0]
    post = m[-1]
    content = m[1]

    new_line = pre + '<a href=' + '"' + src + '">' + '<img' + content + '/>' + '</a>' + post
    f_new.write(new_line)