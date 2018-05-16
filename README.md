# PYpc
Python-based crawler test
creating a new branch

--------------------------------------------
克隆远程仓库到本地：git clone git_address

查看远程仓库信息：git remote -v

查看远程仓库名：git remote

添加远程仓库：git remote add remote_name git_address

查看具体远程仓库信息：git remote show  remote_name

重命名远程仓库：git remote rename old_name new_name

删除远程仓库（解除与远程仓库的关系）：git remote rm remote_name

提交本地修改到git缓存区：git add file_name

推送缓存到git仓库：git commit -m "illustration"

查看分支：git branch

创建分支：git branch branch_name

切换分支：git checkout branch_name

创建+切换分支：git checkout -b branch_name

合并分支到当前分支：git merge branch_name

合并分支并保留分支信息：git merge --no-ff -m "illustration"

删除分支：git branch -d branch_name

推送本地git仓库到远程仓库：git push origin master

查看分支合并图：git log --graph --pretty=oneline --abbrev-commit

退出log模式：q

暂存工作区：git stash

恢复工作区保留stash：git stash apply

删除stash：git stash drop

回复工作区删除stash：git stash pop

查看stash：git stash list

恢复指定stash：git stash apply stash@{0}

拉取远程仓库：git pull origin master

拉取远程仓库某个分支到本地：git pull remote_name branch_name

本地分支与远程分支建立链接：git branch --set-upstream-to branch_name origin/branch_name

本地创建和远程对应的分支：git checkout -b branch_name origin/branch_name

查看远程库信息：git remote -v

创建标签： git tag name

	默认为HEAD,也可以指定commit id。eg: git tag 001

指定标签信息：git tag -a tag_name -m "taginfo"

指定PGP标签： git tag -s tag_name -m "taginfo"

查看所有标签：git tag

查看具体标签信息：git show tag_name

推送本地标签到远程：git push origin tag_name

推送本地所有标签到：git push origin --tags

删除本地标签：git tag -d tag_name

删除远程标签：git push origin :refs/tags/tag_name

删除远程分支：git push origin :branch_name

clone 项目到本地： git clone git_address

命令别名配置： git config --global alias.reNAME NAME

丢弃工作区的修改：git checkout -- file_name

丢弃暂存区的修改：git reset HEAD file_name

查看最后一次提交：git log -1





git生成ssh密钥

一、在git bash下执行  cd ~/.ssh
	如果能进入.ssh目录下，证明之前生成过.ssh密钥，可直接使用
	如果不能进入，则检测配置：分别执行 git config user.name 和 git config user.email
	如果之前没有配置过（运行后没有显示name和Email），则运行git config -global.name 'name' 和 git config -global.email 'email'

二、生成密钥
	运行ssh-keygen -t rsa -C '配置的邮箱地址'
	连续三个回车

三、打开生成的id_rsa.pub(公钥)，复制全部内容到github添加sshkey




--------------------------------------------

git vim order


打开目标文件：vi file_name

解锁vim编辑器进入编辑模式：i

退回锁定模式：esc

进入命令模式：:

不保存退出：quit

保存不退出：write

保存退出：wq

进入可视：右键

复制：选中+Y

粘贴：可视+p

创建文件夹：mkdir + folder

创建文件：touch + file_name

creating a new branch is quick and simple！

git merge test about fast forward



---------------------------------------------
GitHub Order

clone 项目到本地： git clone git_address




