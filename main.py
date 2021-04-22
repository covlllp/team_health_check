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
    total = row["1"] + row["2"] + row["3"]
    row["score"] = (row["1"] * 1 + row["2"] * 2 + row["3"] * 3) / total
    row["Month"] = datetime.strptime(row["Month"], "%m/%d/%y")
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
    fig = px.line(df, x="month", y="score", color="category")
    fig.write_html("index.html")


data = parse_data()
graph_data(data)
