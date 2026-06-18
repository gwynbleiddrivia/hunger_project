"""
=====================================================================================
 CORRECTED SAMPLING DESIGN
 Baseline Study: "Shaping Political Change - Strengthening Girls' Rights,
                  Ending Child Marriage" (THP Bangladesh, BMZ-funded, Phase 2)
=====================================================================================

WHY THIS FILE EXISTS
--------------------
The original `sampling.py` RUNS and is internally consistent, but its statistical
*assumptions* are wrong in ways that make the baseline under-powered and partly
indefensible to a reviewer. This file fixes those assumptions and documents every
decision so it can be defended in the Inception Report (the ToR explicitly asks the
consultant to "justify the sample size with a power calculation or equivalent
statistical rationale").

SUMMARY OF WHAT WAS WRONG IN sampling.py (full reasoning at the bottom of this file):
  1. FABRICATED TARGET. It used target_proportion = 0.23 with the note
     "decreasing child marriage by 10 percentage increase". No ToR indicator has a
     23% target. The 13% baseline indicator's real target is 60%. The "decrease by
     10 percentage points" belongs to a DIFFERENT indicator (% of women 18-24
     married before 18) measured on a DIFFERENT population (18-24, not 11-18).
  2. NON-CONSERVATIVE / WRONG-PURPOSE EFFECT SIZE. A baseline's primary job is to
     ESTIMATE many indicator values precisely (several baselines are "TBD"), not to
     test one hand-picked contrast. Powering on a single lucky contrast that happens
     to minimise n is the opposite of conservative.
  3. UNDER-SIZED. The result (380 girls) gives a margin of error of ~+/-6.2% at
     DEFF 1.5 (and ~+/-7.1% at DEFF 2.0) - worse than the +/-5% standard. A
     defensible design needs ~600-820 adolescent girls.
  4. DESIGN EFFECT TOO LOW. DEFF 1.5 is light for a 4-stage cluster design
     (upazila -> union -> school -> girl) on attitude/norm variables that cluster
     strongly. 2.0 is the defensible default; it should be derived from ICC.
  5. INCONSISTENT SECONDARY GROUPS. Secondary groups got Yamane with NO design
     effect and NO non-response inflation - different rules than the primary group.
  6. WRONG ALLOCATION KEY. Every group (incl. women leaders, VDT, UCMPC members)
     was allocated by SCHOOL counts. Community/committee groups are organised by
     UNION, not by school, so school-weighting misallocates them.
  7. FPC LOGIC BREAKS AT THE CORRECT n. "380/9000 = 4.2% < 5% so skip FPC" is fine
     at 380, but the correct sample is ~9% of 9,000, where FPC does matter.
  8. A MISSING FRAME. The "% of women 18-24 married before 18" impact indicator has
     no population/frame in the ToR and is NOT covered by the 11-18 girls sample.
     It is the statistically most demanding indicator and needs its own sample.

Run:  python sampling_corrected.py
Deps: statsmodels>=0.14, scipy  (same as the original)
"""

import math
from statsmodels.stats.power import NormalIndPower
import statsmodels.stats.proportion as prop

# =====================================================================================
# 0. GLOBAL PARAMETERS  (all defensible, all explicit, all tweakable)
# =====================================================================================
Z = 1.96            # two-sided 95% confidence (z_{1-alpha/2})
ALPHA = 0.05
POWER = 0.80        # conventional 80% power for the change-detection cross-check
P = 0.50            # MAXIMUM-VARIANCE assumption p(1-p)=0.25. Used because (a) several
                    # baseline values are "TBD" in the ToR, and (b) one survey estimates
                    # MANY indicators that sit anywhere from 13% to 55%; sizing on p=0.5
                    # guarantees +/-e precision for ALL of them. This is the standard,
                    # conservative, indicator-agnostic choice (MICS / DHS practice).
E = 0.05            # +/- 5 percentage-point absolute margin of error (sector standard)
NON_RESPONSE = 0.10 # 10% loss (refusal / unusable). Consider 0.15 for very sensitive
                    # modules (child-marriage / SRHR disclosure).


def cochran_n0(z=Z, p=P, e=E):
    """Infinite-population sample size for estimating a proportion to +/- e."""
    return (z ** 2) * p * (1 - p) / (e ** 2)


def apply_fpc(n0, N):
    """Finite Population Correction. Matters once n0 is a non-trivial fraction of N."""
    return n0 / (1 + (n0 - 1) / N)


def inflate_non_response(n, nr=NON_RESPONSE):
    """Correct inflation is n / (1 - nr), NOT n * (1 + nr)."""
    return n / (1 - nr)


def largest_remainder(total, weights):
    """Integer allocation that sums EXACTLY to `total` (Hamilton/largest-remainder).
    Avoids the +/-1 rounding drift the original script printed as '*Note: Rounding...'."""
    raw = {k: total * w for k, w in weights.items()}
    floors = {k: int(math.floor(v)) for k, v in raw.items()}
    remainder = total - sum(floors.values())
    order = sorted(raw, key=lambda k: raw[k] - floors[k], reverse=True)
    for i in range(remainder):
        floors[order[i]] += 1
    return floors


# =====================================================================================
# 1. PRIMARY COHORT - ADOLESCENT GIRLS 11-18  (N = 9,000)
#    This is THE headline number. It drives the budget and the bid.
# =====================================================================================
N_GIRLS = 9000

# ---- 1a. Design effect, derived (not guessed) from intra-cluster correlation -------
# DEFF = 1 + (m - 1) * ICC,  where
#   m   = avg number of girls interviewed per sampled school (cluster)
#   ICC = intra-cluster correlation. For knowledge/attitude/social-norm items in
#         school+community surveys ICC is typically 0.02-0.10; 0.05 is a prudent mid.
# If we spread the sample over ~40 schools, m ~ 20:
ICC = 0.05
GIRLS_PER_CLUSTER = 20
DEFF_DERIVED = 1 + (GIRLS_PER_CLUSTER - 1) * ICC          # ~ 1.95
DEFF_PRIMARY = 2.0    # recommended (rounds the derived value up; conservative)
DEFF_PRIMARY_LEAN = 1.5  # "value" variant if THP accepts wider precision / tighter budget

n0 = cochran_n0()
n_fpc = apply_fpc(n0, N_GIRLS)

def full_pipeline(n_fpc_val, deff, nr=NON_RESPONSE):
    return inflate_non_response(n_fpc_val * deff, nr)

girls_recommended = math.ceil(full_pipeline(n_fpc, DEFF_PRIMARY))
girls_lean        = math.ceil(full_pipeline(n_fpc, DEFF_PRIMARY_LEAN))

# Realised margin of error for the ORIGINAL script's 380 (to show it is under-precise):
def realised_moe(n, deff, p=P, z=Z):
    return z * math.sqrt(deff * p * (1 - p) / n)

print("=" * 80)
print("1. PRIMARY COHORT - ADOLESCENT GIRLS 11-18  (N = 9,000)")
print("=" * 80)
print(f"  Cochran n0 (p=0.5, e=0.05, 95% CI)          : {n0:.1f}")
print(f"  After FPC for N=9,000                        : {n_fpc:.1f}")
print(f"  Derived DEFF = 1+(20-1)*0.05                 : {DEFF_DERIVED:.2f}  -> use {DEFF_PRIMARY}")
print(f"  RECOMMENDED n (DEFF {DEFF_PRIMARY}, +10% non-response) : {girls_recommended}")
print(f"  Lean variant n (DEFF {DEFF_PRIMARY_LEAN}, +10% non-response): {girls_lean}")
print(f"  [Context] original script's n = 380 gives MoE = +/-{realised_moe(380, 1.5)*100:.1f}% "
      f"(DEFF 1.5) / +/-{realised_moe(380, 2.0)*100:.1f}% (DEFF 2.0)")
print(f"  [Context] recommended n = {girls_recommended} gives MoE = "
      f"+/-{realised_moe(girls_recommended, DEFF_PRIMARY)*100:.1f}% (its design DEFF {DEFF_PRIMARY})")

# ---- 1b. CHANGE-DETECTION CROSS-CHECK (this is what the ORIGINAL tried to do) -------
# We confirm the precision-based sample is ALSO big enough to detect the REAL
# baseline->endline changes in the ToR impact/outcome matrix. We size per-arm with
# Cohen's h (two independent cross-sections: baseline vs endline), then inflate by
# DEFF and non-response so it is comparable to the number above.
analysis = NormalIndPower()

def per_arm_for_change(p_base, p_target, deff=DEFF_PRIMARY, nr=NON_RESPONSE):
    h = prop.proportion_effectsize(p_base, p_target)
    n_arm = analysis.solve_power(effect_size=h, nobs1=None, power=POWER, alpha=ALPHA, ratio=1.0)
    return math.ceil(inflate_non_response(n_arm * deff, nr)), abs(h)

real_contrasts = [
    ("Girls' decision-making (Impact 1)",        0.13, 0.60),
    ("Adolescent SRHR knowledge (Sub-obj 1)",    0.55, 0.70),
    ("Community norms reject CM (Sub-obj 4)",     0.30, 0.50),
    ("Stakeholder intervention (Sub-obj 2)",      0.29, 0.70),
    ("CM PREVALENCE 18-24, 10pp drop near 0.5*",  0.50, 0.40),  # the binding one; separate frame
]
print("\n  Change-detection cross-check (per-arm n incl. DEFF & non-response):")
for label, pb, pt in real_contrasts:
    n_arm, h = per_arm_for_change(pb, pt)
    flag = "  <-- BINDING, and on a DIFFERENT population (see section 4)" if "PREVALENCE" in label else ""
    print(f"    {label:<44} {pb:.0%}->{pt:.0%}  |h|={h:.3f}  n/arm={n_arm}{flag}")
print("  => The recommended ~%d girls comfortably detects every change measured on the" % girls_recommended)
print("     11-18 cohort. The ONLY contrast that rivals it is CM prevalence among 18-24")
print("     women, which is a separate frame (section 4) - NOT the 11-18 girls.")

# ---- 1c. Proportional allocation of girls by SCHOOL count (correct key here) --------
# Girls are reached through the 128 schools, so school-count weighting is appropriate
# for THIS group (only). 24+16+36+24+28 = 128.
schools_per_upazila = {
    "Babuganj": 24, "Agailjhara": 16, "Jhalokathi Sadar": 36, "Bhuapur": 24, "Gopalpur": 28,
}
tot_schools = sum(schools_per_upazila.values())
school_w = {k: v / tot_schools for k, v in schools_per_upazila.items()}
girls_alloc = largest_remainder(girls_recommended, school_w)
print(f"\n  Allocation of {girls_recommended} girls by school count (sums exactly, no drift):")
for u, n in girls_alloc.items():
    print(f"    {u:<18}: {n}")
assert sum(girls_alloc.values()) == girls_recommended

# =====================================================================================
# 2. SECONDARY DIRECT GROUPS  (consistent method: Cochran -> FPC -> DEFF -> non-response)
# =====================================================================================
# Frame type drives the design effect AND the allocation key:
#   "school"    -> multi-stage via schools  -> DEFF 2.0, allocate by school counts
#   "community" -> multi-stage via villages -> DEFF 1.5, allocate by union counts
#   "list"      -> near-list / institutional -> DEFF 1.2, allocate by union counts
# When the resulting n exceeds ~60% of N, a CENSUS is cheaper and removes sampling
# error entirely - we flag it rather than sample.
unions_per_upazila = {  # 6+4+9+6+7 = 32 unions (cross-checked against the ToR table)
    "Babuganj": 6, "Agailjhara": 4, "Jhalokathi Sadar": 9, "Bhuapur": 6, "Gopalpur": 7,
}
tot_unions = sum(unions_per_upazila.values())
union_w = {k: v / tot_unions for k, v in unions_per_upazila.items()}

DEFF_BY_FRAME = {"school": 2.0, "community": 1.5, "list": 1.2}
CENSUS_THRESHOLD = 0.60

secondary_groups = {
    # group                         (N,    frame)
    "Adolescent boys":              (1800, "school"),
    "Parents and guardians":        (2100, "community"),
    "Women leaders & GGS leaders":  (300,  "list"),
    "VDT volunteers":               (1512, "community"),
    "Teachers & faith leaders":     (840,  "community"),
    "UCMPC members":                (672,  "list"),
}

print("\n" + "=" * 80)
print("2. SECONDARY DIRECT GROUPS  (Cochran + FPC + DEFF + non-response)")
print("=" * 80)
secondary_targets = {}
for group, (N, frame) in secondary_groups.items():
    deff = DEFF_BY_FRAME[frame]
    n = inflate_non_response(apply_fpc(cochran_n0(), N) * deff)
    n = math.ceil(n)
    frac = n / N
    if frac >= CENSUS_THRESHOLD:
        secondary_targets[group] = N  # census
        print(f"  {group:<30} N={N:<5} frame={frame:<9} n={n} ({frac:.0%}) "
              f"-> CENSUS ALL {N} (sampling fraction too high to bother sampling)")
    else:
        secondary_targets[group] = n
        print(f"  {group:<30} N={N:<5} frame={frame:<9} DEFF={deff} -> n={n} ({frac:.0%})")

# Allocation of each secondary group across upazilas, by the RIGHT key per frame
print("\n  Per-upazila allocation (school-key for school frame, union-key otherwise):")
for group, (N, frame) in secondary_groups.items():
    target = secondary_targets[group]
    weights = school_w if frame == "school" else union_w
    alloc = largest_remainder(target, weights)
    key_name = "school" if frame == "school" else "union"
    tag = " (CENSUS)" if target == N else ""
    print(f"  {group} - total {target}{tag}, by {key_name} count:")
    print("    " + "  ".join(f"{u}:{n}" for u, n in alloc.items()))
    assert sum(alloc.values()) == target

# =====================================================================================
# 3. MANDATORY INSTITUTIONAL CENSUS  (NOT sampled - the ToR requires full coverage)
# =====================================================================================
# ToR scope-of-work bullets require assessing ALL committees and ALL schools:
#   - functionality assessment of ALL UCMPCs: 32 union + 5 upazila = 37 committees
#   - protection/prevention implementation in ALL 128 target schools
# These are CENSUSES of institutions (a checklist per institution), distinct from the
# individual UCMPC-member KAP survey in section 2.
print("\n" + "=" * 80)
print("3. MANDATORY INSTITUTIONAL CENSUS (full enumeration, per ToR scope of work)")
print("=" * 80)
print("  UCMPC functionality assessment : 37 committees (32 union + 5 upazila) - CENSUS")
print("  School YEH-Unit / prevention   : 128 schools - CENSUS")
print("  (These are institution-level checklists, separate from the member KAP survey.)")

# =====================================================================================
# 4. SEPARATE FRAME - CHILD-MARRIAGE PREVALENCE COHORT (women 18-24)   ** GAP **
# =====================================================================================
# Impact indicator 4 ("% of women 18-24 married before 18; decrease >=10pp") is the
# statistically MOST DEMANDING indicator (detecting a 10pp change near p=0.5), AND it
# is measured on women aged 18-24, who are NOT in the 9,000 adolescent-girls frame.
# The ToR gives no population size or sampling frame for this cohort -> this is a real
# gap the consultant MUST flag and resolve (e.g., household listing in sampled clusters).
n_arm_cm, h_cm = per_arm_for_change(0.50, 0.40)  # already includes DEFF 2.0 + non-response
print("\n" + "=" * 80)
print("4. SEPARATE FRAME: CHILD-MARRIAGE PREVALENCE COHORT (women 18-24)  ** ToR GAP **")
print("=" * 80)
print(f"  Detect a 10pp drop (50%->40%) at 80% power, |h|={h_cm:.3f}")
print(f"  Indicative n per round (baseline) incl. DEFF 2.0 + non-response: {n_arm_cm}")
print("  ACTION: ToR provides no 18-24 population/frame. Propose a household-listing")
print("          sub-sample in the selected clusters; do NOT fold this into the 11-18")
print("          girls sample. Without this, indicator 4 cannot be baselined credibly.")

# =====================================================================================
# 5. QUALITATIVE SAMPLING  (refined: disaggregated, saturation-driven)
# =====================================================================================
# The original qualitative matrix was reasonable. Refinements:
#  - FGDs with girls split by age (11-14 / 15-18) AND marital status where ethical,
#    because norms and risk differ sharply by these axes (do-no-harm: never mix
#    married/at-risk girls with general groups; female facilitators only).
#  - State the saturation rule so the count is a planned MINIMUM, not a hard cap.
upazilas = list(schools_per_upazila.keys())
print("\n" + "=" * 80)
print("5. QUALITATIVE SAMPLING MATRIX (planned minimums; extend to thematic saturation)")
print("=" * 80)
fgd_segments = [
    "Adolescent girls 11-14", "Adolescent girls 15-18 (unmarried)",
    "Adolescent boys 13-18", "Parents/guardians", "Women leaders",
]
print("  FGDs (2 per upazila per segment, 6-8 participants, female facilitators for girls):")
for s in fgd_segments:
    print(f"    {s:<36}: {len(upazilas)*2} sessions")
kii_groups = ["Teachers/faith leaders", "UCMPC & UP representatives", "Local govt / duty bearers"]
print("  KIIs (3 per upazila):")
for g in kii_groups:
    print(f"    {g:<36}: {len(upazilas)*3} interviews")
idi_groups = ["At-risk / married adolescent girls", "Parents who considered early marriage"]
print("  IDIs (2 per upazila; trauma-informed, referral pathway on standby):")
for g in idi_groups:
    print(f"    {g:<36}: {len(upazilas)*2} interviews")
print("  RULE: numbers above are MINIMUMS; keep collecting until no new themes emerge.")

# =====================================================================================
# 6. GRAND TOTAL (quantitative individual interviews)
# =====================================================================================
total_quant = girls_recommended + sum(secondary_targets.values())
print("\n" + "=" * 80)
print("6. QUANTITATIVE INTERVIEW TOTALS")
print("=" * 80)
print(f"  Adolescent girls (primary)        : {girls_recommended}")
for g, n in secondary_targets.items():
    print(f"  {g:<33}: {n}")
print(f"  {'-'*33}")
print(f"  TOTAL individual interviews        : {total_quant}")
print(f"  (original sampling.py total was ~{380 + 328 + 336 + 172 + 317 + 271 + 251})")
