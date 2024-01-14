import subprocess,os
import random

# 创建仓库
def create_git_repo(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    os.chdir(folder_path)
    subprocess.run(['git', 'init'], shell=True)

# 提交仓库
def commit_git(time):
    subprocess.run(['git', 'add',"."], shell=True)
    subprocess.run(['git', 'commit',f"--date=\"{time}\"","-m",f"DrawOnGit:Draw at {time}"], shell=True)