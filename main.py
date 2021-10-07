from src.feed import Feed


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    url = "https://www.thesweetestthingblog.com"
    print(url)
    feed1 = Feed(url)

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