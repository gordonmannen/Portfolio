# Create an HTML document using Python

import webbrowser

x = open('WebpageGeneratorProject.html','w')

message = """<html>
<head></head>
<body>
<p>Stay tuned for our amazing summer sale!</p>
</body>
</html>"""

x.write(message)
x.close()

webbrowser.open_new_tab('WebpageGeneratorProject.html')

