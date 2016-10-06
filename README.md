# C-H-Downloader
Scraper to download Cyanide and Happiness comics. 

**Usage:**
```
python chdl.py [mode] [year] [month] [day]
```
mode- 1 to download the comic for a specific day, 2 to download comics for an entire month.

Date Format- YYYY MM DD

**Example:**
```
python chdl.py 1 2016 9 12
```

In case a date argument is not specified, current month/year/day is assumed. Default mode is taken to be 1(Current day's  
comic will be downloaded if no argument is specified.).
