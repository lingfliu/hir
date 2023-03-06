# HIR阶段1架构规划

## 推理引擎示例
详见 `main.py`

## 算法流程
按以下流程规划各功能接口
1. Dataloader 数据导入器，按视频流，视频文件，图片，amc/bvh/c3d等进行划分
2. Preprocess 预处理，包含：归一化（必选），降噪（可选），域转换（可选），压缩（可选）
3. Motion2Vec 编码
4. NN 神经网络推理
5. Posprocess 后处理，包含：增强算法，语义转换

## 算法辅助功能
1. Visual 数据，标签，分析结果可视化代码
2. Utils 工具类：计算，存储等

## 软件功能
1. RPC/Restful 服务器，采用flask实现