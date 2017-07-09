#! /usr/bin/python
print "content-type: text/html\n"

import cgi, cgitb
cgitb.enable()

fromQS = cgi.FieldStorage ()

new = str(fromQS)

amtBRain = new.count('BRain')
amtTears = new.count('Tears')
amtLShuffle = new.count('LShuffle')
amtKoizora = new.count('Koizora')

newlist = []
newlist.append(amtBRain)
newlist.append(amtTears)
newlist.append(amtLShuffle)
newlist.append(amtKoizora)

dramanumber = max(newlist)
dramasnumber = newlist.index(dramanumber)
dramas = ['Beautiful Rain', 'One Litre of Tears', 'Love Shuffle', 'Koizora']
drama = dramas[dramasnumber]

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
  <a href="song.html">Find A Song!</a>
  <a class="active" href="jdrama.html">Find A JDrama!</a>
</div>
<div class="bg"></div>

  <div class="textbox" style="font-family: 'Short Stack';font-size:30px; top:50px; left:200px">
      <h4> <img src="https://media.giphy.com/media/2AH7k1wBZY6JO/giphy.gif" height: 100px width: auto> </h4>
    <b>YOU GOT:</b>JDRAMA
    </div> 

<div class="textbox" style="font-family: 'Short Stack';font-size:15px; top:100px;left:680px;width:400px"> <b>Here's the links to the possible J-dramas you could have gotten! Give them a try!!!</b><br>
    <a href = "https://en.wikipedia.org/wiki/1_Litre_no_Namida_(TV_series)" > One Litre of Tears </a> <br>
    <a href = "https://en.wikipedia.org/wiki/Koizora_(film)" > Koizora </a> <br>
    <a href = "https://en.wikipedia.org/wiki/Love_Shuffle" > Love Shuffle </a>  <br>
    <a href = "https://en.wikipedia.org/wiki/Beautiful_Rain" > Beautiful Rain </a> <br>
</div>





</body>
</html>

'''

htmll = html.replace("JDRAMA", drama)
print htmll
