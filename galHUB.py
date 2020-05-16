#displays the hub of galleries
import pymysql
import cgi

db = pymysql.connect(host='localhost',
    user='gallery',
    passwd='eecs118',
    db= 'gallery')
cur = db.cursor()

#figuring out which link called this page up
form = cgi.FieldStorage()
code = form.getvalue('code') #if adding another gallery

if (code == "-1" and form.getvalue("galName") != ""):  # code for adding gallery
    galName = form.getvalue("galName")
    galDesc = form.getvalue("galDescr")
    sql = ("""INSERT INTO gallery(name, description) 
        VALUES('%s','%s')""" % (galName, galDesc))
    cur.execute(sql)
    db.commit()

#after db update, load it up
galleryList = "SELECT * FROM gallery"
cur.execute(galleryList)


#tabs styling
print ("Content-Type: text/html\r\n\r\n")
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
  <a href="#galleries">List of Galleries</a>
  <a class="active" href="http://localhost:8080/test/cgi-bin/sort.py">Sort</a>
</div>
""")

print ("<h2><font color='white'>Here are the galleries available:</font></h2> <br>")

for row in cur.fetchall():
    #add in hidden value
    print("""
    <form name = "galleryName" action="/test/cgi-bin/gallery.py">
        <input type="hidden" name="galleryID" value="%s">
        <div class="gallery" onCLick="document.forms['galleryName'].submit()">
          <a target="_blank" href="http://localhost:8080/test/cgi-bin/gallery.py">
            <h4><p>%s</p></h4>
          </a>
          <font color = 'white'>Description: %s</font>
        </div>
    </form>
        """ % (str(row[0]), str(row[1]), str(row[2])))  # replace with whatever position it is in row[]
