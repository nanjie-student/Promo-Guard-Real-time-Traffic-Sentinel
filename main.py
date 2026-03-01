import subprocess
import sys

def run_step(command, description):
    print(f"--- Starting: {description} ---")
    result = subprocess.run([sys.executable, command])
    if result.returncode != 0:
        print(f"Error during {description}")
        sys.exit(1)

if __name__ == "__main__":
    # 1. 生成数据
    run_step("gen_traffic.py", "Data Generation")
    
    # 2. 训练模型
    run_step("model_train.py", "Model Training")
    
    print("Full Pipeline Completed!")