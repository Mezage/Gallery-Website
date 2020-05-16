import cgi
import pymysql

db = pymysql.connect(host='localhost',
    user='gallery',
    passwd='eecs118',
    db= 'gallery')
cur = db.cursor()

#figuring out which link called this page up
form = cgi.FieldStorage()
code = form.getvalue('code') #if adding another gallery
#code  = 1 for new artist
#code  = 2 for new image

if (code == "1" and form.getvalue("artist_name") != ""):  # code for adding artist
    artName = form.getvalue("artist_name")
    birth = form.getvalue("birthY")
    country = form.getvalue("country")
    descript = form.getvalue("artDescr")
    sql = ("""INSERT INTO artist(name, birth_year, country, description) 
        VALUES('%s','%s','%s','%s')""" % (artName, birth, country, descript))
    cur.execute(sql)
    db.commit()
if (code == "2" and form.getvalue("title") != ""):  # code for adding picture
    title = form.getvalue("title")
    url = form.getvalue("url")
    location = form.getvalue("location")
    type = form.getvalue("type")
    year = form.getvalue("year")
    artD = form.getvalue("descr")
    gallery = form.getvalue("gallery")
    artist = form.getvalue("artist")

    #retrive what next image ID will be
    nextID = """SELECT MAX(image_id) FROM image"""
    cur.execute(nextID)
    nextID = cur.fetchone()
    if not nextID[0]:               #compensate if DB is empty
        nextID = list(nextID)
        nextID[0] = 0
        nextID = tuple(nextID)



    galleryID = """SELECT gallery_id FROM gallery WHERE name = "%s" """ % gallery
    cur.execute(galleryID)
    galleryID = cur.fetchone()
    artistID = """SELECT artist_id FROM artist WHERE name = "%s" """ % artist
    cur.execute(artistID)
    artistID = cur.fetchone()

    sql = ("""INSERT INTO detail(image_id, year, type, width, height, location, description) 
            VALUES('%s','%s','%s','600','400','%s','%s')""" % (nextID[0]+1, year, type, location, artD))
    cur.execute(sql)

    sql = ("""INSERT INTO image(title, link, gallery_id, artist_id, detail_id) 
        VALUES('%s','%s','%s','%s',LAST_INSERT_ID())""" % (title, url, galleryID[0], artistID[0]))
    cur.execute(sql)
    db.commit()

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
  <a href="#sort">Sort</a>
</div>
""")
print ("<font color ='white'><h3>How would you like to view your photos?</h3></font>")
print("""
<form action = "/test/cgi-bin/sortedView.py" method = "get">
    <input type="hidden" name="sortCode" value="3">
    <input type = "submit" value = "By type" >
    </form>
""")
print("""
<form action = "/test/cgi-bin/sortedView.py" method = "get">
    <input type="hidden" name="sortCode" value="4"><br>
    <input type = "submit" value = "By year" >
    </form>
""")
print("""
<form action = "/test/cgi-bin/sortedView.py" method = "get">
    <input type="hidden" name="sortCode" value="5">
    <br>
    <input type = "submit" value = "By artist" >
    </form>
""")
print("""
<form action = "/test/cgi-bin/sortedView.py" method = "get">
    <input type="hidden" name="sortCode" value="6">
    <br>
    <input type = "submit" value = "By location" >
    </form>
""")
print ("<font color ='white'><h3>How would you like to view your artists?</h3></font>")
print("""
<form action = "/test/cgi-bin/sortedView.py" method = "get">
    <input type="hidden" name="sortCode" value="7">
    <br>
    <input type = "submit" value = "By country" >
    </form>
""")
print("""
<form action = "/test/cgi-bin/sortedView.py" method = "get">
    <input type="hidden" name="sortCode" value="8">
    <br>
    <input type = "submit" value = "By Artist Birth Year" >
    </form>
""")
