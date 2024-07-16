from flask import Flask

app = Flask(__name__)

@app.route('/home')
def home():
    return '''<html>
    <head>
    <title>Home</title>
    </head>
    <body>
    <h1> welcome to the photo gallery, choose a photo you like.</h1>
    <a href="/food1">first picture of food</a>
    <br>
    <a href="/food3">third picture of food</a>
    <br>
    <a href="/pet2">second picture of pet</a>
    <br>
    <a href="/outerspace1">first picture of outerspace</a>
    </body>

    </html>'''
@app.route('/food1')
def food1():
    return '''<html>
    <head>
    <title>f</title>
    </head>
    <body>
    <h1> A food picture</h1>
    <img src="https://www.cnet.com/a/img/resize/36e8e8fe542ad9af413eb03f3fbd1d0e2322f0b2/hub/2023/02/03/afedd3ee-671d-4189-bf39-4f312248fb27/gettyimages-1042132904.jpg?auto=webp&fit=crop&height=1200&width=1200">
    <a href="/home">Go to the Home page </a>
    <a href="/food2">Go to second food picture</a> 
    </body>

    </html>'''

@app.route('/food2')
def food2():
    return '''<html>
    <head>
    <title>f</title>
    </head>
    <body>
    <h1> A food picture</h1>
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR5okG0tz2dWr36k2p9gxbFmqoM4AeW1e3pPQ&s">
    <a href="/food3">Go to third food picture</a> 
    <a href="/food1">Go to first food picture</a> 

    </body>

    </html>'''
@app.route('/food3')
def food3():
    return '''<html>
    <head>
    <title>f</title>
    </head>
    <body>
    <h1> A food picture</h1>
    <img src="https://www.eatingwell.com/thmb/QYZnBgF72TIKI6-A--NyoPa6avY=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/greek-salmon-bowl-f681500cbe054bb1adb607ff55094075.jpeg">
    <a href="/home">Go to the Home page</a>
    <a href="/food2">Go to second food picture</a> 

    </body>

    </html>'''
@app.route('/pet1')
def pet():
    return '''<html>
    <head>
    <title>pet</title>
    </head>
    <body>
    <h1> A pet picture</h1>
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTpS0-nSwynSihq_bRt18k9kwm95zihQ-yIpg&s">
    <a href="/pet2"> Go to second pet picture</a> 

    </body>

    </html>'''
@app.route('/pet2')
def pet2():
    return '''<html>
    <head>
    <title>pet</title>
    </head>
    <body>
    <h1> A pet picture</h1>
    <img src="https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQgByBT5IiAT_a2x9pUVb4VMoOrlzHH7Jrzj-HB5jzHlR4lNLMS">
    <a href="/home">Go to the Home page</a>
    <a href="/pet1"> Go to first pet picture</a> 
    <a href="/pet3"> Go to third pet picture</a> 

    </body>

    </html>'''
@app.route('/pet3')
def pet3():
    return '''<html>
    <head>
    <title>pet</title>
    </head>
    <body>
    <h1> A pet picture</h1>
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTZeKJMewaBtpHcpl1dUs53aexd3XsAckPGTg&s">
    <a href="/pet2"> Go to second pet picture</a> 

    </body>

    </html>'''
@app.route('/outerspace1')
def outerspace():
    return '''<html>
    <head>
    <title>outerspace</title>
    </head>
    <body>
    <h1>An outerspace picture</h1>
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/LH_95.jpg/1200px-LH_95.jpg">
    <a href="/home">Go to the Home page</a>
    <a href="/outerspace2"> Go to second outerspace picture</a> 
    <a href="/outerspace3"> Go to third outerspace picture</a> 
    </body>

    </html>'''
@app.route('/outerspace2')
def outerspace2():
    return '''<html>
    <head>
    <title>outerspace</title>
    </head>
    <body>
    <h1>An outerspace picture</h1>
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT6TaherK34f8vPBSjkn6l4wQtdg7qW6hIBIg&s">
    <a href="/outerspace1"> Go to first outerspace picture</a>
    <a href="/outerspace3"> Go to third outerspace picture</a>

    </body>

    </html>'''
@app.route('/outerspace3')
def outerspace3():
    return '''<html>
    <head>
    <title>outerspace</title>
    </head>
    <body>
    <h1> An outerspace picture</h1>
    <img src="https://s26162.pcdn.co/wp-content/uploads/2019/07/M43_beletsky.jpg">
    <a href="/outerspace1"> Go to first outerspace picture</a>
    <a href="/outerspace2"> Go to third outerspace picture</a>

    </body>

    </html>'''
if __name__ == '__main__':
    app.run(debug=True)