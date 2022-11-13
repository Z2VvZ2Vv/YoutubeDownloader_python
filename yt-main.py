def generate_video_filename():
    return f"{uuid.uuid4()}.mp4"


def download_file(url):
    local_filename = generate_video_filename()
    with requests.get(url, stream=True) as r:
        with open(generate_video_filename(), 'wb') as f:
            shutil.copyfileobj(r.raw, f)
    return local_filename
    
import requests
import shutil
import uuid

#############link de la video ou ID#################
link = "https://www.youtube.com/watch?v=ID_VIDEO"
####################################################
idyt = link.replace("https://www.youtube.com/watch?v=","")

result = requests.get("https://downloader.freemake.com/api/videoinfo/" + idyt)
resultJson = result.json()
getQualities = resultJson.get("qualities")[0]
getUrl = getQualities.get("url")
download_file(getUrl)

