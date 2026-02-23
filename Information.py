# 1. 电脑硬盘中存放代码的地方叫做本地仓库，编写代码的地方称为工作区，网页上如github存放代码的地方叫做远程仓库
#    也有认为.git文件夹里是本地仓库，仓库根目录下的文件是工作区，远程仓库是github上的仓库，这个说法也可以接受


# 2. 本地仓库和远程仓库之间的关系是：本地仓库可以通过git push命令将代码推送到远程仓库
#    远程仓库可以通过git pull命令将代码拉取到本地仓库
#    暂存区是本地仓库中的一个区域，用来暂时存放代码修改的地方，只有将代码修改添加到暂存区中，才能提交到本地仓库中
 

# 3. 在github上创建完仓库后就需要将本地仓库和远程仓库进行关联，也叫做绑定，目的是使两仓库的代码保持同步 

# 第一种方式是git clone 【远程仓库地址】，把远程的git仓库克隆到本地，适合本地仓库没有代码的情况

# 第二种方式是git remote add origin 【远程仓库地址】，适合本地仓库已经有代码的情况
# 这需要先创建一个本地仓库，git init命令可以创建一个本地仓库，然后再使用命令将新创建的本地库与远程库进行绑定



#-----------------------------------------------------------------------------------------------------------------------------------------------
# 一些git命令的输出信息的含义：

# 1. git status得到的信息永远按分支状态 → 已追踪文件变更 → 未追踪文件 → 暂存区总结的顺序
# on branch main：你当前所在的分支是main

# Your branch is up to date with 'origin/main'：你的本地main分支和远程orgin/main分支是同步的，没有任何差异
# 同步代表着本地没有未推送的提交；远程没有未拉取的提交；分支层面无任何冲突/不同步问题

# Your branch is ahead of 'origin/main' by 1 commit.
# 本地main分支的提交记录，比GitHub远程origin/main分支多1个（你之前执行过git commit但没执行git push）

# Changes to be committed 确定要提交的状态即暂存区
# renamed: old_file_name -> new_file_name 表示文件被重命名了
# deleted: file_name 表示文件被删除了

# Changes not staged for commit：有文件被修改了，但还没有添加到暂存区  
# 乱码文件名终端对中文/特殊字符的编码转义，Git能识别，只是显示乱码

# Untracked files：有文件没有被Git追踪到，说明这些文件是新添加的，Git还没有记录它们的状态
# 这些文件需要使用git add命令添加到暂存区

# no changes added to commit 
# 表示没有任何文件被添加到暂存区，也没有任何文件被修改




# 2. git push的日志信息，大体包含以下内容
# Enumerating objects: 4, done. Git 正在枚举（统计）要推送到远程的「数据对象」（文件 / 提交记录 / 版本数据等），共统计到 4 个对象，已完成枚举

# Counting objects: 100% (4/4), done. 
# 核对要推送的对象数量，确认总共有 4 个对象需要被推送，已完成核对

# Delta compression using up to 16 threads
# Git启用增量压缩（只传输文件变更的部分，而非整个文件），最多用16个线程并行压缩（线程数由你的 CPU 决定）

# Compressing objects: 100% (3/3), done.
# 压缩要传输的3个核心对象，已完成

# Writing objects: 100% (3/3), 2.79 KiB
# 传输速度和传输量，已完成传输

# Total 3 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
# 本次传输3个对象，其中1个是增量数据（只传了文件修改的部分）；无重复传输的内容

# remote: Resolving deltas: 100% (1/1), completed with 1 local object.
# GitHub远程服务器正在解析收到的增量数据，100% 完成，且和本地数据匹配无误

# To https://github.com/VVickt0ry/git__use.git
# 本次推送的目标远程仓库地址

# dc39a89..ede8c05 main -> main


# 5. 在github上传代码前，会进行登录并检验你上传的代码仓库是不是你的，有没有权限
# 常用的检验方式有两种
# https方式和ssh方式，https方式需要输入用户名和密码，ssh方式需要生成ssh密钥并上传到github上，这样就可以免去每次上传代码都要输入用户名和密码的麻烦
# 还可以使用：用户名+pat令牌



# 6. git会自动创建的master分支，master分支是默认的主分支，所有的代码修改都会提交到master分支上
# 这个分支一般用于保存经过测试的稳定代码
# 想开发新功能，就要再复制出一个develop分支，这个分支用来保存开发过程中的代码



# 7. 想合并分支的话，需要先在develop分支上，把文件先提交到暂存区，再提交代码文件，
# 之后再切换回master分支，再使用命令进行合并



# 8. 所有项目文件都要放在和.git同一目录下，绝对不要修改 / 写入.git文件夹里的任何内容
# 这个文件夹完全由Git自动管理，手动修改/ 删除 / 写入文件都会导致仓库损坏（比如无法提交、推送，甚至丢失版本记录）
# Git管理的是 “仓库根目录下的所有文件 / 文件夹”（.git除外）
# 仓库根目录可以嵌套子文件夹（比如code/、figures/）：
# 只要子文件夹在根目录下（和.git同级），Git 都会正常管理



# (HEAD -> main, origin/main, origin/HEAD)
# HEAD -> main：你当前正处于本地main分支
# origin/main：本地main分支和 GitHub 远程main分支指向同一个提交（同步）；
# origin/HEAD：GitHub 远程仓库的 “默认分支”（就是main）
# Initial commit：这是你第一次初始化仓库时的默认提交信息（GitHub 创建仓库时自动生成，或本地git init后第一次commit的备注），代表仓库的 “起点”






