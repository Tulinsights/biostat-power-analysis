from statsmodels.stats.power import TTestIndPower

# Parameters for our fictional Blood Pressure drug
effect_size = 0.5  # We expect a medium improvement
alpha = 0.05       # 5% Significance level
power = 0.80       # 80% Power

# Initialize the power analysis object
analysis = TTestIndPower()

# Calculate sample size
sample_size = analysis.solve_power(
    effect_size=effect_size, 
    power=power, 
    alpha=alpha, 
    ratio=1.0, 
    alternative='two-sided'
)

print(f"To detect an effect size of {effect_size}, we need:")
print(f"Approximately {round(sample_size)} patients per group.")

# Bonus: Visualize the Power Curve
import matplotlib.pyplot as plt
analysis.plot_power(dep_var='nobs', nobs=np.arange(5, 100), effect_size=[0.2, 0.5, 0.8])
plt.title('Power Curve: Sample Size vs. Power')
plt.show()
