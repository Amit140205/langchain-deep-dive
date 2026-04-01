from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import WebBaseLoader

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")

prompt = PromptTemplate(
    template="Answer the following question \n {question} from the following text \n {text}",
    input_variables=["question","text"]
)

parser = StrOutputParser()

url = "https://www.flipkart.com/apple-macbook-air-m4-16-gb-256-gb-ssd-macos-sequoia-mc6t4hn-a/p/itm7c1831ce25509?pid=COMH9ZWQCJGMZGXE&lid=LSTCOMH9ZWQCJGMZGXEBSSIQU&marketplace=FLIPKART&q=macbook+air+m4&store=6bo%2Fb5g&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_2_7_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_2_7_na_na_na&fm=organic&iid=9df2c43d-afa1-43ec-8d99-f967f3569c20.COMH9ZWQCJGMZGXE.SEARCH&ppt=None&ppn=None&ssid=n0qx48qzzk0000001765812605144&qH=a3dc101ea3bce06d"

loader = WebBaseLoader(url)

docs = loader.load()

chain = prompt | model | parser

result = chain.invoke({
    "question": "What is the peak brightness of the product",
    "text": docs[0].page_content
})

print(result)