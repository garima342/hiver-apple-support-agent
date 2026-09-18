import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
class Retriever:
    def __init__(self,history):
        self.history=history.reset_index(drop=True)
        self.v=TfidfVectorizer(lowercase=True,strip_accents='unicode',ngram_range=(1,2),min_df=1,sublinear_tf=True)
        self.X=self.v.fit_transform(self.history.customer_message.astype(str)) if len(self.history) else None
    def search(self,q,k=3,exclude_conversation_id=None):
        if self.X is None:return []
        scores=cosine_similarity(self.v.transform([str(q)]),self.X).ravel()
        out=[]
        for i in np.argsort(-scores):
            r=self.history.iloc[int(i)]
            if exclude_conversation_id is not None and str(r.conversation_id)==str(exclude_conversation_id):continue
            out.append({'customer_message':r.customer_message,'support_reply':r.support_reply,'conversation_id':r.conversation_id,'similarity':float(scores[i])})
            if len(out)>=k:break
        return out
