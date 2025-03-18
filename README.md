# ddb-html-to-markdown
A simple Python script which cleans up and converts html pages from dndbeyond.com to markdown files for importing into obsidian. This project should only be used to create local copies of dnd beyond content for your own use (e.g. for editing and making notes when running games).

# How to use
The script is simple and can be run from within your Coding IDE. 

Step 1: clone repository

Step 2: save html files you want to be converted in the /to_convert folder.

Step 3: run script

Step 4: markdown files will be saved in /markdown_output

## Python libraries required
The script requires the following libraries to work. Note: os is usually installed along with python, so does not need to be installed separately.

1. Beautiful Soup
2. html2text
3. os

## How it works
The script has two stages. Firstly, it cleans up the html files by removing website content that is not required including header info, footer info, website navigation and so on. It also converts some special characters to a readable format. 

Once the html files are clean, the script converts them to markdown. Markdown files do not contain links or images.





