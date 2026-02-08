# 📚 LIBRIS - Advanced Librarian AI Agent

> **Free for the world to use** • Powered by Claude AI • Open Source

LIBRIS (Library Intelligence & Research Information System) is an advanced AI librarian specializing in historical and philosophical collections. It helps researchers, students, and curious minds discover and analyze texts spanning 3000 BC to present.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-app-name.streamlit.app)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Powered by Claude](https://img.shields.io/badge/Powered%20by-Claude%20AI-blue)](https://www.anthropic.com)

---

## ✨ Features

### 🔍 **Intelligent Search**
- Search across ~1,100 historical and philosophical works
- Natural language queries ("find ancient Greek ethics")
- Cross-cultural perspectives (Greek, Islamic, Chinese, Indian, etc.)
- Transliteration-aware matching

### 📄 **Document Processing**
- Upload reading lists, syllabi, bibliographies
- Automatic bibliographic data extraction
- Categorization by era, genre, and tradition
- Gap analysis and thematic insights

### 🌍 **Cross-Cultural Knowledge**
- Ancient Greek & Roman philosophy
- Islamic Golden Age texts
- Chinese Confucian & Daoist classics
- Indian philosophical traditions
- Medieval European thought
- Modern philosophy & social theory

### 📊 **Multiple Export Formats**
- BibTeX (for academic papers)
- CSV (for spreadsheets)
- JSON (for databases)
- Plain text (for notes)

---

## 🚀 Try It Now

**Live Demo:** [https://your-app-name.streamlit.app](https://your-app-name.streamlit.app)

No installation required! Just visit the link and start exploring.

---

## 💻 Run Locally

### Prerequisites
- Python 3.8 or higher
- Anthropic API key ([get one here](https://console.anthropic.com/settings/keys))

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/libris.git
   cd libris
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set your API key:**
   
   Create a `.streamlit/secrets.toml` file:
   ```toml
   ANTHROPIC_API_KEY = "your-api-key-here"
   ```
   
   Or set environment variable:
   ```bash
   export ANTHROPIC_API_KEY="your-api-key-here"
   ```

4. **Run the app:**
   ```bash
   streamlit run streamlit_app.py
   ```

5. **Open your browser:**
   Navigate to `http://localhost:8501`

---

## 🌐 Deploy Your Own

### Deploy to Streamlit Cloud (FREE)

1. **Fork this repository** on GitHub
2. **Sign up** at [share.streamlit.io](https://share.streamlit.io)
3. **Create new app:**
   - Repository: `yourusername/libris`
   - Branch: `main`
   - Main file: `streamlit_app.py`
4. **Add secrets:**
   - Go to app settings → Secrets
   - Add: `ANTHROPIC_API_KEY = "your-key"`
5. **Deploy!** Your app will be live at `your-app-name.streamlit.app`

**Full deployment guide:** See [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)

---

## 📖 Usage Examples

### Search for Books
```
Search: "ancient Greek ethics"
→ Returns: Plato's Republic, Aristotle's Nicomachean Ethics, etc.
```

### Upload a Syllabus
```
Upload: philosophy_101_syllabus.pdf
→ LIBRIS extracts all readings and categorizes them
```

### Ask Questions
```
You: "What are the major schools of Buddhist philosophy?"
LIBRIS: [Detailed explanation with key texts]
```

### Export Results
```
After any search, export as:
- BibTeX for LaTeX papers
- CSV for spreadsheets
- JSON for databases
```

---

## 🎓 Use Cases

- **Academic Research** - Find and organize historical texts
- **Teaching** - Create comprehensive reading lists
- **Student Study** - Explore philosophical traditions
- **Library Science** - Catalog and cross-reference collections
- **Personal Learning** - Discover new authors and works

---

## 🛠️ Technology Stack

- **Frontend:** Streamlit
- **AI Backend:** Anthropic Claude API (Claude Sonnet 4.5)
- **Language:** Python 3.8+
- **Hosting:** Streamlit Cloud (free tier)

---

## 💰 Cost & Usage

### For Users (Free!)
- Completely free to use
- No account required
- No usage limits

### For Deployers
- **Hosting:** FREE on Streamlit Cloud
- **API Costs:** ~$3-10/month depending on usage
  - 100 searches: ~$1-2
  - 50 document uploads: ~$2.50-5
  - Typical monthly cost: $5-15

**Note:** You can set usage limits in Anthropic console to control costs.

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### Ideas for Contributions
- 🌍 Add more cultural/linguistic traditions
- 📚 Expand the knowledge base
- 🎨 Improve UI/UX
- 🔍 Enhance search algorithms
- 📱 Create mobile app version
- 🌐 Add translations (internationalization)
- 📖 Write documentation
- 🐛 Report bugs

### How to Contribute
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

**You are free to:**
- ✅ Use commercially
- ✅ Modify
- ✅ Distribute
- ✅ Private use

**With attribution and including the license notice.**

---

## 🙏 Acknowledgments

- **Anthropic** - For Claude AI technology
- **Streamlit** - For the amazing web framework
- **Contributors** - Everyone who helps make knowledge accessible
- **Open Source Community** - For inspiration and support

---

## 📞 Support & Contact

- **Issues:** [GitHub Issues](https://github.com/yourusername/libris/issues)
- **Discussions:** [GitHub Discussions](https://github.com/yourusername/libris/discussions)
- **Email:** your-email@example.com

---

## 🗺️ Roadmap

### Current Version (v1.0)
- ✅ Core search functionality
- ✅ Document processing
- ✅ Multiple export formats
- ✅ Web interface

### Planned Features
- 🔜 Advanced filtering (date ranges, regions)
- 🔜 Visualization of intellectual lineages
- 🔜 Collaborative collections
- 🔜 Mobile app
- 🔜 API for developers
- 🔜 Multi-language support
- 🔜 Integration with Zotero/Mendeley

---

## 📊 Statistics

- **~1,100** core philosophical and historical works
- **3000 BC - Present** temporal coverage
- **Multiple traditions** - Greek, Roman, Islamic, Chinese, Indian, African, European
- **Free forever** - Committed to open access

---

## ⚠️ Important Notes

### API Key Security
- **Never commit your API key to GitHub**
- Use Streamlit secrets or environment variables
- The `.gitignore` file is configured to prevent accidental commits
- Rotate your key if accidentally exposed

### Fair Use
- LIBRIS is designed for educational and research purposes
- Respect copyright when using exported bibliographies
- Cite sources appropriately in your work

### Accuracy
- LIBRIS uses AI and may occasionally make errors
- Always verify critical information from primary sources
- Report inaccuracies via GitHub Issues

---

## 🌟 Star This Project

If you find LIBRIS useful, please ⭐ star this repository to help others discover it!

---

## 📚 Related Projects

- [Claude AI](https://www.anthropic.com/claude) - The AI powering LIBRIS
- [Streamlit](https://streamlit.io) - The web framework
- [Project Gutenberg](https://www.gutenberg.org) - Free ebooks
- [Stanford Encyclopedia of Philosophy](https://plato.stanford.edu) - Philosophy reference
- [Internet Archive](https://archive.org) - Digital library

---

<div align="center">

**Made with ❤️ for the world**

[🌐 Live Demo](https://your-app-name.streamlit.app) • [📖 Documentation](DEPLOYMENT_GUIDE.md) • [🐛 Report Bug](https://github.com/yourusername/libris/issues) • [💡 Request Feature](https://github.com/yourusername/libris/issues)

</div>
