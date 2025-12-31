# practicing with streams
import sys

# 输出提示信息
sys.stdout.write("Enter the name of the file: ")
sys.stdout.flush()  # 强制刷新缓冲区，确保提示信息立即显示
file = sys.stdin.readline().strip()  # 去掉换行符

try:
    with open(file, "r") as F:
        while True:
            line = F.readline()  # 一次读取一行，避免内存占用过高
            if not line:  # 文件结束时退出循环
                sys.stderr.write("End of file reached\n")
                break
            sys.stdout.write(line)  # 输出每一行内容
except FileNotFoundError:
    sys.stderr.write(f"Error: File '{file}' not found.\n")
except Exception as e:
    sys.stderr.write(f"An error occurred: {e}\n")
