# 智慧能源数据分析项目

> 本项目针对智慧能源系统运行数据，完成数据预处理、异常检测、聚类分析与可视化展示，适合上传到 GitHub 仓库并作为数据分析报告。

## 项目概述

本项目以 `Data SJ.ipynb` 为主分析文件，使用 `pandas`、`scikit-learn`、`matplotlib`、`seaborn` 等工具完成:

- 原始数据读取与缺失值检查
- KNN 填充缺失值
- IQR 异常值识别与可视化标记
- 物理异常过滤（回水温度 <= 供水温度）
- 计算冷负荷并进行标准化
- KMeans 聚类与簇数优选（手肘法 + 轮廓系数）
- 聚类结果导出与工况分析

## 当前工作区文件说明

- `Data SJ.ipynb` - 主分析 notebook
- `智慧能源作业_数据预处理.xlsx` - 预处理/清洗结果（当前输出）
- `智慧能源作业_最终聚类结果.xlsx` - 聚类分析结果
- `docs/` - 推荐放置项目结构图、流程图和说明图像
- `data/raw/` - 推荐存放原始数据文件
- `data/processed/` - 推荐存放清洗后和中间结果数据
- `notebooks/` - 推荐存放 Jupyter Notebook 文件
- `results/` - 推荐存放最终导出的结果文件

## 推荐目录结构

```text
/Data
  /data
    /raw               # 原始数据
    /processed         # 清洗后、分析中间结果
  /notebooks           # Jupyter notebook 文件
  /results             # 最终分析结果文件
  /docs                # 项目结构图、流程图、报告图示
  README.md
  requirements.txt
```

## 运行说明

1. 使用 Python 3.8+ 环境
2. 安装依赖:

```bash
pip install -r requirements.txt
```

3. 打开 `Data SJ.ipynb` 并按照顺序运行各个代码单元
4. 输出文件将保存为:
   - `智慧能源作业_已处理.xlsx`
   - `智慧能源作业_聚类清洗版.xlsx`
   - `智慧能源作业_最终聚类结果.xlsx`

## 关键分析流程

1. 读取 `智慧能源作业.xlsx`
2. 对数值列使用 KNN 填充缺失值
3. 使用 IQR 方法识别并标记异常值
4. 过滤物理异常数据（回水温度 <= 供水温度）
5. 计算冷负荷并进行特征标准化
6. 通过手肘法与轮廓系数选择聚类个数
7. 使用 KMeans 聚类并导出工况标签
8. 可视化分析工况分布与冷负荷变化

## GitHub 上传建议

- 将重要文件放入对应目录
- `data/raw/` 中只放原始数据，不要上传敏感信息
- `docs/` 中放置结构图、流程图、示意图
- 通过 `README.md` 说明分析过程和目录规划
- 可以附加 `LICENSE`、`CONTRIBUTING.md` 以完善仓库

## 仓库地址

`https://github.com/luckys-max/data-analysis`

---

如果你希望，我可以继续帮你把当前文件移动到推荐目录，并生成更多可视化图表。
