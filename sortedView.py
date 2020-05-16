import cgi
import pymysql

db = pymysql.connect(host='localhost',
    user='gallery',
    passwd='eecs118',
    db= 'gallery')
cur = db.cursor()
cur2 = db.cursor()      #separate cursor for looking through db

#3= by type
#4= by year created
#5= by artist
#6= by location
#7= by artist country
#8= by artistDOB

#figuring out which link called this page up
form = cgi.FieldStorage()
code = form.getvalue('sortCode')
index=0

sql = ("SELECT * FROM image ")
cur.execute(sql)

if (code == "3"):
    index=1
elif (code == "4"):
    index=2
elif (code == "5"):
    index=4
elif (code == "6"):
    index=3
elif (code == "7"):
    index=5
else:
    index=6


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
""")
print ("""
* {
  box-sizing: border-box;
}

#myInput {
  
  background-position: 10px 10px;
  background-repeat: no-repeat;
  width: 40%;
  font-size: 16px;
  padding: 12px 20px 12px 40px;
  border: 1px solid #ddd;
  margin-bottom: 4px;
}

#myTable {
  border-collapse: collapse;
  width: 100%;
  border: 1px solid #ddd;
  font-size: 18px;
}

#myTable th, #myTable td {
  text-align: left;
  padding: 12px;
}

#myTable tr {
  border-bottom: 1px solid #ddd;
}

#myTable tr.header, #myTable tr:hover {
  background-color: #f1f1f1;
}
</style>
</head>
""")
print("<body bgcolor = '#636E5A'>")         #background color
print("""
<div class="topnav">
  <a class="active" href="http://localhost:8080/test/cgi-bin/Input.py">Home</a>
  <a class="active" href="http://localhost:8080/test/cgi-bin/galHUB.py">List of Galleries</a>
  <a class="active" href="http://localhost:8080/test/cgi-bin/sort.py">Sort</a>
</div>
<br>
""")
print ("""
<input type="text" id="myInput" onkeyup="myFunction()" placeholder="Search by how you indicated" title="Type in a name">

<table id="myTable">
  <tr class="header">
    <th style="width:14%;">Image and Title</th>
    <th style="width:14%;">Image Type</th>
    <th style="width:14%;">Year Created</th>
    <th style="width:14%;">Image Location</th>
    <th style="width:14%;">Artist</th>
    <th style="width:14%;">Artist's Country</th>
    <th style="width:14%;">Artist's Birth Year</th>
  </tr>""")
for row in cur.fetchall():  #iterating through image db
    artID = """SELECT * FROM artist WHERE artist_id = "%s" """ % row[4]
    cur2.execute(artID)
    artID = cur2.fetchone()
    details = """SELECT * FROM detail WHERE detail_id = "%s" """ % row[5]
    cur2.execute(details)
    details = cur2.fetchone()

    print ("""
      <tr>
        <td>%s
        <img src="%s" alt="no_image" width="300" height="200">
        </td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
      </tr>
    """ % (row[1], row[2], details[3], details[2], details[6], artID[1], artID[3], artID[2]))

print ("</table>")
print ("""
<script>
function myFunction() {
  var input, filter, table, tr, td, i, txtValue;
  input = document.getElementById("myInput");
  filter = input.value.toUpperCase();
  table = document.getElementById("myTable");
  tr = table.getElementsByTagName("tr");
  for (i = 0; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td")[%d];
    if (td) {
      txtValue = td.textContent || td.innerText;
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    }       
  }
}
</script>
</body>
""" % index)