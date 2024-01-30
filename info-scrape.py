
# Import necessary libraries
import requests
import urllib

# Define your Google Search API key
api_key = "..."

# Define your search query
search_query = "best restaurants in New York"

# Build the Google Search API URL
base_url = "https://www.googleapis.com/customsearch/v1?"
params = {
    "cx": "...",
    "q": search_query,
    "key": api_key,
}

url = base_url + urllib.parse.urlencode(params)

# Send the request and get the response
response = requests.get(url)

# Check for successful response
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Extract search results
    results = data["items"]

    # Print search results
    for result in results:
        print(f"Title: {result['title']}")
        print(f"Snippet: {result['snippet']}")
        print(f"URL: {result['link']}")
        print("---")
else:
    print(f"Error: {response.status_code}")
