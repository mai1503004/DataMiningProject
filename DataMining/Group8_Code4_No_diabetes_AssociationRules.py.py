import pandas as pd
import squarify
import matplotlib.pyplot as plt
import matplotlib.cm as cm

file_path = r"D:\1. KÌ 1 NĂM 3\1. KHO VÀ KHAI PHÁ DỮ LIỆU\4. CUỐI KÌ\1. DATA\2. DATA KẾT QUẢ\KETQUA_NO_DIABETES\KETQUA_NO_DIABETES_PHANTICH.xlsx"

data = pd.read_excel(file_path, usecols=[0], header=0)

data.columns = ['Factors']

data['Factors'] = data['Factors'].str.split(',')
data['Factors'] = data['Factors'].apply(lambda x: [item.strip().lower() for item in x])  # Loại bỏ khoảng trắng và chuẩn hóa chữ hoa/thường

factor_counts = data['Factors'].explode().value_counts()

min_frequency = 10  

factor_counts = factor_counts[factor_counts >= min_frequency]

labels = factor_counts.index
sizes = factor_counts.values

norm = plt.Normalize(vmin=min(sizes), vmax=max(sizes))  
colors = cm.Reds(norm(sizes)) 

plt.figure(figsize=(12, 8))
squarify.plot(sizes=sizes, label=labels, alpha=0.8, color=colors, edgecolor='black', linewidth=1)

plt.title("Treemap: Tần suất xuất hiện của các yếu tố", fontsize=16)
plt.axis('off') 

plt.show()
