class TextFormatter:
    def format_content(self, text):
        return text.upper()

class HTMLFormatter:
    def format_content(self, text):
        return f"<div>{text}</div>"

class MarkdownFormatter:
    def format_content(self, text):
        return f"**{text}**"

def apply_formatting(formatter_instance, content):
    """
    Applies formatting to content using the provided formatter instance.
    This function relies on duck typing: any object with a 'format_content' method works.
    """
    return formatter_instance.format_content(content)

if __name__ == "__main__":
    message = "Hello, Advanced Polymorphism!"

    text_formatter = TextFormatter()
    html_formatter = HTMLFormatter()
    markdown_formatter = MarkdownFormatter()

    print(f"Text Formatted: {apply_formatting(text_formatter, message)}")
    print(f"HTML Formatted: {apply_formatting(html_formatter, message)}")
    print(f"Markdown Formatted: {apply_formatting(markdown_formatter, message)}")