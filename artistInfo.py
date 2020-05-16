import cgi
import pymysql

db = pymysql.connect(host='localhost',
    user='gallery',
    passwd='eecs118',
    db= 'gallery')
cur = db.cursor()

#figuring out which image it is
form = cgi.FieldStorage()
artistID = form.getvalue('artistID')


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

artsy = """SELECT * FROM artist WHERE artist_id = "%s" """ % artistID
cur.execute(artsy)
artsy = cur.fetchone()

print ("""
Artist: %s<br>
Birth Year: %s<br>
Country of Origin: %s<br>
Description: %s
</body>
""" % (artsy[1], artsy[2], artsy[3], artsy[4]))