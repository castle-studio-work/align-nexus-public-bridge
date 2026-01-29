import os
import markdown
import json

files_data = []
base_html_template = """<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>body{{font-family:sans-serif;max-width:800px;margin:40px auto;padding:20px;line-height:1.6;}}</style>
</head>
<body>
{}
</body>
</html>"""

# 掃描目前的 md 檔案 (排除 index.md 等)
for filename in os.listdir('.'):
    if filename.endswith('.md') and filename not in ['index.md', 'links.md']:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
            # 提取前三行非空內容作為預覽
            lines = [l.strip() for l in content.split('\n') if l.strip()]
            preview = " | ".join(lines[:3])
            
            # 轉換為 HTML
            html_content = markdown.markdown(content)
            full_html = base_html_template.format(html_content)
            
            html_filename = filename.replace('.md', '.html')
            with open(html_filename, 'w', encoding='utf-8') as hf:
                hf.write(full_html)
            
            files_data.append({
                "name": filename,
                "html": html_filename,
                "preview": preview
            })

# 輸出 JSON 供 index.html 使用
with open('files_data.json', 'w', encoding='utf-8') as jf:
    json.dump(files_data, jf, ensure_ascii=False)

