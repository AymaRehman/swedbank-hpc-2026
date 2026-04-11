## Production Readiness & Compliance with GDPR Regulations

This document covers the GDPR posture of the current system, ethical AI constraints, and what a real banking integration would require before deployment at scale.

---

### 1. Current System Architecture

The API is stateless by design. The `/classify` endpoint receives an SMS message, vectorizes it using the saved vectorizer, runs it through the trained Logistic Regression model, and returns a prediction with a confidence score.   
**No message content, no prediction result, and no metadata is written to disk or retained in memory between requests**.

The system currently processes personal data only transiently for the duration of a single HTTP request.

---