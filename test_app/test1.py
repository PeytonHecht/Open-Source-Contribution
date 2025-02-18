from h2o_wave import main, app, Q, ui

@app('/')
async def serve(q: Q):

    table_rows = [
        ui.table_row(name='row1', cells=['John', 'Doe', "7042 23rd Ave", "123-456-7890"]),
        ui.table_row(name='row2', cells=['John', 'Doe', "7042 23rd Ave", "123-456-7890"]),
        ui.table_row(name='row3', cells=['John', 'Doe', "7042 23rd Ave", "123-456-7890"]),
    ]
    column_names = ["name", "surname", "address", "phone"]
    columns_to_test = {
        "no_width": [ui.table_column(name=x, label=x) for x in column_names],
        "min_width_0": [ui.table_column(name=x, label=x, min_width="0px") for x in column_names],
        "max_width_100": [ui.table_column(name=x, label=x, max_width="200px") for x in column_names],
        "min_width_0_and_max_width_100": [ui.table_column(name=x, label=x, min_width="0px", max_width="200px") for x in column_names]
    }

    q.page["meta"] = ui.meta_card("", layouts=[ui.layout("xs", width="800px", zones=[ui.zone("default")])])

    for k in columns_to_test.keys():
        q.page[k] = ui.form_card(box='default', items=[
            ui.text_xl(k),
            ui.table(name=k, columns=columns_to_test[k], rows=table_rows)
        ])

    await q.page.save()