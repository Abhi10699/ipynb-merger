from argparse import ArgumentParser
from bs4 import BeautifulSoup
from pathlib import Path


def read_html(file_path, perm = "r"):
  with open(file_path, perm,encoding="utf-8") as f:
    f.seek(0)
    file_contents = f.read()
    soup = BeautifulSoup(file_contents, features="html.parser")
    f.close()
  return soup

def main(read_files, out_path):
  
  
  # check if html files exists
  
  for file in read_files:
    p = Path(file)
    if not p.exists():
      raise Exception(f"{file} does not exists")
    
  template_soup = read_html("./template.html","r")
  file_soups = []
  
  # read files
  for file in read_files:
    file_soup = read_html(file_path=file)
    file_soups.append(file_soup)

  # read template body

  template_body = template_soup.find("body")
  
  # merge loop
  for html in file_soups:
    html_body = html.find("body").find_next("div",{"id": "notebook"})
    template_body.append(html_body)
  # output file
  
  with open(out_path, "w+", encoding="utf-8") as f:
    f.write(str(template_soup))
    f.close()
  
  print("Files Merged Successfully!")
  
  
if __name__ == "__main__":
  parser = ArgumentParser()
  
  # add arguments
  parser.add_argument(
    '-f',
    "--files",
    nargs="+",
    help='list of html file paths',
    required=True
  )
  parser.add_argument(
    "-o",
    "--out_file",
    type=str,
    help="output html file path",
    required=True
  )
  
  # parse arguments
  
  prog_args = parser.parse_args()
  
  read_files = prog_args.files
  out_file_path =  prog_args.out_file
  
  main(read_files, out_file_path)