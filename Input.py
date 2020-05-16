#main home webpage
import cgi
import time

current_hour = time.strptime(time.ctime(time.time())).tm_hour

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

print("<body bgcolor = '#636E5A'>")  # background color

print("""
<div class="topnav" >
  <a href="#home">Home</a>
  <a class="active" href="http://localhost:8080/test/cgi-bin/galHub.py">List of Galleries  </a>
  <a class="active" href="http://localhost:8080/test/cgi-bin/sort.py">Sort</a>
</div>
""")
# create website title
print("""       <center>                                            
      <h1><font color = 'white'>Image Galleries</font></h1>
      <h4><font color = "white"><p id = 'display'></p></font></h5>
      <h4><font color = 'white'>Display your images here in Image Galleries</font></h4>
      </center>""")

print ("<script>")
if current_hour < 12 :
    print("""
    document.getElementById("display").innerHTML = "Good morning!" """)
elif current_hour >= 12 and current_hour < 15 :
    print("""
        document.getElementById("display").innerHTML = "Good afternoon!" """)
elif current_hour >= 15 :
    print("""
        document.getElementById("display").innerHTML = "Good evening!" """)

print("</script>")

# get info new gallery
print('<p><font size = "4" color = "white">Add new image gallery: </p>')
print("""
    <form action = "/test/cgi-bin/galHUB.py" method = "get">
    <input type="hidden" name="code" value="-1">
    <font color = 'white'>Name of New Gallery:   <input type = "text" name = "galName"></font><br>
    <font color = 'white'>Description of Gallery:   <input type = "text" name = "galDescr"></font><br>
    <input type = "submit" value = "Upload" >
    </form>
""")
#get info for new artist
print('<p><font size = "4" color = "white">Add new Artist: </p>')
print("""
    <form action = "/test/cgi-bin/sort.py" method = "get">
    <input type="hidden" name="code" value="1">
    <font color = 'white'>Artist Name:   <input type = "text" name = "artist_name"></font><br>
    <font color = 'white'>Year Born (input 0 if unknown):  <input type = "text" name = "birthY" /></font><br>
    <font color = 'white'>Country of Origin:  <input type = "text" name = "country" /></font><br>
    <font color = 'white'>Artist Description: <input type = "text" name = "artDescr" size = '30' ></font><br>
    <input type = "submit" value = "Upload" >
    </form>
""")
#get info for new photo
print('<p><font size = "4" color = "white">Add new image to gallery:  </p>')
print('<p><font size = "3" color = "white">Note: desired gallery and artist must already be added</p>')
print("""
    <form action = "/test/cgi-bin/sort.py" method = "get">
    <input type="hidden" name="code" value="2">
    <font color = 'white'>Image Title:   <input type = "text" name = "title"></font><br>
    <font color = 'white'>Image URL:     <input type = "text" name = "url"></font><br>
    <font color = 'white'>Image location:     <input type = "text" name = "location"></font><br>
    <font color = 'white'>Image type (ex: food, place...):     <input type = "text" name = "type"></font><br>
    <font color = 'white'>Year Created:  <input type = "text" name = "year" /></font><br>
    <font color = 'white'>Description:   <input type = "text" name = "descr" size = '30' ></font><br>
    <font color = 'white'>Add to which existing gallery:   <input type = "text" name = "gallery"></font><br>
    <font color = 'white'>Artist:   <input type = "text" name = "artist"></font><br>
    <input type = "submit" value = "Upload" >
    </form>
""")

print("</body>")

