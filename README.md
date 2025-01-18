Aya Maguire <aya.maguire@gmail.com>
	
AttachmentsSun, Jan 5, 4:11 PM (13 days ago)
	
to Jeffrey
I ran the script locally and scraped all the files. Here they are:
https://drive.google.com/file/d/1RuFcrpSqqPn5bUnOpYEIGDrBkyQRJv30/view?usp=drive_link

But if you want to be able to do this yourself in the future, you can use the script I've attached.

To run it:

1. Create a folder where you want to save the files
2. Save this script
3. Open the script and, on line 4, replace "/Users/aya/Desktop/chess_pgns/" with your folder

Note that I've hardcoded which files to grab. In this case, it will grab all pgns between 920 and 1573. Update that if you want to run this later, starting at 1574, for example.

Next, it depends on whether you have something called "pip" installed on your computer. Pip is the "package manager" for Python. If you do, you should be able to just run:
> pip install requests

Then then the script:
> python3 chess_pgns_for_dad.py

from wherever you've saved it. Let me know what happens, we may need to do a screenshare.

If you don't have pip installed, I think you'll need to google how to install pip for Windows. Since I don't know Windows, I'm not sure.
