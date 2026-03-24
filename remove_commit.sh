#!/bin/bash

echo "========================================"
echo "删除包含 API Key 的 commit"
echo "========================================"

TARGET_COMMIT="b64d0bdee07ff1b4b64b4fa03bd6361186a940f3"

echo ""
echo "目标 commit: $TARGET_COMMIT"
echo ""

# 设置环境变量避免警告
export FILTER_BRANCH_SQUELCH_WARNING=1

# 使用 git filter-branch 删除特定 commit
echo "正在删除敏感 commit..."
git filter-branch -f --commit-filter "
if [ \"\$GIT_COMMIT\" = \"$TARGET_COMMIT\" ]; then
    echo \"Skipping commit: \$GIT_COMMIT\"
    skip_commit
else
    git commit-tree \"\$@\"
fi
" HEAD

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Commit 删除成功!"
    echo ""
    
    # 清理备份
    echo "清理备份引用..."
    for ref in $(git for-each-ref --format='%(refname)' refs/original/); do
        git update-ref -d $ref
    done
    
    # 垃圾回收
    echo "执行垃圾回收..."
    git reflog expire --expire=now --all
    git gc --prune=now --aggressive
    
    echo ""
    echo "========================================"
    echo "验证结果"
    echo "========================================"
    
    # 验证
    if git log --all --oneline | grep -q "$TARGET_COMMIT"; then
        echo "❌ Commit 仍然存在"
    else
        echo "✅ Commit 已成功删除!"
    fi
    
    echo ""
    echo "现在可以执行强制推送："
    echo "git push -f origin master"
else
    echo ""
    echo "❌ 删除失败"
fi
