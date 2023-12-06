import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./process_data/01_unemp.csv",sep=",")

#print(df)


filtered_id = df[df["Country Name"] == "Austria"]["2022"].idxmin()
print("Austria's Unemployment in 2022")
print(df[df.index == filtered_id])

# minimum unemploy
min_index = df["2022"].idxmin()
print("Lowest Unemployment of 2022")
print(df[df.index == min_index])


fig, ax = plt.subplots()

x_axis = [df[df.index == filtered_id]["Country Name"], df[df.index == min_index]["Country Name"]]
y_axis = [df[df.index == filtered_id]["2022"], df[df.index == min_index]["2022"]]
bar_labels = ['red', 'blue']
bar_colors = ['tab:red', 'tab:blue']

ax.bar(x_axis, y_axis, label=bar_labels, color=bar_colors)

ax.set_ylabel('fruit supply')
ax.set_title('Fruit supply by kind and color')
ax.legend(title='Fruit color')

plt.show()


