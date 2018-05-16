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

clone 项目到本地： git clone git_address

命令别名配置： git config --global alias.reNAME NAME

丢弃工作区的修改：git checkout -- filename

丢弃暂存区的修改：git reset HEAD filename

查看随后一次提交：git log -1



git生成ssh密钥

一、在git bash下执行  cd ~/.ssh
	如果能进入.ssh目录下，证明之前生成过.ssh密钥，可直接使用
	如果不能进入，则检测配置：分别执行 git config user.name 和 git config user.email
	如果之前没有配置过（运行后没有显示name和Email），则运行git config -global.'name' 和 git config -global.email 'email'

二、生成密钥
	运行ssh-keygen -t rsa -C '配置的邮箱地址'
	连续三个回车
三、打开生成的id_rsa.pub(公钥)，复制全部内容到github添加sshkey




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

创建文件夹：mkdir + folder

创建文件：touch + file_name

creating a new branch is quick and simple！

git merge test about fast forward



---------------------------------------------
GitHub Order

clone 项目到本地： git clone git_address




