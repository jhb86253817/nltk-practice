import nltk

#create a tree by adding labels and lists to nodes 
tree1 = nltk.Tree('NP', ['Alice'])
tree2 = nltk.Tree('NP', ['the', 'rabbit'])
tree3 = nltk.Tree('VP', ['chased', tree2])
tree4 = nltk.Tree('S', [tree1, tree3])
#some methods of tree
print tree4[1]
print tree4[1].node
print tree4.leaves()
print tree4.draw()

#traverse the tree 
def traverse(t):
    try:
        t.node 
    except AttributeError:
        print t,

    else:
        #now we know t.node is defined
        print '(', t.node,
        for child in t:
            traverse(child)
        print ')',
traverse(tree4)

