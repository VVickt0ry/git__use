
# 1. To https://github.com/VVickt0ry/git__use.git
#  ! [rejected]        main -> main (fetch first)
# error: failed to push some refs to 'https://github.com/VVickt0ry/git__use.git'
# hint: Updates were rejected because the remote contains work that you do not have locally.

# ! [rejected]：表示推送被拒绝
# 关键原因：remote contains work that you do not have locally（远程有你本地没有的内容）
# Git的推送规则是：只有当本地分支包含远程分支的所有提交记录时，才能成功推送

# 拉取远程最新内容并合并到本地
# 处理合并冲突（仅当步骤 1 提示冲突时需要）
# 重新推送本地提交到远程







# 2. Processes are running in session:表示当前会话中仍有进程在执行，没有正常结束。
# Close anyway? 无论如何都要关闭这个会话吗

# 这个提示最常出现在以下情况：
# 执行git commit时，进入了Vim编辑器编辑提交信息，但没有正常保存退出（比如直接关闭了终端窗口），导致Git进程还在等待编辑器返回结果
# 执行git merge、git rebase 等操作时，中途关闭了终端，导致操作未完成，子进程仍在运行

# 在 Vim 中按 Esc → 输入 :q! 强制退出，终止提交
# 执行 Git 操作时，尽量在终端内正常完成流程（比如编辑提交信息后用 :wq 保存退出，而不是直接关窗口）






















