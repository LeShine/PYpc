# PYpc
Python-based crawler test
creating a new branch

--------------------------------------------
提交本地修改到git缓存区：git add filename

推送缓存到git仓库：git commit -m "illustration"

查看分支：git branch

创建分支：git branch branchname

切换分支：git checkout branchname

创建+切换分支：git checkout -b branchname

合并分支到当前分支：git merge branchname

合并分支并保留分支信息：git merge --no-ff -m "illustration"

删除分支：git branch -d branchname

推送本地git仓库到远程仓库：git push origin master

查看分支合并图：git log --graph --pretty=oneline --abbrev-commit

退出log模式：q

暂存工作区：git stash

恢复工作区保留stash：git stash apply

删除stash：git stash drop

回复工作区删除stash：git stash pop

查看stash：git stash list

恢复指定stash：git stash apply stash@{0}

拉取远程仓库：git pull

本地分支与远程分支建立链接：git branch --set-upstream-to branchname origin/branchname

本地创建和远程对应的分支：git checkout -b branch-name origin/branch-name

查看远程库信息：git remote -v

创建标签： git tag name

	默认为HEAD,也可以指定commit id。eg: git tag 001

指定标签信息：git tag -a tagname -m "taginfo"

指定PGP标签： git tag -s tagname -m "taginfo"

查看所有标签：git tag

查看具体标签信息：git show tagname

推送本地标签到远程：git push origin tagname

推送本地所有标签到：git push origin --tags

删除本地标签：git tag -d tagname

删除远程标签：git push origin :refs/tags/tagname

删除远程分支：git push origin :branch_name






--------------------------------------------

git vim order


打开目标文件：vi file-name

解锁vim编辑器进入编辑模式：i

退回锁定模式：esc

进入命令模式：:

不保存退出：quit

保存不退出：write

保存退出：wq

进入可视：右键

复制：选中+Y

粘贴：可视+p

creating a new branch is quick and simple！

git merge test about fast forward





