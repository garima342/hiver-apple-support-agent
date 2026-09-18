# Apple Support AI Agent 

## Pipeline
Intent classification → historical retrieval → grounded reply drafting → escalation.

## Quick run
```bash
pip install -r requirements.txt
python run.py
```
Optional LLM:
```bash
export OPENAI_API_KEY=YOUR_KEY
export OPENAI_MODEL=gpt-4o-mini
python run.py
```

## Historical corpus
Put the AppleSupport conversation file at `data/applesupport_conversations.csv` with `conversation_id`, `company`, and `conversation`. Build pairs:
```python
from src.data_prep import build_history
import pandas as pd
df=pd.read_csv('data/applesupport_conversations.csv')
h=build_history(df[df.company.eq('AppleSupport')])
h.to_csv('data/apple_history_pairs.csv',index=False)
```
The retriever uses TF-IDF cosine similarity and supports excluding the evaluation conversation ID.

## Golden set
`data/golden_candidates.csv` contains 500 sampled messages. `src/prepare_golden.py` creates 200 examples with machine **suggestions**. The assignment requires hand-labelled data, so final labels must be reviewed/confirmed by a human before claiming the set is hand-labelled.

## Evaluation
Report majority baseline, TF-IDF+LinearSVC baseline, generic reply baseline, top-1 retrieval baseline, and retrieval+LLM agent. For replies use an LLM judge plus human ratings on the same small subset and report agreement. Exclude all golden conversation IDs from training/retrieval in the final evaluation.
