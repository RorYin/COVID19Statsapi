# Get COVID19 Stats using this api 

<br>

## Requirements: flask,Beautiful Soup,lxml parser 
<br>


### To install flask run the command on your terminal/cmd
``` pip install flask ``` <br>
### To install Beautiful Soup the command on your terminal/cmd
``` pip install bs4 ``` <br>
### To install lxml parser the command on your terminal/cmd
``` pip install lxml ``` <br>

# api usage:

### To get world stats:
``` https://baseurl.herokuapp.com/?q=world ```

### Sample Response
``` [
  {
    "Active Cases": "35,777,844 ",
    "Deaths": "1,049,700",
    "Recovered": "26,907,997"
  }
]

```
<br>

### To get specific country stats:

``` https://baseurl.herokuapp.com/?q=Country_name ```

### Country_name:

```
india
us
indonesia
brazil
russia
colombia
spain
peru
argentina
south-africa
france
uk
iran
iraq
bangladesh
saudi-arabia
italy
philippines
turkey
pakistan
germany
israel
japan
china


...basically every "Country name" in lower case 
```
<br>

## If you run the app.py on your pc ,you see the api working on the below link
``` http://127.0.0.1:5000/?q=india ```
<br>
<br>

## Get your baseurl by deploying to heroku 👇
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/RorYin/COVID19Statsapi)

<br>

## **Star the Repo in case you liked it :)**
### © [Dhanush N](https://github.com/RorYin)