from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score,f1_score,classification_report

def train_classifier(df):
    m=Pipeline([('tfidf',TfidfVectorizer(lowercase=True,strip_accents='unicode',ngram_range=(1,2),min_df=2,max_df=.95,sublinear_tf=True)),('clf',LinearSVC(class_weight='balanced',random_state=42))])
    m.fit(df.clean_message.astype(str),df.intent); return m
def evaluate_classifier(m,df):
    p=m.predict(df.clean_message.astype(str))
    return {'accuracy':accuracy_score(df.intent,p),'macro_f1':f1_score(df.intent,p,average='macro'),'report':classification_report(df.intent,p,zero_division=0)},p
