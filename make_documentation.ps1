Get-ChildItem -Filter *.py | ForEach-Object {
    pdoc --html $_.Name --output-dir ./docs --force
}
