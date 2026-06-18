# MEAL Expert & Data Analyst — Full Role Map for the THP Child-Marriage Baseline

**Context:** Baseline study for *"Shaping Political Change – Strengthening Girls' Rights, Ending Child Marriage"* (THP Bangladesh, **BMZ-funded**, Phase 2, May 2026–Apr 2029). Mixed-methods, 5 upazilas / 32 unions / 128 schools, ~6-week consultancy. The ToR names two relevant roles:

> **Research Methodology / MEAL Expert** — "Strong quantitative and qualitative research skills; experience developing MEAL frameworks and indicator tracking systems; proficiency in SPSS or equivalent; experience with power calculations and sampling design."
>
> **Data Analyst** — "Proficiency in SPSS, STATA or R or any AI-based platform; experience in statistical analysis for social research; ability to manage and clean large datasets."

This document maps **everything** these two roles must own. Written paranoid: the failure modes are spelled out, because in a child-protection baseline a quiet methodological mistake becomes an ethical and donor-reporting problem.

---

## 0. How the two roles differ (and where they collide)

| Dimension | **MEAL Expert** | **Data Analyst** |
|---|---|---|
| Core question | "Are we measuring the **right** things, the **right** way, ethically?" | "Given the data, what does it **actually say**, and is it **clean and correct**?" |
| Owns | Theory of change ↔ indicators ↔ tools ↔ sampling ↔ analysis plan ↔ indicator baseline table | Data pipeline: entry → cleaning → coding → statistics → tables/figures → reproducible outputs |
| Time-centre of gravity | Inception + design + interpretation + recommendations | Post-fieldwork (cleaning + analysis), but **must** be consulted at design |
| Deliverable ownership | Inception report, sampling justification, indicator baseline table, MEAL recommendations | Cleaned/anonymised SPSS+Excel dataset, analysis syntax, tabulations, figures |
| Accountability if wrong | Wrong indicator definition, unrepresentative sample, ethics breach | Miscoded variable, wrong denominator, non-reproducible result |

**The collision zone (where baselines die):** the **analysis plan** and the **indicator operationalisation**. If the MEAL Expert defines "girl can decide whether/when/whom to marry" but the Data Analyst codes the variable differently than the questionnaire captured it, the baseline value is wrong and *nobody notices until endline disagrees with it.* These two people must co-author the **Indicator Reference Sheet** (see §3) before a single byte of data is collected.

---

## 1. MEAL EXPERT — responsibilities, paranoid edition

### 1.1 Frameworks & theory
- **Reconstruct the Theory of Change / Logframe** from the ToR's Impact Matrix (Overall → 4 Project-objective indicators → 4 Sub-objectives with their indicators). The ToR *gives* you the results chain; your job is to make it measurable.
- **Convert each indicator to SMART form** and decide: numerator, denominator, unit of analysis, recall period ("last 12 months" appears repeatedly), disaggregation, data source, and **measurement method**. The ToR *mandates* disaggregation by **sex, age group, District/Upazila/Union, school-enrolment status, and stakeholder type** — bake this into every tool and every dataset variable.
- **OECD-DAC / BMZ lens:** BMZ reporting expects relevance, coherence, effectiveness, efficiency, impact, sustainability. A baseline mostly serves *effectiveness* and *impact* (establishing the counterfactual reference values), but write the indicator table so it survives a BMZ/THP-Germany audit.

### 1.2 The indicator traps (read twice)
- **Baseline ≠ endline construct.** Impact indicator 1 baseline is *"13% able to participate in decisions regarding their marriage"* but the **target is phrased differently**: *"object to marriage before legal age **AND** decide whether/when/whom."* These are **two different constructs**. If you measure the endline construct at baseline you will *not* get 13%. **Flag this in the inception report and define one stable operationalisation** used at both time points, or the "change" is an artefact of question wording.
- **"TBD" baselines.** Several indicators say *"the exact baseline value will be established during the baseline"* (prevention action, stakeholder engagement, CM prevalence 18–24, CMPC functionality, school measures). You are responsible for **defining each one precisely now**, because the target (e.g., "+10 percentage points", ">=40% functional") is meaningless without a fixed definition.
- **Minimum functionality criteria.** Indicator 6 and Sub-objective 3 hinge on a **"minimum functionality criteria"** for the 37 UCMPCs and 128 School YEH Units defined "in the proposal." **Get that proposal definition** — composition, ≥2 documented meetings/12 months, written decisions, ≥1 documented follow-up. Build the institutional checklist to score *exactly* those criteria, yes/no, auditable.
- **Different populations for different indicators.** "% of women **18–24** married before 18" is **not** the 11–18 girls cohort. It needs its own frame (see sampling). Missing this is the single most common technical error in child-marriage baselines.

### 1.3 Sampling & power (the ToR explicitly demands a power calculation)
- Own the sampling strategy end-to-end: frame definition, stage design (upazila → union → school → respondent), **probability** selection method, **design effect**, **finite population correction**, **non-response inflation**, and **proportional allocation** across strata.
- **Defend the sample size with a written rationale.** See `sampling_corrected.py` and §5 below — the recommended adolescent-girls sample is **~819** (95% CI, ±5%, p=0.5, DEFF 2.0, +10% non-response), not 380.
- **Selection mechanism, not just size.** A correct *n* drawn non-randomly is still biased. Specify: how schools are selected (PPS — probability proportional to enrolment), how girls are listed and selected within school (systematic random from class registers), and how out-of-school girls are reached (they are part of the 9,000 and the most at-risk — *school-only sampling silently excludes the highest-risk girls*, a fatal coverage bias).
- **Weights.** If you use PPS or disproportionate allocation, you must compute and apply **survey weights** at analysis. Decide now; tell the Data Analyst.

### 1.4 Tools, training, fieldwork, ethics
- Design and **pre-test/pilot** all instruments: quantitative survey, FGD guides, KII guides, IDI guides, institutional checklists (school + UCMPC). Pilot in a non-sample union; revise; document.
- **Enumerator training & the safeguarding spine.** The ToR makes this contractual: written **parental consent + adolescent assent**; **female enumerators for girls/women**; **referral pathway** (enumerators trained to give hotline/local-service info on disclosure of active risk/abuse); **do-no-harm** (no re-traumatisation); anonymisation + secure storage. Build a **referral protocol document** and a **disclosure/incident log** before fieldwork. THP **Child Protection Policy** breach = contract termination — this is not boilerplate.
- **ERIC standards** (Ethical Research Involving Children) and child-safeguarding are the governing ethics frame here, not generic adult-survey ethics.

### 1.5 Analysis oversight, reporting, recommendations
- Author the **Analysis Plan** *before* data exist (pre-specified tables, disaggregations, indicator computations) — this is your insurance against fishing and against the Data Analyst guessing.
- **Triangulate** quant ↔ qual. The ToR wants the "what" *and* the "why." Build a triangulation matrix: each indicator gets a quantitative value + qualitative explanation + (where relevant) institutional-assessment evidence.
- Produce the **standalone Indicator Baseline Table** (a named deliverable): per indicator → baseline value, measurement method, disaggregation, data source, data-quality/limitation notes.
- Deliver **practical MEAL recommendations** for project implementation and the project's *own* ongoing MEAL system (indicator tracking, frequency, responsible parties, data flow).

### 1.6 MEAL-Expert failure modes (the "no mercy" list)
1. School-based sampling that **excludes out-of-school and married girls** → undercounts the highest-risk group → baseline looks rosier than reality → project looks like it "failed" at endline when it didn't.
2. Powering on a single convenient contrast (the original `sampling.py` error) → under-sized survey → endline "change" not statistically detectable → **the whole impact claim collapses**.
3. Letting baseline and endline question wording drift → fake change.
4. No survey weights when design is unequal-probability → biased point estimates.
5. Treating the 18–24 CM-prevalence indicator as part of the 11–18 sample → indicator un-baselinable.
6. Forgetting the *institutional census* (37 UCMPCs + 128 schools are **censused**, not sampled) and trying to "sample" them.
7. Social-desirability bias on sensitive items (child marriage attitudes) with no mitigation (e.g., list experiments, indirect questioning, self-administered modules) → inflated "good" attitudes.
8. Recall bias on "last 12 months" items with no anchoring → noise.

---

## 2. DATA ANALYST — responsibilities, paranoid edition

### 2.1 Before data (yes, before)
- Co-build the **codebook / data dictionary** with the MEAL Expert: every variable name, type, allowed values, missing-value codes, skip logic, and the **exact indicator formula** it feeds.
- **Force structured digital capture.** Push for KoboToolbox / ODK / SurveyCTO / CommCare with built-in validation (ranges, skip logic, required fields, GPS, audio-audit for QA). Paper → double data entry with reconciliation if digital is impossible. Set this up *before* fieldwork — retrofitting validation after collection is how dirty data happens.

### 2.2 Data management & cleaning ("manage and clean large datasets")
- **Reproducible, syntax-driven cleaning** — *never* clean by clicking in SPSS/Excel. Every transformation in a saved, commented script (SPSS syntax `.sps`, Stata `.do`, or R script). The output must regenerate from raw with one run. The ToR wants the **dataset in SPSS and/or Excel** plus raw qualitative notes/transcripts as annexes — your syntax is the bridge.
- Cleaning checklist: duplicates; out-of-range; logical inconsistencies (e.g., "married" + "in school" + age 12 — check, don't assume); skip-logic violations; impossible dates; enumerator-level outliers (catches fabrication — flag enumerators whose distributions differ implausibly); missing-data audit and a **documented missing-data strategy** (listwise vs. pairwise vs. imputation — and *justify* it).
- **Anonymisation is a deliverable, not an afterthought.** Strip direct identifiers, generalise quasi-identifiers (exact age → age band, exact village → union), separate the linkage key into a secured file, and check **k-anonymity** on small cells (a 13-year-old married girl in a named small village is identifiable). BMZ = German funder → treat personal data with **GDPR-grade** discipline.

### 2.3 Analysis ("statistical analysis for social research")
- **Descriptive + inferential**, all disaggregated by the mandated axes (sex, age group, district/upazila/union, enrolment status, stakeholder type).
- Apply **survey weights** and account for the **complex design** (clustering/strata) when computing standard errors and confidence intervals — naïve SEs from clustered data are too small and overstate precision. Use `svyset`/`svy:` (Stata), `survey`/`srvyr` (R), or SPSS **Complex Samples** module. *Plain `proportions` on clustered data is wrong.*
- Compute each indicator **exactly** per the Indicator Reference Sheet, with its CI. Cross-tabs with chi-square / proportions tests where comparisons are made. Keep it appropriate — a baseline is mostly **estimation with confidence intervals**, not hypothesis-testing theatre.
- **Reproducible outputs**: tables and figures generated from script, version-controlled, labelled, with n and denominator shown on every table.

### 2.4 Qualitative support
- Manage transcription + **English translation** (a ToR deliverable) of FGD/KII/IDI notes. Set up **thematic coding** (deductive frame from indicators + inductive emergent themes) in NVivo / ATLAS.ti / MAXQDA / Dedoose / Taguette (open-source). Maintain an audit trail (who coded, codebook versions, inter-coder agreement on a subset).

### 2.5 Data-Analyst failure modes (the "no mercy" list)
1. **Point-and-click cleaning** → irreproducible dataset → fails the "cleaned dataset + we can re-run it" expectation and you can't defend any number.
2. **Ignoring the complex design** → CIs too narrow → false precision → indicator "significance" claims that don't hold.
3. **Wrong denominator** (e.g., % of *all* girls vs % of *unmarried* girls who can decide) → indicator silently wrong; this is the most common analysis bug in KAP surveys.
4. **No weights** when selection was unequal-probability → biased estimates.
5. **Weak anonymisation** → re-identification of a child in a child-protection study → ethics + legal breach.
6. Mishandling missing data (silent listwise deletion changes the denominator and the estimate).
7. Mixing **don't know / refused** into "no" → biases sensitive-item estimates.
8. Not screening for **enumerator fabrication / curbstoning** (duplicate GPS, too-fast interviews, low variance) → garbage in, garbage out.

---

## 3. The one artefact both roles co-own: the Indicator Reference Sheet

For **every** ToR indicator, fill this before fieldwork:

| Field | Example (Impact indicator 1) |
|---|---|
| Indicator ID & text | I1 — % unmarried girls who can decide whether/when/whom to marry |
| Numerator | # unmarried girls 11–18 answering "yes" to all decision-agency items |
| Denominator | # unmarried girls 11–18 surveyed (note: *unmarried* only) |
| Question(s) | Qxx–Qyy (exact item numbers in the instrument) |
| Coding rule | yes/no per item; composite = all-yes; DK/refused = not-yes |
| Recall period | n/a (current state) |
| Disaggregation | age band, upazila/union, enrolment status |
| Data source | adolescent-girls quantitative survey |
| Baseline target convention | fix the *same* wording for endline (see §1.2 trap) |
| Data-quality notes | social-desirability risk; female enumerator only |

This sheet is the contract between design (MEAL) and computation (Analyst). It is also half of the **Indicator Baseline Table** deliverable.

---

## 4. Resources to learn from

### 4.1 Sampling & survey methodology (the ToR's "power calculation" demand)
- **Cochran, *Sampling Techniques*** — the canonical sample-size / FPC / stratification reference.
- **Kish, *Survey Sampling*** — design effects, cluster sampling, weighting (where DEFF comes from).
- **Groves et al., *Survey Methodology*** — total survey error, non-response, measurement error.
- **Lohr, *Sampling: Design and Analysis*** — modern, very readable on complex designs & variance estimation.
- **UNICEF MICS** sampling guidance & **DHS Sampling and Household Listing Manual** (free PDFs) — the gold-standard *worked examples* for exactly this kind of multi-stage household/school survey in LMIC settings. **Read these — your design should look like theirs.**
- Sample-size tools to learn: **G\*Power** (free), **OpenEpi**, **Stata `power`**, R **`pwr`** / **`presize`**, and `statsmodels.stats.power` (what your script uses).

### 4.2 MEAL / evaluation frameworks
- **Gertler, Martinez, Premand, Rawlings, Vermeersch — *Impact Evaluation in Practice* (World Bank, free PDF)** — start here for results chains, indicators, counterfactual logic.
- **Khandker, Koolwal, Samad — *Handbook on Impact Evaluation* (World Bank)**.
- **Bamberger, Rugh & Mabry — *RealWorld Evaluation*** — doing rigorous M&E under real budget/time/data constraints (i.e., a 6-week consultancy).
- **BetterEvaluation.org** — practical menu of methods; theory of change; evaluation design.
- **OECD-DAC Evaluation Criteria** (relevance/coherence/effectiveness/efficiency/impact/sustainability) + **DAC Glossary of RBM terms** — the language BMZ reporting uses.
- **UNEG Norms & Standards for Evaluation** — UN-system evaluation quality bar.
- **DIME Analytics — *Development Research in Practice* (World Bank, free)** + the **DIME Wiki** — the best modern, concrete guide to reproducible survey data workflows, field QA, and data management. Pair with **IPA/J-PAL** resources and **Glennerster & Takavarasha, *Running Randomized Evaluations***.

### 4.3 Statistical software & data management
- **SPSS:** Andy Field, *Discovering Statistics Using IBM SPSS Statistics* (also the best plain-English stats primer there is); learn **SPSS syntax** and the **Complex Samples** module.
- **Stata:** Acock, *A Gentle Introduction to Stata*; learn `.do` files and `svyset`/`svy:`.
- **R:** Wickham & Grolemund, *R for Data Science*; Kabacoff, *R in Action*; packages **`survey`**, **`srvyr`**, **`tidyverse`**, **`gtsummary`** (publication tables), **`pwr`**.
- **Tidy data:** Hadley Wickham's *"Tidy Data"* paper — the mental model for clean datasets.
- **Mobile data collection:** KoboToolbox (free, NGO-standard), ODK, SurveyCTO, CommCare — learn form design, validation, skip logic, and back-checks.

### 4.4 Qualitative methods (half this study is qual)
- **Patton, *Qualitative Research & Evaluation Methods*** (and *Utilization-Focused Evaluation*).
- **Miles, Huberman & Saldaña, *Qualitative Data Analysis: A Methods Sourcebook***.
- **Saldaña, *The Coding Manual for Qualitative Researchers***.
- **Braun & Clarke** — reflexive **thematic analysis** (the workhorse method for FGD/KII analysis).
- CAQDAS tools: **NVivo / ATLAS.ti / MAXQDA / Dedoose / Taguette** (Taguette is free/open-source).

### 4.5 Ethics, safeguarding, child marriage measurement (non-negotiable for this ToR)
- **ERIC — Ethical Research Involving Children** (UNICEF/Childwatch) — *the* framework for consent/assent, do-no-harm, researcher conduct with minors. **Read before writing tools.**
- **UNICEF, *Child Protection / Safeguarding in Research*** and your **THP Child Protection Policy** (contractually binding here).
- **WHO ethical & safety recommendations for researching violence against women / girls** — referral pathways, female interviewers, do-no-harm — directly applicable.
- **Council on the early measurement of child marriage:** UNICEF/UNFPA Global Programme to End Child Marriage; **Population Council** child-marriage measurement guidance; **Girls Not Brides** resource hub; **CMRA 2017 (Bangladesh)** text itself.
- **Data protection:** **GDPR** basics (German/BMZ funder) + Bangladesh data-protection considerations; anonymisation/k-anonymity guidance (e.g., UK ICO anonymisation code as a practical primer).

### 4.6 Free courses (if you want structured upskilling fast)
- University of Michigan, *Survey Data Collection and Analytics* specialisation (Coursera).
- World Bank / J-PAL / IPA online **Evaluating Social Programs** and **Data for Development** courses (edX).
- DataCamp / Coursera tracks for **R for survey analysis** or **SPSS**.
- UNICEF **MICS** and **DHS Program** e-learning + their public datasets to *practise complex-survey analysis with real data*.

---

## 5. Bottom line on the sampling (see `sampling_corrected.py`)

The original `sampling.py` **runs and is arithmetically self-consistent**, but its **statistical assumptions are wrong**, so it **under-sizes the study**:

- It powered on a **fabricated target (23%)** — no ToR indicator targets 23%. The real target for the 13% indicator is **60%**; the "10 percentage-point decrease" belongs to a **different indicator on a different population (women 18–24)**.
- A baseline's job is **precise estimation across many indicators** (several "TBD"), so the defensible approach is **p=0.5, ±5%, with finite-population correction, design effect, and non-response inflation** — not a single hand-picked contrast.
- Recommended adolescent-girls sample: **~819** (DEFF 2.0) or **~615** (lean, DEFF 1.5) — vs the original **380**, which only yields a **±6–7% margin of error**.
- Secondary groups are recalculated **consistently** (with DEFF + non-response), small groups flagged for **census**, the **37 UCMPCs and 128 schools treated as a census**, and the **18–24 CM-prevalence cohort flagged as a missing frame** the consultant must resolve.

Run it: `python sampling_corrected.py` (same deps as the original).
