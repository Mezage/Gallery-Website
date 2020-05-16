import cgi
import pymysql

db = pymysql.connect(host='localhost',
    user='gallery',
    passwd='eecs118',
    db= 'gallery')
cur = db.cursor()

#figuring out which image it is
form = cgi.FieldStorage()
imageID = form.getvalue('picID')


################### HTML #######################
print("Content-Type: text/html \n\n")
print("""
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body {
  margin: 0;
  font-family: Arial, Helvetica, sans-serif;
}

.topnav {
  overflow: hidden;
  background-color: #333;
}

.topnav a {
  float: left;
  color: #f2f2f2;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
  font-size: 17px;
}

.topnav a:hover {
  background-color: #ddd;
  color: black;
}

</style>
</head>
""")
#if using external css, use /css/filename.css when acessing it
print("<body bgcolor = '#636E5A'>")  # background color
#actual tabs themselves
print("""
<div class="topnav">
  <a class="active" href="http://localhost:8080/test/cgi-bin/Input.py">Home</a>
  <a class="active" href="http://localhost:8080/test/cgi-bin/galHUB.py">List of Galleries</a>
  <a class="active" href="http://localhost:8080/test/cgi-bin/sort.py">Sort</a>
</div>
""")
im = """SELECT * FROM image WHERE image_id = "%s" """ % imageID
cur.execute(im)
im = cur.fetchone()

print ("""
<center>
<img src="%s" alt="no image" width="600" height="400"><br>
<font color = 'white'>Title: %s <br>
""" % (im[2], im[1]))

details = """SELECT * FROM detail WHERE detail_id = "%s" """ % im[5]
cur.execute(details)
details = cur.fetchone()

print ("""
Created in: %s <br>
Type: %s<br>
Image Location: %s<br>
Description: %s<br>
""" % (details[2], details[3], details[6], details[7]))

arty = """SELECT * FROM artist WHERE artist_id = "%s" """ % im[4]
cur.execute(arty)
arty = cur.fetchone()

print ("""
<form name = "arty" action="/test/cgi-bin/artistInfo.py">
        <input type="hidden" name="artistID" value="%s">
        
            <a target="_blank"  href="http://localhost:8080/test/cgi-bin/artistInfo.py">Created by: %s </a><br>
        <imput type = "submit" value = "look for artist">
</form>
</font>
</center>
""" % (arty[0], arty[1]))
print ("</body>")