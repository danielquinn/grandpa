# Grandpa

This is the archive of all of my Grandpa's home videos over the decades

## Story

My grandfather was the family videographer for over sixty years.  He collected
video from his life from *before my mother was born*, and when he died, I was
worried that that archive had been lost.  Thankfully, we were able to salvage
some of the footage in the form of 38 DVDs he'd made himself by converting the
old formats.  A lot were originally shot on compact magnetic tape, then
converted to VHS, then to DVD.  Others are even older, back when he was carting
around a massive reel-to-reel rig.  These videos were moved to VHS by him
sitting patiently in the basement, with his modern camera pointed at his
projection screen, the audio being fed in through the mic picking up background
ambient room noise.

My grandfather was not an A/V mastermind, but he was an archivist in his own
right.  He managed to collect and curate more than 100 hours out of his
lifetime, and I'm grateful for the times he used to call me down to the
basement to watch the old videos of my mother as a child, or me as a toddler.
I didn't want to let this archive die with him.


## Why isn't this on YouTube?

Google is so afraid of copyright lawyers that home movies with occasional
background music (low quality, ambient background noise) is enough for them to
cry foul and mute my uploads.  Of the four test videos I uploaded, two of them
had the audio stripped from the complete file for "copyright reasons".

This is why we need a federated internet.  Depending on one centralised
American provider for the source of our shared cultural experience is unhealthy
in the extreme.


## Technical

The DVDs I started with were all home-made, with no metadata attached at all
save for the paper insert in the casing, hand-written in Romanian.  I did
my best to transcribe it all into `.nfo` files (translating the Romanian where
I could and leaving it when I had no idea what he was trying to say), which
were then scripted here into writing static HTML both in the primary index on
the home page and on each video's specific page.  I'm using
[select2](http://select2.github.io/) to handle the magical combo box since that
level of js magic is beyond me.

The video itself is digital so it's well preserved, but converting it from
homemade DVD (with variable title numbers and chapters, thanks Grandpa) was
no picnic.  I've managed to use [ffmpeg](https://ffmpeg.org/) to transcode
everything into a format that's web-friendly, and I parallelised the whole
process with Python so I can take advantage of my 16-core super machine and
generate web-friendly versions of the 38 ISO rips in just over a day and half.

If you're curious about the flags used to generate these files, take a look at
[queue.json](https://github.com/danielquinn/grandpa/blob/master/scripts/queue.json).

The video player is HTML5 from [video.js](http://videojs.com/) and the site
itself is simple HTML/CSS/JS + Bootstrap4 so it doesn't look 100% ugly.
