# Decision log
1. AppleSupport chosen for a focused support domain.
2. Ten intents keep taxonomy compact.
3. TF-IDF + Linear SVM provides a fast learned baseline.
4. Conversation-level splitting reduces duplicate leakage.
5. TF-IDF retrieval keeps the prototype simple and reproducible.
6. Top-k evidence is safer than copying one response blindly.
7. Evaluation conversations must be excluded from retrieval.
8. Historical replies are evidence, not policy truth.
9. LLM generation is optional; deterministic fallback keeps the demo runnable.
10. Sensitive cases are escalated.
11. Low retrieval similarity is treated as uncertainty.
12. Passwords/payment credentials are never requested.
13. Suggested labels are kept separate from confirmed golden labels.
14. Reply quality uses an LLM judge plus human agreement evidence.
15. Limitations are explicitly reported.
