## Production Readiness & Compliance with GDPR Regulations

This document covers the GDPR posture of the current system, ethical AI constraints, and what a real banking integration would require before deployment at scale.

---

### 1. Current System Architecture

The API is stateless by design. The `/classify` endpoint receives an SMS message, vectorizes it using the saved vectorizer, runs it through the trained Logistic Regression model, and returns a prediction with a confidence score.   
**No message content, no prediction result, and no metadata is written to disk or retained in memory between requests**.

The system currently processes personal data only transiently for the duration of a single HTTP request.

---

### 2. GDPR Posture

#### Art. 5 — Principles Relating to Processing of Personal Data
[gdpr-info.eu/art-5-gdpr](https://gdpr-info.eu/art-5-gdpr/)

* **Data Minimisation**: Art. 5(1)(c) requires data to be "adequate, relevant and limited to what is necessary".
* **Implementation**: The API accepts only the raw SMS text and returns a classification signal. No sender metadata, timestamps, or account identifiers are collected or stored.
* **Storage Limitation**: The stateless design ensures no personal data is retained beyond the request lifecycle (Art. 5(1)(e)).

#### Art. 6 — Lawfulness of Processing
[gdpr-info.eu/art-6-gdpr](https://gdpr-info.eu/art-6-gdpr/)

In a production banking environment, the legal basis for processing this data would fall under:
* **Art. 6(1)(c)**: "Processing is necessary for compliance with a legal obligation to which the controller is subject" (e.g., Anti-Money Laundering and fraud prevention regulations).
* **Art. 6(1)(f)**: "Processing is necessary for the purposes of the legitimate interests pursued by the controller" (Swedbank) to protect customer assets from fraud.

#### Art. 22 — Automated Individual Decision-Making, including profiling
[gdpr-info.eu/art-22-gdpr](https://gdpr-info.eu/art-22-gdpr/)

* **The Right**: The data subject shall have the right not to be subject to a decision based solely on automated processing, including profiling, which produces legal effects concerning him or her or similarly significantly affects him or her.
* **Safeguard**: The current prototype is not the decision-maker; it acts as a decision-support tool for human fraud analysts or bank-side systems.
* **Exemption**: This keeps the system within exemptions at Art. 22(2)(a) ("necessary for entering into, or performance of, a contract between the data subject and a data controller") and preserves "the right to obtain human intervention on the part of the controller" at Art. 22(3).

#### Art. 25 — Data protection by design and by default
[gdpr-info.eu/art-25-gdpr](https://gdpr-info.eu/art-25-gdpr/)

* **Design**: The stateless API, API key authentication, and HTTPS transport are consistent with Art. 25's requirement for appropriate technical measures.

#### Art. 35 — Data Protection Impact Assessment (DPIA)
[gdpr-info.eu/art-35-gdpr](https://gdpr-info.eu/art-35-gdpr/)

Deployment at scale would trigger the requirement for a DPIA prior to processing, covering the nature of the data, necessity, risks to individuals, and technical mitigations.

---