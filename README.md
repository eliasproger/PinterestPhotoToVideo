
# Pinterest Photo To TikTok Video

This script download photo from pinterest and make 60 seconds video.

How to start:  

Type into cmd:  
```commandline
git clone https://github.com/EliasProger/PinterestPhotoToTikTokVideo.git  
```

```commandline
pip install -r requirements.txt
```
After run: pinterest-downloader.py  
```commandline
python pinterest-downloader.py
```
And input UserName/BoardName

<b><u>Type into config.json Image Folder Path</u></b>  

<b><u>Type into config.json Video Folder Path</u></b>

For create Videos

You can run main.py  
```commandline
python main.py
```
or

Type This Code:
```python
from main import filter_image, image_resize, save_video, sub_video
import json

path = json.load(open('config.json', 'r'))["Image Folder Path"]

filter_image(path)
image_resize(path)
save_video(path)
sub_video()
```