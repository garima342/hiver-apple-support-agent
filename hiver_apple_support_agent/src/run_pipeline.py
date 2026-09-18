import os,pandas as pd
from sklearn.model_selection import GroupShuffleSplit
from .taxonomy import weak_intent
from .model import train_classifier,evaluate_classifier

def main():
 d=pd.read_csv('data/golden_candidates.csv');d['clean_message']=d.clean_message.fillna('').astype(str);d['intent']=d.clean_message.map(weak_intent);d=d[d.intent!='other']
 if d.intent.nunique()<2: print('Not enough classes for classifier.');return
 tr,te=next(GroupShuffleSplit(n_splits=1,test_size=.2,random_state=42).split(d,groups=d.conversation_id));train,test=d.iloc[tr],d.iloc[te]
 m=train_classifier(train);metrics,p=evaluate_classifier(m,test)
 pd.DataFrame({'metric':['accuracy','macro_f1'],'value':[metrics['accuracy'],metrics['macro_f1']]}).to_csv('results/intent_metrics.csv',index=False)
 open('results/classification_report.txt','w').write(metrics['report']);test.assign(prediction=p).to_csv('results/intent_predictions.csv',index=False)
 print(metrics['report'])
if __name__=='__main__':main()
