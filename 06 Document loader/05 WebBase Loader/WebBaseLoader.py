from langchain_community.document_loaders import WebBaseLoader

url = "https://www.flipkart.com/apple-macbook-air-m4-16-gb-256-gb-ssd-macos-sequoia-mc6t4hn-a/p/itm7c1831ce25509?pid=COMH9ZWQCJGMZGXE&lid=LSTCOMH9ZWQCJGMZGXEBSSIQU&marketplace=FLIPKART&q=macbook+air+m4&store=6bo%2Fb5g&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_2_7_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_2_7_na_na_na&fm=organic&iid=9df2c43d-afa1-43ec-8d99-f967f3569c20.COMH9ZWQCJGMZGXE.SEARCH&ppt=None&ppn=None&ssid=n0qx48qzzk0000001765812605144&qH=a3dc101ea3bce06d"

loader = WebBaseLoader(url)

docs = loader.load()

# print(docs)

# print(len(docs))

print(docs[0].page_content)