st = input().upper()
word_lst = list(set(st))
cnt_lst = [st.count(w) for w in word_lst]
mx_cnt = max(cnt_lst)
if cnt_lst.count(mx_cnt) > 1:
    print('?')
else:
    print(word_lst[cnt_lst.index(mx_cnt)])