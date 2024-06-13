import requests as re

base_url = "https://www.whenisthenextmcufilm.com/api"

def next_mcu_movie(release=""):
    if release:
        url = base_url + "/?date="+release
    else: 
        url = base_url
    response = re.get(url)

    if response.ok: 
        results = response.json()
        title = results.get("title")
        release_date = results.get("release_date")
        overview = results.get("overview")
        output = f"<h2>Title: {title} </h2><p>{overview}<br>{release_date}</p>"
        return output, release_date
    
if __name__ == "__main__":
    next, release = next_mcu_movie()
    print(next)
    next, release = next_mcu_movie(release)
    print(next)
    

     