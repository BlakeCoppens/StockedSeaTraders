from dotenv import load_dotenv
from pprint import pprint
import requests
import os
import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion

load_dotenv()
kernel = sk.Kernel()
api_key,org_id = sk.openai_settings_from_dot_env()
kernel.add_chat_service("chat-gpt",OpenAIChatCompletion("gpt-3.5-turbo",api_key,org_id))
skill = kernel.import_semantic_skill_from_directory("plugins","StockFinder" )
stockfinding = skill["StockInfo"]

def findStockInfo(companyName):
    return stockfinding(companyName)

if __name__ == "__main__":
    print('\n*** Get Stock Information***\n')
    company = input("Please enter a stock abbreviation: ")
    response = findStockInfo(company)
    
    print("\n")
    print(response)