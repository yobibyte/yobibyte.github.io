sed -i '$d' feed.xml
echo "<item><title>What&apos;s up?</title><link>https://yobibyte.github.io/whatsup.html</link><description><![CDATA[What's up?]]></description><guid>https://yobibyte.github.io/whatsup.html</guid><pubDate>" >> feed.xml
echo "$(date -R)" >> feed.xml
echo "</pubDate><content:encoded><![CDATA[" >> feed.xml
echo "<h1>What's up?</h1>" >> feed.xml
echo "<h3>$(date)</h3>" >> feed.xml
echo "<p>" >> feed.xml
cat tweet.txt >> feed.xml
echo "</p>" >> feed.xml
echo "]]></content:encoded></item>" >> feed.xml
echo "</channel></rss>" >> feed.xml
