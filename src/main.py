from textnode import TextNode, TextType

def main():
    node = TextNode("test", TextType.BOLD, "www.google.com")
    print(node)

main()