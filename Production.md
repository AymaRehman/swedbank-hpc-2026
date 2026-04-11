## Production Readiness & Compliance with GDPR Regulations

This document covers the GDPR posture of the current system, ethical AI constraints, and the mandatory EU AI Act requirements for a real banking integration before deployment at scale.
---

### 1. Current System Architecture

The API is stateless by design. The `/classify` endpoint receives an SMS message, vectorizes it using the saved vectorizer, runs it through the trained Logistic Regression model, and returns a prediction with a confidence score.   
**No message content, no prediction result, and no metadata is written to disk or retained in memory between requests**.

The system currently processes personal data only transiently for the duration of a single HTTP request.

---

### 2. GDPR Posture

As of 2026, the system must comply with [**General Data Protection Regulation**](https://gdpr-info.eu).

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

#### Art. 15 — Right of access by the data subject
[gdpr-info.eu/art-15-gdpr](https://gdpr-info.eu/art-15-gdpr/)
Under Art. 15(1)(h), customers have the right to request "meaningful information about the logic involved" in any automated system. 
The prototype makes use of **Logistic Regression** allowing for extraction of feature importance (TF-IDF weights), therefore making it possible to explicitly show which specific terms contributed to a "Spam" classification, satisfying the requirement for explainability.


#### Art. 22 — Automated Individual Decision-Making, including profiling
[gdpr-info.eu/art-22-gdpr](https://gdpr-info.eu/art-22-gdpr/)

* **The Right**: The data subject shall have the right not to be subject to a decision based solely on automated processing, including profiling, which produces legal effects concerning him or her or similarly significantly affects him or her.
* **Safeguard**: The current prototype is not the decision-maker; it acts as a decision-support tool for human fraud analysts or bank-side systems.
* **Exemption**: This keeps the system within exemptions at Art. 22(2)(a) ("necessary for entering into, or performance of, a contract between the data subject and a data controller") and preserves "the right to obtain human intervention on the part of the controller" at Art. 22(3).

#### Art. 25 — Data protection by design and by default
[gdpr-info.eu/art-25-gdpr](https://gdpr-info.eu/art-25-gdpr/)

* **Design**: The stateless API, API key authentication, and HTTPS transport are consistent with Art. 25's requirement for appropriate technical measures.

#### Art. 26 — Joint controllers
[gdpr-info.eu/art-26-gdpr](https://gdpr-info.eu/art-26-gdpr/)
* **Controllership**: Per Art. 26, the collaboration between **RTU** and **Swedbank** requires a clear definition of who determines the purposes and means of processing during the training and deployment phases.

#### Art. 33 — Notification of a personal data breach to the supervisory authority
[gdpr-info.eu/art-33-gdpr](https://gdpr-info.eu/art-33-gdpr/)

While the API is stateless, any interception of the data in transit (the request stream) would constitute a personal data breach. Production deployment requires a documented procedure to notify the **Datu valsts inspekcija (DVI)** within 72 hours of discovery.

#### Art. 35 — Data Protection Impact Assessment (DPIA)
[gdpr-info.eu/art-35-gdpr](https://gdpr-info.eu/art-35-gdpr/)

Deployment at scale would trigger the requirement for a DPIA prior to processing, covering the nature of the data, necessity, risks to individuals, and technical mitigations.

---

### 3. EU AI Act Compliance

As of 2026, the system must comply with [**Regulation (EU) 2024/1689 (The EU AI Act)**](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689).

#### High-Risk Classification
Systems used in banking to evaluate behavior or prevent fraud are often treated as **High-Risk** if they impact a user's access to financial services.

#### Fundamental Rights Impact Assessment (FRIA)
Per **Art. 27** of the AI Act, as a financial institution, Swedbank must perform a **FRIA** before deploying this system. This assessment evaluates:
* The potential for biased outcomes against specific demographic groups.
* The impact on the "Right to Non-Discrimination" and "Consumer Protection."

#### Technical Requirements
* **Art. 13 (Transparency and provision of information to deployers)**   
We must provide instructions for use to the bank's fraud analysts.
* **Art. 14 (Human oversight)**   
The interface must allow analysts to disregard or override the AI's output.
* **Art. 15 (Accuracy, robustness and cybersecurity)**   
The model must be tested against adversarial attacks.

---

### 4. Ethical AI Constraints

* **Human-in-the-loop**: The model must function as a decision-support tool. High-confidence spam flags should route to analyst queues, while borderline cases must involve manual review before action.
* **Bias and Fairness**: The current training dataset is English-dominant. In production, performance must be monitored by language (e.g., Latvian vs. English) and demographic segments to ensure no disparate impact.
* **Explainability**: Logistic Regression provides interpretable coefficients. Influential TF-IDF token weights can be surfaced to analysts to justify why a specific message was flagged.
* **Right to Contestation**: Consistent with Art. 22(3), customers must have a clear route to contest a fraud flag with a human representative.

---

### 5. What Real Banking Integration Would Require

| Requirement | Current State | Production Requirement |
| :--- | :--- | :--- |
| **Message Transport** | HTTPS (REST) | Internal VPC / private network, end-to-end encrypted |
| **DPIA & FRIA** | Not applicable (prototype) | Mandatory before production under GDPR Art. 35 & AI Act Art. 27 |
| **Monitoring** | None | Real-time false positive/negative monitoring by segment |
| **Incident Response** | None | Breach notification procedure per Art. 33 (72-hour window) |

The Latvian supervisory authority for both GDPR and AI Act oversight is the **Datu valsts inspekcija (DVI)**: [dvi.gov.lv](https://www.dvi.gov.lv/en).

---

### 6. Summary

The current prototype is GDPR compatible because it is stateless, stores nothing and supports human-in-the-loop decision-making. Scaling to production introduces formal obligations, primarily Art. 6, 22, and 35 of the GDPR and Art. 27 of the AI Act, that require architectural commitments to oversight, impact assessments, and formal model governance.