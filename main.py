import requests
from nicegui import ui  # type:ignore[import-untyped]
from nicegui.events import ValueChangeEventArguments  # type:ignore[import-untyped]

with ui.row():
    # TODO this label is ugly
    ui.label("Filter products: ")
    input_field = ui.input(label="Text", placeholder="filter items")

columns = [
    {
        "name": "title",
        "label": "Title",
        "field": "title",
        "required": True,
        "align": "left",
    },
    {
        "name": "price",
        "label": "Price",
        "field": "price",
        "sortable": True,
    },
    {
        "name": "description",
        "label": "Description",
        "field": "description",
        "sortable": True,
    },
]

table = ui.table(columns=columns, rows=[], row_key="name")


# TODO load this asynchronously
response = requests.get("https://dummyjson.com/products")
table.rows = response.json()["products"]


def on_input_change(change: ValueChangeEventArguments) -> None:
    input_text: str = change.value
    response = requests.get(
        "https://dummyjson.com/products/search", params={"q": input_text}
    )
    table.rows = response.json()["products"]


input_field.change_handler = on_input_change

ui.run(dark=True)
