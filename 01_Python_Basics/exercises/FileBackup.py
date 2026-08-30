import shutil
import os

class FileBackup:
    """
    上下文管理器：进入时自动备份文件（生成 .bak 副本），退出时打印备份路径。
    """
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.backup_path = filepath + ".bak"

    def __enter__(self):
        shutil.copy2(self.filepath, self.backup_path)  # 复制文件内容及元数据
        return self  # 可返回自身或备份路径，这里返回自身方便访问属性

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"备份文件已保存至: {self.backup_path}")
        # 返回 False 表示不吞异常，None 等同于 False
        return False

# 示例用法
with FileBackup("data.txt") as fb:
    # 在 with 块内修改原文件
    with open(fb.filepath, "a") as f:
        f.write("新内容\n")
    print("文件已修改")