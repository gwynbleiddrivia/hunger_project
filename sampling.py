# Calculating the required sample size 

import math # to round up census later
from statsmodels.stats.power import NormalIndPower
import statsmodels.stats.proportion as prop

baseline_proportion = 0.13 # 13% of surveyed unmarried girls state that they are able to participate in decisions regarding their marriage
target_proportion = 0.23 # Goal of decreasing child marriage by 10 percentage increase

alpha = 0.05
statistical_power = 0.8

effect_size = prop.proportion_effectsize(baseline_proportion, target_proportion)
analysis = NormalIndPower()
base_sample = analysis.solve_power(effect_size = effect_size, nobs1=None, power=statistical_power, alpha=alpha, ratio=1.0)

print(f"Required sample size per group: {math.ceil(base_sample)}")
# Required sample size per group: 228

# 228 is a Simple Random Sample, assuming a perfectly randomed distribution of the sample, not accounting for non-response and other issues that may arise during data collection. 


# Applying a standard design effect of 1.5 to correct the variance and to account for the complex situations like similarity of responses within same clusters or same social envs (like same school, same community or same villages)
design_effect = 1.5

# Assuming 10% of the survey is unusable ore refused due to no response 
non_response_rate = 0.1


clustered_sample = base_sample * design_effect # Adjusting for design effect

final_adjusted_sample = clustered_sample / (1 - non_response_rate) # Adjusting for non-response

required_sample_size = math.ceil(final_adjusted_sample)
print(f"Adjusted required sample size per group: {required_sample_size}")
# Adjusted required sample size per group: 380
# 380/9000 is 4.2%, less than 5% of the total population of adolescent girls, so FPC Yamane formula is not needed. Nevertheless, Yamane formula in this case gives almost the same result.



# Proportional allocation across Upazillas, school number
upazilla_school_counts = {
    "Babuganj": 24,
    "Agailjhara": 16,
    "Jhalokathi Sadar": 36,
    "Bhuapur": 24,
    "Gopalpur": 28
}

total_schools = sum(upazilla_school_counts.values())
allocated_samples = {}

for upazilla, school_count in upazilla_school_counts.items():
    weight_upazilla = school_count / total_schools
    target_upazilla_sample = weight_upazilla * required_sample_size
    allocated_samples[upazilla] = target_upazilla_sample

for upazilla, target in allocated_samples.items():
    print(f"{upazilla}: {math.ceil(target)} samples")

print(f"Total allocated samples: {math.ceil(sum(allocated_samples.values()))}")
"""
Babuganj: 72 samples
Agailjhara: 48 samples
Jhalokathi Sadar: 107 samples
Bhuapur: 72 samples
Gopalpur: 84 samples
Total allocated samples: 380
"""




margin_of_error = 0.05
secondary_populations = {
    "Adolescent boys": 1800,
    "Parents and guardians": 2100,
    "Women leaders": 300,
    "VDT volunteers": 1512,
    "Teachers and faith leaders": 840,
    "UCMPC members": 672
}
# Using Yamane's formula: n = N / (1 + N * e^2)

for group, population in secondary_populations.items():
    # Calculate the denominator: 1 + N(e^2)
    denominator = 1 + (population * (margin_of_error ** 2))
    
    # Calculate the required sample and round up
    sample_size = math.ceil(population / denominator)
    
    print(f"{group}: {sample_size} surveys")

"""
Adolescent boys: 328 surveys
Parents and guardians: 336 surveys
Women leaders: 172 surveys
VDT volunteers: 317 surveys
Teachers and faith leaders: 271 surveys
UCMPC members: 251 surveys
"""



total_schools = 128
upazila_weights = {
    "Babuganj": 24 / total_schools,
    "Agailjhara": 16 / total_schools,
    "Jhalokathi Sadar": 36 / total_schools,
    "Bhuapur": 24 / total_schools,
    "Gopalpur": 28 / total_schools
}

secondary_targets = {
    "Adolescent boys": 328,
    "Parents and guardians": 336,
    "Women leaders": 172,
    "VDT volunteers": 317,
    "Teachers and faith leaders": 271,
    "UCMPC members": 251
}

for group, total_sample in secondary_targets.items():
    print(f"\n{group} (Total: {total_sample} surveys)")
    
    group_tally = 0
    for upazila, weight in upazila_weights.items():
        # Distribute the group's total sample by the Upazila's weight
        allocated = round(total_sample * weight)
        group_tally += allocated
        print(f"  {upazila}: {allocated}")
        
    # Verify the rounding math stays close to the target
    if group_tally != total_sample:
        print(f"  *Note: Rounding adjusted total to {group_tally}")


"""
Adolescent boys (Total: 328 surveys)
  Babuganj: 62
  Agailjhara: 41
  Jhalokathi Sadar: 92
  Bhuapur: 62
  Gopalpur: 72
  *Note: Rounding adjusted total to 329

Parents and guardians (Total: 336 surveys)
  Babuganj: 63
  Agailjhara: 42
  Jhalokathi Sadar: 94
  Bhuapur: 63
  Gopalpur: 74

Women leaders (Total: 172 surveys)
  Babuganj: 32
  Agailjhara: 22
  Jhalokathi Sadar: 48
  Bhuapur: 32
  Gopalpur: 38

VDT volunteers (Total: 317 surveys)
  Babuganj: 59
  Agailjhara: 40
  Jhalokathi Sadar: 89
  Bhuapur: 59
  Gopalpur: 69
  *Note: Rounding adjusted total to 316

Teachers and faith leaders (Total: 271 surveys)
  Babuganj: 51
  Agailjhara: 34
  Jhalokathi Sadar: 76
  Bhuapur: 51
  Gopalpur: 59

UCMPC members (Total: 251 surveys)
  Babuganj: 47
  Agailjhara: 31
  Jhalokathi Sadar: 71
  Bhuapur: 47
  Gopalpur: 55
"""






## FGD, KIIs, and IDIs sample size


upazilas = ["Babuganj", "Agailjhara", "Jhalokathi Sadar", "Bhuapur", "Gopalpur"]

# FGDs: For homogenous community norms
fgd_groups = ["Adolescent girls", "Adolescent boys", "Parents and guardians", "Women leaders"]
fgds_per_upazila = 2

# KIIs: For institutional and expert perspectives
kii_groups = ["Teachers and faith leaders", "UCMPC members", "Local government officials"]
kiis_per_upazila = 3

# IDIs: Added per ToR requirement for sensitive, individual narratives
idi_groups = ["At-risk adolescent girls", "Parents who considered early marriage"]
idis_per_upazila = 2

print("\n--- Qualitative Sampling Matrix ---")

print("Focus Group Discussions (FGDs):")
for group in fgd_groups:
    total_fgds = len(upazilas) * fgds_per_upazila
    print(f"{group}: {total_fgds} sessions ({fgds_per_upazila} per Upazila)")
    
print("\nKey Informant Interviews (KIIs):")
for group in kii_groups:
    total_kiis = len(upazilas) * kiis_per_upazila
    print(f"{group}: {total_kiis} interviews ({kiis_per_upazila} per Upazila)")

print("\nIn-Depth Interviews (IDIs):")
for group in idi_groups:
    total_idis = len(upazilas) * idis_per_upazila
    print(f"{group}: {total_idis} interviews ({idis_per_upazila} per Upazila)")
    
print("\n--- Institutional Functionality Assessments ---")
print("Secondary Schools: 128 locations")
print("Child Marriage Prevention Committees (UCMPCs): 37 committees")



"""
Focus Group Discussions (FGDs):
Adolescent girls: 10 sessions (2 per Upazila)
Adolescent boys: 10 sessions (2 per Upazila)
Parents and guardians: 10 sessions (2 per Upazila)
Women leaders: 10 sessions (2 per Upazila)

Key Informant Interviews (KIIs):
Teachers and faith leaders: 15 interviews (3 per Upazila)
UCMPC members: 15 interviews (3 per Upazila)
Local government officials: 15 interviews (3 per Upazila)

In-Depth Interviews (IDIs):
At-risk adolescent girls: 10 interviews (2 per Upazila)
Parents who considered early marriage: 10 interviews (2 per Upazila)

--- Institutional Functionality Assessments ---
Secondary Schools: 128 locations
Child Marriage Prevention Committees (UCMPCs): 37 committees
"""