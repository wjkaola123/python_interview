from markitdown import MarkItDown

md = MarkItDown()
result = md.convert("吴杰.pdf")

with open("resume.md", "w", encoding="utf-8") as f:
    f.write(result.text_content)
