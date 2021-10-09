from src.feed import Feed
from src.url import *



# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    url1A = "https://www.thesweetestthingblog.com"
    url1B = "https://www.thesweetestthingblog.com/rss"

    url2A = "https://careerkarma.com/blog/bootcamps/rss/"
    url2B = "https://careerkarma.com/blog/bootcamps/"

    specialCase = "https://careerkarma.com/"

    validateURL(url1A)
    validateURL(url1B)
    # feed1 = Feed(url)

    print("End")


    # import xml.dom.minidom as MiniDom
    # # or xml.dom.minidom.parseString(xml_string)
    # dom = MiniDom.parseString(response.content)
    # pretty_xml_as_string = dom.toprettyxml()
    #
    # print(pretty_xml_as_string)
    #
    # with open('response.xml', 'r+') as f:
    #     f.write(pretty_xml_as_string