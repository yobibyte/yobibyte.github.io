use chrono::Utc;
use rss::{Channel, ItemBuilder};
use rss::{ChannelBuilder, Guid};
use std::env;
use std::fs::File;
use std::io::BufReader;

fn main() {
    let feed_path = "../feed.xml";
    let file = File::open(feed_path).unwrap();
    let mut channel = Channel::read_from(BufReader::new(file)).unwrap();
    // println!("{}", channel);

    let args: Vec<String> = env::args().collect();
    if args.len() < 2 {
        println!("Provide path to the html page as an argument!");
    }

    let website_url = "https://yobibyte.github.io";
    let page_full_url = format!("{website_url}/{}", args[1]);
    println!("{}", page_full_url);

    let title = "title".to_string();
    let guid = Guid {
        value: page_full_url.clone(),
        permalink: true,
    };
    let new_item = ItemBuilder::default()
        .title(title)
        .guid(guid)
        .link(page_full_url)
        .pub_date(Utc::now().to_rfc2822())
        .build();

    let mut items = channel.items_mut().to_vec();
    items.push(new_item);
    channel.set_items(items);

    let file = File::create(feed_path).expect("Cannot create file");
    channel.write_to(file).unwrap(); // write to the channel to a writer

    // get html content
    // embed html into xml items
    /* <content:encoded><![CDATA[
        <!DOCTYPE html>
        <html lang="en">
        <head>
          <meta charset="UTF-8"/>
          <title>Your HTML Page</title>
          <style>
            /* Optional inline CSS */
          </style>
        </head>
        <body>
          <h1>Hello from Your HTML Page</h1>
          <p>This is the full content of your page, including any images, styles, etc.</p>
          <!-- Make sure all links, images, etc. are absolute URLs if you need them to load properly in RSS readers -->
        </body>
        </html>
      ]]></content:encoded>
    */
}

//TODO: automate html -> feed.xml entry.
//Start with just adding without checking if there is an entry with a similar page already.
//Do the check after.
