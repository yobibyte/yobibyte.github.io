cd ~/dev/compressor
python3 app.py --task daily-arxiv
cd ~/dev/yobibyte.github.io/ywg
python3 ywg.py ad && git add -A && git commit -m 'daily' && git push
