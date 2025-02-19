# SEO Markdown Linter

This repository provides a **GitHub Actions workflow** and a **Python-based linter** to ensure Markdown files follow SEO best practices. It is designed for bloggers, technical writers, and content creators who use **Markdown-based static site generators** (like Hugo) and want to optimize their posts for search engines.

Created by [sedward5](https://sedward5.com), this tool enforces **title length, description length, word count, and heading structure** to improve content visibility and ranking.

---

## 📌 Features

✅ **Title & Description Checks**: Ensures metadata meets SEO-friendly character limits.  
✅ **Word Count Enforcement**: Flags posts that are too short to rank well.  
✅ **H1 Heading Validation**: Prevents improper use of `#` headings, which can impact readability and SEO.  
✅ **GitHub Actions Integration**: Automatically lints changed Markdown files in pull requests and commits.  

---

## 📂 Repository Structure

```
📦 seo-markdown-linter
 ┣ 📂 .github/workflows
 ┃ ┗ 📜 seo-linter.yml       # GitHub Actions workflow for automated linting
 ┣ 📂 scripts
 ┃ ┗ 📜 seo_linter.py        # Python script that performs the SEO checks
 ┗ 📜 README.md              # Documentation (you are here!)
```

---

## 🚀 How to Use

### **1️⃣ Add to Your Repository**
Clone this repo or copy the `scripts/` and `.github/workflows/` directories into your project:

```sh
git clone https://github.com/your-username/seo-markdown-linter.git
cd seo-markdown-linter
```

Or manually copy:

- `scripts/seo_linter.py` → Your repository's `scripts/`
- `.github/workflows/seo-linter.yml` → Your repository's `.github/workflows/`

---

### **2️⃣ Configure the Linter**
Edit `scripts/seo_linter.py` to adjust thresholds like **minimum word count, title length, and H1 usage**.

Example:
```python
MIN_WORD_COUNT = 500  # Adjust as needed
TITLE_MIN = 50
TITLE_MAX = 75
DESC_MIN = 120
DESC_MAX = 158
ALLOW_H1 = False  # Set to True if you want to allow one H1 heading
```

---

### **3️⃣ Enable GitHub Actions**
Once added to your repository, GitHub Actions will automatically run the linter when Markdown files are changed.

To manually trigger a check, run:
```sh
python scripts/seo_linter.py path/to/your-file.md
```

If running via GitHub Actions, simply push a Markdown file change to trigger the workflow.

---

## 📖 Why This Matters

SEO-optimized Markdown ensures **better search rankings**, **improved readability**, and **consistent formatting** across posts. By automating this process, you save time and maintain quality content without manual SEO audits.

---
