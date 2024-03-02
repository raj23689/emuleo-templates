from vivid import App
from pathlib import Path

pages = Path(__file__).parent / 'pages'
server = Path(__file__).parent / 'server'
static = Path(__file__).parent / 'static'
styles = Path(__file__).parent / 'styles'
scripts = Path(__file__).parent / 'scripts'

app = App(
    pages=pages,
    server=server,
    static=static,
    styles=styles,
    scripts=scripts,
    type='ssr'
)

app.init()
app.run()