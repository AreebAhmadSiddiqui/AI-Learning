# Realtime Currency Converter

import os
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
import requests

load_dotenv()
# Tool Create

@tool
def getConversionFactor(base_currency: str , target_currency:str) -> float:
    """This functions fetches the currency factor between a given base currency and a target currency"""

    url=f'https://v6.exchangerate-api.com/v6/{os.getenv('EXCHANGE_RATE_API_KEY')}/pair/{base_currency}/{target_currency}'

    response=requests.get(url)
    return response.json()

@tool
def convertCurrencies(base_currency_value: int, conversion_rate: float ) -> float:
    """This functions multiplies the base_currency_value with the conversion_rate and returns the output"""

    result=base_currency_value*conversion_rate
    return result

# print(getConversionFactor.invoke({'base_currency':'USD','target_currency':'INR'}))

## {'result': 'success', 'documentation': 'https://www.exchangerate-api.com/docs', 'terms_of_use': 'https://www.exchangerate-api.com/terms', 'time_last_update_unix': 1762819201, 'time_last_update_utc': 'Tue, 11 Nov 2025 00:00:01 +0000', 'time_next_update_unix': 1762905601, 'time_next_update_utc': 'Wed, 12 Nov 2025 00:00:01 +0000', 'base_code': 'USD', 'target_code': 'INR', 'conversion_rate': 88.7476}

# print(convertCurrencies.invoke({'base_currency_value':10,'conversion_rate':85.16}))


# Tool binding

llm=ChatGoogleGenerativeAI(model='gemini-2.5-flash')

llm_with_tools=llm.bind_tools([getConversionFactor,convertCurrencies])

## Tool calling

messages=[HumanMessage('What is the conversion factor between USD and INR, and if you get the conversion factor can you convert 12 USD to INR')]

ai_mssg=llm_with_tools.invoke(messages)

print(ai_mssg)