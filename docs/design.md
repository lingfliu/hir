# HIR阶段1架构规划

## 代码示例
推理：`main_infer.py`

训练：`main_train.py`

可视化：`main_visual.py`

## 算法供能
按设计算法程规划，本项目包含以下功能
1. Dataloader 数据导入器，按视频流，视频文件，图片，amc/bvh/c3d等进行划分
2. Preprocess 预处理，包含：归一化（必选），降噪（可选），域转换（可选），压缩（可选）
3. Motion2Vec 编码 (待实现)
4. TGNN网络推理 (classifier, interact_detector, predictor)
5. Posprocess 后处理，包含：增强算法，语义转换

## 算法辅助功能
1. Visual 数据，标签，分析结果可视化代码
2. Utils 工具类：计算，存储等

## 软件功能
1. RPC/Restful 服务器，采用flask实现

## 核心概念
1. TGNN：Temporal Graph Neural Network
2. Motion2Vec：Motion to Vector，运动序列编码器