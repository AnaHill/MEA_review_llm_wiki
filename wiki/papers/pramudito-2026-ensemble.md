---
tags: [machine-learning, cardiac-safety]
---

# Stacking ensemble machine learning for cardiac safety assessment using hiPSC-CM MEA data

**Authors:** M.A. Pramudito, Y.N. Fuadah, Y.S. Kim, K.M. Lim  
**Year:** 2026  
**Venue:** Annals of Biomedical Engineering 54:1334–1344  
**DOI:** 10.1007/s10439-026-03978-1  
**PubMed:** https://pubmed.ncbi.nlm.nih.gov/41586860/  
**File:** *(no PDF downloaded)*

> **Note:** Confirmed real. DOI and PubMed ID verified by author. Bibliographic details (author initials, issue 5, May 2026, pp. 1334–1344) and the abstract-level content below checked against Europe PMC record for PMID 41586860 on 2026-10-15. Not open access; full text not read, so everything below is abstract-level only.

## Contribution
Tests whether a stacking ensemble of classifiers predicts Torsades de Pointes (TdP) risk from hiPSC-CM MEA data better than single classifiers. Per the abstract, the ensemble outperformed all single classifiers.

## Methodology
*(Abstract-level; full text not read)*  
Base learners: random forest, XGBoost and a shallow neural network, combined with a meta-classifier. Inputs are two simple field-potential-derived features. Evaluated on 16 unseen CiPA reference compounds. Which two features, and the training data source, are not stated in the abstract and remain unknown.

## Findings
*(Abstract-level; full text not read)*  
The stacking ensemble outperformed all single classifiers; the XGBoost-based meta-classifier is reported to reach perfect discrimination (AUC 1.000) on the 16 unseen compounds. The authors conclude that external validation with additional MEA datasets is needed before translational use.

## Limitations
Authors' own caveat: external validation on additional MEA datasets still needed. Our additional observation: a perfect AUC on only 16 compounds is a small test set, so the result should be cited cautiously. Full text needed to assess feature definitions (e.g. which FPD correction is used).

## Relevance to our paper
Cited in main.md as an example of machine learning integration with MEA data for TdP risk prediction, representing a methodological frontier beyond threshold-based FPDcF analysis.

## See also
- [[wiki/papers/matsuda-2025-uhd.md]]
- [[wiki/papers/altrocchi-2023-chronic.md]]
- [[wiki/papers/park-2025-cardiotoxicity.md]]
- [[wiki/papers/weiser-bitoun-2026-physiomea.md]]
