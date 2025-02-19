import sys
import frontmatter
import re

# Configurable limits
TITLE_MIN = 50
TITLE_MAX = 75
DESC_MIN = 120
DESC_MAX = 158
MIN_WORD_COUNT = 500
ALLOW_H1 = False  # Set to True if H1s are allowed, False if not

def lint_markdown(file_path):
    errors = []
    
    with open(file_path, 'r', encoding='utf-8') as f:
        post = frontmatter.load(f)  # Load front matter and content

    title = post.get('title', '')
    description = post.get('description', '')
    content = post.content  # Correct way to get Markdown body

    # Check title length
    if not (TITLE_MIN <= len(title) <= TITLE_MAX):
        errors.append(f"Title length ({len(title)} characters) is out of range ({TITLE_MIN}-{TITLE_MAX}): '{title}'")

    # Check description length
    if not (DESC_MIN <= len(description) <= DESC_MAX):
        errors.append(f"Description length ({len(description)} characters) is out of range ({DESC_MIN}-{DESC_MAX}): '{description}'")

    # Check word count
    word_count = len(content.split())
    if word_count < MIN_WORD_COUNT:
        errors.append(f"Word count ({word_count}) is below minimum required ({MIN_WORD_COUNT}).")

    # Check for H1 headings using regex
    h1_count = len(re.findall(r'(?m)^# (?!#)', content))  # Matches single H1s at start of a line
    if (not ALLOW_H1 and h1_count > 0) or (ALLOW_H1 and h1_count > 1):
        errors.append(f"Invalid number of H1 headings ({h1_count}). Allowed: {'1' if ALLOW_H1 else '0'}.")

    # Print errors if found
    if errors:
        print("\nSEO Linter Errors Found:")
        for err in errors:
            print(f"- {err}")
        sys.exit(1)  # **Exit with non-zero status to fail the action**

    print("✅ SEO checks passed.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python seo_linter.py <markdown-file>")
        sys.exit(1)

    lint_markdown(sys.argv[1])
