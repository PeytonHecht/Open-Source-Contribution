from h2o_wave import main, app, Q, ui

@app('/')
async def serve(q: Q):
    q.page['test'] = ui.markdown_card(
        box='1 1 2 2',
        title='Test App',
        content='Hello, this is a test!'
    )
    await q.page.save()