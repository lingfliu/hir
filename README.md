# Human Interaction Recognition
# 人员交互行为识别算法引擎

## 0. 简介
人员交互行为识别包含人体行为姿态估测，运动序列分类，多人交互与HOI检测等多项任务。
本引擎包含基于单目视频图像与深度视频图像的人员交互行为识别算法，包含训练、推理、数据管理服务。

## 1. 项目结构

- `./models`：模型
- `./detectors`：物体识别与追踪
- `./pose_estimator`：2D 与3D姿态估计
- `./preprocess`：预处理
- `./hir_analysis`：交互行为识别
- `./media_tools`: 视频处理工具

## 2. 运行环境
- Ubuntu 22.04
- Pytorch 1.13
- CUDA 11.6
- Python 3.8

## 3. 示例脚本
推理引擎运行示例见 `main_infer.py`

## 4. 引用
如果您使用了本项目，请引用如下论文：
```
@article{li2021human,
  title={Human Interaction Recognition in Video},
```

