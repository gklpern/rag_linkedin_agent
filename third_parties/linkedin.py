from dotenv import load_dotenv
import requests
import os
load_dotenv()



def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
    """Scrape information from LinkedIn profiles."""

    if mock:
        linkedin_profile_url = "https://gist.githubusercontent.com/emarco177/859ec7d786b45d8e3e3f688c6c9139d8/raw/32f3c85b9513994c572613f2c8b376b633bfc43f/eden-marco-scrapin.json"
        response = requests.get(linkedin_profile_url, timeout=10)
    else:
        api_endpoint = "https://api.scrapin.io/enrichment/profile"
        params = {
            "apikey": os.environ.get("SCRAPIN_API_KEY"),
            "linkedInUrl": linkedin_profile_url,
        }
        response = requests.get(api_endpoint, params=params, timeout=10)

    json_data = response.json()
    person_data = json_data.get("person")

    if not person_data:
        print(f"[UYARI] 'person' verisi alınamadı. Yanıt: {json_data}")
        return {}

    cleaned_data = {
        k: v
        for k, v in person_data.items()
        if v not in ([], "", None) and k not in ["certifications"]
    }

    return cleaned_data


if __name__ == "__main__":
    print(
        scrape_linkedin_profile(
            linkedin_profile_url="https://www.linkedin.com/in/eden-marco/"
        ),
    )