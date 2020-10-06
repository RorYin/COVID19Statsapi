import requests
import bs4
from flask import Flask,jsonify,request

#Setting the flask app
app = Flask(__name__)
app.url_map.strict_slashes=False

def getdata(query):
    if query=="world":
        url="https://www.worldometers.info/coronavirus"

    else:
        url=f"https://www.worldometers.info/coronavirus/country/{query}"

    res = requests.get(url).text
    output=[]
    soup = bs4.BeautifulSoup(res,'lxml')
    i = soup.find_all('div',class_="maincounter-number")
    result={"Active Cases":i[0].span.text,"Recovered":i[2].span.text,"Deaths":i[1].span.text}
    output.append(result)
    return output


@app.route('/')
def home():
    query=request.args.get('q')
    out="Thank You for using api,you have sucessfully deployed it \nHead over to documentation to know how to use api https://github.com/RorYin/COVID19Statsapi"
    if query == None:
        return out
    else:
        data=getdata(query)
        
    return jsonify(data)






if __name__ == '__main__':
    app.debug=True
    app.run()    