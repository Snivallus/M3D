# from LaMed.src.model.language_model import LamedLlamaForCausalLM, LamedPhi3ForCausalLM
import sys
import os

# 关键路径设置（根据实际位置修改）
project_root = os.path.abspath("/kaggle/working/M3D")  # 指向包含LaMed的父目录
sys.path.insert(0, project_root)  # 必须插入到路径列表最前面

# 测试路径是否生效
try:
    import LaMed
    print("✅ LaMed包导入成功")
except ImportError:
    print("❌ LaMed包导入失败, 请检查路径设置")
    exit(1)