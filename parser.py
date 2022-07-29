import csv
import time
import requests
import os
from bs4 import BeautifulSoup
import lxml
import json


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

    soup = BeautifulSoup(src, "lxml")
    pages_count = int(soup.find("li", class_="pagination-item pages col-06").find_all("a")[-2].text)

    for i in range(1, pages_count + 1):
        url = f"https://swisstime.by/catalog/filter/gender-is-muzhskie/apply/?PAGEN_1={i}"

        r = requests.get(url=url, headers=headers)
        with open(f"data/page_{i}.html", "w", encoding="UTF-8") as file:
            file.write(r.text)

        time.sleep(2)

    return pages_count


def collect_options(pages_count):
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

    data = []
    for page in range(1, pages_count + 1):
        with open(f"data/page_{page}.html", encoding="UTF-8") as file:
            src = file.read()

        soup = BeautifulSoup(src, "lxml")
        watch_cards = soup.find_all("a", class_="st-card__link")

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

    with open("parsing_results.json", "a", encoding="UTF-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    print(f"The work has done")


def main():
    pages_count = get_pages()
    collect_options(pages_count=pages_count)


if __name__ == '__main__':
    main()
