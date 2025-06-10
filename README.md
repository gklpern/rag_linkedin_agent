# Ice Breaker

This project uses a LangChain-powered agent to extract professional information from a person's LinkedIn profile using only their name.
Features

     Google Search Agent to find LinkedIn profiles by full name

     LLM (LLaMA 3 via Ollama) for smart reasoning and data extraction

     Structured output as JSON using a custom output parser

     Mock mode for testing LinkedIn scraping without live requests

 How It Works

    Input: You provide a full name (e.g., Gökalp Eren Akol).

    LinkedIn Lookup Agent: Uses a ReAct agent to find the LinkedIn profile URL via Google search.

    Scraper: Fetches (mocked) LinkedIn data.

    LLM Reasoning: Llama 3 processes the profile content and extracts structured summary information (e.g., job title, company).

    Output: A JSON object containing relevant professional details and the user's photo URL.
