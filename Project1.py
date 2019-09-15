This assignment is based on a data challenge from the Michigan Data Science Team (MDST).

The Michigan Data Science Team (MDST) and the Michigan Student Symposium for Interdisciplinary Statistical Sciences (MSSISS) have partnered
with the City of Detroit to help solve one of the most pressing problems facing Detroit - blight. Blight violations are issued by the city 
to individuals who allow their properties to remain in a deteriorated condition. Every year, the city of Detroit issues millions of dollars
in fines to residents and every year, many of these fines remain unpaid. Enforcing unpaid blight fines is a costly and tedious process, so 
the city wants to know: how can we increase blight ticket compliance?

The first step in answering this question is understanding when and why a resident might fail to comply with a blight ticket. This is where
predictive modeling comes in. For this assignment, your task is to predict whether a given blight ticket will be paid on time.



import pandas as pd
import numpy as np

def blight_model():
    from sklearn.preprocessing import LabelEncoder
    from sklearn.linear_model import Ridge, HuberRegressor
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import roc_auc_score
    from sklearn.metrics import roc_curve, auc   
    from sklearn.svm import SVC
  
    train = pd.read_csv('train.csv', encoding = "ISO-8859-1")
    test = pd.read_csv('test.csv')
    
    train = train[np.isfinite(train['compliance'])]

    train.drop(['agency_name', 'inspector_name', 'violator_name', 'non_us_str_code', 'violation_description', 
                'grafitti_status', 'ticket_issued_date', 'hearing_date', 'balance_due', 'payment_date', 'payment_status',
                'collection_status', 'compliance_detail', 'payment_amount','violation_zip_code', 'country','violation_street_number',
                'violation_street_name', 'mailing_address_str_number', 'mailing_address_str_name', 
                'city', 'state', 'zip_code','disposition','violation_code'], axis=1, inplace=True)
        
    train_columns = list(train.columns.values)
    train_columns.remove('compliance')
    test = test[train_columns]
  
    if 1:
        X_train, X_test, y_train, y_test = train_test_split(train.ix[:, train.columns != 'compliance'], train['compliance'])
        ridgereg = HuberRegressor( alpha= 40.0, epsilon= 2.2).fit(X_train , y_train)
        pred = ridgereg.predict(X_test)
        fpr_lr, tpr_lr, _ = roc_curve(y_test, ridgereg.decision_function(X_test))
        roc_auc_lr = auc(fpr_lr, tpr_lr)
        #print('AUC value', roc_auc_lr)
    
    return pd.DataFrame(ridgereg.predict(test), test.ticket_id)
