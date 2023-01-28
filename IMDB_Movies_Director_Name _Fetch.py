from bs4 import BeautifulSoup
import requests

moviename = input("Enter the movie name")
moviename = moviename.lower()

r=requests.get('htps://www.imdb.com/chart/top/')
html = r.text
soup = BeautifulSoup(html, 'html.parser')
tb=soup.find('tbody',{'class':'lister-list'})
trs=tb.findAll('tr',{'class'})
trs=tb.findAll('tr')

for tr in trs:
  td= tr.find('td',{'class':'titleColumn'})
  imdbmovie=td.a.string.strip().lower()
  # print(imdbmovie)
  if moviename == imdbmovie:
    movieid = td.a['href']
    # print(movieid)
    movieurl = f'https://www.imdb.com/{movieid}'
    #print(movieurl)
    r1 = requests.get('https://www.imdb.com/{movieid}')
    html = r1.text
    soup2 = BeautifulSoup(html, 'html.parser')
    print(soup2)
    # div = soup.find('div', {'class'} : )
    
    #OUTPUT
   Enter the movie name the godfather

<!DOCTYPE html>

<html lang="en">
<head>
<meta charset="utf-8"/>
<title>404 Error - IMDb</title>
<style>
html, body {
  height: 100%;
}
body {
  margin: auto;
  width: 1008px;
  background-color: #D4D9DD;
  font-family: Verdana, Arial, sans-serif;
}
a {
  text-decoration: none;
}
a:hover {
  text-decoration: underline;
}
a:link, a:hover, a:visited {
  color: #136CB2;
}
a:active {
  color: #E7BE00;
}
#error {
  height: 100%;
  background-color: white;
  border-left: 1px solid #999999;
  border-right: 1px solid #999999;
  box-shadow: 0 0 5px 5px #C5CACD;
}
.error_message {
  color: #999999;
  font-size: 17.5px;
  padding: 30px 70px 20px;
}
.error_bubble {
  font-family: Arial, helvetica, sans-serif;
  font-weight: bold;
  border-radius: 8px;
  -moz-border-radius: 8px;
  margin: 0 70px 0 70px;
  padding: 50px;
}
.error_bubble div {
  display: inline-block;
  vertical-align: middle;
}
.error_quote {
  color: #FFFFFF;
  font-size: 30px;
  line-height: 1.35em;
  padding-left: 50px;
  width: 500px;
}
.error_code {
  font-size: 100px;
  line-height: 50px;
  margin-top:8px
}
.error_arrow {
  border-color: #DECA16 transparent transparent transparent;
  border-style: solid;
  border-width: 21px 0px 0px 32px;
  height: 0;
  left: 700px;
  line-height: 0;
  position: relative;
  top: -1px;
  width: 0;
}
.error_code > span {
  font-size: 50px;
}
.error_attrib {
  color: #999999;
  float: right;
  font-size: 14px;
  font-style: italic;
  padding: 10px 70px 36px;
}
.error_code_403 .error_bubble,
.error_code_404 .error_bubble,
.error_code_400 .error_bubble,
.error_code_409 .error_bubble  {
  background: none repeat scroll 0% 0% #DECA16;
  border: 1px solid #DECA16;
}
.error_code_403 .error_code,
.error_code_404 .error_code,
.error_code_400 .error_code,
.error_code_409 .error_code {
  color: #BFAD13;
}
.error_code_500 .error_bubble {
  background: none repeat scroll 0% 0% #EDCA24;
  border: 1px solid #EDCA24;
}
.error_code_500 .error_code {
  color: #CCAD1F;
}
.error_code_500 .error_arrow{
  border-color: #EDCA24 transparent transparent transparent;
}
.error_code_503 .error_bubble {
  background: none repeat scroll 0% 0% #2E9CEA;
  border: 1px solid #2E9CEA;
}
.error_code_503 .error_code {
  color: #2173B2;
}
.error_code_503 .error_arrow {
  border-color: #2E9CEA transparent transparent transparent;
}
a.btn {
  background-repeat: repeat-x; 
  background-color: #ECE2C6;
  background-image: linear-gradient(rgba(255,255,255,.8) 5%, rgba(255,255,255,0.0) 70%, rgba(255,255,255,0.8) 100%); 
  background-image: -moz-linear-gradient(rgba(255,255,255,.8) 5%, rgba(255,255,255,0.0) 70%, rgba(255,255,255,0.8) 100%); 
  background-image: -webkit-linear-gradient(rgba(255,255,255,.8) 5%, rgba(255,255,255,0.0) 70%, rgba(255,255,255,0.8) 100%); 
  background-image: -ms-linear-gradient(rgba(255,255,255,.8) 5%, rgba(255,255,255,0.0) 70%, rgba(255,255,255,0.8) 100%); 
  border-color: #E0E0E0 #C0C0C0 #C0C0C0 #E0E0E0;
  border-radius: 3px 3px 3px 3px;
  border-style: solid;
  border-width: 1px;
  color: #000000;
  cursor: pointer;
  float: right;
  margin-right: 70px;
  margin-top: 26px;
  padding: 0.3em 0.6em;
  text-decoration: none;
}
a.btn:hover {
  background-image: none;
  border-color: #E6B800;
}
.clear {
  clear: both;
}
  </style>
</head>
<body>
<div class="error_code_404" id="error">
<div class="error_message">
        The requested URL was not found on our server.
        <a href="/">Go to the homepage</a> »
    </div>
<div class="error_bubble">
<div class="error_code">404<br/><span>ERROR</span></div>
<div class="error_quote">Always remember, Frodo, the page is trying to get back to its master. It wants to be found.</div>
</div>
<div class="error_arrow"></div>
<div class="error_attrib">
<span>Gandalf, </span><a href="/title/tt0120737/">The Lord of the Rings: The Fellowship of the Ring (2001)</a>
</div>
<div class="clear"></div>
</div>
<!-- The next level -->
</body>
</html>


