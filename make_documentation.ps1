# adrien.godoy@ecoles-epsi.net

Get-ChildItem -Filter src/*.py | ForEach-Object {
    pdoc --html $_.Name --output-dir ./docs --force
}
