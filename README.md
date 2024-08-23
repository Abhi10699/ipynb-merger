# IPython Notebook Merger

A Python tool designed to merge multiple Jupyter notebooks and generate a single HTML file for easy submission or sharing. It simplifies the process of combining notebooks and presenting them in a cohesive format.

## Purpose

During College Homework Submission, our professor expects all the work in a single HTML file, which means we have to combine all the notebooks and convert them to HTML. Doing this everytime costs alot of time and is not efficient. Thus I made this tool for my classmates and myself to make this process easier for everybody :)

## Limitation

- Only works with notebooks exported from certain version of jupyter-notebook. Not sure which one.. **Future Enhancement**

## Installation

1. Clone Repository
```bash
git clone https://github.com/Abhi10699/PyMergeNotebooks.git
```

2. Change Directory
```bash
cd PyMergeNotebooks
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Merge Files
```bash
python app.py ./1.html ./2.html -o ./merged.html
```
