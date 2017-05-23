from urllib.request import urlopen
from urllib.request import urlretrieve
import re



def main():
    startparse()


def startparse():
    url = input("Input URL to scrape: ")
    try:
        html = urlopen(url)
        print("parsing: " + url)
        read = html.read().decode('latin-1')
        parseme(read, url)
    except:
        print("Error: No scrapeable URL input.")

def parseme(read, url):

    pattern = re.compile('(<a\shref=\"[^\"]+.pdf\")')
    links = pattern.findall(read)
    #TODO more regex impl
    if not links:
        print("no pdfs found")

    for i in range(len(links)):
        print("pdf file found: ")

        link = links[i]
        link = link[9:len(link) -1]
        name = link.split("/")[-1]

        print("parsing: " +url +  link )
        try:
            urlretrieve(url + link, name)
        except:
            print("pdf error")


if __name__ == "__main__":
    main()
