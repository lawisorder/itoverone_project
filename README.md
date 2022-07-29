![logo](https://media.proglib.io/posts/2021/04/01/07742583e2b12531cfeea3cb65698a2b.jpg)


![python](https://img.shields.io/pypi/pyversions/py?color=green&logoColor=black&style=plastic) ![size](https://img.shields.io/github/languages/code-size/lawisorder/itoverone_project)
![wies](https://img.shields.io/github/watchers/lawisorder/itoverone_project?label=wies&logoColor=red&style=social)
![forks](https://img.shields.io/github/forks/lawisorder/itoverone_project?style=social)
<a id="anchor"></a>
# "Parser_fo_everybody"
***
## Contex:

This is the first independent project. Based on the task on one of the freelance online applications. The task has already been completed, but it intrigued me. I decided to try myself.
***
## Required libraries
* [CSV](https://pypi.org/project/csv23/) - (Comma Separated Values) format is the most common import and export format for spreadsheets and databases.
* [Requests](https://pypi.org/project/requests/) - HTTP library for the Python programming language. The goal of the project is to make HTTP requests simpler and more human-friendly.
* [BeautifulSoup](https://pypi.org/project/beautifulsoup4/) - Python package for parsing HTML and XML documents (including having malformed markup, i.e. non-closed tags, so named after tag soup).
* [Lxml](https://pypi.org/project/lxml/) - the most feature-rich and easy-to-use library for processing XML and HTML in the Python language.
* Os - one of the built-in python modules. Processing files with this module includes creating, renaming, moving, deleting files and folders, getting a list of all files and directories, and more. The module includes a lot of methods and tools for other operations: handling environment variables, managing system processes, as well as command line arguments and even extended file attributes that are only found in Linux.
* Json - (JavaScript Object Notation) built-in module. Module allows you to encode and decode data in a convenient format.
* Time - built-in module for working with time in Python.
***
## Installation:
```python
- pip install csv
- pip install time
- pip install requests
- pip install os
- pip install BeautifulSoup
- pip install lxml
- pip install json
```

## Algorithms (main steps):

* The site has over 40 product pages. Сreate a function that processes all pages, regardless of their number, and saves the result as html pages.
```python
def get_pages():
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
    }

    req = requests.get(url="https://swisstime.by/catalog/filter/gender-is-muzhskie/apply/", headers=headers)

    if not os.path.exists("data"):
        os.mkdir("data")

    with open("data/page_1.html", "w", encoding="UTF-8") as file:
        file.write(req.text)

    with open("data/page_1.html", encoding="UTF-8") as file:
        src = file.read()
    .
    .
    for i in range(1, pages_count + 1):
    url = f"https://swisstime.by/catalog/filter/gender-is-muzhskie/apply/?PAGEN_1={i}"

    r = requests.get(url=url, headers=headers)
    with open(f"data/page_{i}.html", "w", encoding="UTF-8") as file:
        file.write(r.text)   
    
    # create a time lag so as not to overload the site with requests
    time.sleep(2)    
```
* processing the received pages and collecting information
```python
def collect_options(pages_count):
    # create a csv-file and give it headers 
    with open("data_results.csv", "w", encoding="UTF-8") as file:
        writer = csv.writer(file)
        writer.writerow(
            (
                "Бренд",
                "Модель",
                "Цена",
                "Имеется в продаже"
            )
        )    
```
  * collect the information   
```python
for item in watch_cards:
         watch_brand = item.find("div", class_="st-card__brand").text
         watch_model = item.find("div", class_="st-card__model").text
         watch_price = item.find("div", class_="st-card__price").text
         watch_stock = item.find("div", class_="st-card__stock").text.strip()
         watch_url = f'https://swisstime.by{item.get("href")}'

         data.append(
             {
                 "watch_brand": watch_brand,
                 "watch_model": watch_model,
                 "watch_price": watch_price,
                 "watch_stock": watch_stock,
                 "watch_url": watch_url
                }
         )
```
 * fill out csv-file
```python
 with open("data_results.csv", "a", encoding="UTF-8") as file:
    writer = csv.writer(file)
    writer.writerow(
        (
            watch_brand,
            watch_model,
            watch_price,
            watch_stock
        )
    )
```
  * create and fill out json-file
```python
with open("parsing_results.json", "a", encoding="UTF-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)
```
## Resume:

The parcing process is not so dificult. The main thing is the analysis of the structure of the site, the search for patterns in the display of information in it and the choice of information processing options.


[вверх](#anchor)
