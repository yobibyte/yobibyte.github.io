#!/usr/bin/env bash

# Script to add a content of the html page to the feed.xml.
# Use as ./upd.sh page.html

TITLE=$(cat "$1" | grep -oP "<h1>\K.*?(?=</h1>)")
if [[ -z $TITLE ]]; then
    TITLE="New update!"
fi

sed -i '$d' feed.xml
echo "<item><title>${TITLE}<link>https://yobibyte.github.io/"$1"</link><description><![CDATA[${TITLE}]]></description><guid>https://yobibyte.github.io/"$1"</guid><pubDate>" >> feed.xml
echo $(date +"%a, %d %b %Y %H:%M:%S %z") >> feed.xml
echo "</pubDate><content:encoded><![CDATA[" >> feed.xml
cat "$1" >> feed.xml
echo "]]></content:encoded></item>" >> feed.xml
echo "</channel></rss>" >> feed.xml
