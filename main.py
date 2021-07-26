import csv
from datetime import datetime
import pandas
import plotly.express as px


def parse_data():
    with open("data.csv") as csvfile:
        rows = csv.DictReader(csvfile)
        data = []
        for row in rows:
            sanitized_row = sanitize_row(row)
            data.append(sanitized_row)
        return data


def sanitize_row(row):
    row["1"] = float(row["1"])
    row["2"] = float(row["2"])
    row["3"] = float(row["3"])
    row["4"] = float(row["4"])
    row["5"] = float(row["5"])
    total = row["1"] + row["2"] + row["3"] + row["4"] + row["5"]
    row["score"] = round(
        (row["1"] * 1 + row["2"] * 2 + row["3"] * 3 + row["4"] * 4 + row["5"] * 5)
        / total,
        2,
    )
    row["Month"] = datetime.strptime(row["Month"], "%m/%d/%y")
    if row["Month"] < datetime.strptime("8/1/21", "%m/%d/%y"):
        row["score"] = round(
            (row["2"] * 1.5 + row["3"] * 3 + row["4"] * 4.5) / total,
            2,
        )

    return row


def graph_data(data):
    category = []
    month = []
    score = []
    for row in data:
        category.append(row["Category"])
        month.append(row["Month"])
        score.append(row["score"])

    df = pandas.DataFrame({"category": category, "month": month, "score": score})
    fig = px.line(
        df,
        x="month",
        y="score",
        color="category",
        text="score",
        hover_name="category",
        range_y=[0.9, 5.1],
    )
    fig.show()
    fig.write_html("index.html")


data = parse_data()
graph_data(data)
