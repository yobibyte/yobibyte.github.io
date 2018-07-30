
pelican content
ghp-import output -b master
git push origin master

git checkout inner #just to be sure
git add -A
git commit -m 'update'
git push origin inner
