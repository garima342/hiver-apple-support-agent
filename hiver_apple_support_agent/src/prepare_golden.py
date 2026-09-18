import pandas as pd
from .taxonomy import weak_intent
from .agent import escalate
def main():
    d=pd.read_csv('data/golden_candidates.csv').head(200).copy()
    d['suggested_intent']=d.clean_message.map(weak_intent)
    d['suggested_escalation']=d.clean_message.map(lambda x:'yes' if escalate(x,.0)[0] else 'no')
    for c in ['golden_intent','golden_escalation','escalation_reason','human_notes']:d[c]=''
    d.to_csv('data/golden_eval_set.csv',index=False)
    return d
if __name__=='__main__':main()
