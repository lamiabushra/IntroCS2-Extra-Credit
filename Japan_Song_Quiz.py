#! /usr/bin/python
print "content-type: text/html\n"

import cgi, cgitb
cgitb.enable()

fromQS = cgi.FieldStorage ()

new = str(fromQS)

amtYuuki = new.count('Yuuki')
amtFuyugeshiki = new.count('Fuyugeshiki')
amtPonPonPon = new.count('PonPonPon')
amtFuture = new.count('Future')
amtMiraiE = new.count('MiraiE')

newlist = []
newlist.append(amtYuuki)
newlist.append(amtFuyugeshiki)
newlist.append(amtPonPonPon)
newlist.append(amtFuture)
newlist.append(amtMiraiE)

songnumber = max(newlist)
songsnumber = newlist.index(songnumber)
songs = ['Yuuki', 'Fuyugeshiki', 'PonPonPon', 'Future', 'MiraiE']
song = songs[songsnumber]

html = '''
<!DOCTYPE html>
<html>
<head>
<link href='https://fonts.googleapis.com/css?family=Short Stack' rel='stylesheet'>

<style>
body, html {
    height: 100%;
    margin: 0;
}

.bg {

    background-image: url("https://c1.staticflickr.com/9/8002/7240235238_eedb23fb0e_b.jpg");
    height: 100%; 
    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;
}

.navbar {
  overflow: hidden;
  background-color: #333;
  position: fixed;
}

.navbar a {
  float: left;
  display: block;
  color: #f2f2f2;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
  font-size: 17px;
}

.navbar a:hover {
  background-color: #FCEB63;
  color: black;
}

.navbar a.active {
    background-color: #FFED05;
    color: white;
}

div.textbox {
  margin: 3%;
  background-color: #ffffff;
  border: 1px solid black;
  opacity: 0.8;
  filter: alpha(opacity=80);
  text-align: center;
   position: absolute;
}

div.textbox p {
  margin: 3%;
  color: #000000;
}
</style>
</head>
<body>

<div class="navbar" style="font-family:'Short Stack';text-transform:uppercase;">
  <a  href="japan.html">Home</a>
  <a href="me.html">About</a>
  <a href="holidays.html">Holidays</a>
  <a href="food.html">cuisine</a>
  <a href="tips.html">Useful Phrases</a>
  <a class="active" href="song.html">Find A Song!</a>
  <a href="jdrama.html">Find A JDrama!</a>
</div>
<div class="bg"></div>

  <div class="textbox" style="font-family: 'Short Stack';font-size:30px; top:50px; left:250px">
      <h4> <img src="https://68.media.tumblr.com/25d974fe0912546883b798ae4c665551/tumblr_nlvvdiziv81tx7tlmo1_400.gif" height: 100px width: auto> </h4>
    <b>YOU GOT:</b>SONGTITLE
    </div> 

<div class="textbox" style="font-family: 'Short Stack';font-size:15px; top:100px;left:600px;width:400px"> <b>Here's the links to the possible songs you could have gotten! Give them a try!!!</b><br>
    <a href = "https://www.youtube.com/watch?v=f6Eyu2V4iDs" > Mirai E </a> by Kiroro ! <br>
    <a href = "https://www.youtube.com/watch?v=aKkEbdif0LE" > The Future </a> by C - UTE <br>
    <a href = "https://www.youtube.com/watch?v=yzC4hFK5P3g" > PONPONPON </a> by Kyari Pamyu Pamyu <br>
    <a href = "https://www.youtube.com/watch?v=Qpq93Dqy0EM" > Yuuki 100% </a> from Hikaru Genji <br>
    <a href = "https://www.youtube.com/watch?v=cSQVkZmMHKc" > Tsugaru Kaikyou Fuyugeshiki </a> by Sayuri Ishikawa <br>
</div>





</body>
</html>

'''

htmll = html.replace("SONGTITLE", song)
print htmll
