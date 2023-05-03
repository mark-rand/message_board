import http.client
import xml.etree.ElementTree as ET
import re


def get_news():
    conn = http.client.HTTPSConnection("feeds.skynews.com")
    payload = ""
    conn.request("GET", "/feeds/rss/home.xml", payload)
    res = conn.getresponse()
    data = res.read()
    root = ET.fromstring(data.decode("utf-8"))
    news_text = "News from Sky: "
    for child in root.find('channel').findall('item'):
        title = child.findall('title')[0]
        news_text = news_text + title.text + " ... "
    return news_text


def get_weather(location, friendly_name):
    conn = http.client.HTTPSConnection("weather-broker-cdn.api.bbci.co.uk")
    payload = ""
    conn.request("GET", f"/en/observation/rss/{location}", payload)
    res = conn.getresponse()
    data = res.read()
    root = ET.fromstring(data.decode("utf-8"))
    weather = ""
    for child in root.iter('title'):
        weather = weather + child.text + " ... "
    temp = re.findall("[0-9]+°C", weather)
    formatted_weather = f"  Current Temp. in {friendly_name}: {temp[0]}  "
    return formatted_weather


if __name__ == "__main__":
    print(get_news())
    print(get_weather("2643743", "London"))
