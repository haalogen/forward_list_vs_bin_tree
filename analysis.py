import func as fu
import re
import matplotlib.pyplot as plt
import numpy as np

def main():
#    -George_Orwell
#    read the text; parse it into words
    text = None
    fname = '1984-George_Orwell.txt'
    with open(fname, 'r') as f:
        text = f.read().lower()
    
#    replaces anything that is not a lowercase letter, space or 
#    apostrophe with a space
    text = re.sub('[^a-z]+', " ", text)
    words = text.split()
    
#    1) fill the fwd_list
    fwd_list = fu.FwdList()
    
    for word in words:
        fwd_list.add(word)
    
    
    fwd_list_stat = []
    current = fwd_list.head
    while current != None:
        fwd_list_stat.append([current.getCount(), current.getData()])
        current = current.getNext()
    
    
    fwd_list_stat.sort(reverse=True)
        
    
    count_arr_fwd = []
    for item in fwd_list_stat:
         count_arr_fwd.append(item[0])
    
    
#    2) fill the bin_tree
    bin_tree = fu.BinarySearchTree()
    
    for word in words:
        bin_tree.put(word)
    
    bin_tree_stat = bin_tree.get_all_nodes()
    
    bin_tree_stat.sort(reverse=True)
    
    count_arr_tree = []
    for item in bin_tree_stat:
        count_arr_tree.append(item[0])
    
    equal = (bin_tree_stat == fwd_list_stat)
    print "Fwd_list and Bin_tree are equivalent:", equal
    
    
    
    
    
#    plot histogram from fwd_list
    fig_list = plt.figure()
    ax_list = fig_list.add_subplot(111)
    ax_list.plot(range(len(count_arr_fwd)),  count_arr_fwd)
    
    label = "FwdList. Top 20 most popular words:\n"
    for i in range(20):
        label += str(fwd_list_stat[i]) + '\n'
    label += '\n'
    
    limits = ax_list.axis()
    x = 0.6 * (limits[0] + limits[1])
    y = 0.2 * (limits[2] + limits[3])
    ax_list.text(x, y, label, fontsize=10)


#    plot histogram from bin_tree
    fig_tree = plt.figure()
    ax_tree = fig_tree.add_subplot(111)
    ax_tree.plot(range(len(count_arr_tree)), count_arr_tree, color='r')
    
    label2 = "BinTree. Top 20 most popular words:\n"
    for i in range(20):
        label2 += str(bin_tree_stat[i]) + '\n'
    label2 += '\n'
    
    limits = ax_tree.axis()
    x = 0.6 * (limits[0] + limits[1])
    y = 0.2 * (limits[2] + limits[3])
    ax_tree.text(x, y, label2, fontsize=10)
    
    # saving plots
    fig_list.savefig("fwd_list_%r_words" % len(count_arr_fwd))
    fig_tree.savefig("bin_tree_%r_words" % len(count_arr_tree))
    
if __name__ == '__main__':
    main()


