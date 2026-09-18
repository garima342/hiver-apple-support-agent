import pandas as pd,os
from sklearn.metrics import accuracy_score,f1_score,classification_report
p='data/golden_eval_set.csv'
if not os.path.exists(p):print('Run python -m src.prepare_golden first')
else:
 d=pd.read_csv(p);x=d[d.golden_intent.fillna('').str.len()>0]
 if len(x):
  print(classification_report(x.golden_intent,x.suggested_intent,zero_division=0));print('accuracy=',accuracy_score(x.golden_intent,x.suggested_intent));print('macro_f1=',f1_score(x.golden_intent,x.suggested_intent,average='macro'))
 else:print('No confirmed golden labels yet. Review suggested_intent and fill golden_intent.')
