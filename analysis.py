import func as fu
import re
import matplotlib.pyplot as plt
import numpy as np

def main():
    
#    read the text; parse it into words
    text = None
    fname = '1984_small.txt'
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
        
    
    count_arr = []
    for item in fwd_list_stat:
        count_arr.append(item[0])
    
    
#    2) fill the bin_tree
    
    
    
    
    
    
#    plot histogram from fwd_list
    fig_list = plt.figure()
    ax_list = fig_list.add_subplot(111)
    ax_list.plot(range(len(count_arr)), count_arr)
    
    label = "FwdList. Top 20 most popular words:\n"
    for i in range(20):
        label += str(fwd_list_stat[i]) + '\n'
    label += '\n'
    
    limits = ax_list.axis()
    x = 0.6 * (limits[0] + limits[1])
    y = 0.2 * (limits[2] + limits[3])
    ax_list.text(x, y, label, fontsize=10)

#    plt.show()
#    plot histogram from bin_tree
    
    
    # saving plots
    fig_list.savefig("fwd_list_%r_words" % len(count_arr))

if __name__ == '__main__':
    main()


