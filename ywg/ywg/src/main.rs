use std::fs::File;
use std::io::BufReader;
use rss::Channel;

fn main() {
    let feed_path = "../../feed.xml"; 
    let file = File::open(feed_path).unwrap();
    let channel = Channel::read_from(BufReader::new(file)).unwrap();
    println!("{}", channel);
}

//TODO: automate html -> feed.xml entry.
//Start with just adding without checking if there is an entry with a similar page already.
//Do the check after.
