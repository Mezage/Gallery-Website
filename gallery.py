import cgi
import pymysql
counter = 0

#To Create a Connection with MySQL Server
db = pymysql.connect(host='localhost',
    user='gallery',
    passwd='eecs118',
    db= 'gallery')
#host is address of server, 127.0.0.1 means own computer (local)
cur = db.cursor()

#getting value from first page
form = cgi.FieldStorage()
galID = form.getvalue('galleryID')

sql = """SELECT COUNT(*) FROM image WHERE gallery_id = "%s" """ % galID
cur.execute(sql)
counter = cur.fetchone()

images = """SELECT * FROM image WHERE gallery_id = "%s" """ % galID
cur.execute(images)


print("Content-Type: text/html\r\n\r\n")    #HTML is following
#setting up picture gallery
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
""")
print("""
    div.gallery {
        margin: 5px;
        border: 1px solid #ccc;
        float: left;
        width: 180px;
    }

    div.gallery:hover {
        border: 1px solid #777;
    }
    
    div.gallery img {
        width: 100%;
        height: auto;
    }

    div.desc {
        padding: 15px;
        text-align: center;
        color: white
    }
</style>
</head>
""")
print("<h1><center><font color = 'white'>Gallery Images</font></center></h1>")
print("<body bgcolor = '#636E5A'>")         #background color
print("""
<div class="topnav">
  <a class="active" href="http://localhost:8080/test/cgi-bin/Input.py">Home</a>
  <a class="active" href="http://localhost:8080/test/cgi-bin/galHUB.py">List of Galleries</a>
  <a class="active" href="http://localhost:8080/test/cgi-bin/sort.py">Sort</a>
</div>
""")

print ("<font color = 'white'><p>This is your gallery, it has %s picture(s)</p></font>" % counter[0])

#################################################### picture slots ###############################
for row in cur.fetchall():
    print("""
    <form name = "picture" action="/test/cgi-bin/pictureInfo.py">
        <input type="hidden" name="picID" value="%s">
        <div class="gallery" onCLick="document.forms['picture'].submit()">
          <a target="_blank" href="http://localhost:8080/test/cgi-bin/pictureInfo.py">
            <img src="%s" alt="no image" width="600" height="400">
          </a>
          <div class="desc">Title: %s</div>
        </div>
    </form>
    """ % (row[0], row[2], row[1]))

#buttons
#print('<center><button type = "button" onclick = "Change()">Add Image</button></center>')

print("</body>")