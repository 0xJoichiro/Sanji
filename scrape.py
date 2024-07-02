import requests
from bs4 import BeautifulSoup

url = "https://www.dailywarden.com/"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # Find the code section
    code_section = soup.find("table", {"data-code-marker": "true"})

    if code_section:
        # Find all the lines of code
        lines_of_code = code_section.find_all("tr", {"data-code-marker": "true"})

        # Extract the line numbers and content
        sloc_info = []
        for line in lines_of_code:
            line_number = line.find("td", class_="blob-num").text.strip()
            line_content = line.find("td", class_="blob-code-inner").text.strip()
            sloc_info.append((line_number, line_content))

        # Print the SLOC information
        for line_number, line_content in sloc_info:
            print(f"Line {line_number}: {line_content}")
    else:
        print("Could not find the code section on the page.")
else:
    print(f"Failed to fetch the page. Status code: {response.status_code}")
