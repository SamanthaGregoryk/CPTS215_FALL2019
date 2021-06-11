class Tree():
    tree = {}

    def decision_tree(self, inputs, attrb):
        '''
        Method that builds a tree using object oriented programming. 
        '''
        self.tree = build_tree(inputs, attrb, split_candidates = None)
        
def build_tree(inputs, attrb, split_candidates = None):
    '''
    implements the ID3 algorithm to build a decision tree
    '''
    if split_candidates is None:
        # this is the first pass
        split_candidates = list(inputs[0][0].keys())
        
    num_examples = len(inputs)
    # count Trues and Falses in the examples
    num_trues = len([label for attributes, label in inputs if label == True])
    num_falses = num_examples - num_trues
    
    # part (1) in the ID3 algorithm -> all same class label
    if num_trues == 0: # no trues, this is a False leaf node
        return False
    if num_falses == 0: # no falses, this is a True leaf node
        return True
    
    # part (2) in the ID3 algorithm -> list of attributes is empty -> leaf node with majority class label
    if not split_candidates: 
        return num_trues >= num_falses
    
    # part (3) in ID3 algorithm -> split on best attribute
    split_attribute = find_min_entropy_partition(inputs, split_candidates)
    partitions = partition_by(inputs, split_attribute)
    new_split_candidates = split_candidates[:]
    new_split_candidates.remove(split_attribute)
    
    # recursively build the subtrees
    subtrees = {}
    for attribute_value, subset in partitions.items():
        subtrees[attribute_value] = build_tree(subset, new_split_candidates)
        
    # missing (or unexpected) attribute value
    subtrees[None] = num_trues > num_falses
    
    return (split_attribute, subtrees)
