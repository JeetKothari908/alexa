import webbrowser
text = input('what do you want to search?  ')
webbrowser.open_new_tab("https://www.google.com/search?q=" + text + "&start=")
