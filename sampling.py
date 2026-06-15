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