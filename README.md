# Mangareader-Downloader-v2

This is a fork of [Mangareader-Downloader-v2](https://github.com/1s0n/Mangareader-Downloader-v2) by [1s0n](https://github.com/1s0n).

While looking for a good way to store offline versions of coloured manga I came across the downloader. However I wanted better batch downloads and set off to make that happen using the conventions I saw on mangareader.to.

This is more of a side project to see whats possible in python as I learn. In the future, I may instead choose to submit a proper PR with the original author.


## Requirements
To use this, ensure you have chromedriver_autoinstaller, selenium and PyMuPDF installed using pip


## How to run

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
This allows easier automation, which I will hopefully add later.


# Stitching manga into pdf
Now that the manga is downloaded (you can check in the "temp" folder), run stitcher.py and wait for it to generate the pdfs from the downloaded manga, which will be in the downloads folder. 

## Batching into volumes
My goal would eventually be to set things up so that I can choose specific chapters to batch into a volume automatically.

For now, the easiest method to do this is to rename files and move them into a single folder. 
For example, rename a folder as Vol.1, and then number the images subsequently manually.
It is not ideal and in a future branch this will be addressed.







## NOTES FROM 1s0n:
 ``There is a problem where the program only downloads a part of the manga, 
this is due to the way I detect the end of a manga, which is to search for the image in each page, and if the image isn't there after 30 retries, it gives up.
Directly reading the number from the webpage wont work either because the read might get intercepted by ads, which breaks everything, and an adblock is a pain to try to implement in selenium.
I will try to come up with a fix.``
