# libraries
import matplotlib.pyplot as plt
import squarify    # pip install squarify (algorithm for treemap)
import pandas as pd

# Create a data frame with fake data
df = pd.DataFrame({'2020_amount':[1203715085.77,5566676161.54,398745781.93,569617581.78,10000000000.00,827794389.62], 'funding_source':["GOG Contingency Fund", "IMF", "AfDB", "EU", "BOG-COVID-19 BONDS","Other GoG"] })

# plot it
squarify.plot(sizes=df['2020_amount'], label=df['funding_source'], alpha=.9 )
plt.axis('off')
plt.show()