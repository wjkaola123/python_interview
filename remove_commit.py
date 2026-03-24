import subprocess
import os

project_path = r"C:\Users\wjkao\PycharmProjects\pythonProject"
os.chdir(project_path)

print("="*60)
print("删除包含 API Key 的 commit")
print("="*60)

# 获取所有 commit 列表
print("\n1️⃣ 获取 commit 历史...")
result = subprocess.run(['git', 'log', '--oneline'], capture_output=True, text=True)
commits = result.stdout.strip().split('\n')
print(f"总共有 {len(commits)} 个 commits")

# 找到目标 commit 的位置
target_commit = "b64d0bd"
target_index = None
for i, commit in enumerate(commits):
    if target_commit in commit:
        target_index = i
        print(f"\n✅ 找到目标 commit: {commit}")
        break

if target_index is None:
    print(f"\n❌ 未找到目标 commit: {target_commit}")
    exit(1)

# 获取目标 commit 的父 commit
parent_count = target_index + 1
print(f"\n2️⃣ 准备重写历史，需要 rebase {parent_count} 个 commits")

# 使用 git filter-branch 删除特定 commit
print("\n3️⃣ 使用 git filter-branch 删除敏感 commit...")
filter_cmd = f"git filter-branch -f --commit-filter 'if [ \"$GIT_COMMIT\" = \"{target_commit}dee07ff1b4b64b4fa03bd6361186a940f3\" ]; then skip_commit; else git commit-tree \"$@\"; fi' HEAD"
result = subprocess.run(filter_cmd, shell=True, capture_output=True, text=True)
print(result.stdout)
if result.stderr:
    print(result.stderr)

# 清理 backup refs
print("\n4️⃣ 清理备份引用...")
subprocess.run(['git', 'for-each-ref', '--format="%(refname)"', 'refs/original/'], 
               capture_output=True, text=True)
subprocess.run('git for-each-ref --format="%(refname)" refs/original/ | ForEach-Object { git update-ref -d $_ }', 
               shell=True, capture_output=True)

# 垃圾回收
print("\n5️⃣ 执行垃圾回收...")
result = subprocess.run(['git', 'reflog', 'expire', '--expire=now', '--all'], 
                       capture_output=True, text=True)
result = subprocess.run(['git', 'gc', '--prune=now', '--aggressive'], 
                       capture_output=True, text=True)
print("垃圾回收完成")

# 验证
print("\n6️⃣ 验证 commit 是否已删除...")
result = subprocess.run(['git', 'log', '--all', '--oneline'], capture_output=True, text=True)
if target_commit in result.stdout:
    print(f"\n❌ Commit {target_commit} 仍然存在")
else:
    print(f"\n✅ Commit {target_commit} 已成功删除!")

print("\n7️⃣ 检查是否还有敏感信息...")
result = subprocess.run(['git', 'log', '-p', '--all'], capture_output=True, text=True)
if "sk-" in result.stdout and len([line for line in result.stdout.split('\n') if 'sk-' in line and 'api_key' in line.lower()]) > 0:
    print("⚠️ 警告：可能还有 API Key 存在于历史中")
else:
    print("✅ 没有发现明显的 API Key")

print("\n" + "="*60)
print("现在可以尝试强制推送：git push -f origin master")
print("="*60)
