def TPos(y_test, y_pred):
    '''
    Upper left of the confusion matrix. 
    The statement is true and is positive.
    '''
    return sum((y_test == 1) and (y_pred == 1))

def TNeg(y_test, y_pred):
    '''
    Bottom right of the confusion matrix. 
    The statement is true and is negative.
    '''
    return sum((y_test == 0) and (y_pred == 0))

def FPos(y_test, y_pred):
    '''
    Bottom left of the confusion matrix. 
    The statement is false and is positive.
    '''
    return sum((y_test == 0) and (y_pred == 1))

def FNeg(y_test, y_pred):
    '''
    Upper right of the confusion matrix. 
    The statement is false and is negative.
    '''
    return sum((y_test == 1) and (y_pred == 0))

def C_Matrix(y_test, y_pred):
    '''
    Assigns variables to the matrix so we can
    calcualte evaulation metrics.
    '''
    TP = TPos(y_test,y_pred)
    FN = FNeg(y_test,y_pred)
    FP = FPos(y_test,y_pred)
    TN = TNeg(y_test,y_pred)
    return TP,FN,FP,TN

def accuracy(y_test, y_predict):
    '''
    Proportion of correct classifications out of 
    all the classifications available. 
    '''
    TP, FN, FP, TN = C_Matrix(y_test, y_predict) 
    
    correct = TP + TN 
    incorrect = TP + TN + FP + FN
        
    accuracy = correct / (correct + incorrect)
    return accuracy    
    
def precision(y_test, y_predict):
    '''
    This is the postive predictive value. It is the 
    proportion of correct postives out of all 
    classifed postivies.
    '''
    TP, FN, FP, TN = C_Matrix(y_test, y_predict)
    
    precision = TP / (TP + FP)
    return precision

def recall(y_test, y_predict):
    '''
    This is the true postive rate. It is the proportion
    of correcrly classifed postives out of all postivies. 
    '''
    TP, FN, FP, TN = C_Matrix(y_test, y_predict)

    recall = TP / (TP + FN)
    return recall

def F1_score(precision, recall):
    '''
    Summarizes a classifier in a singlen number. 
    '''
    F1_score = 2(precision * recall) / (precision + recall)
    return F1_score

