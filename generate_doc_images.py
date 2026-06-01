import matplotlib.pyplot as plt

# 图1：文件夹结构图
fig, ax = plt.subplots(figsize=(8, 6))
ax.axis('off')
ax.set_title('推荐仓库目录结构', fontsize=16, pad=20)
texts = [
    ('Data', 0.5, 0.9),
    ('data/', 0.2, 0.75),
    ('raw/', 0.1, 0.62),
    ('processed/', 0.3, 0.62),
    ('notebooks/', 0.7, 0.75),
    ('results/', 0.7, 0.62),
    ('docs/', 0.7, 0.49),
    ('README.md', 0.5, 0.35),
    ('requirements.txt', 0.5, 0.25),
]
for text, x, y in texts:
    ax.text(x, y, text, fontsize=12, ha='center', va='center', bbox=dict(facecolor='#f7f7f7', edgecolor='#333', boxstyle='round,pad=0.3'))

arrow_params = dict(arrowstyle='-|>', color='#444', mutation_scale=12)
ax.annotate('', xy=(0.2, 0.78), xytext=(0.5, 0.86), arrowprops=arrow_params)
ax.annotate('', xy=(0.7, 0.78), xytext=(0.5, 0.86), arrowprops=arrow_params)
ax.annotate('', xy=(0.1, 0.65), xytext=(0.2, 0.73), arrowprops=arrow_params)
ax.annotate('', xy=(0.3, 0.65), xytext=(0.2, 0.73), arrowprops=arrow_params)
ax.annotate('', xy=(0.7, 0.65), xytext=(0.5, 0.73), arrowprops=arrow_params)
ax.annotate('', xy=(0.7, 0.52), xytext=(0.5, 0.73), arrowprops=arrow_params)
ax.annotate('', xy=(0.5, 0.33), xytext=(0.5, 0.6), arrowprops=arrow_params)
ax.annotate('', xy=(0.5, 0.23), xytext=(0.5, 0.5), arrowprops=arrow_params)
fig.savefig('docs/folder_structure.png', dpi=150, bbox_inches='tight')
plt.close(fig)

# 图2：分析流程图
fig, ax = plt.subplots(figsize=(10, 6))
ax.axis('off')
ax.set_title('智慧能源数据分析流程', fontsize=16, pad=20)
steps = [
    '1. 读取原始数据',
    '2. KNN 填充缺失值',
    '3. IQR 异常检测',
    '4. 物理异常过滤',
    '5. 特征标准化',
    '6. KMeans 聚类分析',
    '7. 结果导出与可视化',
]
for i, text in enumerate(steps):
    ax.text(0.5, 0.85 - i * 0.11, text, fontsize=12, ha='center', va='center', bbox=dict(facecolor='#eaf2f8', edgecolor='#3a6ea5', boxstyle='round,pad=0.4'))
    if i < len(steps) - 1:
        ax.annotate('', xy=(0.5, 0.78 - i * 0.11), xytext=(0.5, 0.76 - i * 0.11), arrowprops=dict(arrowstyle='-|>', color='#333', mutation_scale=12))
fig.savefig('docs/analysis_workflow.png', dpi=150, bbox_inches='tight')
plt.close(fig)

print('Generated docs/folder_structure.png and docs/analysis_workflow.png')
