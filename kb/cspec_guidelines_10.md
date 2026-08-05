<!-- Generated: 2026-08-05T00:35:22.564181+00:00 | Parser: 0.1.0 -->

# TPM1

Document: ClinGen Cardiomyopathy Expert Panel Specifications to the ACMG/AMP Variant Interpretation Guidelines for TPM1 Version 1.0
CSpec ID: GN100
VCEP: Cardiomyopathy Variant Curation Expert Panel
Version: 1.0
Status: current_released
Diseases: MONDO:0005045
Modes of inheritance: https://hpo.jax.org/app/browse/term/HP:0000006
Fetched: 2026-08-05T00:33:27.068091+00:00
Source API: https://cspec.genome.network/cspec/api/SequenceVariantInterpretation/id/GN100

## BA1 — Moderate

Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

Applicability: Not applicable



## BA1 — Stand Alone

Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

Applicability: Applicable

Allele frequency is **≥0.001** based on the **filtering allele frequency (FAF)** in **gnomAD** in the subpopulation with the highest frequency (popmax).

The values used to calculate the BA1 threshold were derived from studies in Northern European populations that have been relatively well-characterized with regards to disease prevalence and variant spectrum. These thresholds can be applied to any population where disease prevalence is considered comparable (1/300 or lower).

The threshold is applicable when assessing variants in the context of autosomal dominant cardiomyopathy. 

gnomAD is the preferred database for this calculation. If a subpopulation specific FAF other than the popmax is needed, this value can be calculated using the AlleleFrequencyApp on the [CardioDB website](https://cardiodb.org/allelefrequencyapp/).

1.  Using the Inverse AF tab, enter in the population size and the number of alleles identified and it will calculate the FAF.  
2.  Set confidence to 0.95 (95%).
3.  If the FAF is ≥0.001, this rule can be applied.

The FAF by platform (e.g., exome vs. genome; v.2.1.1 vs. v.3.1.1) should be considered, the larger population is most likely to have the most accurate representation of “true” population allele frequency.

Caution is needed when considering any population cohorts that are smaller than the smallest subpopulations within gnomAD v.2.1.1 (e.g., ~5000 individuals or ~10,000 alleles). Despite this conservative nature of this threshold and approach, in smaller cohorts, the observed allele frequency may less accurately reflect the true allele frequency. Traditionally, once a variant is classified as Benign, it is rarely re-evaluated and so the highest confidence is needed to establish that classification on an allele frequency alone.

## BA1 — Strong

Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

Applicability: Not applicable



## BA1 — Supporting

Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

Applicability: Not applicable



## BA1 — Very Strong

Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

Applicability: Not applicable



## BP1 — Moderate

Missense variant in a gene for which primarily truncating variants are known to cause disease.

Applicability: Not applicable



## BP1 — Stand Alone

Missense variant in a gene for which primarily truncating variants are known to cause disease.

Applicability: Not applicable



## BP1 — Strong

Missense variant in a gene for which primarily truncating variants are known to cause disease.

Applicability: Not applicable



## BP1 — Supporting

Missense variant in a gene for which primarily truncating variants are known to cause disease.

Applicability: Not applicable



## BP1 — Very Strong

Missense variant in a gene for which primarily truncating variants are known to cause disease.

Applicability: Not applicable



## BP2 — Moderate

Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.

Applicability: Not Applicable



## BP2 — Stand Alone

Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.

Applicability: Not applicable



## BP2 — Strong

Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.

Applicability: Not Applicable



## BP2 — Supporting

Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.

Applicability: Applicable

Other variants must be pathogenic as defined by these specifications.

Testing of parents or other informative relatives is often required to determine _cis_/_trans_ status.

If a variant is seen in _trans_ (or as double heterozygous) with another pathogenic variant in ≥2 cases and the phenotype is not more severe than when either of the two variants are seen in isolation, this rule may be applied (i.e., high confidence this variant is NOT contributing to disease).

*   \<1% of cases of HCM have >1 pathogenic or likely pathogenic variant (0.6%; Alfares _et al._ 2015[<sup>17</sup>](#pmid_25611685)).

This rule cannot be applied when the variant has only been observed in _cis_ with a pathogenic variant as its significance in isolation is unknown in this scenario. 

Caution is needed if using this criterion as a primary piece of evidence for classifying a variant as likely benign/benign (i.e., only 2 SUPPORTING criteria are sufficient for a likely benign classification).

## BP2 — Very Strong

Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.

Applicability: Not applicable



## BP3 — Moderate

In frame-deletions/insertions in a repetitive region without a known function.

Applicability: Not applicable



## BP3 — Stand Alone

In frame-deletions/insertions in a repetitive region without a known function.

Applicability: Not applicable



## BP3 — Strong

In frame-deletions/insertions in a repetitive region without a known function.

Applicability: Not applicable



## BP3 — Supporting

In frame-deletions/insertions in a repetitive region without a known function.

Applicability: Not applicable



## BP3 — Very Strong

In frame-deletions/insertions in a repetitive region without a known function.

Applicability: Not applicable



## BP4 — Moderate

Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.

Applicability: Not Applicable



## BP4 — Stand Alone

Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.

Applicability: Not applicable



## BP4 — Strong

Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.

Applicability: Not Applicable



## BP4 — Supporting

Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.

Applicability: Applicable

As many _in silico_ algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. Meta-predictors, such as REVEL, are preferred over multiple individual predictors.

Use of REVEL (Ioannidis et al. 2016[<sup>13</sup>](#pmid_27666373)) is recommended at thresholds of **≤0.40 for BP4**.

Clinical judgment is needed if any individual algorithms or conservation data are contradictory to REVEL data.

Positive predictive value for benign/no impact predictions is generally higher than for pathogenic/impact predictions.

[SpliceAI](https://spliceailookup.broadinstitute.org)[<sup>14</sup>](#pmid_30661751) is recommended for evaluation of predicted splice impacts.

## BP4 — Very Strong

Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.

Applicability: Not applicable



## BP5 — Moderate

Variant found in a case with an alternate molecular basis for disease.

Applicability: Not applicable



## BP5 — Stand Alone

Variant found in a case with an alternate molecular basis for disease.

Applicability: Not applicable



## BP5 — Strong

Variant found in a case with an alternate molecular basis for disease.

Applicability: Not applicable



## BP5 — Supporting

Variant found in a case with an alternate molecular basis for disease.

Applicability: Not applicable



## BP5 — Very Strong

Variant found in a case with an alternate molecular basis for disease.

Applicability: Not applicable



## BP6 — Moderate

Reputable source recently reports variant as benign, but the evidence is not available to the laboratory to perform an independent evaluation.

Applicability: Not applicable

This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee.

## BP6 — Stand Alone

Reputable source recently reports variant as benign, but the evidence is not available to the laboratory to perform an independent evaluation.

Applicability: Not applicable

This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee.

## BP6 — Strong

Reputable source recently reports variant as benign, but the evidence is not available to the laboratory to perform an independent evaluation.

Applicability: Not applicable

This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee.

## BP6 — Supporting

Reputable source recently reports variant as benign, but the evidence is not available to the laboratory to perform an independent evaluation.

Applicability: Not applicable

This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee.

## BP6 — Very Strong

Reputable source recently reports variant as benign, but the evidence is not available to the laboratory to perform an independent evaluation.

Applicability: Not applicable

This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee.

## BP7 — Moderate

A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.

Applicability: Not Applicable



## BP7 — Stand Alone

A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.

Applicability: Not applicable



## BP7 — Strong

A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.

Applicability: Not Applicable



## BP7 — Supporting

A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.

Applicability: Applicable

Also applicable to **intronic variants outside the splice consensus sequence (-4 and +7 outward)** for which splicing prediction algorithms predict no impact to the splice consensus sequence NOR the creation of a new splice site AND the nucleotide is not highly conserved.

Rule can be combined with BP4 to make a variant likely benign per Richards _et al._ 2015[<sup>1</sup>](#pmid_25741868).

## BP7 — Very Strong

A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.

Applicability: Not applicable



## BS1 — Moderate

Allele frequency is greater than expected for disorder.

Applicability: Not Applicable



## BS1 — Stand Alone

Allele frequency is greater than expected for disorder.

Applicability: Not Applicable



## BS1 — Strong

Allele frequency is greater than expected for disorder.

Applicability: Applicable

Allele frequency is **≥0.0001 for** _**TPM1**_ based on the **filtering allele frequency (FAF)** in **gnomAD** in the subpopulation with the highest frequency (popmax).

Criterion BS1 may only be used as standalone evidence to classify a variant as Likely Benign in the absence of conflicting data. See SVI guidance (Tavtigian _et al._ 2018[<sup>15</sup>](#pmid_29300386); Tavtigian _et al._ 2020[<sup>16</sup>](#pmid_32720330)). 

See BA1 for additional specifications that also apply to BS1.

## BS1 — Supporting

Allele frequency is greater than expected for disorder.

Applicability: Not Applicable



## BS1 — Very Strong

Allele frequency is greater than expected for disorder.

Applicability: Not applicable



## BS2 — Moderate

Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

Applicability: Not applicable



## BS2 — Stand Alone

Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

Applicability: Not applicable



## BS2 — Strong

Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

Applicability: Not applicable



## BS2 — Supporting

Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

Applicability: Not applicable



## BS2 — Very Strong

Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

Applicability: Not applicable



## BS3 — Moderate

Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

Applicability: Applicable

See PS3 specifications.

## BS3 — Stand Alone

Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

Applicability: Not applicable



## BS3 — Strong

Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

Applicability: Applicable

See PS3 specifications.

## BS3 — Supporting

Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

Applicability: Applicable

See PS3 specifications.

## BS3 — Very Strong

Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

Applicability: Not applicable



## BS4 — Moderate

Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

Applicability: Not Applicable



## BS4 — Stand Alone

Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

Applicability: Not applicable



## BS4 — Strong

Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

Applicability: Applicable

Any non-segregations should be carefully evaluated to rule out a phenocopy or the presence of a second disease-causing variant before considering it as conflicting or benign evidence. 

1.  The presence of “phenocopies” (e.g., athlete’s heart, hypertensive heart disease, ischemic cardiomyopathy, alcoholic cardiomyopathy, diabetic cardiomyopathy) can mimic non-segregation (i.e., lack of segregation) among affected individuals. 
2.  Families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent ‘non-segregation’.

Because of these possibilities, **multiple (≥2) non-segregations** that are highly unlikely to be phenocopies or due to alternate variants (e.g., those without a possible alternate cause) **are required to apply this rule**.  A higher number of non-segregations is necessary for instances where alternative causes are possible (e.g., non-segregation in a sibling with childhood onset cardiomyopathy versus a grandparent with hypertension and HCM).

Careful consideration of the above points is required when using this data as conflicting evidence, especially when overall evidence supports likely pathogenic or pathogenic.

## BS4 — Supporting

Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

Applicability: Not Applicable



## BS4 — Very Strong

Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

Applicability: Not applicable



## PM1 — Moderate

Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

Applicability: Not applicable



## PM1 — Stand Alone

Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

Applicability: Not applicable



## PM1 — Strong

Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

Applicability: Not applicable



## PM1 — Supporting

Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

Applicability: Not applicable



## PM1 — Very Strong

Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

Applicability: Not applicable



## PM2 — Moderate

Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.

Applicability: Not Applicable



## PM2 — Stand Alone

Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.

Applicability: Not applicable



## PM2 — Strong

Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.

Applicability: Not applicable



## PM2 — Supporting

Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.

Applicability: Applicable

The values used to calculate the PM2 thresholds were derived from studies in Northern European populations that have been relatively well-characterized with regards to disease prevalence and variant spectrum. These thresholds can be applied to any population where disease prevalence is considered comparable (1/500 or lower), where the most frequent pathogenic variant accounts for no more than 2% of cases (e.g., has an allele frequency of ≤0.02 in cases based on the upper bound of 95% CI), and where the penetrance of a pathogenic variant is expected to be at least 50% (Kelly _et al._ 2018[<sup>10</sup>](#pmid_29300372)).

A threshold of **≤0.00004** in the subpopulation with the highest frequency when using the upper bound of the 95% CI activates this rule.

1.  Alternatively, this is equivalent to the variant NOT being observed more than once (≤1 allele) in gnomAD v.2.1.1 in one of the non-founder populations (e.g., absence required from the Other and Ashkenazi Jewish subpopulations).
2.  Applying a threshold of ≤0.00004 (upper bound of 95% CI of the allele frequency in gnomAD) is equivalent to the variant being seen in a single subpopulation and that subpopulation meets any of the following:
    *   **Allele Count (AC) in Allele Number (AN)**
    *   ≤1 in ≥120,000
    *   ≤2 in ≥160,000
    *   ≤3 in ≥195,000
    *   ≤4 in ≥230,000

gnomAD is the preferred database for this calculation, but currently only displays the filtering allele frequency (FAF), which is equivalent to a lower bound estimate of the 95% CI, when the upper bound is what is needed.

*   Confidence interval tools, such as [Confit-de-MAF](https://www.genecalculators.net/confit-de-maf.html), can be used to determine the upper bound of the 95% CI of the observed allele frequency.

Due to current technical limitations of next generation sequencing technologies, minor allele frequencies for complex variants (e.g., large indels) may not be accurately represented in population databases.

Caution should be used when a variant is only identified, or over-represented, in one of the smaller gnomAD populations, as the gnomAD allele frequencies may not accurately represent the true population frequency.

Population databases may contain affected or pre-symptomatic individuals for diseases with reduced penetrance/variable onset.

## PM2 — Very Strong

Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.

Applicability: Not applicable



## PM3 — Moderate

For recessive disorders, detected in trans with a pathogenic variant
Note: This requires testing of parents (or offspring) to determine phase.

Applicability: Not applicable



## PM3 — Stand Alone

For recessive disorders, detected in trans with a pathogenic variant
Note: This requires testing of parents (or offspring) to determine phase.

Applicability: Not applicable



## PM3 — Strong

For recessive disorders, detected in trans with a pathogenic variant
Note: This requires testing of parents (or offspring) to determine phase.

Applicability: Not applicable



## PM3 — Supporting

For recessive disorders, detected in trans with a pathogenic variant
Note: This requires testing of parents (or offspring) to determine phase.

Applicability: Not applicable



## PM3 — Very Strong

For recessive disorders, detected in trans with a pathogenic variant
Note: This requires testing of parents (or offspring) to determine phase.

Applicability: Not applicable



## PM4 — Moderate

Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

Applicability: Applicable

Strength of rule should be carefully considered and may require downgrading to SUPPORTING based on the predicted impact of the variant, including the size of the deletion/insertion, its location, and conservation of the region. 

For genes where PVS1 is not applicable (i.e., where there is no evidence that pLOF variants cause disease), consider using this rule at MODERATE or SUPPORTING strength for truncating variants that do NOT undergo nonsense mediated decay (NMD).

## PM4 — Stand Alone

Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

Applicability: Not applicable



## PM4 — Strong

Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

Applicability: Not Applicable



## PM4 — Supporting

Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

Applicability: Not Applicable



## PM4 — Very Strong

Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

Applicability: Not applicable



## PM5 — Moderate

Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

Applicability: Applicable

This criterion can be used at MODERATE if a different missense variant at the same codon has been classified as _pathogenic_ using these modified guidelines without application of PM5.

The impact of the amino acid change being evaluated needs to be compared to the impact of the amino acid change that is established as pathogenic (e.g., a change of Ala to His is less severe than Ala to Cys change). Consider reducing the strength of this rule to SUPPORTING if the predicted impact is not expected to be equivalent or more severe.

PM5 should not be combined with PM1.  If both are applicable at MODERATE weight, use of PM5 is most appropriate since it is variant specific.

## PM5 — Stand Alone

Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

Applicability: Not applicable



## PM5 — Strong

Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

Applicability: Not Applicable



## PM5 — Supporting

Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

Applicability: Applicable

This criterion can be considered at SUPPORTING if a different missense variant at the same codon has been classified as _likely pathogenic_ using these modified guidelines without application of PM5.

The impact of the amino acid change being evaluated needs to be compared to the impact of the amino acid change that is established as likely pathogenic (e.g., a change of Ala to His is less severe than Ala to Cys change). Consider reducing the strength of this rule to NOT APPLICABLE if the predicted impact is not expected to be equivalent or more severe.

PM5 should not be combined with PM1.  The one with the higher strength should be applied, but if both are applicable at SUPPORTING weight, use of PM5 is most appropriate since it is variant specific.

## PM5 — Very Strong

Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

Applicability: Not applicable



## PM6 — Moderate

Assumed de novo, but without confirmation of paternity and maternity.

Applicability: Applicable

Refer to SVI guidance on number/combination of cases required based on phenotype specificity[<sup>2</sup>](#url_c73e109e-b916-5a72-b7b1-1762446f3c11).

For most cardiomyopathies, it is recommended to default to “phenotype consistent with gene but not highly specific”. Clinical judgment is required for shifting to a higher or lower phenotypic consistency. 

See PS2 for additional considerations.

## PM6 — Stand Alone

Assumed de novo, but without confirmation of paternity and maternity.

Applicability: Not applicable



## PM6 — Strong

Assumed de novo, but without confirmation of paternity and maternity.

Applicability: Not Applicable



## PM6 — Supporting

Assumed de novo, but without confirmation of paternity and maternity.

Applicability: Not Applicable



## PM6 — Very Strong

Assumed de novo, but without confirmation of paternity and maternity.

Applicability: Not applicable



## PP1 — Moderate

Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.

Applicability: Applicable

Due to the genotypic and phenotypic heterogeneity of inherited cardiomyopathies, segregation thresholds have been conservatively set at **≥5** **segregations** (LOD score of 1.5) for **MODERATE**.

Although rare for inherited cardiomyopathies, when the phenotype/presentation of a variant within and across families is highly specific (e.g., early-onset severe RCM in all affected individuals), the following thresholds as proposed by Jarvik and Browning (2016)[<sup>11</sup>](#pmid_27236918) can be considered: 

*   MODERATE evidence requires ≥4 segregations (LOD score of 1.2)

Only genotype positive/phenotype positive individuals are counted as segregations, which can include affected obligate carriers. Genotype positive/phenotype negative individuals are generally less informative for cardiomyopathy genes due to variable age at onset and reduced penetrance.

Phenotypes should be clinically confirmed, whenever possible, and should not include individuals with a suspected diagnosis.  

Important considerations include:

1.  Segregation of a variant within a single family or haplotype has the potential to represent linkage disequilibrium with another undetected variant.  If linkage disequilibrium is a concern, consider downgrading strength of segregation. 
2.  Use of segregation criteria should be carefully evaluated if variant frequency meets criteria for BS1 (see below).
3.  Caution is needed when counting segregations in presence of other possible disease-causing variants, as both variants may be contributing to the phenotype. 
4.  Caution is needed when distantly related (≥3<sup>rd</sup> degree) affected individuals are connected by unknown or unaffected relatives (raises possibility of multiple causes of disease).

## PP1 — Stand Alone

Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.

Applicability: Not applicable



## PP1 — Strong

Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.

Applicability: Applicable

Due to the genotypic and phenotypic heterogeneity of inherited cardiomyopathies, segregation thresholds have been conservatively set at **≥7** **segregations** (LOD score of 2.1) for **STRONG**.

Although rare for inherited cardiomyopathies, when the phenotype/presentation of a variant within and across families is highly specific (e.g., early-onset severe RCM in all affected individuals), the following thresholds as proposed by Jarvik and Browning (2016)[<sup>11</sup>](#pmid_27236918) can be considered: 

*   STRONG evidence requires ≥5 segregations (LOD score of 1.5)

Only genotype positive/phenotype positive individuals are counted as segregations, which can include affected obligate carriers. Genotype positive/phenotype negative individuals are generally less informative for cardiomyopathy genes due to variable age at onset and reduced penetrance.

Phenotypes should be clinically confirmed, whenever possible, and should not include individuals with a suspected diagnosis.  

Important considerations include:

1.  Segregation of a variant within a single family or haplotype has the potential to represent linkage disequilibrium with another undetected variant.  If linkage disequilibrium is a concern, consider downgrading strength of segregation. 
2.  Use of segregation criteria should be carefully evaluated if variant frequency meets criteria for BS1.
3.  Caution is needed when counting segregations in presence of other possible disease-causing variants, as both variants may be contributing to the phenotype. 
4.  Caution is needed when distantly related (≥3<sup>rd</sup> degree) affected individuals are connected by unknown or unaffected relatives (raises possibility of multiple causes of disease).

## PP1 — Supporting

Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.

Applicability: Applicable

Due to the genotypic and phenotypic heterogeneity of inherited cardiomyopathies, segregation thresholds have been conservatively set at **≥3** **segregations** (LOD score of 0.9) for **SUPPORTING**. The thresholds as proposed by Jarvik and Browning (2016)[<sup>11</sup>](#pmid_27236918) are the same at ≥3 segregations (LOD score of 0.9) for supporting.

Only genotype positive/phenotype positive individuals are counted as segregations, which can include affected obligate carriers. Genotype positive/phenotype negative individuals are generally less informative for cardiomyopathy genes due to variable age at onset and reduced penetrance.

Phenotypes should be clinically confirmed, whenever possible, and should not include individuals with a suspected diagnosis.  

Important considerations include:

1.  Segregation of a variant within a single family or haplotype has the potential to represent linkage disequilibrium with another undetected variant.  If linkage disequilibrium is a concern, consider downgrading strength of segregation. 
2.  Use of segregation criteria should be carefully evaluated if variant frequency meets criteria for BS1 (see below).
3.  Caution is needed when counting segregations in presence of other possible disease-causing variants, as both variants may be contributing to the phenotype. 
4.  Caution is needed when distantly related (≥3<sup>rd</sup> degree) affected individuals are connected by unknown or unaffected relatives (raises possibility of multiple causes of disease).

## PP1 — Very Strong

Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.

Applicability: Not applicable



## PP2 — Moderate

Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

Applicability: Not applicable



## PP2 — Stand Alone

Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

Applicability: Not applicable



## PP2 — Strong

Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

Applicability: Not applicable



## PP2 — Supporting

Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

Applicability: Applicable

Application of this rule takes into consideration empirical data quantifying levels of rare missense variant enrichment in HCM referral cohorts compared to population-based cohorts (Walsh _et al._ 2019[<sup>12</sup>](#pmid_30696458)) rather than the missense constraint score in gnomAD. 

On the basis of data from Walsh _et al._ 2019[<sup>12</sup>](#pmid_30696458), **PP2 is currently** **only applicable to** _**TPM1**_ **for HCM** (transcripts ENST00000403994 and NM\_001018005.2)_._

Data from HCM case cohorts was used to derive these cluster regions. Therefore, this rule should NOT be applied when additional evidence for the variant supports that the variant causes a phenotype other than HCM (e.g., variant seen in multiple DCM cases).

Enrichment was not observed for DCM in any genes.

## PP2 — Very Strong

Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

Applicability: Not applicable



## PP3 — Moderate

Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

Applicability: Not Applicable



## PP3 — Stand Alone

Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

Applicability: Not applicable



## PP3 — Strong

Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

Applicability: Not Applicable



## PP3 — Supporting

Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

Applicability: Applicable

As many _in silico_ algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. Meta-predictors, such as REVEL, are preferred over multiple individual predictors.

Use of REVEL (Ioannidis _et al._ 2016[<sup>13</sup>](#pmid_27666373)) is recommended at thresholds of **≥0.70 for PP3**.

Clinical judgment is needed if any individual algorithms or conservation data are contradictory to REVEL data.

Positive predictive value for benign/no impact predictions is generally higher than for pathogenic/impact predictions.

[SpliceAI](https://spliceailookup.broadinstitute.org)[<sup>14</sup>](#pmid_30661751) is recommended for evaluation of predicted splice impacts.

## PP3 — Very Strong

Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

Applicability: Not applicable



## PP4 — Moderate

Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.

Applicability: Not applicable



## PP4 — Stand Alone

Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.

Applicability: Not applicable



## PP4 — Strong

Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.

Applicability: Not applicable



## PP4 — Supporting

Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.

Applicability: Not applicable



## PP4 — Very Strong

Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.

Applicability: Not applicable



## PP5 — Moderate

Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

Applicability: Not applicable

This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee.

## PP5 — Stand Alone

Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

Applicability: Not applicable

This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee.

## PP5 — Strong

Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

Applicability: Not applicable

This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee.

## PP5 — Supporting

Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

Applicability: Not applicable

This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee.

## PP5 — Very Strong

Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

Applicability: Not applicable

This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee.

## PS1 — Moderate

Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

Applicability: Not Applicable



## PS1 — Stand Alone

Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

Applicability: Not applicable



## PS1 — Strong

Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

Applicability: Applicable

No cardiomyopathy specifications. Apply as outlined by Richards _et al_. 2015[<sup>1</sup>](#pmid_25741868).

Example of when rule should NOT be applied. NM\_000256.3(_MYBPC3_): c.2308G>A (p.Asp770Asn) has an established impact on splicing leading to nonsense mediated decay (NMD) and should not be used to provide evidence for other variants observed to result in the same amino acid change.

## PS1 — Supporting

Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

Applicability: Not Applicable



## PS1 — Very Strong

Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

Applicability: Not applicable



## PS2 — Moderate

De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

Applicability: Not Applicable



## PS2 — Stand Alone

De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

Applicability: Not applicable



## PS2 — Strong

De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

Applicability: Applicable

Refer to SVI guidance on number/combination of cases required based on phenotype specificity[<sup>2</sup>](#url_c73e109e-b916-5a72-b7b1-1762446f3c11).

For most cardiomyopathies, it is recommended to default to **Phenotype consistency: “Phenotype consistent with gene but not highly specific”**. Clinical judgment is required for shifting to a higher or lower category. 

For use as a STRONG or VERY STRONG criterion, ideally parents have been thoroughly clinically evaluated without evidence of cardiomyopathy (ideally using a combination of ECG and echocardiogram or cardiac MRI for maximum sensitivity).

A family history consistent with _de novo_ inheritance should not have any clinical signs or symptoms suggestive of cardiomyopathy in a 1<sup>st</sup> or 2<sup>nd</sup> degree relative, for example: 

1.  Sudden death under 60 years of age
2.  Heart transplant
3.  Implantable cardiac defibrillator (ICD) under 60 years of age
4.  Features of cardiomyopathy (e.g., systolic dysfunction, hypertrophy, left ventricular enlargement in an individual without risk factors).
5.  Other related/overlapping cardiomyopathies

Examples of non-suspicious family history may include non-specific clinical features (e.g., palpitations, syncope, borderline/inconclusive echocardiogram findings, heart attack if age appropriate and suspected to result from coronary artery disease), but every attempt should be made to clarify features. 

Generally, this criterion is only applicable in the ABSENCE of any other possible disease-causing variants.  If other pathogenic or likely pathogenic variants are present, consider decreasing points assigned or overall weight.

## PS2 — Supporting

De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

Applicability: Not Applicable



## PS2 — Very Strong

De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

Applicability: Not Applicable



## PS3 — Moderate

Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

Applicability: Applicable

**In vivo models (e.g., variant knock-in animal models)**

Mammalian variant-specific knock-in animal models that produce a phenotype consistent with the clinical phenotype in humans (e.g., structural and/or functional cardiac abnormalities, premature death, arrhythmia) may be considered as **MODERATE** evidence

**NOTE:** The following assays/models do NOT meet criteria

1.  Assays that are known to be associated with non-specific cardiac phenotypes (e.g., morpholino-induced pericardial edema in zebrafish)
2.  In vivo evidence that is not variant specific, such as whole gene alterations (i.e., cDNA or whole gene transgenic mice and whole or partial gene knock-out mice)

## PS3 — Stand Alone

Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

Applicability: Not applicable



## PS3 — Strong

Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

Applicability: Applicable

**In vitro splicing assays (e.g., RNA studies)**

_In vitro_ splicing assays may be considered as **STRONG** evidence, providing the following criteria are met.

*   Prior knowledge of predominant transcripts in cardiac tissue

Analysis undertaken using RNA extracted from cardiac tissue from the individual with the variant

Analysis undertaken using RNA extracted from whole blood providing the relevant transcripts (isoforms) are expressed in blood and are at sufficient levels to assess splice disruption.

Assay shows a clear, reproducible and convincing effect on splicing (i.e. a distinct splice product, present at a level comparable to the splice product from the wild-type allele), which is not observed in controls

*   Confirmation of abnormal splice product by Sanger sequencing

**NOTE:** Mini-gene assay in non-patient derived cell lines are NOT considered to provide STRONG evidence.

**NOTE:**  Whether to activate this rule needs to be reconciled with the variant spectrum and disease mechanism for the gene at hand (i.e., consider whether the effect is likely to lead to LOF or an in-frame alteration and whether this type of effect is expected to be disease causing) (Abou Tayoun _et al._ 2018[<sup>3</sup>](#pmid_30192042)).

## PS3 — Supporting

Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

Applicability: Applicable

_**In vitro**_ **assays (e.g., biochemical assays of myofilament function, motility assays, human iPSC-CM)**

While some _in vitro_ assays may provide evidence that a variant in a cardiomyopathy gene has an effect on protein and/or myofilament function, at present, there are no validated “gold-standard” assays that are considered to reliably predict the clinical phenotype.

As such, in the cardiomyopathy genes listed in these guidelines, data from individual _in vitro_ studies are unlikely to meet the criteria required to assign this rule at more than SUPPORTING level.

## PS3 — Very Strong

Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

Applicability: Not Applicable



## PS4 — Moderate

The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.
Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.
Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.

Applicability: Applicable

Currently few well-designed case-control studies have been performed for inherited cardiomyopathies.  Until such studies become available, comparative analyses can be undertaken using case data (e.g., internal and/or published cohorts) and control data from population-level cohorts (e.g., gnomAD). 

Cohorts used in these analyses should meet the following criteria: 

1.  The cases have a clinical diagnosis of the specified disorder or related phenotype (e.g., all cases have HCM or another relevant phenotype\*). 
    *   When assessing cases, it's important to consider how likely another potential cause of the phenotype has been excluded.  This includes considering the presence of other variants in relevant genes (particularly those likely to be contributing to phenotype) and the extent of testing performed (i.e., single gene sequencing, panel testing, whole exome/genome sequencing).
2.  The controls should not be derived from study populations that might be enriched for the specified disorder.
3.  The denominator of the cohorts must be available (e.g., variant detected in 5 out of 3,500 cases and 1 out of 60,000 controls).
4.  The cohorts do not include closely related individuals (i.e., family members are not included in the case counts).
5.  The cohorts do not overlap with other cohorts being used in the analysis (i.e., cases are not being counted more than once).
6.  The population diversity of the case and control cohorts are broadly similar.
7.  Consider the size of the case cohort — larger cohorts are likely to provide more accurate estimates of variant frequency; therefore, it may be preferable to use data from the largest available case series for case-control analyses (e.g., Walsh _et al._ 2017[<sup>5</sup>](#pmid_27532257), [DECIPHER](https://www.deciphergenomics.org/gene/TPM1/patient-overlap/snvs)).

To account for limitations that arise when performing unmatched case-control analyses, the following stringent OR threshold is recommended:

*   **MODERATE** evidence requires the lower bound of the 95% CI around the OR to be **≥10**

A PS4 calculator is available at [www.cardiodb.org](https://www.cardiodb.org/ps4_calculator/ps4_calculator.html).

If multiple cohorts are available, the final ORs and associated CIs need to be harmonized across all cohorts to determine the final level (e.g., if 2 large cohorts have an OR of ~6 and a third small cohort has an OR of 11, application at a SUPPORTING level should be considered).  

**\*RELEVANT PHENOTYPES:**

1.  Cases of HCM and RCM may be combined as they are considered part of the same disease spectrum. 
2.  For the eight genes covered by these guidelines, the combination of probands with other phenotypes should be reviewed by a clinical expert to determine if grouping is appropriate. 
3.  Additional considerations for LVNC and end-stage HCM: 
    *   Due to the current debate about whether isolated LVNC represents a true disease entity or variation of typical cardiac morphology (Anderson _et al._ 2017[<sup>6</sup>](#pmid_28395867); Oechslin _et al._ 2017[<sup>7</sup>](#pmid_28545618); Hershberger _et al._ 2017[<sup>8</sup>](#pmid_29212902); Ross _et al._ 2020[<sup>9</sup>](#pmid_31143950)), individuals with isolated LVNC should NOT be added to proband or segregation counts (including individuals with isolated LVNC in a family with other cardiomyopathies).

HCM and DCM have distinct mechanisms of disease and therefore pathogenetic variants are not anticipated to cause both primary phenotypes. While occurrence in both phenotypes may initially be considered as evidence against pathogenicity, end-stage HCM can present similarly to DCM. Careful consideration is needed before including DCM or related phenotypes in case or segregation data for primarily HCM variants.

## PS4 — Stand Alone

The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.
Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.
Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.

Applicability: Not applicable



## PS4 — Strong

The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.
Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.
Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.

Applicability: Applicable

Currently few well-designed case-control studies have been performed for inherited cardiomyopathies.  Until such studies become available, comparative analyses can be undertaken using case data (e.g., internal and/or published cohorts) and control data from population-level cohorts (e.g., gnomAD). 

Cohorts used in these analyses should meet the following criteria: 

1.  The cases have a clinical diagnosis of the specified disorder or related phenotype (e.g., all cases have HCM or another relevant phenotype\*). 
    *   When assessing cases, it's important to consider how likely another potential cause of the phenotype has been excluded.  This includes considering the presence of other variants in relevant genes (particularly those likely to be contributing to phenotype) and the extent of testing performed (i.e., single gene sequencing, panel testing, whole exome/genome sequencing).
2.  The controls should not be derived from study populations that might be enriched for the specified disorder.
3.  The denominator of the cohorts must be available (e.g., variant detected in 5 out of 3,500 cases and 1 out of 60,000 controls).
4.  The cohorts do not include closely related individuals (i.e., family members are not included in the case counts).
5.  The cohorts do not overlap with other cohorts being used in the analysis (i.e., cases are not being counted more than once).
6.  The population diversity of the case and control cohorts are broadly similar.
7.  Consider the size of the case cohort — larger cohorts are likely to provide more accurate estimates of variant frequency; therefore, it may be preferable to use data from the largest available case series for case-control analyses (e.g., Walsh _et al._ 2017[<sup>5</sup>](#pmid_27532257), [DECIPHER](https://www.deciphergenomics.org/gene/TPM1/patient-overlap/snvs)).

To account for limitations that arise when performing unmatched case-control analyses, the following stringent OR threshold is recommended:

*   **STRONG** evidence requires the lower bound of the 95% confidence interval (CI) around the odds ratio (OR) estimate to be **≥20**

A PS4 calculator is available at [www.cardiodb.org](https://www.cardiodb.org/ps4_calculator/ps4_calculator.html).

If multiple cohorts are available, the final ORs and associated CIs need to be harmonized across all cohorts to determine the final level (e.g., if 2 large cohorts have an OR of ~6 and a third small cohort has an OR of 11, application at a SUPPORTING level should be considered).  

**\*RELEVANT PHENOTYPES:**

1.  Cases of HCM and RCM may be combined as they are considered part of the same disease spectrum. 
2.  For the eight genes covered by these guidelines, the combination of probands with other phenotypes should be reviewed by a clinical expert to determine if grouping is appropriate. 
3.  Additional considerations for LVNC and end-stage HCM: 
    *   Due to the current debate about whether isolated LVNC represents a true disease entity or variation of typical cardiac morphology (Anderson _et al._ 2017[<sup>6</sup>](#pmid_28395867); Oechslin _et al._ 2017[<sup>7</sup>](#pmid_28545618); Hershberger _et al._ 2017[<sup>8</sup>](#pmid_29212902); Ross _et al._ 2020[<sup>9</sup>](#pmid_31143950)), individuals with isolated LVNC should NOT be added to proband or segregation counts (including individuals with isolated LVNC in a family with other cardiomyopathies).

HCM and DCM have distinct mechanisms of disease and therefore pathogenetic variants are not anticipated to cause both primary phenotypes. While occurrence in both phenotypes may initially be considered as evidence against pathogenicity, end-stage HCM can present similarly to DCM. Careful consideration is needed before including DCM or related phenotypes in case or segregation data for primarily HCM variants.

## PS4 — Supporting

The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.
Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.
Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.

Applicability: Applicable

Currently few well-designed case-control studies have been performed for inherited cardiomyopathies.  Until such studies become available, comparative analyses can be undertaken using case data (e.g., internal and/or published cohorts) and control data from population-level cohorts (e.g., gnomAD). 

Cohorts used in these analyses should meet the following criteria: 

1.  The cases have a clinical diagnosis of the specified disorder or related phenotype (e.g., all cases have HCM or another relevant phenotype\*). 
    *   When assessing cases, it's important to consider how likely another potential cause of the phenotype has been excluded.  This includes considering the presence of other variants in relevant genes (particularly those likely to be contributing to phenotype) and the extent of testing performed (i.e., single gene sequencing, panel testing, whole exome/genome sequencing).
2.  The controls should not be derived from study populations that might be enriched for the specified disorder.
3.  The denominator of the cohorts must be available (e.g., variant detected in 5 out of 3,500 cases and 1 out of 60,000 controls).
4.  The cohorts do not include closely related individuals (i.e., family members are not included in the case counts).
5.  The cohorts do not overlap with other cohorts being used in the analysis (i.e., cases are not being counted more than once).
6.  The population diversity of the case and control cohorts are broadly similar.
7.  Consider the size of the case cohort — larger cohorts are likely to provide more accurate estimates of variant frequency; therefore, it may be preferable to use data from the largest available case series for case-control analyses (e.g., Walsh _et al._ 2017[<sup>5</sup>](#pmid_27532257), [DECIPHER](https://www.deciphergenomics.org/gene/TPM1/patient-overlap/snvs)).

To account for limitations that arise when performing unmatched case-control analyses, the following stringent OR threshold is recommended:

*   **SUPPORTING** evidence requires the lower bound of the 95% CI around the OR to be **≥5**

A PS4 calculator is available at [www.cardiodb.org](https://www.cardiodb.org/ps4_calculator/ps4_calculator.html).

If multiple cohorts are available, the final ORs and associated CIs need to be harmonized across all cohorts to determine the final level (e.g., if 2 large cohorts have an OR of ~6 and a third small cohort has an OR of 11, application at a SUPPORTING level should be considered).  

**\*RELEVANT PHENOTYPES:**

1.  Cases of HCM and RCM may be combined as they are considered part of the same disease spectrum. 
2.  For the eight genes covered by these guidelines, the combination of probands with other phenotypes should be reviewed by a clinical expert to determine if grouping is appropriate. 
3.  Additional considerations for LVNC and end-stage HCM: 
    *   Due to the current debate about whether isolated LVNC represents a true disease entity or variation of typical cardiac morphology (Anderson _et al._ 2017[<sup>6</sup>](#pmid_28395867); Oechslin _et al._ 2017[<sup>7</sup>](#pmid_28545618); Hershberger _et al._ 2017[<sup>8</sup>](#pmid_29212902); Ross _et al._ 2020[<sup>9</sup>](#pmid_31143950)), individuals with isolated LVNC should NOT be added to proband or segregation counts (including individuals with isolated LVNC in a family with other cardiomyopathies).

HCM and DCM have distinct mechanisms of disease and therefore pathogenetic variants are not anticipated to cause both primary phenotypes. While occurrence in both phenotypes may initially be considered as evidence against pathogenicity, end-stage HCM can present similarly to DCM. Careful consideration is needed before including DCM or related phenotypes in case or segregation data for primarily HCM variants.

## PS4 — Very Strong

The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.
Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.
Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.

Applicability: Not Applicable



## PVS1 — Moderate

Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.

Applicability: Not applicable



## PVS1 — Stand Alone

Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.

Applicability: Not applicable



## PVS1 — Strong

Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.

Applicability: Not applicable



## PVS1 — Supporting

Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.

Applicability: Not applicable



## PVS1 — Very Strong

Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.

Applicability: Not applicable



# USH2A

Document: ClinGen Hearing Loss Expert Panel Specifications to the ACMG/AMP Variant Interpretation Guidelines for CDH23, COCH, GJB2,
KCNQ4, MYO6, MYO7A, SLC26A4, TECTA and USH2A Version 2.0
CSpec ID: GN005
VCEP: Hearing Loss Variant Curation Expert Panel
Version: 2.0
Status: current_released
Diseases: MONDO:0019501; MONDO:0019497; MONDO:0010134
Modes of inheritance: 
Fetched: 2026-08-05T00:32:05.813250+00:00
Source API: https://cspec.genome.network/cspec/api/SequenceVariantInterpretation/id/GN005

## BA1 — Moderate

Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

Applicability: Not Applicable for this VCEP



## BA1 — Stand Alone

Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

Applicability: Applicable with VCEP specification

MAF of ≥0.005 (0.5%) for autosomal recessive; MAF of ≥0.001 (0.1%) for autosomal dominant.

## BA1 — Strong

Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

Applicability: Not Applicable for this VCEP



## BA1 — Supporting

Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

Applicability: Not Applicable for this VCEP



## BA1 — Very Strong

Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

Applicability: Not Applicable for this VCEP



## BP1 — Moderate

Missense variant in a gene for which primarily truncating variants are known to cause disease.

Applicability: Not Applicable for this VCEP



## BP1 — Stand Alone

Missense variant in a gene for which primarily truncating variants are known to cause disease.

Applicability: Not Applicable for this VCEP



## BP1 — Strong

Missense variant in a gene for which primarily truncating variants are known to cause disease.

Applicability: Not Applicable for this VCEP



## BP1 — Supporting

Missense variant in a gene for which primarily truncating variants are known to cause disease.

Applicability: Not Applicable for this VCEP



## BP1 — Very Strong

Missense variant in a gene for which primarily truncating variants are known to cause disease.

Applicability: Not Applicable for this VCEP



## BP2 — Moderate

Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.

Applicability: Not Applicable for this VCEP



## BP2 — Stand Alone

Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.

Applicability: Not Applicable for this VCEP



## BP2 — Strong

Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.

Applicability: Not Applicable for this VCEP



## BP2 — Supporting

Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.

Applicability: Applicable with VCEP specification

Observed in trans with a dominant variant/observed in cis with a pathogenic variant (use with caution).
Use with caution. For genes that are associated with both dominant and recessive hearing loss, consider whether an earlier onset/more severe phenotype could be present if variant is identified in trans with a dominant variant.

## BP2 — Very Strong

Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.

Applicability: Not Applicable for this VCEP



## BP3 — Moderate

In frame-deletions/insertions in a repetitive region without a known function.

Applicability: Not Applicable for this VCEP



## BP3 — Stand Alone

In frame-deletions/insertions in a repetitive region without a known function.

Applicability: Not Applicable for this VCEP



## BP3 — Strong

In frame-deletions/insertions in a repetitive region without a known function.

Applicability: Not Applicable for this VCEP



## BP3 — Supporting

In frame-deletions/insertions in a repetitive region without a known function.

Applicability: Applicable with VCEP specification

In-frame indels in repeat region without known function.
No changes. Follow recommendations as outlined in Richard 2015 and/or ClinGen's Sequence Variant Interpretation working group.

## BP3 — Very Strong

In frame-deletions/insertions in a repetitive region without a known function.

Applicability: Not Applicable for this VCEP



## BP4 — Moderate

Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.

Applicability: Not Applicable for this VCEP



## BP4 — Stand Alone

Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.

Applicability: Not Applicable for this VCEP



## BP4 — Strong

Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.

Applicability: Not Applicable for this VCEP



## BP4 — Supporting

Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.

Applicability: Applicable with VCEP specification

Computational evidence suggests no impact; REVEL score ≤0.15 or no impact to splicing in MaxEntScan.

## BP4 — Very Strong

Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.

Applicability: Not Applicable for this VCEP



## BP5 — Moderate

Variant found in a case with an alternate molecular basis for disease.

Applicability: Not Applicable for this VCEP



## BP5 — Stand Alone

Variant found in a case with an alternate molecular basis for disease.

Applicability: Not Applicable for this VCEP



## BP5 — Strong

Variant found in a case with an alternate molecular basis for disease.

Applicability: Not Applicable for this VCEP



## BP5 — Supporting

Variant found in a case with an alternate molecular basis for disease.

Applicability: Applicable with VCEP specification

Variant in an autosomal dominant gene found in a patient with an alternate explanation.
* Autosomal recessive: Do not use. An individual could be carrier of pathogenic variant and have an alternate cause. Therefore, BP5 shouldn’t be used as evidence for benign in this case.
* Autosomal dominant: Can use BP5 as outlined by Richards 2015.

 * Caveat: consider whether multiple pathogenic autosomal dominant variants could cause a more severe phenotype or whether multigenic inheritance is known to occur (example: Bardet-Biedl syndrome).

## BP5 — Very Strong

Variant found in a case with an alternate molecular basis for disease.

Applicability: Not Applicable for this VCEP



## BP6 — Moderate

Reputable source recently reports variant as benign, but the evidence is not available to the laboratory to perform an independent evaluation.

Applicability: Not Applicable for this VCEP



## BP6 — Stand Alone

Reputable source recently reports variant as benign, but the evidence is not available to the laboratory to perform an independent evaluation.

Applicability: Not Applicable for this VCEP



## BP6 — Strong

Reputable source recently reports variant as benign, but the evidence is not available to the laboratory to perform an independent evaluation.

Applicability: Not Applicable for this VCEP



## BP6 — Supporting

Reputable source recently reports variant as benign, but the evidence is not available to the laboratory to perform an independent evaluation.

Applicability: Not Applicable for this VCEP



## BP6 — Very Strong

Reputable source recently reports variant as benign, but the evidence is not available to the laboratory to perform an independent evaluation.

Applicability: Not Applicable for this VCEP



## BP7 — Moderate

A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.

Applicability: Not Applicable for this VCEP



## BP7 — Stand Alone

A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.

Applicability: Not Applicable for this VCEP



## BP7 — Strong

A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.

Applicability: Not Applicable for this VCEP



## BP7 — Supporting

A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.

Applicability: Applicable with VCEP specification

Silent variant with no predicted impact to splicing.
No changes. Follow recommendations as outlined in Richard 2015 and/or ClinGen's Sequence Variant Interpretation working group.

## BP7 — Very Strong

A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.

Applicability: Not Applicable for this VCEP



## BS1 — Moderate

Allele frequency is greater than expected for disorder.

Applicability: Not Applicable for this VCEP



## BS1 — Stand Alone

Allele frequency is greater than expected for disorder.

Applicability: Not Applicable for this VCEP



## BS1 — Strong

Allele frequency is greater than expected for disorder.

Applicability: Applicable with VCEP specification

MAF of ≥0.003 (0.3%) for autosomal recessive; MAF of ≥0.0002 (0.02%) for autosomal dominant. Likely benign, provided there is no conflicting evidence.

## BS1 — Supporting

Allele frequency is greater than expected for disorder.

Applicability: Applicable with VCEP specification

MAF of ≥0.0007 (0.07%) for autosomal recessive. No BS1_Supporting criteria for autosomal dominant.

## BS1 — Very Strong

Allele frequency is greater than expected for disorder.

Applicability: Not Applicable for this VCEP



## BS2 — Moderate

Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

Applicability: Not Applicable for this VCEP



## BS2 — Stand Alone

Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

Applicability: Not Applicable for this VCEP



## BS2 — Strong

Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

Applicability: Applicable with VCEP specification

Observation of variant (biallelic with known pathogenic variant for recessive) in controls inconsistent with disease penetrance.
* Advise caution when using this rule, since most of hearing loss is autosomal recessive, and autosomal dominant hearing loss could display reduced penetrance or variable expression.
* However, if biallelic observations in controls are inconsistent with disease penetrance, this may be applicable.

## BS2 — Supporting

Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

Applicability: Not Applicable for this VCEP



## BS2 — Very Strong

Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

Applicability: Not Applicable for this VCEP



## BS3 — Moderate

Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

Applicability: Not Applicable for this VCEP



## BS3 — Stand Alone

Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

Applicability: Not Applicable for this VCEP



## BS3 — Strong

Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

Applicability: Not Applicable for this VCEP



## BS3 — Supporting

Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

Applicability: Applicable with VCEP specification

Functional study shows no deleterious effect (predefined list).
* Recommend that functional evidence is not used as strong evidence, due to the absence of well-established functional studies for hearing loss genes.
* Guidance on functional evidence at supporting level is as follows (see functional spreadsheets attached):
 * GJB2: electrical coupling assays, dye transfer assays → BS3_Supporting
  * Dye Transfer Assays: Expect results that compare the fluorescence of a variant-transfected cell to both a negative control (or H2O injected control) and a wildtype-transfected cell. BS2_Supporting can be applied if the variant results in dye transfer comparable to the wildtype.
  * Electrical Coupling Assays: Expect results comparing the current of the variant-transfected cells to both a negative control (or H2O injected control) and a wildtype-transfected cell. BS2_Supporting would be applied if the variant results in a current comparable to the wildtype.
 * SLC26A4: Radio isotope and fluorescence assays → BS3_Supporting
  * Radio Isotope Assays: BS3_Supporting would be applied if the variant results in iodide efflux levels comparable to the wildtype.
  * Fluorescence assay: BS3_Supporting would be applied if the variant results in fluorescence comparable to the wildtype
 * COCH: Localization, secretion, and dimerization studies performed using immunofluorescence and Western blotting techniques → BS3_Supporting
  * Localization: BS3_Supporting would be applied if the variant results in extracellular deposits comparable to the wildtype.
  * Secretion: BS3_Supporting would be applied if the variant results in secretion comparable to the wildtype.
  * Dimerization: In a non-reducing environment, wildtype cochlin migrate quickly and appear smaller than in the reduced state because the structure is maintained by disulfide bonds. BS3_Supporting would be applied if the variant results in molecular weight and size comparable to the wildtype.
* If not listed above, OK to use BS3_Supporting for other genes/functional analyses if
 * The assay has been validated by a known pathogenic and benign variant AND
 * There is plausible reason that the function the assay is testing relates to the phenotype AND
 * The assay conditions are likely to mimic the physiological environment.

## BS3 — Very Strong

Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

Applicability: Not Applicable for this VCEP



## BS4 — Moderate

Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

Applicability: Not Applicable for this VCEP



## BS4 — Stand Alone

Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

Applicability: Not Applicable for this VCEP



## BS4 — Strong

Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

Applicability: Applicable with VCEP specification

Non-segregation with disease.
* Phenotype+/genotype-
 * Strong evidence for benign.
 * Be cautious when using this as the possibility for phenocopy is high. The hearing loss phenotype should be consistent within the family to consider it a non-segregation, though intra-familial variability has been reported. Factors to consider are:
  * Age of onset (ie. congenital/early childhood vs. adult onset).
 * Hearing loss prevalence increases significantly with age. A congenital hearing loss in a child and a late onset hearing loss in a grandparent would not be a consistent phenotype.
  * Severity (ie - mild vs. profound).
   * Minor differences may exist among family members.
   * Keep in mind that progression in older individuals may account for a discrepancy between individuals.
  * Sex -based differences (infertility, genes on X chromosomes)
 * Audiogram shape.
  * May not be completely consistent among family members even with same etiology.
* Genotype+/phenotype-
 * Confounding variables to applying this rule: Age-related/sex-related penetrance, variable expressivity, etc.
 * If the gene is associated with later onset and individual with the non-segregation is beyond the expected age that the hearing loss would occur, consider applying BS4_Supporting
 * Recommend only using for fully penetrant genes (typically genes associated with AR hearing loss).
 * Must be confident that patient is truly unaffected and a hearing loss is not missed or subclinical. Be cautious if only phenotyping was newborn hearing screening. Diagnostic audiometric testing (auditory brainstem response (ABR) or audiogram should be required).
 * Any evidence for reduced penetrance, do not use BS4

## BS4 — Supporting

Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

Applicability: Not Applicable for this VCEP



## BS4 — Very Strong

Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

Applicability: Not Applicable for this VCEP



## PM1 — Moderate

Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

Applicability: Applicable with VCEP specification

Mutational hot spot or well-studied functional domain without benign variation (KCNQ4 pore-forming region).
* KCNQ4 (NM_004700.4) gene - missense variants located within amino acids 271-292 can be awarded PM1. This region is the pore-forming intramembrane region where many variants that cause autosomal dominant hearing loss are located (Naito et al. 2013, PMID: 23717403; https://www.uniprot.org/uniprot/P56696). There are only two missense variants in this region in gnomAD, each with only single allele (http://gnomad.broadinstitute.org/; rs763326539: 1/33578 Latino chromosomes; rs55737429: 1/111720 European chromosomes).

## PM1 — Stand Alone

Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

Applicability: Not Applicable for this VCEP



## PM1 — Strong

Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

Applicability: Not Applicable for this VCEP



## PM1 — Supporting

Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

Applicability: Not Applicable for this VCEP



## PM1 — Very Strong

Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

Applicability: Not Applicable for this VCEP



## PM2 — Moderate

Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.

Applicability: Not Applicable for this VCEP



## PM2 — Stand Alone

Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.

Applicability: Not Applicable for this VCEP



## PM2 — Strong

Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.

Applicability: Not Applicable for this VCEP



## PM2 — Supporting

Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.

Applicability: Applicable with VCEP specification

Absent/Rare in population databases (absent or ≤0.00007 (0.007%) for autosomal recessive, ≤0.00002 (0.002%) for autosomal dominant).
* Background: Rarity or absence in the general population is not robust evidence for pathogenicity, particularly for autosomal recessive disorders. However, the ACMG/AMP Guidelines were devised in such a way that absence or rarity were considered moderate evidence towards pathogenicity, and the framework requires multiple pieces of evidence to classify a variant as likely pathogenic or pathogenic.

## PM2 — Very Strong

Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.

Applicability: Not Applicable for this VCEP



## PM3 — Moderate

For recessive disorders, detected in trans with a pathogenic variant
Note: This requires testing of parents (or offspring) to determine phase.

Applicability: Applicable with VCEP specification

1 point awarded from tables 7a and 7b.
Example: Detected in trans with a pathogenic variant (recessive).

## PM3 — Stand Alone

For recessive disorders, detected in trans with a pathogenic variant
Note: This requires testing of parents (or offspring) to determine phase.

Applicability: Not Applicable for this VCEP



## PM3 — Strong

For recessive disorders, detected in trans with a pathogenic variant
Note: This requires testing of parents (or offspring) to determine phase.

Applicability: Applicable with VCEP specification

2 points awarded from tables 7a and 7b
Example: Detected in trans in 2 probands with a pathogenic variant (recessive).

## PM3 — Supporting

For recessive disorders, detected in trans with a pathogenic variant
Note: This requires testing of parents (or offspring) to determine phase.

Applicability: Applicable with VCEP specification

0.5 points awarded from tables 7a and 7b
Examples: Two variants that meet PM2_Supporting detected in trans; OR
a homozygous variant meeting PM2_Supporting.

## PM3 — Very Strong

For recessive disorders, detected in trans with a pathogenic variant
Note: This requires testing of parents (or offspring) to determine phase.

Applicability: Applicable with VCEP specification

4 points awarded from tables 7a and 7b
Example: Detected in trans in ≥4 probands with a pathogenic variant (recessive).

## PM4 — Moderate

Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

Applicability: Applicable with VCEP specification

Protein length change due to an in-frame deletion or insertion that are not located in repetitive regions.
* No changes. Follow recommendations as outlined in ACMG/AMP guidelines and/or Sequence Variant Interpretation working group.

## PM4 — Stand Alone

Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

Applicability: Not Applicable for this VCEP



## PM4 — Strong

Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

Applicability: Not Applicable for this VCEP



## PM4 — Supporting

Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

Applicability: Not Applicable for this VCEP



## PM4 — Very Strong

Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

Applicability: Not Applicable for this VCEP



## PM5 — Moderate

Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

Applicability: Applicable with VCEP specification

Missense change at same codon as another pathogenic missense variant.
No changes. Follow recommendations as outlined in ACMG/AMP guidelines and/or Sequence Variant Interpretation working group.

## PM5 — Stand Alone

Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

Applicability: Not Applicable for this VCEP



## PM5 — Strong

Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

Applicability: Applicable with VCEP specification

Missense change at same codon as two different pathogenic missense variants.
* Located at an amino acid residue with known pathogenic variation (at least 2 other variants at the same site meet pathogenic criteria for based on independent data)
* Caveat: Assess whether the variants in question could have an impact at the DNA level, such as through splicing impacts.

## PM5 — Supporting

Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

Applicability: Not Applicable for this VCEP



## PM5 — Very Strong

Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

Applicability: Not Applicable for this VCEP



## PM6 — Moderate

Assumed de novo, but without confirmation of paternity and maternity.

Applicability: Applicable with VCEP specification

See PS2 above

## PM6 — Stand Alone

Assumed de novo, but without confirmation of paternity and maternity.

Applicability: Not Applicable for this VCEP



## PM6 — Strong

Assumed de novo, but without confirmation of paternity and maternity.

Applicability: Not Applicable for this VCEP



## PM6 — Supporting

Assumed de novo, but without confirmation of paternity and maternity.

Applicability: Not Applicable for this VCEP



## PM6 — Very Strong

Assumed de novo, but without confirmation of paternity and maternity.

Applicability: Not Applicable for this VCEP



## PP1 — Moderate

Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.

Applicability: Applicable with VCEP specification

Segregation in two affected relatives for recessive and 4 affected relatives for dominant.

## PP1 — Stand Alone

Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.

Applicability: Not Applicable for this VCEP



## PP1 — Strong

Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.

Applicability: Applicable with VCEP specification

Segregation in three affected relatives for recessive and five affected relatives for dominant.

## PP1 — Supporting

Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.

Applicability: Applicable with VCEP specification

Segregation in one affected relative for recessive and two affected relatives for dominant.

## PP1 — Very Strong

Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.

Applicability: Not Applicable for this VCEP



## PP2 — Moderate

Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

Applicability: Not Applicable for this VCEP



## PP2 — Stand Alone

Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

Applicability: Not Applicable for this VCEP



## PP2 — Strong

Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

Applicability: Not Applicable for this VCEP



## PP2 — Supporting

Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

Applicability: Not Applicable for this VCEP



## PP2 — Very Strong

Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

Applicability: Not Applicable for this VCEP



## PP3 — Moderate

Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

Applicability: Not Applicable for this VCEP



## PP3 — Stand Alone

Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

Applicability: Not Applicable for this VCEP



## PP3 — Strong

Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

Applicability: Not Applicable for this VCEP



## PP3 — Supporting

Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

Applicability: Applicable with VCEP specification

REVEL score ≥0.7, or predicted impact to splicing using MaxEntScan.
* Use REVEL and MAXENTSCAN.
 * For missense variants, award PP3 if REVEL score is ≥0.7.
 * If splicing is predicted to be impacted, either creation of a cryptic splice site, or disruption of a native splice site, award PP3.
* For splice variants (except for canonical -/+1 or 2), use MAXENTSCAN.
 * For -/+ 1 or 2 splice variants, do not use PP3 if you are using PVS1.

## PP3 — Very Strong

Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

Applicability: Not Applicable for this VCEP



## PP4 — Moderate

Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.

Applicability: Not Applicable for this VCEP



## PP4 — Stand Alone

Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.

Applicability: Not Applicable for this VCEP



## PP4 — Strong

Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.

Applicability: Not Applicable for this VCEP



## PP4 — Supporting

Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.

Applicability: Applicable with VCEP specification

Patient's phenotype highly specific for gene or fully sequenced gene set (see specifications in Table 7).

## PP4 — Very Strong

Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.

Applicability: Not Applicable for this VCEP



## PP5 — Moderate

Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

Applicability: Not Applicable for this VCEP



## PP5 — Stand Alone

Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

Applicability: Not Applicable for this VCEP



## PP5 — Strong

Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

Applicability: Not Applicable for this VCEP



## PP5 — Supporting

Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

Applicability: Not Applicable for this VCEP



## PP5 — Very Strong

Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

Applicability: Not Applicable for this VCEP



## PS1 — Moderate

Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

Applicability: Not Applicable for this VCEP



## PS1 — Stand Alone

Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

Applicability: Not Applicable for this VCEP



## PS1 — Strong

Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

Applicability: Applicable with VCEP specification

Same amino acid change as an established pathogenic variant; OR
splice variants at same nucleotide and with similar impact prediction as previously reported pathogenic variant.
* Established variant must meet criteria for pathogenicity by the HL specifications
 * Can also use PS1 for splice variants located in the splice consensus sequence, at the same nucleotide position as a previously reported pathogenic variant
  * Example: c.105+1G>C is known to be pathogenic, can use PS1 for c.105+1G>T
* No additional hearing loss specifications for missense variants. Follow recommendations as outlined in Richard 2015 and/or the Sequence Variant Interpretation working group within ClinGen.

* Caveat (from ACMG/AMP guidelines): Assess the possibility that the variant may act directly through the DNA change (e.g. through splicing disruption as assessed by at least computational analysis) instead of through the amino acid change)

## PS1 — Supporting

Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

Applicability: Not Applicable for this VCEP



## PS1 — Very Strong

Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

Applicability: Not Applicable for this VCEP



## PS2 — Moderate

De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

Applicability: Applicable with VCEP specification

1 point per tables 5a and 5b:
Examples: 1 proven de novo occurrence (phenotype consistent but not specific to gene); OR
1 assumed de novo occurrence; OR 2 assumed de novo occurrences (phenotype/gene not specific).

## PS2 — Stand Alone

De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

Applicability: Not Applicable for this VCEP



## PS2 — Strong

De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

Applicability: Applicable with VCEP specification

2 points per tables 5a and 5b:
Examples: 1 proven de novo occurrence; OR 2 assumed de novo occurrences.

## PS2 — Supporting

De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

Applicability: Applicable with VCEP specification

0.5 points per tables 5a and 5b:
Example: 1 assumed de novo occurrence (phenotype/gene not specific).

## PS2 — Very Strong

De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

Applicability: Applicable with VCEP specification

4 points per tables 5a and 5b:
Examples: 2 proven de novo occurrences; OR 1 proven + 2 assumed de novo occurrences; OR
4 assumed de novo occurrences.

## PS3 — Moderate

Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

Applicability: Applicable with VCEP specification

Validated functional studies show a deleterious effect (predefined list): GJB2: electrical coupling assays, dye transfer assays → PS3_Moderate
* Dye Transfer Assays: Expect results that compare the fluorescence of a variant-transfected cell to
both a negative control (or H2O injected control) and a wildtype-transfected cell. PS3_Moderate
would be applied if the variant results in no dye transfer or significantly different dye transfer when
compared to the wildtype.
* Electrical Coupling Assays: Expect results comparing the current of the variant-transfected cells to both a negative control (i.e. H2O injected control) and a wildtype-transfected cell. PS3_Moderate would be applied if the variant results in significantly different current compared to the wildtype, and the current is comparable to background levels/negative control.

## PS3 — Stand Alone

Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

Applicability: Not Applicable for this VCEP



## PS3 — Strong

Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

Applicability: Applicable with VCEP specification

Knock-in mouse model demonstrates the phenotype.

## PS3 — Supporting

Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

Applicability: Applicable with VCEP specification

SLC26A4: Radio isotope and fluorescence assays → PS3_Supporting
* Radio Isotope Assays: PS3_Supporting would be applied when cells transfected with mutant SLC26A4 show a statistically significant decreased efflux of iodide compared to wildtype pendrin.
* Fluorescence Assays: PS3_Supporting would be applied when a cell transfected with the mutant SLC26A4 shows a statistically significant difference in fluorescence (ΔFmax %) compared to the wildtype protein, and when the fluorescence is not significantly different from that of an empty vector control.
COCH: Localization, secretion, and dimerization studies performed using immunofluorescence and
Western blotting techniques →PS3_Supporting
* Localization: PS3_Supporting would be applied if the mutant cochlin protein does not aggregate into extracellular deposits or in the perinuclear region, comparable to the localization of wildtype cochlin.
* Secretion: PS3_Supporting would be applied if cochlin protein containing the variant does not show secretion from transfected cells, but aggregates in cell regions such as the ER, Golgi and nucleus or is degraded.
* Dimerization: In a non-reducing environment, wildtype cochlin migrate quickly and appear smaller than in the reduced state because the structure is maintained by disulfide bonds. PS3_Supporting would be applied if the cochlin protein containing the variant forms more, or less, stable disulfide bonds when compared to the wildtype in non-reducing conditions.
* If not listed above, OK to use PS3_Supporting for other genes/functional analyses if
  * The assay has been validated by a known pathogenic and benign variant AND  
  * There is plausible reason that the function the assay is testing relates to the phenotype AND
  * The assay conditions are likely to mimic the physiological environment.

## PS3 — Very Strong

Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

Applicability: Not Applicable for this VCEP



## PS4 — Moderate

The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.
Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.
Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.

Applicability: Applicable with VCEP specification

Autosomal dominant: ≥6 probands with variant, and variant meets PM2_Supporting.

## PS4 — Stand Alone

The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.
Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.
Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.

Applicability: Not Applicable for this VCEP



## PS4 — Strong

The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.
Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.
Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.

Applicability: Applicable with VCEP specification

Fisher Exact or Chi-Squared analysis shows statistical increase in cases over controls, OR
Autosomal dominant: ≥15 probands with variant, and variant meets PM2_Supporting.

## PS4 — Supporting

The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.
Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.
Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.

Applicability: Applicable with VCEP specification

Autosomal dominant: ≥2 probands with variant, and variant meets PM2_Supporting.

## PS4 — Very Strong

The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.
Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.
Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.

Applicability: Not Applicable for this VCEP



## PVS1 — Moderate

Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.

Applicability: Applicable with VCEP specification

See PVS1 flowchart for PVS1_Moderate variants in gene where LOF is a known mechanism of disease.

## PVS1 — Stand Alone

Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.

Applicability: Not Applicable for this VCEP



## PVS1 — Strong

Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.

Applicability: Applicable with VCEP specification

See PVS1 flow chart for PVS1_Strong variants in gene where LOF is a known mechanism of disease.
* PVS1 should also be considered for the following genes with variants assessed in the Hearing Loss Variant Pilot: GJB2, CDH23, USH2A, SLC26A4, MYO6, MYO7A, TECTA, KCNQ4.
* For other genes, LOF must be an established disease mechanism, and the gene/disease association must be Strong or Definitive clinical validity level as outlined in Strande et al. 2017 (PMID: 28552198).
* If above criteria is met, follow PVS1 flowchart as recommended by the SVI.

## PVS1 — Supporting

Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.

Applicability: Applicable with VCEP specification

See PVS1 flowchart for PVS1_Supporting variants in gene where LOF is a known mechanism of disease.

## PVS1 — Very Strong

Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.

Applicability: Applicable with VCEP specification

Null variant in a gene with established LOF as a disease mechanism; see PVS1_Strong, PVS1_Moderate, PVS1_Supporting for reduced evidence applications.

# VHL

Document: ClinGen VHL Expert Panel Specifications to the ACMG/AMP Variant Interpretation Guidelines for VHL Version 1.1
CSpec ID: GN078
VCEP: VHL Variant Curation Expert Panel
Version: 1.1
Status: current_released
Diseases: MONDO:0008667
Modes of inheritance: https://hpo.jax.org/app/browse/term/HP:0000006
Fetched: 2026-08-05T00:33:07.336464+00:00
Source API: https://cspec.genome.network/cspec/api/SequenceVariantInterpretation/id/GN078

## BA1 — Moderate

Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

Applicability: Not Applicable for this VCEP



## BA1 — Stand Alone

Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

Applicability: Applicable

Use a BA1 cut off of >=0.000156 (0.0156%) GroupMax Filtering Allele Frequency in gnomAD (based on gnomAD v4 release).

## BA1 — Strong

Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

Applicability: Not Applicable for this VCEP



## BA1 — Supporting

Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

Applicability: Not Applicable for this VCEP



## BA1 — Very Strong

Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

Applicability: Not Applicable for this VCEP



## BP1 — Moderate

Missense variant in a gene for which primarily truncating variants are known to cause disease.

Applicability: Not applicable



## BP1 — Stand Alone

Missense variant in a gene for which primarily truncating variants are known to cause disease.

Applicability: Not applicable



## BP1 — Strong

Missense variant in a gene for which primarily truncating variants are known to cause disease.

Applicability: Not applicable



## BP1 — Supporting

Missense variant in a gene for which primarily truncating variants are known to cause disease.

Applicability: Not applicable



## BP1 — Very Strong

Missense variant in a gene for which primarily truncating variants are known to cause disease.

Applicability: Not applicable



## BP2 — Moderate

Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.

Applicability: Not Applicable



## BP2 — Stand Alone

Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.

Applicability: Not Applicable for this VCEP



## BP2 — Strong

Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.

Applicability: Applicable

i) -variant observed in trans with a known pathogenic variant (phase confirmed), in the absence of congenital polycythemia (clinical manifestations or molecular)

ii) -OR observed in the homozygous state in an individual without personal &/or family history of Von Hippel-Lindau disease or congenital polycythemia

iii) -OR observed _in cis_ or with unknown phase with three or more different pathogenic _VHL_ variants

## BP2 — Supporting

Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.

Applicability: Applicable

\-variant is observed _in cis_ (or phase is unknown) w/ a pathogenic _VHL_ variant

## BP2 — Very Strong

Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.

Applicability: Not Applicable for this VCEP



## BP3 — Moderate

In frame-deletions/insertions in a repetitive region without a known function.

Applicability: Not Applicable



## BP3 — Stand Alone

In frame-deletions/insertions in a repetitive region without a known function.

Applicability: Not applicable



## BP3 — Strong

In frame-deletions/insertions in a repetitive region without a known function.

Applicability: Not Applicable



## BP3 — Supporting

In frame-deletions/insertions in a repetitive region without a known function.

Applicability: Applicable

BP3 can be applied to the 8x GXEEX AA repeat motif in the 5’ end of VHL p30 (AA14-AA48). Otherwise, the rest of the coding regions in VHL do not contain repeats (and none contain LINE/SINE, low complexity or other repeat types as identified by RepeatMasker) and BP3 is not applicable.

## BP3 — Very Strong

In frame-deletions/insertions in a repetitive region without a known function.

Applicability: Not applicable



## BP4 — Moderate

Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.

Applicability: Not Applicable



## BP4 — Stand Alone

Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.

Applicability: Not Applicable for this VCEP



## BP4 — Strong

Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.

Applicability: Not Applicable



## BP4 — Supporting

Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.

Applicability: Applicable

Due to the lack of benign variants, and the drop in classification accuracy for benign VHL variants, missense predictors should not be used to assign the BP4 evidence code. 

BP4 can be applied to assess lack of splicing impact, with concordance of Splice AI (≤0.1) and VarSeak (Class 1 or Class 2).

## BP4 — Very Strong

Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.

Applicability: Not Applicable for this VCEP



## BP5 — Moderate

Variant found in a case with an alternate molecular basis for disease.

Applicability: Not Applicable



## BP5 — Stand Alone

Variant found in a case with an alternate molecular basis for disease.

Applicability: Not applicable



## BP5 — Strong

Variant found in a case with an alternate molecular basis for disease.

Applicability: Not Applicable



## BP5 — Supporting

Variant found in a case with an alternate molecular basis for disease.

Applicability: Applicable

BP5 can be applied for two or more co-occurrences with pathogenic variants in a different gene that fully explained the patient's phenotype, but specific circumstances would need to be met in order for a case to be considered for inclusion. First, the variant in the other gene must be considered highly penetrant, with both the individual's age, tumour type and gender taken into consideration. Additionally, the patient's personal and family history (including up to 2nd degree relatives) should not overlap with features seen in VHL and VHL tumour histologies. As an example, an individual with a personal and family history of pheochromocytoma who harbored a _VHL_ variant in addition to a pathogenic SDHB variant BP5 would not apply, because pheochromocytoma is a known risk in VHL and the _VHL_ variant might have contributed to this individual's pheochromocytoma cancer risk. However, an individual with a personal and family history of chromophobic RCC who was positive for a _VHL_ variant as well as a pathogenic FLCN variant would be considered for BP5 application, as non-clear cell RCC is not associated with VHL disease.

## BP5 — Very Strong

Variant found in a case with an alternate molecular basis for disease.

Applicability: Not applicable



## BP6 — Moderate

Reputable source recently reports variant as benign, but the evidence is not available to the laboratory to perform an independent evaluation.

Applicability: Not Applicable for this VCEP



## BP6 — Stand Alone

Reputable source recently reports variant as benign, but the evidence is not available to the laboratory to perform an independent evaluation.

Applicability: Not Applicable for this VCEP



## BP6 — Strong

Reputable source recently reports variant as benign, but the evidence is not available to the laboratory to perform an independent evaluation.

Applicability: Not Applicable for this VCEP



## BP6 — Supporting

Reputable source recently reports variant as benign, but the evidence is not available to the laboratory to perform an independent evaluation.

Applicability: Not Applicable for this VCEP



## BP6 — Very Strong

Reputable source recently reports variant as benign, but the evidence is not available to the laboratory to perform an independent evaluation.

Applicability: Not Applicable for this VCEP



## BP7 — Moderate

A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.

Applicability: Not Applicable



## BP7 — Stand Alone

A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.

Applicability: Not Applicable for this VCEP



## BP7 — Strong

A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.

Applicability: Not Applicable



## BP7 — Supporting

A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.

Applicability: Applicable

To evaluate splice prediction, use the BP4 code. If BP4 is met for lack of splice effect, BP7 can be applied to silent or intronic variants where the PhyloP score is ≤0.2.

## BP7 — Very Strong

A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.

Applicability: Not Applicable for this VCEP



## BS1 — Moderate

Allele frequency is greater than expected for disorder.

Applicability: Not Applicable



## BS1 — Stand Alone

Allele frequency is greater than expected for disorder.

Applicability: Not Applicable



## BS1 — Strong

Allele frequency is greater than expected for disorder.

Applicability: Applicable

Use BS1 cut off of  >=0.0000156 (0.00156%) GroupMax Filtering Allele Frequency in gnomAD (based on gnomAD v4).

## BS1 — Supporting

Allele frequency is greater than expected for disorder.

Applicability: Not Applicable



## BS1 — Very Strong

Allele frequency is greater than expected for disorder.

Applicability: Not Applicable for this VCEP



## BS2 — Moderate

Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

Applicability: Not Applicable



## BS2 — Stand Alone

Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

Applicability: Not Applicable for this VCEP



## BS2 — Strong

Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

Applicability: Applicable

VHL is not highly penetrant _at an early age._ BS2 can be applied if: There are at least 3 individuals, all >=65yo, unaffected, harboring the same variant, _**with full phenotyping and screening**_ for the absence of VHL-related cancers.

## BS2 — Supporting

Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

Applicability: Applicable

VHL is not highly penetrant _at an early age._ BS2\_Supporting can be applied if: At least 3 individuals, all >=65yo, unaffected, harboring the same variant, _**lacking full phenotyping and screening**_, with no noted VHL-related cancers

## BS2 — Very Strong

Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

Applicability: Not Applicable for this VCEP



## BS3 — Moderate

Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

Applicability: Not Applicable



## BS3 — Stand Alone

Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

Applicability: Not Applicable for this VCEP



## BS3 — Strong

Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

Applicability: Not Applicable



## BS3 — Supporting

Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

Applicability: Applicable

• HIF 1/2a assay replicates WT function and/or

• VBC complex stability is not affected and/or 

• ECM formation/fibronectin binding is unaffected 

This rule can be used and weighted as appropriate for functional tests of variants prior to codon 54 (which show the VHL19 product is not impacted). Evidence of benign effect for VHL Type 1 and 2A/B can be seen when HIF1/2a displays degradation (i.e. replicates WT function), and/or the VHL Elongin C, Elongin B, Cullin2 RBX1 (VCB-CR) E3 ubiquitin ligase complex stability is not affected and/or ECM formation/fibronectin binding is unaffected. Note: VHL Type 2C variants typically do not affect HIF1/2a; absence of HIF1/2a alone when testing a suspected VHL Type 2C variant should not be used for BS3. Functional studies of fibronectin and ECM formation are needed for VHL Type 2C. Follow modified SVI guidance for functional assays, general controls and benign controls. For splicing variants (and intronic/synonymous), RNA assays must demonstrate no impact on splicing.

## BS3 — Very Strong

Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

Applicability: Not Applicable for this VCEP



## BS4 — Moderate

Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

Applicability: Not Applicable



## BS4 — Stand Alone

Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

Applicability: Not Applicable for this VCEP



## BS4 — Strong

Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

Applicability: Applicable

Lack of segregation is seen in affected members of ≥2 families

## BS4 — Supporting

Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

Applicability: Applicable

Lack of segregation is seen in 1 family.

## BS4 — Very Strong

Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

Applicability: Not Applicable for this VCEP



## PM1 — Moderate

Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

Applicability: Applicable

Putative missense variants that are known germline hotspots AND/OR in key functional domains AND/OR somatic variants that have ≥10 instances for the same AA in cancerhotspots.org. See the table of Germline and Somatic Hotspots.

## PM1 — Stand Alone

Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

Applicability: Not Applicable for this VCEP



## PM1 — Strong

Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

Applicability: Not Applicable



## PM1 — Supporting

Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

Applicability: Applicable

Putative missense variants seen in somatic databases, having \<10 instances for the same AA in cancerhotspots.org. See the table of Germline and Somatic Hotspots.

## PM1 — Very Strong

Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

Applicability: Not Applicable for this VCEP



## PM2 — Moderate

Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.

Applicability: Not Applicable



## PM2 — Stand Alone

Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.

Applicability: Not Applicable for this VCEP



## PM2 — Strong

Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.

Applicability: Not Applicable for this VCEP



## PM2 — Supporting

Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.

Applicability: Applicable

PM2\_Supporting can be applied for variants either absent from gnomAD or with \<= 0.00000156 (0.000156%) GroupMax Filtering Allele Frequency in gnomAD (based on gnomAD v4 release). If no GroupMax Filtering Allele Frequency is calculated (ex. due to a single variant present), PM2\_Supporting may also be applied.

## PM2 — Very Strong

Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.

Applicability: Not Applicable for this VCEP



## PM3 — Moderate

For recessive disorders, detected in trans with a pathogenic variant
Note: This requires testing of parents (or offspring) to determine phase.

Applicability: Not applicable



## PM3 — Stand Alone

For recessive disorders, detected in trans with a pathogenic variant
Note: This requires testing of parents (or offspring) to determine phase.

Applicability: Not applicable



## PM3 — Strong

For recessive disorders, detected in trans with a pathogenic variant
Note: This requires testing of parents (or offspring) to determine phase.

Applicability: Not applicable



## PM3 — Supporting

For recessive disorders, detected in trans with a pathogenic variant
Note: This requires testing of parents (or offspring) to determine phase.

Applicability: Not applicable



## PM3 — Very Strong

For recessive disorders, detected in trans with a pathogenic variant
Note: This requires testing of parents (or offspring) to determine phase.

Applicability: Not applicable



## PM4 — Moderate

Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

Applicability: Applicable

In-frame insertion / deletions in the B and alpha domains and stop-loss variants adding significant additional amino acids to VHL [<sup>15</sup>](#pmid_20560986) cites multiple pathogenic cases and experimental evidence of stop loss extensions in VHL that are associated with Type 2A VHL disease).  The functional domains are: Beta (β) domain (AA 63 - 155, Nuclear Export), Alpha (ɑ) domain (AA 156-192, Elongin C binding), and Second Beta (β) domain (AA 193-204). 

PM4 does not apply to in-frame indels prior to codon 54 that do not alter the Met54 VHL p19 codon and beyond.

## PM4 — Stand Alone

Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

Applicability: Not Applicable for this VCEP



## PM4 — Strong

Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

Applicability: Not Applicable



## PM4 — Supporting

Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

Applicability: Not Applicable



## PM4 — Very Strong

Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

Applicability: Not Applicable for this VCEP



## PM5 — Moderate

Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

Applicability: Applicable

Pathogenicity of prior variant is established by interpretation of the VHL VCEP or variants with pathogenicity established using VHL VCEP specifications. The Grantham distance should be used to compare variants. The variant under consideration must be equal or a larger distance than the classified pathogenic variant (Grantham, 1974, Table 2 [<sup>16</sup>](#pmid_4843792) ). Splice metapredictors should be used to ensure the variant is not predicted to have an effect on splicing.

## PM5 — Stand Alone

Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

Applicability: Not Applicable for this VCEP



## PM5 — Strong

Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

Applicability: Not Applicable



## PM5 — Supporting

Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

Applicability: Not Applicable



## PM5 — Very Strong

Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

Applicability: Not Applicable for this VCEP



## PM6 — Moderate

Assumed de novo, but without confirmation of paternity and maternity.

Applicability: Applicable

See PS2 evidence code for scoring and phenotypes. Assumed _de novo_ receives half the points as compared to maternity and paternity confirmed _de novo_. If paternity and maternity are not confirmed, score as the PM6 code. PM6 can receive “VeryStrong” strength. For example, if there are >4 de novo probands with Danish Criteria and none have paternity confirmed, this can receive PM6\_VeryStrong. Note: the VCI as of Nov 2022 does not allow PM6\_VeryStrong. Instead apply the PS2 evidence code and increase the strength to “VeryStrong” with a note that paternity and/or maternity is not confirmed.

## PM6 — Stand Alone

Assumed de novo, but without confirmation of paternity and maternity.

Applicability: Not applicable



## PM6 — Strong

Assumed de novo, but without confirmation of paternity and maternity.

Applicability: Not Applicable



## PM6 — Supporting

Assumed de novo, but without confirmation of paternity and maternity.

Applicability: Not Applicable



## PM6 — Very Strong

Assumed de novo, but without confirmation of paternity and maternity.

Applicability: Not applicable



## PP1 — Moderate

Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.

Applicability: Applicable

5 – 6 meioses across ≥1 family.

## PP1 — Stand Alone

Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.

Applicability: Not Applicable for this VCEP



## PP1 — Strong

Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.

Applicability: Applicable

\>7 meioses across >=2 families

## PP1 — Supporting

Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.

Applicability: Applicable

3 – 4 meioses across ≥1 family.

## PP1 — Very Strong

Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.

Applicability: Not Applicable for this VCEP



## PP2 — Moderate

Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

Applicability: Not applicable



## PP2 — Stand Alone

Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

Applicability: Not applicable



## PP2 — Strong

Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

Applicability: Not applicable



## PP2 — Supporting

Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

Applicability: Not applicable



## PP2 — Very Strong

Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

Applicability: Not applicable



## PP3 — Moderate

Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

Applicability: Not Applicable



## PP3 — Stand Alone

Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

Applicability: Not Applicable for this VCEP



## PP3 — Strong

Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

Applicability: Not Applicable



## PP3 — Supporting

Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

Applicability: Applicable

For missense variants, use REVEL score >=0.664. 

For splice variants, concordance of Splice AI (>0.5) and VarSeak (class 4 or class 5).

## PP3 — Very Strong

Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

Applicability: Not Applicable for this VCEP



## PP4 — Moderate

Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.

Applicability: Not applicable



## PP4 — Stand Alone

Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.

Applicability: Not applicable



## PP4 — Strong

Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.

Applicability: Not applicable



## PP4 — Supporting

Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.

Applicability: Not applicable



## PP4 — Very Strong

Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.

Applicability: Not applicable



## PP5 — Moderate

Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

Applicability: Not Applicable for this VCEP



## PP5 — Stand Alone

Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

Applicability: Not Applicable for this VCEP



## PP5 — Strong

Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

Applicability: Not Applicable for this VCEP



## PP5 — Supporting

Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

Applicability: Not Applicable for this VCEP



## PP5 — Very Strong

Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

Applicability: Not Applicable for this VCEP



## PS1 — Moderate

Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

Applicability: Not Applicable



## PS1 — Stand Alone

Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

Applicability: Not Applicable for this VCEP



## PS1 — Strong

Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

Applicability: Applicable

Applied only to variants with interpretation by the VHL VCEP or by a variant with pathogenicity established using VHL VCEP specifications.

## PS1 — Supporting

Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

Applicability: Not Applicable



## PS1 — Very Strong

Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

Applicability: Not Applicable for this VCEP



## PS2 — Moderate

De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

Applicability: Applicable

Phenotype consistent but not highly specific. Ex. VHL spectrum cancer without family history or strong indication of VHL phenotype. (≥1 but less than 2 _de novo_ points)

## PS2 — Stand Alone

De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

Applicability: Not Applicable for this VCEP



## PS2 — Strong

De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

Applicability: Applicable

Phenotype highly specific for the gene (Danish Criteria) (≥2 but less than 4 _de novo_ points).

## PS2 — Supporting

De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

Applicability: Applicable

Phenotype consistent but not highly specific (≥0.5 but less than 1 _de novo_ points) Ex. subject included in a VHL cohort, but specific information on tumor types is not provided.

## PS2 — Very Strong

De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

Applicability: Applicable

A single proband cannot be very strong evidence, but multiple probands can be combined to reach very strong (4+ points).

## PS3 — Moderate

Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

Applicability: Not Applicable



## PS3 — Stand Alone

Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

Applicability: Not Applicable for this VCEP



## PS3 — Strong

Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

Applicability: Not Applicable



## PS3 — Supporting

Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

Applicability: Applicable

Acceptable assays that display functional effect in VHL are the following:  

• HIF 1/2a degradation assays -- HIF1/2a is not degraded and/or 

• VBC complex stability is affected and/or

• Pathogenicity supported by abnormal ECM formation and impaired fibronectin binding [<sup>1</sup>](#pmid_9651579) , [<sup>2</sup>](#pmid_11331613) , [<sup>3</sup>](#pmid_11358843) , [<sup>17</sup>](#pmid_14706840)

Multiple studies and publications confirm the role of VHL in HIF1/2a regulation and VBC complex stability for VHL Type 1, and 2A/B, as well as fibronectin binding/deposition and assays evaluating extra-cellular matrix composition. In-vitro assays should display total loss of HIF1/2a degradation (i.e. HIF1/2a presence) for VHL Type 1, and 2A/B.  VHL Type 2C should display presence of HIF1/2a (with VBC complex stability variably affected and fibronectin deposition/extra cellular matrix composition affected). These assays are typically performed in Renal Cell Carcinoma (RCC) cells lacking VHL, introducing normal pVHL as a control in addition to a variant-VHL, then comparing HIF1/2a levels to WT pVHL. Brnich et al proposed 10 controls to achieve PS3\_Supporting and 11 for PS3\_Moderate [<sup>10</sup>](#pmid_31892348). We propose to _follow the workflow outlined in Brnich et al._  Type 2C VHL variants are typically missense variants in the alpha domain of VHL, and do not usually affect HIF1/2a. If HIF1/2a maintains presence and VHL Type 2C is suspected, assays evaluating fibronectin deposition or extracellular matrix assembly should be used. 

**SPLICING:** **PS3:** RNA transcripts carrying splicing mutation display splicing defects in patient cells. **PS3\_Moderate**: RNA transcripts carrying splicing mutation display splicing defects in in-vivo or in-vitro assays.   **Functional Assay Documentation** : [https://drive.google.com/file/d/1w8P8zs1fHUolaAYmBL1jw-vcjsX3N_yh/view?usp=sharing](https://drive.google.com/file/d/1w8P8zs1fHUolaAYmBL1jw-vcjsX3N_yh/view?usp=sharing)

## PS3 — Very Strong

Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

Applicability: Not Applicable



## PS4 — Moderate

The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.
Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.
Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.

Applicability: Applicable

**2 – 4 points the PS4 cut-off and Proband Scoring Tables from a mix of any of the following phenotypes: specific, consistent and nonspecific.**

## PS4 — Stand Alone

The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.
Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.
Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.

Applicability: Not Applicable for this VCEP



## PS4 — Strong

The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.
Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.
Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.

Applicability: Applicable

**5-15 points the PS4 cut-off and Proband Scoring Tables from a mix of any of the following phenotypes: specific, consistent and nonspecific.**

## PS4 — Supporting

The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.
Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.
Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.

Applicability: Applicable

**1 point the PS4 cut-off and Proband Scoring Tables from a mix of any of the following phenotypes: specific, consistent and nonspecific.**

## PS4 — Very Strong

The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.
Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.
Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.

Applicability: Applicable

**16+ points the PS4 cut-off and Proband Scoring Tables from a mix of any of the following phenotypes: specific, consistent and nonspecific.**

## PVS1 — Moderate

Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.

Applicability: Not Applicable



## PVS1 — Stand Alone

Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.

Applicability: Not Applicable for this VCEP



## PVS1 — Strong

Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.

Applicability: Not Applicable



## PVS1 — Supporting

Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.

Applicability: Not Applicable



## PVS1 — Very Strong

Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.

Applicability: Applicable

**LINK TO PVS1 DECISION TREE DOCUMENT:** [**https://drive.google.com/file/d/1mGfChgxbGVbzYn6Ggmb9rYvoGGah25ll/view?usp=sharing**](https://drive.google.com/file/d/1mGfChgxbGVbzYn6Ggmb9rYvoGGah25ll/view?usp=sharing)

**Do not apply PVS1 for truncations that occur prior to Codon 54 (including frameshift events that start and end prior to Codon 54 but the truncation extends beyond Codon 54.)**

**Note1: Exon presence in biologically relevant transcripts:** In some transcripts exon 2 of _VHL_ is skipped and expressed at low levels. The function of this transcript is not fully known. Exon 2 comprises almost the entirety of the nuclear export function region of the Beta domain and is critical for known VHL function. Exon 1 contains the only initiator codons in _VHL_. Exon 3 contains the elongin binding function. _**All exons should be considered as "present in biologically relevant transcripts" in the PVS1 decision tree.**_

**Note 2: The 10% PVS1 downgrade to Moderate cannot apply to VHL** because of the small size.

**Nonsense Mediated Decay** [<sup>5</sup>](#pmid_22825683) [<sup>4</sup>](#pmid_20145706)  **NMD experimental evidence in 1st exon after codon 54 and to 5' region of 2nd exon (codon 138)**.\*\*

**Critical Domains:**

1st Beta (β) domain (63-154), especially Nuclear Export (114-155)

Alpha (ɑ) domain (155-192), especially Elongin C binding (157 - 172)

Second Beta domain (193-204)   

_Truncating variants after Met54 and predicted to undergo NMD (from AA55-AA136/c.408) or in the beta or alpha domains can receive PVS1, and those outside the second Beta domain (205-213) can receive PVS1\_Moderate downgrade to account for minimal loss of VHL protein. Notably a frame shift deletion at 205 is pathogenic in ClinVar (ID 18971) as are stop loss extension variants in the last codons (see PM4)._

**SPLICE: If any canonical exon is skipped, the variant receives PVS1.** If a cryptic splice disrupts the reading frame, and is in a critical domain (AA63-AA204) or is predicted to undergo NMD (AA55-AA136) it receives PVS1. If it is outside a critical domain and predicted to undergo NMD (AA55-62), it receives PVS1\_Strong (the second site outside of critical domains AA205-213 is not predicted to undergo NMD). If a cryptic splice does not alter the reading frame, and is in a critical domain (AA 63-204), it can receive PVS1\_Strong, and if it is outside the critical domain (AA 205-213) or  in an NMD prediction (AA 55-62), it receives PVS1\_Moderate. Note:  There is a cryptic exon (E1) in intron 1 [<sup>7</sup>](#pmid_31996412) [<sup>6</sup>](#pmid_29891534), and silent variants in exon 2 that are reported to cause skipping of exon 1. If there is functional evidence of exon skipping (RNA splice assay) then PVS1 can apply. Do not double count evidence. Ex. PVS1 should be used in place of PS3 functional evidence confirming splice alteration, but PS3 evidence code could still apply to other relevant assays confirming effect on HIF1/2a presence etc. 

**EXON DELETION:** SVI PVS1 decision tree modified for whole exon deletions. There are only 3 exons in _VHL_ and each has an important functional domain. Any exon deletion of _VHL_ receives PVS1. 

**EXON DUPLICATION:** Follow PVS1 decision tree. Note: few pathogenic exon duplications are reported in ClinVar.   (ID:417571, ID:584137). These have no literature cited. 

**INITIATION CODON:** VHL Met 1 (in VHL p30) truncation or missense would not affect VHL p19, as VHL has a second start at codon 54 (VHL p19), it cannot be scored in the PVS1 decision tree. After that, no other viable alternative starts are known. Start loss at codon 54 would presumably result in an impact, as VHL p30 and p19 would be truncated prior to any known functional domains (PVS1). Ong 2007 has 1 family (2 subjects) with Met54X and reports cerebellar hemangioblastomas. There is no functional study in the paper for this variant. Olschwang et al 1998 VHL Type 2A, one subject with 161insT (FS result). There is no functional study in the paper. Missense at Met 54 (VHL p19 initiation codon) would presumably not result in as strong an impact as the full length VHL p30 would still be produced (PVS1 decision tree = N/A). ClinVar has M54T (ID:819688) and M54L (ID:843990). M54T is uncertain, with no other evidence provided. M54L references M54I which segregates in homozygous state with erythrocytosis in individuals of Moroccan descent [<sup>9</sup>](#pmid_26224408) [<sup>8</sup>](#pmid_27578599), and those heterozygous for M54I did not present VHL phenotype [<sup>9</sup>](#pmid_26224408).

# VWF

Document: ClinGen von Willebrand Disease  Expert Panel Specifications to the ACMG/AMP Variant Interpretation Guidelines for VWF Version 1.0
CSpec ID: GN081
VCEP: von Willebrand Disease  Variant Curation Expert Panel
Version: 1.0
Status: current_released
Diseases: MONDO:0015628; MONDO:0015629; MONDO:0015630; MONDO:0013304; MONDO:0024574
Modes of inheritance: https://hpo.jax.org/app/browse/term/HP:0000006; https://hpo.jax.org/app/browse/term/HP:0000005
Fetched: 2026-08-05T00:33:09.930511+00:00
Source API: https://cspec.genome.network/cspec/api/SequenceVariantInterpretation/id/GN081

## BA1 — Moderate

Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

Applicability: Not applicable



## BA1 — Stand Alone

Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

Applicability: Applicable

Appropriate to use for variants with a Popmax MAF of >0.1 in gnomAD.

## BA1 — Strong

Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

Applicability: Not applicable



## BA1 — Supporting

Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

Applicability: Not applicable



## BA1 — Very Strong

Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

Applicability: Not applicable



## BP1 — Moderate

Missense variant in a gene for which primarily truncating variants are known to cause disease.

Applicability: Not applicable



## BP1 — Stand Alone

Missense variant in a gene for which primarily truncating variants are known to cause disease.

Applicability: Not applicable



## BP1 — Strong

Missense variant in a gene for which primarily truncating variants are known to cause disease.

Applicability: Not applicable



## BP1 — Supporting

Missense variant in a gene for which primarily truncating variants are known to cause disease.

Applicability: Not applicable



## BP1 — Very Strong

Missense variant in a gene for which primarily truncating variants are known to cause disease.

Applicability: Not applicable



## BP2 — Moderate

Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.

Applicability: Not applicable



## BP2 — Stand Alone

Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.

Applicability: Not applicable



## BP2 — Strong

Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.

Applicability: Not applicable



## BP2 — Supporting

Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.

Applicability: Not applicable



## BP2 — Very Strong

Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.

Applicability: Not applicable



## BP3 — Moderate

In frame-deletions/insertions in a repetitive region without a known function.

Applicability: Not applicable



## BP3 — Stand Alone

In frame-deletions/insertions in a repetitive region without a known function.

Applicability: Not applicable



## BP3 — Strong

In frame-deletions/insertions in a repetitive region without a known function.

Applicability: Not applicable



## BP3 — Supporting

In frame-deletions/insertions in a repetitive region without a known function.

Applicability: Not applicable



## BP3 — Very Strong

In frame-deletions/insertions in a repetitive region without a known function.

Applicability: Not applicable



## BP4 — Moderate

Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.

Applicability: Not Applicable



## BP4 — Stand Alone

Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.

Applicability: Not applicable



## BP4 — Strong

Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.

Applicability: Not Applicable



## BP4 — Supporting

Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.

Applicability: Applicable

Use for missense variants that have a REVEL score of less than or equal to 0.290 AND SpliceAI cutoff of \<0.1. Use SpliceAI cutoff of \<0.1 for other variant types.

## BP4 — Very Strong

Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.

Applicability: Not applicable



## BP5 — Moderate

Variant found in a case with an alternate molecular basis for disease.

Applicability: Not Applicable



## BP5 — Stand Alone

Variant found in a case with an alternate molecular basis for disease.

Applicability: Not applicable



## BP5 — Strong

Variant found in a case with an alternate molecular basis for disease.

Applicability: Not Applicable



## BP5 — Supporting

Variant found in a case with an alternate molecular basis for disease.

Applicability: Applicable

A second variant in VWF may be considered an alternate molecular basis for disease when that variant is LP/P (as evaluated by the VWD VCEP) and fully explains the phenotype of the patient's reported VWD subtype.

## BP5 — Very Strong

Variant found in a case with an alternate molecular basis for disease.

Applicability: Not applicable



## BP6 — Moderate

Reputable source recently reports variant as benign, but the evidence is not available to the laboratory to perform an independent evaluation.

Applicability: Not applicable

This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee.

## BP6 — Stand Alone

Reputable source recently reports variant as benign, but the evidence is not available to the laboratory to perform an independent evaluation.

Applicability: Not applicable

This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee.

## BP6 — Strong

Reputable source recently reports variant as benign, but the evidence is not available to the laboratory to perform an independent evaluation.

Applicability: Not applicable

This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee.

## BP6 — Supporting

Reputable source recently reports variant as benign, but the evidence is not available to the laboratory to perform an independent evaluation.

Applicability: Not applicable

This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee.

## BP6 — Very Strong

Reputable source recently reports variant as benign, but the evidence is not available to the laboratory to perform an independent evaluation.

Applicability: Not applicable

This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee.

## BP7 — Moderate

A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.

Applicability: Not Applicable



## BP7 — Stand Alone

A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.

Applicability: Not applicable



## BP7 — Strong

A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.

Applicability: Not Applicable



## BP7 — Supporting

A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.

Applicability: Applicable

Use SpliceAI for splicing predictor with a cutoff score of \<0.1.

## BP7 — Very Strong

A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.

Applicability: Not applicable



## BS1 — Moderate

Allele frequency is greater than expected for disorder.

Applicability: Not Applicable



## BS1 — Stand Alone

Allele frequency is greater than expected for disorder.

Applicability: Not Applicable



## BS1 — Strong

Allele frequency is greater than expected for disorder.

Applicability: Applicable

Appropriate to use for variants with a Popmax MAF of >0.01 in gnomAD.

## BS1 — Supporting

Allele frequency is greater than expected for disorder.

Applicability: Not Applicable



## BS1 — Very Strong

Allele frequency is greater than expected for disorder.

Applicability: Not applicable



## BS2 — Moderate

Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

Applicability: Not applicable



## BS2 — Stand Alone

Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

Applicability: Not applicable



## BS2 — Strong

Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

Applicability: Not applicable



## BS2 — Supporting

Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

Applicability: Not applicable



## BS2 — Very Strong

Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

Applicability: Not applicable



## BS3 — Moderate

Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

Applicability: Not applicable



## BS3 — Stand Alone

Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

Applicability: Not applicable



## BS3 — Strong

Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

Applicability: Not applicable



## BS3 — Supporting

Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

Applicability: Not applicable



## BS3 — Very Strong

Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

Applicability: Not applicable



## BS4 — Moderate

Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

Applicability: Not Applicable



## BS4 — Stand Alone

Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

Applicability: Not applicable



## BS4 — Strong

Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

Applicability: Applicable

Appropriate to use when two or more relatives have the phenotype consistent with VWD type 2 without harboring the variant identified in other affected family members. Additionally, there is not another established cause of type 2 VWD (e.g. - there are not multiple type 2 VWD diagnoses) segregating in the family.

## BS4 — Supporting

Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

Applicability: Applicable

Appropriate to use when only one relative has the phenotype consistent with VWD type 2 without harboring the variant identified in other affected family members. Additionally, there is not another established cause of type 2 VWD (e.g. - there are not multiple type 2 VWD diagnoses) segregating in the family.

## BS4 — Very Strong

Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

Applicability: Not applicable



## PM1 — Moderate

Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

Applicability: Not applicable



## PM1 — Stand Alone

Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

Applicability: Not applicable



## PM1 — Strong

Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

Applicability: Not applicable



## PM1 — Supporting

Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

Applicability: Not applicable



## PM1 — Very Strong

Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

Applicability: Not applicable



## PM2 — Moderate

Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.

Applicability: Not Applicable



## PM2 — Stand Alone

Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.

Applicability: Not applicable



## PM2 — Strong

Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.

Applicability: Not applicable



## PM2 — Supporting

Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.

Applicability: Applicable

Use code for variants with a popmax MAF of \<0.0001 in gnomAD.

## PM2 — Very Strong

Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.

Applicability: Not applicable



## PM3 — Moderate

For recessive disorders, detected in trans with a pathogenic variant
Note: This requires testing of parents (or offspring) to determine phase.

Applicability: Not applicable



## PM3 — Stand Alone

For recessive disorders, detected in trans with a pathogenic variant
Note: This requires testing of parents (or offspring) to determine phase.

Applicability: Not applicable



## PM3 — Strong

For recessive disorders, detected in trans with a pathogenic variant
Note: This requires testing of parents (or offspring) to determine phase.

Applicability: Not applicable



## PM3 — Supporting

For recessive disorders, detected in trans with a pathogenic variant
Note: This requires testing of parents (or offspring) to determine phase.

Applicability: Not applicable



## PM3 — Very Strong

For recessive disorders, detected in trans with a pathogenic variant
Note: This requires testing of parents (or offspring) to determine phase.

Applicability: Not applicable



## PM4 — Moderate

Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

Applicability: Applicable

Use with no specification for type 2A and 2M. This rule code is not applicable to variants associated with type 2B disease, since type 2B is only associated with gain of function variants.

## PM4 — Stand Alone

Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

Applicability: Not applicable



## PM4 — Strong

Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

Applicability: Not Applicable



## PM4 — Supporting

Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

Applicability: Not Applicable



## PM4 — Very Strong

Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

Applicability: Not applicable



## PM5 — Moderate

Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

Applicability: Applicable

Use code when previously reported variant reaches a pathogenic classification using the VWD Type 2 rule specifications. Previously reported variant can be associated with a different type of VWD.

Code may also be applied when two previously reported variants reach a likely pathogenic classification using the VWD Type 2 rule specifications. Previously reported variants can be associated with a different type of VWD.

## PM5 — Stand Alone

Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

Applicability: Not applicable



## PM5 — Strong

Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

Applicability: Not Applicable



## PM5 — Supporting

Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

Applicability: Applicable

Use code when previously reported variant reaches a likely pathogenic classification using the VWD Type 2 rule specifications. Previously reported variant can be associated with a different type of VWD.

## PM5 — Very Strong

Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

Applicability: Not applicable



## PM6 — Moderate

Assumed de novo, but without confirmation of paternity and maternity.

Applicability: Not applicable



## PM6 — Stand Alone

Assumed de novo, but without confirmation of paternity and maternity.

Applicability: Not applicable



## PM6 — Strong

Assumed de novo, but without confirmation of paternity and maternity.

Applicability: Not applicable



## PM6 — Supporting

Assumed de novo, but without confirmation of paternity and maternity.

Applicability: Not applicable



## PM6 — Very Strong

Assumed de novo, but without confirmation of paternity and maternity.

Applicability: Not applicable



## PP1 — Moderate

Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.

Applicability: Applicable

Appropriate to use when there are multiple families each reported to have two or more meioses.

## PP1 — Stand Alone

Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.

Applicability: Not applicable



## PP1 — Strong

Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.

Applicability: Not Applicable



## PP1 — Supporting

Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.

Applicability: Applicable

Appropriate to use when there are 2 or more meioses within a single family.

## PP1 — Very Strong

Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.

Applicability: Not applicable



## PP2 — Moderate

Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

Applicability: Not applicable



## PP2 — Stand Alone

Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

Applicability: Not applicable



## PP2 — Strong

Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

Applicability: Not applicable



## PP2 — Supporting

Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

Applicability: Not applicable



## PP2 — Very Strong

Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

Applicability: Not applicable



## PP3 — Moderate

Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

Applicability: Not Applicable



## PP3 — Stand Alone

Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

Applicability: Not applicable



## PP3 — Strong

Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

Applicability: Not Applicable



## PP3 — Supporting

Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

Applicability: Applicable

Appropriate to use for missense variants that have a REVEL score of greater or equal to 0.644 OR a SpliceAI score suggestive of a splicing defect (greater or equal to 0.5).

## PP3 — Very Strong

Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

Applicability: Not applicable



## PP4 — Moderate

Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.

Applicability: Applicable

The patient must have a clinical phenotype of excessive mucocutaneous bleeding and required laboratory values to use the PP4 rule code at the moderate strength. See Table 2A for required and consistent laboratory values.

## PP4 — Stand Alone

Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.

Applicability: Not applicable



## PP4 — Strong

Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.

Applicability: Not Applicable



## PP4 — Supporting

Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.

Applicability: Applicable

The patient must have a clinical phenotype of excessive mucocutaneous bleeding and required laboratory values to use the PP4 rule code at the supporting strength. See Table 2B for required and consistent laboratory values.

## PP4 — Very Strong

Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.

Applicability: Not applicable



## PP5 — Moderate

Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

Applicability: Not applicable

This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee.

## PP5 — Stand Alone

Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

Applicability: Not applicable

This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee.

## PP5 — Strong

Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

Applicability: Not applicable

This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee.

## PP5 — Supporting

Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

Applicability: Not applicable

This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee.

## PP5 — Very Strong

Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

Applicability: Not applicable

This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee.

## PS1 — Moderate

Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

Applicability: Applicable

Use with no specification except comparison variant must be classified as likely pathogenic using rules from the VWD VCEP.

## PS1 — Stand Alone

Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

Applicability: Not applicable



## PS1 — Strong

Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

Applicability: Applicable

Use with no specification except comparison variant must be classified as pathogenic using rules from the VWD VCEP.

## PS1 — Supporting

Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

Applicability: Not Applicable



## PS1 — Very Strong

Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

Applicability: Not applicable



## PS2 — Moderate

De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

Applicability: Applicable

Use proposed SVI point recommendations for **“Phenotype consistent with gene but not highly specific”** if the proband meets **PP4 criteria**.  Use **“Phenotype highly specific for gene”** phenotype consistency if the proband meets **PP4\_Moderate criteria**. See Table 1 attached. Required 1 point.

## PS2 — Stand Alone

De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

Applicability: Not applicable



## PS2 — Strong

De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

Applicability: Applicable

Use proposed SVI point recommendations for **“Phenotype consistent with gene but not highly specific”** if the proband meets **PP4 criteria**.  Use **“Phenotype highly specific for gene”** phenotype consistency if the proband meets **PP4\_Moderate criteria**. See Table 1 attached. Required 2 points.

## PS2 — Supporting

De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

Applicability: Applicable

Use proposed SVI point recommendations for **“Phenotype consistent with gene but not highly specific”** if the proband meets **PP4 criteria**. If the proband meets PP4\_Moderate criteria, use a moderate or higher evidence weight (see above). See Table 1 attached. Required 0.5 point.

## PS2 — Very Strong

De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

Applicability: Applicable

Use proposed SVI point recommendations for **“Phenotype consistent with gene but not highly specific”** if the proband meets **PP4 criteria**.  Use **“Phenotype highly specific for gene”** phenotype consistency if the proband meets **PP4\_Moderate criteria**. See Table 1 attached. Required 4 points.

## PS3 — Moderate

Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

Applicability: Not Applicable



## PS3 — Stand Alone

Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

Applicability: Not applicable



## PS3 — Strong

Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

Applicability: Applicable

Either 

(1) In a transgenic animal model, must demonstrate minimal to no function.

OR

(2) The following types of assays using recombinant vWF are approved for each subtype:

Subtype 2A = A multimerization assay in which the variant is expressed in a recombinant system (either independently or coexpressed with WT) resulting in abnormal multimers, with a reported loss of HMWM, AND, to confirm this is consistent with the variant's mechanism of disease, there must be a patient harboring the variant with a clinical assay also showing loss of HMWMs. This evidence must be published in a peer reviewed journal and a picture of the gel must be visible for evaluation.

Subtype 2B = A GP1b or platelet binding assay indicating gain of function by increased binding at low doses of ristocetin

Subtype 2M = Either (1) A GP1b or platelet binding assay OR (2) Collagen binding assay, indicating loss of function by decreased binding 

See attached spreadsheet for examples of approved assay instances to use for this rule code. There are no universal thresholds for these assays; however, the relevant results should be described as clinically significant if assays were performed in a clinical laboratory or statistically significant if pertaining to research findings.

## PS3 — Supporting

Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

Applicability: Applicable

Subtype 2A = Either (1) a multimerization assay in which the variant is expressed in a recombinant system (either independently or coexpressed with WT) resulting in abnormal multimers, with a reported loss of HMWM. This evidence must be published in a peer reviewed journal and a picture of the gel must be visible for evaluation. (2) a ADAMTS susceptibility assay indicating increased susceptibility relative to WT.

## PS3 — Very Strong

Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

Applicability: Not Applicable



## PS4 — Moderate

The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.
Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.
Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.

Applicability: Applicable

Appropriate to use code when there are 2-3 probands that meet the laboratory phenotype of the PP4 definition for a specific VWD type 2 phenotype (i.e. – all probands must qualify for a clinical diagnosis of the same VWD type 2 phenotype based on laboratory criteria stated under PP4).

## PS4 — Stand Alone

The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.
Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.
Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.

Applicability: Not applicable



## PS4 — Strong

The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.
Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.
Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.

Applicability: Applicable

Appropriate to use code when there are 4-7 probands that meet the laboratory phenotype of the PP4 definition for a specific VWD type 2 phenotype (i.e. – all probands must qualify for a clinical diagnosis of the same VWD type 2 phenotype based on laboratory criteria stated under PP4).

## PS4 — Supporting

The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.
Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.
Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.

Applicability: Applicable

Appropriate to use code when there is 1 proband that meets the laboratory phenotype of the PP4 definition for a specific VWD type 2 phenotype.

## PS4 — Very Strong

The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.
Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.
Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.

Applicability: Applicable

Appropriate to use code when there are 8 or more probands that meet the laboratory phenotype of the PP4 definition for a specific VWD type 2 phenotype (i.e. – all probands must qualify for a clinical diagnosis of the same VWD type 2 phenotype based on laboratory criteria stated under PP4).

## PVS1 — Moderate

Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.

Applicability: Not applicable



## PVS1 — Stand Alone

Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.

Applicability: Not applicable



## PVS1 — Strong

Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.

Applicability: Not applicable



## PVS1 — Supporting

Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.

Applicability: Not applicable



## PVS1 — Very Strong

Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.

Applicability: Not applicable



Document: ClinGen von Willebrand Disease  Expert Panel Specifications to the ACMG/AMP Variant Interpretation Guidelines for VWF Version 1.0
CSpec ID: GN090
VCEP: von Willebrand Disease  Variant Curation Expert Panel
Version: 1.0
Status: current_released
Diseases: MONDO:0015631
Modes of inheritance: https://hpo.jax.org/app/browse/term/HP:0000007
Fetched: 2026-08-05T00:33:17.555652+00:00
Source API: https://cspec.genome.network/cspec/api/SequenceVariantInterpretation/id/GN090

## BA1 — Moderate

Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

Applicability: Not applicable



## BA1 — Stand Alone

Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

Applicability: Applicable

Appropriate to use for variants with a Popmax MAF of >0.1 in gnomAD.

## BA1 — Strong

Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

Applicability: Not applicable



## BA1 — Supporting

Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

Applicability: Not applicable



## BA1 — Very Strong

Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

Applicability: Not applicable



## BP1 — Moderate

Missense variant in a gene for which primarily truncating variants are known to cause disease.

Applicability: Not applicable



## BP1 — Stand Alone

Missense variant in a gene for which primarily truncating variants are known to cause disease.

Applicability: Not applicable



## BP1 — Strong

Missense variant in a gene for which primarily truncating variants are known to cause disease.

Applicability: Not applicable



## BP1 — Supporting

Missense variant in a gene for which primarily truncating variants are known to cause disease.

Applicability: Not applicable



## BP1 — Very Strong

Missense variant in a gene for which primarily truncating variants are known to cause disease.

Applicability: Not applicable



## BP2 — Moderate

Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.

Applicability: Not applicable



## BP2 — Stand Alone

Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.

Applicability: Not applicable



## BP2 — Strong

Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.

Applicability: Not applicable



## BP2 — Supporting

Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.

Applicability: Not applicable



## BP2 — Very Strong

Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.

Applicability: Not applicable



## BP3 — Moderate

In frame-deletions/insertions in a repetitive region without a known function.

Applicability: Not applicable



## BP3 — Stand Alone

In frame-deletions/insertions in a repetitive region without a known function.

Applicability: Not applicable



## BP3 — Strong

In frame-deletions/insertions in a repetitive region without a known function.

Applicability: Not applicable



## BP3 — Supporting

In frame-deletions/insertions in a repetitive region without a known function.

Applicability: Not applicable



## BP3 — Very Strong

In frame-deletions/insertions in a repetitive region without a known function.

Applicability: Not applicable



## BP4 — Moderate

Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.

Applicability: Not Applicable



## BP4 — Stand Alone

Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.

Applicability: Not applicable



## BP4 — Strong

Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.

Applicability: Not Applicable



## BP4 — Supporting

Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.

Applicability: Applicable

Use for missense variants that have a REVEL score of less than or equal to 0.290 AND SpliceAI cutoff of \<0.1. Use SpliceAI cutoff of \<0.1 for other variant types.

## BP4 — Very Strong

Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.

Applicability: Not applicable



## BP5 — Moderate

Variant found in a case with an alternate molecular basis for disease.

Applicability: Not Applicable



## BP5 — Stand Alone

Variant found in a case with an alternate molecular basis for disease.

Applicability: Not applicable



## BP5 — Strong

Variant found in a case with an alternate molecular basis for disease.

Applicability: Not Applicable



## BP5 — Supporting

Variant found in a case with an alternate molecular basis for disease.

Applicability: Applicable

A second variant in VWF may be considered an alternate molecular basis for disease when that variant is LP/P (as evaluated by the VWD VCEP) and fully explains the phenotype of the patient's reported VWD subtype.

## BP5 — Very Strong

Variant found in a case with an alternate molecular basis for disease.

Applicability: Not applicable



## BP6 — Moderate

Reputable source recently reports variant as benign, but the evidence is not available to the laboratory to perform an independent evaluation.

Applicability: Not applicable

This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee.

## BP6 — Stand Alone

Reputable source recently reports variant as benign, but the evidence is not available to the laboratory to perform an independent evaluation.

Applicability: Not applicable

This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee.

## BP6 — Strong

Reputable source recently reports variant as benign, but the evidence is not available to the laboratory to perform an independent evaluation.

Applicability: Not applicable

This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee.

## BP6 — Supporting

Reputable source recently reports variant as benign, but the evidence is not available to the laboratory to perform an independent evaluation.

Applicability: Not applicable

This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee.

## BP6 — Very Strong

Reputable source recently reports variant as benign, but the evidence is not available to the laboratory to perform an independent evaluation.

Applicability: Not applicable

This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee.

## BP7 — Moderate

A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.

Applicability: Not Applicable



## BP7 — Stand Alone

A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.

Applicability: Not applicable



## BP7 — Strong

A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.

Applicability: Not Applicable



## BP7 — Supporting

A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.

Applicability: Applicable

Use SpliceAI for splicing predictor with a cutoff score of 0.

## BP7 — Very Strong

A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.

Applicability: Not applicable



## BS1 — Moderate

Allele frequency is greater than expected for disorder.

Applicability: Not Applicable



## BS1 — Stand Alone

Allele frequency is greater than expected for disorder.

Applicability: Not Applicable



## BS1 — Strong

Allele frequency is greater than expected for disorder.

Applicability: Applicable

Appropriate to use for variants with a Popmax MAF of >0.01 in gnomAD.

## BS1 — Supporting

Allele frequency is greater than expected for disorder.

Applicability: Not Applicable



## BS1 — Very Strong

Allele frequency is greater than expected for disorder.

Applicability: Not applicable



## BS2 — Moderate

Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

Applicability: Not applicable



## BS2 — Stand Alone

Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

Applicability: Not applicable



## BS2 — Strong

Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

Applicability: Not applicable



## BS2 — Supporting

Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

Applicability: Not applicable



## BS2 — Very Strong

Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

Applicability: Not applicable



## BS3 — Moderate

Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

Applicability: Not applicable



## BS3 — Stand Alone

Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

Applicability: Not applicable



## BS3 — Strong

Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

Applicability: Not applicable



## BS3 — Supporting

Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

Applicability: Not applicable



## BS3 — Very Strong

Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

Applicability: Not applicable



## BS4 — Moderate

Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

Applicability: Not Applicable



## BS4 — Stand Alone

Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

Applicability: Not applicable



## BS4 — Strong

Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

Applicability: Applicable

Appropriate to use when two or more relatives have the phenotype consistent with VWD type 2 without harboring the variant identified in other affected family members. Additionally, there is not another established cause of type 2 VWD (e.g. - there are not multiple type 2 VWD diagnoses) segregating in the family.

## BS4 — Supporting

Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

Applicability: Applicable

Appropriate to use when only one relative has the phenotype consistent with VWD type 2 without harboring the variant identified in other affected family members. Additionally, there is not another established cause of type 2 VWD (e.g. - there are not multiple type 2 VWD diagnoses) segregating in the family.

## BS4 — Very Strong

Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

Applicability: Not applicable



## PM1 — Moderate

Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

Applicability: Not applicable



## PM1 — Stand Alone

Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

Applicability: Not applicable



## PM1 — Strong

Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

Applicability: Not applicable



## PM1 — Supporting

Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

Applicability: Not applicable



## PM1 — Very Strong

Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

Applicability: Not applicable



## PM2 — Moderate

Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.

Applicability: Not Applicable



## PM2 — Stand Alone

Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.

Applicability: Not applicable



## PM2 — Strong

Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.

Applicability: Not applicable



## PM2 — Supporting

Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.

Applicability: Applicable

Use code for variants with a popmax MAF of \<0.005 in gnomAD.

## PM2 — Very Strong

Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.

Applicability: Not applicable



## PM3 — Moderate

For recessive disorders, detected in trans with a pathogenic variant
Note: This requires testing of parents (or offspring) to determine phase.

Applicability: Applicable

Use SVI recommended point system for this code for probands with a VWD type 2N diagnosis. Total of 1 point required.

## PM3 — Stand Alone

For recessive disorders, detected in trans with a pathogenic variant
Note: This requires testing of parents (or offspring) to determine phase.

Applicability: Not applicable



## PM3 — Strong

For recessive disorders, detected in trans with a pathogenic variant
Note: This requires testing of parents (or offspring) to determine phase.

Applicability: Applicable

Use SVI recommended point system for this code for probands with a VWD type 2N diagnosis. Total of 2 points required.

## PM3 — Supporting

For recessive disorders, detected in trans with a pathogenic variant
Note: This requires testing of parents (or offspring) to determine phase.

Applicability: Applicable

Use SVI recommended point system for this code for probands with a VWD type 2N diagnosis. Total of 0.5 points required.

## PM3 — Very Strong

For recessive disorders, detected in trans with a pathogenic variant
Note: This requires testing of parents (or offspring) to determine phase.

Applicability: Applicable

Use SVI recommended point system for this code for probands with a VWD type 2N diagnosis. Total of 4 points required.

## PM4 — Moderate

Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

Applicability: Applicable

Use with no specification.

## PM4 — Stand Alone

Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

Applicability: Not applicable



## PM4 — Strong

Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

Applicability: Not Applicable



## PM4 — Supporting

Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

Applicability: Not Applicable



## PM4 — Very Strong

Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

Applicability: Not applicable



## PM5 — Moderate

Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

Applicability: Applicable

Use code when previously reported variant reaches a pathogenic classification using the VWD Type 2 rule specifications. Previously reported variant can be associated with a different type of VWD.

Code may also be applied when two previously reported variants reach a likely pathogenic classification using the VWD Type 2 rule specifications. Previously reported variants can be associated with a different type of VWD.

## PM5 — Stand Alone

Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

Applicability: Not applicable



## PM5 — Strong

Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

Applicability: Not Applicable



## PM5 — Supporting

Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

Applicability: Applicable

Use code when previously reported variant reaches a likely pathogenic classification using the VWD Type 2 rule specifications. Previously reported variant can be associated with a different type of VWD.

## PM5 — Very Strong

Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

Applicability: Not applicable



## PM6 — Moderate

Assumed de novo, but without confirmation of paternity and maternity.

Applicability: Not applicable



## PM6 — Stand Alone

Assumed de novo, but without confirmation of paternity and maternity.

Applicability: Not applicable



## PM6 — Strong

Assumed de novo, but without confirmation of paternity and maternity.

Applicability: Not applicable



## PM6 — Supporting

Assumed de novo, but without confirmation of paternity and maternity.

Applicability: Not applicable



## PM6 — Very Strong

Assumed de novo, but without confirmation of paternity and maternity.

Applicability: Not applicable



## PP1 — Moderate

Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.

Applicability: Applicable

Appropriate to use when a proband has two affected family members.

## PP1 — Stand Alone

Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.

Applicability: Not applicable



## PP1 — Strong

Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.

Applicability: Applicable

Appropriate to use when a proband has three affected family members.

## PP1 — Supporting

Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.

Applicability: Applicable

Appropriate to use when a proband has one affected family member.

## PP1 — Very Strong

Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.

Applicability: Not applicable



## PP2 — Moderate

Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

Applicability: Not applicable



## PP2 — Stand Alone

Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

Applicability: Not applicable



## PP2 — Strong

Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

Applicability: Not applicable



## PP2 — Supporting

Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

Applicability: Not applicable



## PP2 — Very Strong

Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

Applicability: Not applicable



## PP3 — Moderate

Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

Applicability: Not Applicable



## PP3 — Stand Alone

Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

Applicability: Not applicable



## PP3 — Strong

Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

Applicability: Not Applicable



## PP3 — Supporting

Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

Applicability: Applicable

Appropriate to use for missense variants that have a REVEL score of greater or equal to 0.644 OR a SpliceAI score suggestive of a splicing defect (greater or equal to 0.5).

## PP3 — Very Strong

Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

Applicability: Not applicable



## PP4 — Moderate

Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.

Applicability: Applicable

The patient must have a clinical phenotype of excessive mucocutaneous bleeding and required laboratory values to use the PP4 rule code, including a low factor VIII activity level and evidence of decreased VWF:FVIII binding.

Additional consistent information should be noted but is not required, including either normal or low VWF:Ag, normal high molecular weight multimers, and sequencing with duplication/deletion analysis of the F8 gene.

## PP4 — Stand Alone

Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.

Applicability: Not applicable



## PP4 — Strong

Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.

Applicability: Not Applicable



## PP4 — Supporting

Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.

Applicability: Not Applicable



## PP4 — Very Strong

Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.

Applicability: Not applicable



## PP5 — Moderate

Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

Applicability: Not applicable

This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee.

## PP5 — Stand Alone

Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

Applicability: Not applicable

This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee.

## PP5 — Strong

Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

Applicability: Not applicable

This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee.

## PP5 — Supporting

Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

Applicability: Not applicable

This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee.

## PP5 — Very Strong

Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

Applicability: Not applicable

This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee.

## PS1 — Moderate

Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

Applicability: Applicable

Use with no specification except comparison variant must be classified as likely pathogenic using rules from the VWD VCEP.

## PS1 — Stand Alone

Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

Applicability: Not applicable



## PS1 — Strong

Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

Applicability: Applicable

Use with no specification except comparison variant must be classified as pathogenic using rules from the VWD VCEP.

## PS1 — Supporting

Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

Applicability: Not Applicable



## PS1 — Very Strong

Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

Applicability: Not applicable



## PS2 — Moderate

De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

Applicability: Applicable

Use proposed SVI point recommendations for **“Phenotype consistent with gene but not highly specific”** if the proband meets **PP4 criteria**.  Use **“Phenotype highly specific for gene”** phenotype consistency if the proband meets **PP4\_Moderate criteria**. See Table 1 attached. Required 1 point.

## PS2 — Stand Alone

De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

Applicability: Not applicable



## PS2 — Strong

De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

Applicability: Applicable

Use proposed SVI point recommendations for **“Phenotype consistent with gene but not highly specific”** if the proband meets **PP4 criteria**.  Use **“Phenotype highly specific for gene”** phenotype consistency if the proband meets **PP4\_Moderate criteria**. See Table 1 attached. Required 2 points.

## PS2 — Supporting

De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

Applicability: Applicable

Use proposed SVI point recommendations for **“Phenotype consistent with gene but not highly specific”** if the proband meets **PP4 criteria**. If the proband meets PP4\_Moderate criteria, use a moderate or higher evidence weight (see above). See Table 1 attached. Required 0.5 point.

## PS2 — Very Strong

De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

Applicability: Applicable

Use proposed SVI point recommendations for **“Phenotype consistent with gene but not highly specific”** if the proband meets **PP4 criteria**.  Use **“Phenotype highly specific for gene”** phenotype consistency if the proband meets **PP4\_Moderate criteria**. See Table 1 attached. Required 4 points.

## PS3 — Moderate

Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

Applicability: Not Applicable



## PS3 — Stand Alone

Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

Applicability: Not applicable



## PS3 — Strong

Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

Applicability: Applicable

Either (1) in a transgenic animal model, must demonstrate minimal to no function. (2) a Factor VIII binding assay using recombinant vWF resulting in decreased binding compared to WT.

See attached spreadsheet for examples of approved assay instances to use for this rule code. There are no universal thresholds for these assays; however, the relevant results should be described as clinically significant if assays were performed in a clinical laboratory or statistically significant if pertaining to research findings.

## PS3 — Supporting

Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

Applicability: Not Applicable



## PS3 — Very Strong

Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

Applicability: Not Applicable



## PS4 — Moderate

The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.
Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.
Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.

Applicability: Not applicable



## PS4 — Stand Alone

The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.
Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.
Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.

Applicability: Not applicable



## PS4 — Strong

The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.
Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.
Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.

Applicability: Not applicable



## PS4 — Supporting

The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.
Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.
Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.

Applicability: Not applicable



## PS4 — Very Strong

The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.
Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.
Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.

Applicability: Not applicable



## PVS1 — Moderate

Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.

Applicability: Not applicable



## PVS1 — Stand Alone

Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.

Applicability: Not applicable



## PVS1 — Strong

Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.

Applicability: Not applicable



## PVS1 — Supporting

Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.

Applicability: Not applicable



## PVS1 — Very Strong

Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.

Applicability: Not applicable


