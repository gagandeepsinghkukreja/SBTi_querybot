
import requests
from sbti_chatbot.sbti_utils import get_company_info

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1"
headers = {"Authorization": "Bearer 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"}

def format_context(company_record):
    fields = ["Company Name", "Country", "Target Status", "Target Type", "Sector"]
    return "\n".join(f"{k}: {company_record.get(k, '')}" for k in fields)

def query_huggingface(prompt):
    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 150,
            "temperature": 0.7,
            "do_sample": True
        }
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()[0]["generated_text"]

def answer_query(user_query, df):
    for company in df["Company Name"].dropna().unique():
        if company.lower() in user_query.lower():
            record = get_company_info(df, company)
            if record:
                context = format_context(record[0])
                prompt = f"Given the following data:\n{context}\n\nAnswer the following:\n{user_query}"
                return query_huggingface(prompt).split("Answer:")[-1].strip()
    return "Sorry, I couldn't find that company in the dataset."
