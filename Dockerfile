from python:latest
RUN mkdir -p /temp/uploads/
WORKDIR /home/app/py_merge_notebook
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["flask","run","--host=0.0.0.0"]