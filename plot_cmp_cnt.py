import matplotlib.pyplot as plt

dict_sz = []
list_cmp_cnt = []
tree_cmp_cnt = []
with open('cmp_cnt.txt', 'r') as f:
    for line in f: 
        words = line.split()
        dict_sz.append(int(words[0]))
        list_cmp_cnt.append(int(words[1]))
        tree_cmp_cnt.append(int(words[2]))
    

fig_cmp = plt.figure()
ax_cmp_up = fig_cmp.add_subplot(211)
ax_cmp_up.plot(dict_sz, list_cmp_cnt, label='FwdList')
ax_cmp_up.plot(dict_sz, tree_cmp_cnt, label='BinTree')

ax_cmp_down = fig_cmp.add_subplot(212)
ax_cmp_down.semilogy(dict_sz, list_cmp_cnt, label='FwdList')
ax_cmp_down.semilogy(dict_sz, tree_cmp_cnt, label='BinTree')


ax_cmp_up.set_xlabel("DICT_SIZE")
ax_cmp_up.set_ylabel("# of CMP operations")
ax_cmp_down.set_xlabel("DICT_SIZE")
ax_cmp_down.set_ylabel("# of CMP operations")

ax_cmp_up.legend(loc=2)
ax_cmp_up.set_title("# of CMP (compare) operations depending on DICT_SIZE")
plt.show()
