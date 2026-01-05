# Master's Thesis – Polygenic Risk Scores for Type 2 Diabetes: Analysing Consensus and Viability

This repository contains the code developed during my Master's thesis, which focuses on the assessment and comparison of polygenic risk score (PRS) models for Type 2 Diabetes (T2D), with an emphasis on individual risk ranking and model equivalence.

---

## Abstract
In recent years, polygenic risk score models have become powerful tools for analyzing the genetic contribution of common diseases and human characteristics, facilitating the development of genetic tests for risk prediction and better cohort definition for clinical trials. A polygenic risk score is a weighted sum of several variants’ allele counts, where their weights reflect the magnitude of the association of each allele with a specific human body characteristic or disease. Given the complex genetic nature of type 2 diabetes, polygenic risk scores can be useful in the prediction of the genetic contribution of an individual developing this condition. In this thesis, the 64 polygenic risk score models developed for European populations available in PGS Catalog are assessed with the purpose of creating a consensus model that would best fit the Portuguese population and would accurately predict the genetic risk of developing type 2 diabetes. From this analysis, it was concluded that, without evaluating the existent linkage disequilibrium between the different variants of the several models, it is not possible to find a core set of variants to define a consensus model. As an alternative approach, we propose to compare the models by evaluating their capability of ranking individuals of a certain cohort consistently. Consequently, models that would guarantee the same ranking can be considered equivalent. To validate this approach, 2 cohorts were selected: one comprising 50 individuals from Harvard’s Personal Genome Project and the other with 23 individuals from the OpenSNP database. To identify the most similar polygenic risk score models, the different models were clustered according to the rankings of the different individuals they generated, using two different clustering methods: Hierarchical clustering and K-Means. This analysis suggests that, despite different sizes and the use of different variant alleles,it was possible to identify a set of models that can consistently rank the different cohorts. 

**Keywords:** Genetic Predisposition; Linkage Disequilibrium; Polygenic Risk Scores; Preventive Medicine; Ranking; Type 2
diabetes

The full Master's thesis document is publicly available [here](https://ulisboa-my.sharepoint.com/:f:/g/personal/ist192773_tecnico_ulisboa_pt/IgDwRc8o-lJKQqdeOdS9zfsoASx9OvItGPJkZd8klBswrso?e=00ToXM) and provides a detailed description of the methods, results, and discussion

----

## Repository overview

This repository includes scripts for:
- Post-processing of PLINK-generated PRS outputs
- Aggregation of polygenic risk scores across individuals and models
- Ranking individuals based on genetic risk
- Extraction of model-specific metadata (e.g. number of valid predictors)
- Comparison and clustering of PRS models based on individual rankings

The repository does not include raw genotype data.

----

## Disclaimer

This repository is intended for academic and research purposes. Some scripts reflect intermediate or exploratory stages of analysis conducted during the development of the Master's thesis.
