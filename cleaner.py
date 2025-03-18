# import libraries
import html2text
import os
from bs4 import BeautifulSoup

# set directory for to_convert (drop files here to be converted) 
# and to_save (where markdown files will be saved)
to_convert = "to_convert"
to_save = "markdown_output"

# get list of files in to_convert folder
files = os.listdir(to_convert)

# uses Beautiful Soup to strip out header, footer, navigation text
#open html_file and reads it
for file in files:  
    with open(to_convert+'/'+file, 'r', encoding='utf-8', errors='ignore') as fff:
        html_content = fff.read()

    # reads file with beautiful soup
    soup = BeautifulSoup(html_content, 'html.parser')
    soup.encode('UTF-8')

    # create list of div class you want to remove from html document
    classes = ['ddb-site-banner', 'b-noscript', 'ddb-footer', 'site-bar__container', 'page-header', 'p-article-byline']

    # create list of div id you want to remove from html document
    ids = ['mega-menu-target', 'skip-to-content-link']

    # look through to remove classes
    for div in classes:
        element = soup.find(class_=div)
        if element:
            element.decompose()

    # loop through to remove ids
    for id in ids:
        element = soup.find(id=id)
        if element:
            element.decompose()

    # removes website header and footer
    if soup.header:
        soup.header.decompose()
    if soup.footer:
        soup.footer.decompose()

    # overwrite the file with the new cleaned version
    with open(to_convert+'/'+file, 'w', encoding='utf-8') as ffff: #overwrite the file
        ffff.write(str(soup))

# now html files are cleaned, runs them through html2text to convert them to markdown
# set html2text function and options: see config for all options
cleaner = html2text.HTML2Text()
cleaner.ignore_images = True
cleaner.ignore_links = True
cleaner.body_width = 0

# Conversion loop: performs conversion for each file in to_convert
# opens and reads each file from files
for file in files:
    with open(to_convert+'/'+file, "r", encoding='UTF-8', errors='ignore') as f:
        html = f.read()

    # change unicode characters to single or double quotation mark to be read by markdown
    tidy_html = html.replace("’", "'").replace("“", "\"").replace("”","\"")

    # convert html file to markdown
    text = cleaner.handle(tidy_html)

    # Open a file and write the conversion to it
    with open(to_save+'/'+file, 'w') as ff:
        ff.write(text)   

# Rename converted files in to_save folder
# get list of files in to_save folder
converted = os.listdir(to_save)

# rename each converted files
for convert in converted:
    newfiles = []
    newfiles.append(os.path.splitext(convert)[0]+'.md')
    for newfile in newfiles:
        os.replace(to_save+'/'+convert, to_save+'/'+newfile)

print("File conversion complete!")