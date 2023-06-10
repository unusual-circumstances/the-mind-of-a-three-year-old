# Office Weather Development Log

Documentation for me developing this project!

## Dev Log 1 - May 24, 2023

This project is being developed with interoperability and learning the building blocks in mind. I also need to make sure that feature creep does not cause me to be distracted so often that I don't actually deploy any NFTs (as is typical with me).

The first thing I need to do is limit the first collection in size and scope. The first collection will be named something like "Winter Attack Genesis" and will be a small / limited collection of 10-25 pieces of AI generated art post processed and placed in custom built frames in Blender, saved as Blender assets.

**Let's break down what needs to be done:**

[x] Generate the images - I've completed this, 10 images
[ ] Post process the images so they all have similar filters and coloring.
[ ] Design the Metadata for the images, this will include the MidJourney prompt.
[ ] Model picture frames in blender using this tutorial: Creating Photo Frame Assets in Blender, Johnny Matthews https://www.youtube.com/watch?v=Apz-ioWfV_U&t=49s
[ ] Launch collection on testnet
[ ] Launch collection on mainnet

I have a lot of work to do all of this. But, once I've done it once it will go a lot more smoothly for the next collections. I'll probably launch a bunch of winter attack collections, and then get to work on the custom smart contract called "The Splitter Contract" that I will use to link the collections up.

The general idea behind this collection and other collections using the splitter contract is that if you hold an NFT in any of the collections that are linked up via the splitter contract, you receive a percentage of future minting proceeds from any other collection that is connected to the collection you minted via splitter. All of the flow of proceeds will be programmatic. The parameters (such as what % of the minting and trading commissions flow to holders of NFTs in which collection) will eventually be only adjustable by on-chain governance.

The primary goal is to use these collections as a development playground to beta test some of my ideas regarding decentralization and interconnectivity as well as to begin the process of community building, with the ultimate goal that all roads lead to the Flarnchain blockchain, and bringing the worlds inside my head to life and "onchain" as they say. I recently read an article about the concept of "onchain" which I'll have to drum up and post here later.

That's it for tonight on the developer log. I was supposed to be writing my newsletter tonight, but I got distracted by this project. I'm going to copy and paste most of this log in my newsletter as a way to fill it out and go to bed at a reasonable time.


## Dev Log 2 - May 25, 2023

I put some effort into modelling a picture frame based on the Johnny Matthews youtube tutorial. Made a ton of progress and had a working picture frame with one of my art images added to the frame! It was quite exciting, until I went to "mark" the picture as an asset, and then Blender promptly crashed on me. I didn't save at any point along the way, so all of that work was lost. Hopefully I learned a valuable lesson with Blender to *save early and save often*.

I also have been noticing a lot of crashes with fairly benign actions in my version of Blender, which was something like 3.0.2, so I uninstalled that version and installed the latest version of Blender: Blender 3.5.1. Hopefully this version is a lot more stable! I'm feeling a bit defeated after having all my work crash, but I will quickly describe some of the things I need to learn more about / things I was learning while creating the picture frame:

1. [x] Drawing with Bezier Curves - lots of things to learn. I found that the shortcut `ctrl + v` is your friend here.
2. [x] Joining geometry - connecting vertexes and edges. Not really sure how do do this properly.
3. [o] UV Unwrapping / UV Mapping - I do not understand this in the slightest!
4. [o] Materials versus textures, and the shading editor. This stuff completely confounds me.
5. [o] Marking an object as an asset. That crashed my program on Blender 3.0.2, so hopefully 3.5.1 doesn't do that.

That's all for now. I might dive back into Blender later tonight.

## Dev Log 3 - May 29, 2023

I successfully created a picture frame and added one of the art images to it. It looks pretty cool. However, I was not able to successfully create the picture frame as an asset that behaved in the way I wanted to. I could stick the picture to a wall and it orients correctly, but only on walls that are aligned with the x-axis in blender. Walls that are aligned with the y-axis caused the asset placement to rotate counter-clockwise 90 degrees in the wrong direction.

This problem continues to persist, and I even created a Reddit post asking for some help on how to fix the issue. No useful advice has been provided to date. I think wall placement behaving in unexpected ways actually made me discouraged with this project, and I took a couple days off. I'm back at it though, since I need to push forward and start working on what the nft asset itself is going to be.

An NFT is essentially a receipt on a blockchain, that usually points to an image or other piece of media. The other piece of media can be stored on a server or in some other way, such as being stored on the IPFS (the Inter-Planetary File System). Most NFTs are stored on IPFS, because that is a decentralized and immutable way of storing media that will allow said media to persist and not be subjec to the whims of some centralized entity.

There are many services that streamline the process of using IPFS, but the two I am most familiar with and that are mentioned in the Stargaze docs, as well as mentioned in other NFT platform docs are as follows:

- Pinata Cloud

- NFT Storage

I also need to make this log into a webpage that is easily sharable, so people can read this and see what I'm up to and potentially contribute code or other ideas and suggestions. For now I'm going ask ChatGPT to make a choie for me - which it recommended Github Pages. According to ChatGPT, I should create a Github Pages branch called `gh-pages` then use that branch to commit my dev-logs so that they can be easily formatted as a webpage.

=

Okay so I created a new branch called `gh-pages` and figure this is a good opportunity to push beyond my current skills and understanding of github. Multiple branches still kind of makes my head spin and feels intimidating, but that's how I'll learn.

Anyways, to keep things simple, I'll continue to track my logs here in the main branch and just keep a running history, then whenever I want to update the gh-pages page with my logs I'll just copy and paste the good stuff from this log into the gh-pages log, so that the publicly facing version (this is of course publicly available too, but since its just in a github directory people will need to seek it out rather than like... being a live webpage).

Speaking of a webpage, I think long term, unusual-circumstances should have it's own webpage to increase the quality of the collection, and also to link up with other on-chain stuff that I'm building. That's for another day though. It is *overwhelming* when I consider the amount and variety of skills needed to do this whole thing right. I need to think of that as an exciting *opportunity* rather than just being scary.

End of log for now.

## Dev Log 4 - June 8, 2023

I spent some time adding art to the spring-deluge collection, only to realize that I was checked out on the gh-pages branch, which is *no bueno* when trying to update the main branch with assets.

This project is serving a super important purpose of helping me to really learn and develop good habits with git. Checking out the gh-pages branch should always be followed up with checking out the main branch after pushing an update to the gh page. Otherwise, I'm going to end up redoing a lot of work...

OR! I could learn git and do some merges when that happens. It shouldn't really be a problem for me. I need to do better.

I also think that whenever I'm struggling with something to work on, I can always just jump on over here and start writing in the dev log. I wonder though... Should the dev log be a separate file for each log rather than one gigantic running file? this file is already getting pretty large. It's only 77 lines of code, but each line is a full paragraph! I think I'm going to setup a python scripts folder to practice regular expressions on this log at the bare minimum.

## Dev Log 5 - June 9, 2023

Just need to accomplish a couple things to maintain my streak of pushing code and making progress every single day no matter what.

Even writing text in Mark-Up is still coding right?

So anyways, let's talk about metadata.

I need to devise a method to affix metadata to the nfts. I haven't really read much about the process of adding metadata to NFTs just sort of... the process of coming up with metadata for NFTs. The metadata is basically all of the onchain stuff for nfts, so it's actually extremely important.

What I was thinking was... what if the metadata was enough information to get very close to recreating the NFT programatically. The metadata is basically the DNA of the nft.

I think about it like this:

- the metadata is basically the DNA of the NFT
- the image of the nft is just a pointer to some place off chain
- when you store the image on the IPFS, you are pointing a telescope into space. Those space objects will forever be there, but they are distant objects that you cannot reach out and touch here on eart.
- that's images stored in the IPFS.
- permanent (at least to the best of our knowledge) but distant.
- what if we could make nfts where the media itself is closer.
- I understand that storing the bytes associated with raster images or god forbid mp4/gif files would be completely unrealistic given the replicated-state-machine nature of blockchains... so there perhaps is another optimization solution
- i seek that solution

Anyways, there are definitely ways to store nfts on-chain as svg files. I don't know if this is possible on stargaze. I think pixel wizards uses svgs, but i dont know if those svgs are stored on-chain.

I need to start poking around the code bases and on-chain stuff for some of the more prominent projects to get a better understanding of what tech is being utilized to deploy projects.

# Dev Log 6 - June 10, 2023 *first commit

This is the first commit for the continuing dev-log of Unusual Circumstances. This develog has branching paths depending on which of the repos you are reading the dev logs in. Each one starts when the repo started, but picked off at the last dev log that was worked on prior to the new repo being created.

I know, I probably didn't explain that very well, but there's most certainly a protocol for determining which dev-log is the one copied to the next log, essentially which collections get to be parents, and have offspring. You know what's interesting? We don't really talk about how 'parent-child' infers the concept of offspring... like some piece of software hase a kid, or that kid has a mother or father. Makes you think. 

Anyways, this repo is another collection in unusual-circustmances. The subcollections are going to essentially follow the premise that the starting piece for each subcollection will be a prompt from a three year old. Most of the starting pieces will employ ai generative art, but most, if not all collections, will also employ a mixture of other multimedia including Blender 3d rendering software, pixel art created with aesprite, post processing in krita, probably some art drawn in MS paint (one of my favorite drawing softwares), but probably many more.

The first collection is going to be derived from this prompt from an actual three-year old:

> we don't put toilet paper in our noses, we put paper towels in our shoes

