from bs4 import BeautifulSoup
from os import listdir

def read_html(file_path, perm = "r"):
  with open(file_path, perm,encoding="utf-8") as f:
    f.seek(0)
    file_contents = f.read()
    soup = BeautifulSoup(file_contents, features="html.parser")
    f.close()
  return soup


template_soup = read_html("./template.html","r")
merge_soups = []
files = listdir("./test")

for file in files:
  try:
    file_path = f"./test/{file}"
    file_soup = read_html(file_path)
    merge_soups.append(file_soup)
  except Exception as e:
    print(f"error reading {file}")
    print(e)

template_body = template_soup.find("body")

for idx, html in enumerate(merge_soups):
  try:
    html_body = html.find("body").find_next("div",{
      "id": "notebook"
    })
    template_body.append(html_body)
  except Exception as e:
    print(idx, files[idx])
    
with open("out/template_write.html", "w+", encoding="utf-8") as f:
  f.write(str(template_soup))
  f.close()