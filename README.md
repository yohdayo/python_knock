# Python-Knock(NLP)  
http://www.cl.ecei.tohoku.ac.jp/nlp100/  

### 初期設定  
---------  
> git clone git@gitl.cl.cs.okayama-u.ac.jp:jun/python-knock.git  
> git branch [自分のアカウント名]  
> git checkout [自分のアカウント名]  
> [何らかの作業後commit]  
> git push --set-upstream origin [自分のアカウント名]  
（１回のみ，次からは普通にgit push）  

### 自分のプログラムをmasterにmergeする方法  
---------  
1. 特定ファイルをマージ  
> git checkout [ブランチ名] -- [ファイル名]  
 
2. ブランチごとマージ（下位ディレクトリをmergeしたい時）  
> git merge --squash [ブランチ名] --no-commit  
> git status見ながら調整後commit (ex. rm *.py)  