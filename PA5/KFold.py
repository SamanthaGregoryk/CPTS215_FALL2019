def k_fold(clf, train_index, test_index, size):
    '''
    Examples are divied into test and
    train subsets and is iterated k 
    times until all the data is satisfied. 
    '''
    k_f = KFold(2201, n_splits = size, shuffle = False)
    outcomes = []
    
    for (train_index, test_index) in k_f:
        trainX, testX = train_X.values[train_index], train_X.values[test_index]
        trainY, testY = train_y.values[train_index], train_y.values[test_index]
        
        clf.fit(trainX, trainY)
        
        pred = clf.predict(testX)
        accur = accuracy(testY, pred)
        outcomes.append(accur)
        
    mean_outcome = np.mean(outcomes)
    return mean_outcome    



