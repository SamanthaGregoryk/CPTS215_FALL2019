def compute_entropy(class_probabilities):
    '''
    class_probabilities is a list of class probabilities
    '''
    terms = [-pi * np.log2(pi) for pi in class_probabilities if pi] # ignore zero probabilities
    H = np.sum(terms)
    return H

def compute_class_probabilities(instance_labels):
    '''
    instance_labels is a list of each examples' class label
    '''
    num_examples = len(instance_labels)
    counts = list(Counter(instance_labels).values())
    probabilities = np.array(counts) / num_examples
    return probabilities

def compute_subset_entropy(subset):
    '''
    subset is a list of instances as two-item tuples (attributes, label)
    '''
    labels = [label for _, label in subset]
    probabilities = compute_class_probabilities(labels)
    entropy = compute_entropy(probabilities)
    return entropy
    
def compute_partition_entropy(subsets):
    '''
    subsets is a list of class label lists
    '''
    num_examples = np.sum([len(s) for s in subsets])
    entropies = [(len(s) / num_examples) * compute_subset_entropy(s) for s in subsets]
    partition_entropy = np.sum(entropies)
    return partition_entropy

def partition_by(inputs, attribute):
    '''
    inputs is a list of tuple pairs: (attribute_dict, label)
    attribute is the proposed attribute to partition by
    returns a dictionary of attribute value: input subsets pairs
    '''
    subsets = {}
    for example in inputs:
        attribute_value = example[0][attribute]
        if attribute_value in subsets:
            subsets[attribute_value].append(example)
        else: # add this attribute_value to the dict
            subsets[attribute_value] = [example]
    return subsets

def partition_entropy_by(inputs, attribute):
    '''
    compute the partition
    compute the entropy of the partition
    '''
    subsets = partition_by(inputs, attribute)
    entropies = compute_partition_entropy(subsets.values())
    return entropies

def find_min_entropy_partition(inputs, attributes=None):
    '''
    Finds the partition with the minimum about of entropy.
    '''
    if attributes is None:
        attributes = list(inputs[0][0].keys())
    partition_entropies = []
    for attribute in attributes:
        partition_entropy = partition_entropy_by(inputs, attribute)
        print(attribute, partition_entropy)
        partition_entropies.append(partition_entropy)
    min_index = np.argmin(partition_entropies)
    return attributes[min_index]





        