import re,pandas as pd
def extract_pairs(conversation):
    if pd.isna(conversation): return []
    pat=re.compile(r"Customer:\s*(.*?)\s*Support:\s*(.*?)(?=Customer:|$)",re.S|re.I)
    return [(a.strip(),b.strip()) for a,b in pat.findall(str(conversation)) if a.strip() and b.strip()]
def build_history(df):
    rows=[]
    for _,r in df.iterrows():
        for c,s in extract_pairs(r.get('conversation','')):
            rows.append({'conversation_id':r.get('conversation_id'),'customer_message':c,'support_reply':s})
    return pd.DataFrame(rows)
