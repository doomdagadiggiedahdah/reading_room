## what's needed to ship? take a couple of sites, make a summary, link to og article, add to anki.
    ## want to get the tags at some point
        ## I think I'd want to have a storage of the possible tags and feed that in. There's more to this.
    ## figure out how to integrate with OneTab to get all my shit, I'm sure there's a way.
## get article, append with jina
## I'd like to have this in anki at some point, but I'll write to Obs since I can't remember how to add cards in python.


import requests
import json
from openai import OpenAI

url = "https://r.jina.ai/"
site_url = "https://access.redhat.com/security/cve/CVE-2023-45853" # keeping sep to link to later
url = url + site_url
headers = {"Accept": "application/json"}

## get json
res = requests.get(url, headers=headers)
json_data = json.loads(res.content.decode('utf-8'))
web_content = json_data['data']['content']

print(f"here's the content:\n\n{web_content}")

## make summary
prePrompt = "You have an uncanny ability to provide concise yet comprehensive summaries of articles. Please help out our friend with the following request."
prompt = f"""\
<article>{web_content}</article>
Please take the given article and create a 1-2 paragraph "abstract" for it with the following attributes:
- in html formatting
- using the ```python``` formatting, include a python formatted list of possible tags (with hashtags) I could use to find the abstract you created.
- contains the following url at the end to link back to original article: {site_url}
- has between 5-10 emojis
"""

client = OpenAI()
def textFromAI():
    res = client.chat.completions.create(model = "gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": prePrompt},
        {"role": "user", "content": prompt}
    ])
    story = res.choices[0].message.content
    return str(story)

dest = "/home/mat/Obsidian/reading_room/"
abstract = textFromAI()
with open(f"{dest}test.md", "w+") as f:
    f.write(abstract)
