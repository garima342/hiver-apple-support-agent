# Apple Support AI Agent — Report
## Framing
A narrow AppleSupport agent handles intent classification, historical-response retrieval, grounded drafting, and escalation.
## Baselines
Majority intent is the trivial baseline. TF-IDF + Linear SVM is the simple learned baseline. For replies, compare a generic template and top-1 retrieved historical reply against the proposed retrieval+LLM system.
## Escalation
Escalate sensitive financial/security/legal/complaint language, low retrieval similarity, or low intent confidence. Return the reason with the decision.
## Evaluation
Use 150–250 human-confirmed examples. Report intent accuracy/macro-F1, escalation precision/recall/F1, reply-quality scores from an LLM judge, and judge-human agreement on the same human-rated subset.
## Failure analysis
1. Short ambiguous tweets: weak lexical evidence.
2. Multi-intent tweets: one-label taxonomy loses secondary issues.
3. Historical replies may be incomplete or ask for DM rather than solve the issue.
4. Rare intents have fewer examples.
5. Social-media noise (URLs, mentions, emojis) hurts lexical similarity.
## What is misleading about my headline number?
A single score can overstate performance because the sample is historical and domain-specific, tweets are noisy, weak labels are used during prototyping, and retrieval can leak if evaluation conversations are not excluded. LLM-judge scores are also not a replacement for human review.
## Next week
Calibrated confidence, semantic retrieval, multi-intent classification, more reviewed labels, explicit policy versioning, and monitoring/drift checks.
