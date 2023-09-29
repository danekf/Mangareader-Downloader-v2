# Mangareader-Downloader-v2

This is a fork of [Mangareader-Downloader-v2](https://github.com/1s0n/Mangareader-Downloader-v2) by [1s0n](https://github.com/1s0n).

While looking for a good way to store offline versions of coloured manga I came across the downloader. However I wanted better batch downloads and set off to make that happen using the conventions I saw on mangareader.to.

This is more of a side project to see whats possible in python as I learn. In the future, I may instead choose to submit a proper PR with the original author.


## Requirements
To use this, ensure you have chromedriver_autoinstaller, selenium and PyMuPDF installed using pip.


# Using Mangareader Downloader

Run ```main.py``` with the following arguments 

1. __link to the first page__ of the manga __WITHOUT__ the trailing chapter numbers. 

  For example instead of having ```https://mangareader.to/read/demon-slayer-kimetsu-no-yaiba-colored-edition-56676/en/chapter-140``` as the first argument, 
  enter ```https://mangareader.to/read/demon-slayer-kimetsu-no-yaiba-colored-edition-56676/en/chapter-```

2. The number of the __first chapter__ you wish to download (140 in my example)

3. The number of the __final chapter__ you wish to download (lets say 205, if you wanted every chapter available at that link)


A full and complete example would for example be :
```bash
python3 main.py https://mangareader.to/read/demon-slayer-kimetsu-no-yaiba-colored-edition-56676/en/chapter- 140 205
```
4. Find the unstitched images in the _temp_ folder

5. Stitch the images into pdf using stitcher.py by following instructions below. _(NOTE : should be an automatic process, but is currently manual, is a TODO)_


## Stitching manga into pdf
Now that the manga is downloaded (you can check in the "temp" folder), run ```stitcher.py``` and wait for it to generate the pdfs from the downloaded images. 
You will find the stitched chapters in the __stitches__ folder.  



# Batching into volumes
When stitching files together, it will create an incomplete volumes folder. This folder can be used to stitch the various chapters into a single volume. This is an optional thing to once an entire volume is released. 

To use :
1. Create a new folder in the __Incomplete Volumes__ folder with the name you want to give to the volume. ```ex: Demon Slayer - Kimetsu no Yaiba - Vol10```
2. Put each chapter _(found in the stitches folder)_ into its appropriate volume folder.
3. Repeat for all volumes you wish to create.
4. Run ```volume_merger.py```
5. Find merged volumes in __Completed Volumes__ folder.


# Roadmap/TODO :

* [ ] Automatically stitch files in temp folder after download.
    [ ] Clean up temp directory on success.

* [ ] Return function to clean folders after completing a task. Previous implementation seems broken for me.

* [ ] Add metadata to PDFs.
* [ ] Add ability to save stitched files/volumes as CBZ files instead of PDF.
* [ ] Investigate issue in notes from 1s0n.


## NOTES FROM 1s0n:
 ``There is a problem where the program only downloads a part of the manga, 
this is due to the way I detect the end of a manga, which is to search for the image in each page, and if the image isn't there after 30 retries, it gives up.
Directly reading the number from the webpage wont work either because the read might get intercepted by ads, which breaks everything, and an adblock is a pain to try to implement in selenium.
I will try to come up with a fix.``
