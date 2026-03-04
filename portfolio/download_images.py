import os
import re
import requests

# The HTML files to scan
files = ['index.html', 'projects/mixlife.html']
img_dir = 'images'

if not os.path.exists(img_dir):
    os.makedirs(img_dir)

# Regex to find Webflow CDN links
url_pattern = re.compile(r'https://cdn\.prod\.website-files\.com/[a-z0-9/._-]+')

for file_path in files:
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            urls = url_pattern.findall(content)
            for url in set(urls):
                filename = url.split('/')[-1]
                print(f"Downloading: {filename}")
                try:
                    r = requests.get(url)
                    with open(os.path.join(img_dir, filename), 'wb') as img_f:
                        img_f.write(r.content)
                except Exception as e:
                    print(f"Failed to download {url}: {e}")