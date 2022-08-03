N = int(input())
name_list = []
for i in range(N):
    name_list.append(input())

set_ = set()
gomgom = 0
for name in name_list:
    if name == 'ENTER':
        set_.clear()
    else:    
        if name not in set_:
            set_.add(name)
            gomgom += 1

print(gomgom)