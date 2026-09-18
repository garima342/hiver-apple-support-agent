# Apple Support Agent

A small support-agent prototype built for the Hiver SDE Intern take-home assignment.

The idea was to keep the system fairly simple and make each part easy to inspect:

1. classify the customer's issue
2. find similar historical Apple Support conversations
3. draft a response using those examples
4. decide whether the request can be handled automatically or should go to a human

The project uses AppleSupport conversations from the Customer Support on Twitter dataset.

---

## Approach

### Intent classification

I defined a small set of intents based on the types of issues appearing in the AppleSupport conversations:

- battery_issue
- software_update
- app_issue
- account_access
- connectivity
- device_hardware
- storage_performance
- purchase_billing
- feature_how_to
- other

For the initial classifier experiment, I used transparent keyword-based weak labels.

I then compared:

- majority-class baseline
- TF-IDF + Logistic Regression
- TF-IDF + Linear SVM

The classifier is deliberately simple. The goal was to have a baseline that is fast to train, easy to reproduce and easy to debug.

---

## Retrieval

For response grounding, I extracted Customer → Support pairs from the historical conversations.

Given a new customer message, the system:

1. converts the message into TF-IDF features
2. finds the most similar historical customer messages
3. uses their previous support responses as context

This makes it possible to see which historical examples influenced a draft rather than generating a response without any reference to the dataset.

---

## Response generation

When an LLM API key is available, the retrieved examples are passed to the model with instructions to stay within the information present in those examples.

The prompt specifically tells the model not to:

- invent policies
- invent refunds
- invent links
- claim access to a customer's account
- make unsupported guarantees

If an LLM is not available, the project still runs using the top retrieved historical response as a fallback.

---

## Escalation

The prototype does not automatically handle every request.

It escalates when:

- the message looks related to security, fraud, privacy, payment disputes or legal issues
- classifier confidence is low
- there is not a sufficiently similar historical example

Otherwise, it drafts a response for automatic handling.

The escalation rules are intentionally simple and are documented in the code.

---

## Evaluation

The evaluation setup contains:

### Intent metrics

- Accuracy
- Macro F1
- Classification report
- Confusion matrix

### Escalation metrics

- Precision
- Recall
- F1

### Response evaluation

The project also includes an LLM-as-judge setup that scores:

- correctness
- groundedness
- helpfulness
- safety
- overall quality

A small human-reviewed subset can also be compared with the LLM judge to measure agreement.

---

## Golden evaluation set

The repository contains a 200-example evaluation set.

The examples were sampled from the AppleSupport customer messages to cover different types of support requests.

The important distinction is that the final golden labels should be human-reviewed before being used as the final headline evaluation number. The initial classifier labels are weak labels and are not treated as ground truth.

---

## Results

On the initial weak-label experiment, the prototype achieved approximately:

- Accuracy: 0.82
- Macro F1: 0.55

These numbers are useful for comparing the baseline models, but they should not be interpreted as real-world accuracy.

The main reason is that the labels used for this experiment were generated using simple lexical rules rather than independently hand-labelled examples.

The golden set is kept separate for this reason.

---

## Running the project

### 1. Install dependencies
```bash
pip install -r requirements.txt

2. Add the conversation data
Place the AppleSupport conversation file here:
data/applesupport_conversations.csv

3. Run the basic pipeline
python run.py

4. Run evaluation
python evaluate.py
