str = input().upper()
words = list(set(str))

count_list = []
for i in words:
    cnt = str.count(i)
    count_list.append(cnt)

if count_list.count(max(count_list)) > 1:
    print('?')
else:
    max_index = count_list.index(max(count_list))
    print(words[max_index])