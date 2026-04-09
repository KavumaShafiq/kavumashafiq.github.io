import base64
import os
import re

img_dir = r'd:\Users\Award\Desktop\shamim angel\images'
html_file = r'd:\Users\Award\Desktop\shamim angel\index.html'

# Create mapping of image files to base64 data URIs
image_map = {}
for img_file in os.listdir(img_dir):
    if img_file.lower().endswith('.jpg'):
        path = os.path.join(img_dir, img_file)
        with open(path, 'rb') as f:
            b64 = base64.b64encode(f.read()).decode()
        image_map[img_file] = f'data:image/jpeg;base64,{b64}'

# Read HTML file
with open(html_file, 'r', encoding='utf-8') as f:
    html_content = f.read()

# Replace all image paths
for img_file, b64_uri in image_map.items():
    # Replace full Windows paths (with backslashes)
    full_path = os.path.join(img_dir, img_file)
    html_content = html_content.replace(full_path, b64_uri)
    # Also try with forward slashes
    html_content = html_content.replace(full_path.replace('\\', '/'), b64_uri)
    # Replace with regex for any variation
    pattern = rf'src=["\']([^"\']*)?{re.escape(img_file)}["\']'
    html_content = re.sub(pattern, f'src="{b64_uri}"', html_content, flags=re.IGNORECASE)

# Write back to HTML file
with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Successfully embedded {len(image_map)} images into the HTML file!")
print("Your index.html is now self-contained with all images embedded.")
