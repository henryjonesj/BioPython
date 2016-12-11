from STree import STree  #you can change this line according to your Own Suffix Tree
import time
import sys
import itertools as iterator

def st_traverse(seq):
    st = STree(seq)
    DFS(st.root,st)


def DFS(node,st):
    for e,suffix in node.transition_links:
        edgelabel = st.edgeLabel(e, e.parent)
        if not e.is_leaf():
            print "%s" %edgelabel
        else:
            print "%s (%s)" %(edgelabel,e.idx)
        DFS(e, st)
    return

def traverse(node):
    if(node.is_leaf()):
        print node.idx


def is_right_index(first_index, second_index,min,max):
    return second_index>= (first_index+min) and second_index<= (first_index+max)


def st_search(st, pttn):

    START_KEY, (min_fill_in, max_fill_in, KEY1), (minfi, maxfi, KEY2) = pttn;

    START_KEY_Index_List,  KEY1_Index_List,  KEY2_Index_List = st.find_all(START_KEY), st.find_all(KEY1),st.find_all(KEY2)

    Cumulative_Index_List = filter(lambda (stk, k1, k2): is_right_index(stk,k1, 2 * min_fill_in,max_fill_in) and
                                                         is_right_index(k1, k2, min_fill_in + minfi, min_fill_in + maxfi),
                                                         iterator.product(START_KEY_Index_List, KEY1_Index_List, KEY2_Index_List))

    rlt = map(lambda (stk, k1, k2): (stk, st.word[k1: (k2 + min_fill_in)]), Cumulative_Index_List)

    return rlt


def Grading():
    if len(sys.argv)!=2:
        shortseq = "banana";
    else:
        shortseq = sys.argv[1];
    """
        Grading Task one
    """
    st_traverse(shortseq);


    """
        read gene from the file into memory
        build the suffix tree
        specific search pattern
    """
    with open("sequence.fasta.txt",'r') as f:
        print("gene name:%s"%f.readline())
        gene = f.read().replace('\n','');
    
    st = STree(gene)  #change this line according to your suffix tree
    spttn = ["AGGAGG",(3,7,"ATG"),(30,300,"TAG")]
    
    
    """
        Grading Task Two: Suffix Tree Method
    """
    start = time.time()
    for i in range(10000):
        L1 = st_search(st,spttn)
    t = (time.time()-start)/10000.0
    print("Suffix Tree Method found %d results with %f seconds:"%(len(L1), t))
    for i,s in L1:
        print("\t%d %s"%(i,s))



if __name__== "__main__":
    Grading()


