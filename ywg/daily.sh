cd ~/dev/compressor
python3 app.py --task daily-arxiv
cd ~/dev/yobibyte.github.io/ywg
ywg ad && git add -A && git commit -m 'daily' && git push
