# 定义变量
PYTHON = venv/bin/python
PIP = venv/bin/pip

.PHONY: setup generate train run-all

# 1. 安装环境
setup:
	$(PYTHON) -m venv venv
	$(PIP) install numpy pandas torch transformers matplotlib

# 2. 生成数据
generate:
	$(PYTHON) gen_traffic.py

# 3. 训练模型
train:
	$(PYTHON) model_train.py

# 4. 一键运行全流程 (Your Unified Tool)
run-all: generate train
	@echo "Data generated and Model trained successfully!"