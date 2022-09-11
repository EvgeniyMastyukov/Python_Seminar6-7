from datetime import datetime as dt
data = None
with open('school/students.csv','r') as file:
    data = file.read()

def create():
    time = dt.now().strftime('%H:%M')
    style = 'style = "font-size:22px;"'
    html = '<html>\n  <head>List of students</head>\n <body>\n'

    html += '<p \n{}> {} \n{} </p>'\
        .format(style,time, data)
    html += '</body>\n </html>'
    
    with open('school/index.html', 'w') as page:
        page.write(html)
    return html