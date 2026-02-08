# 🤝 Contributing to LIBRIS

Thank you for your interest in making LIBRIS better! This guide will help you contribute to making knowledge more accessible worldwide.

---

## 🌟 Ways to Contribute

You don't need to be a developer to help!

### For Everyone:
- 🐛 **Report Bugs** - Found something that doesn't work? Let us know!
- 💡 **Suggest Features** - Have an idea? Share it!
- 📝 **Improve Documentation** - Help others understand LIBRIS better
- 🌍 **Translate** - Help make LIBRIS multilingual
- 📢 **Spread the Word** - Share LIBRIS with others who might benefit

### For Developers:
- 🔧 **Fix Bugs** - Help squash issues
- ✨ **Add Features** - Build new capabilities
- 🎨 **Improve UI/UX** - Make LIBRIS more beautiful and usable
- ⚡ **Optimize Performance** - Make it faster and more efficient
- 🧪 **Write Tests** - Improve code quality and reliability

### For Researchers & Scholars:
- 📚 **Expand Knowledge Base** - Add more texts and traditions
- 🔍 **Improve Search** - Enhance categorization and tagging
- 🌐 **Add Cultural Perspectives** - Include underrepresented traditions
- ✅ **Verify Accuracy** - Check bibliographic data

---

## 🚀 Quick Start for Contributors

### 1. Fork the Repository

1. Go to https://github.com/yourusername/libris
2. Click "Fork" (top right)
3. You now have your own copy!

### 2. Clone Your Fork

```bash
git clone https://github.com/YOUR-USERNAME/libris.git
cd libris
```

### 3. Create a Branch

```bash
git checkout -b feature/your-feature-name
```

**Branch naming:**
- Feature: `feature/add-export-format`
- Bug fix: `fix/search-error`
- Documentation: `docs/improve-readme`

### 4. Make Your Changes

- Edit files locally
- Test thoroughly
- Follow code style guidelines (see below)

### 5. Commit Your Changes

```bash
git add .
git commit -m "Add feature: brief description"
```

**Good commit messages:**
- ✅ "Add CSV export functionality"
- ✅ "Fix: Search not returning Chinese texts"
- ✅ "Docs: Add deployment troubleshooting"
- ❌ "update"
- ❌ "fix bug"

### 6. Push to Your Fork

```bash
git push origin feature/your-feature-name
```

### 7. Create Pull Request

1. Go to your fork on GitHub
2. Click "Pull Request"
3. Fill in:
   - **Title:** Clear, concise description
   - **Description:** What changed and why
   - **Related Issue:** Link to issue if applicable
4. Click "Create Pull Request"

---

## 📋 Contribution Guidelines

### Code Style

**Python (PEP 8):**
```python
# Good
def search_books(query: str, max_results: int = 10) -> list:
    """Search for books matching the query.
    
    Args:
        query: Search query string
        max_results: Maximum number of results to return
        
    Returns:
        List of matching books
    """
    # Implementation
    pass

# Bad
def search(q,m=10):
    # Implementation
    pass
```

**Streamlit:**
```python
# Use clear variable names
user_query = st.text_input("Search Query")

# Add helpful text
st.markdown("**Tip:** Try searching for author names or themes")

# Use session_state for persistence
if 'messages' not in st.session_state:
    st.session_state.messages = []
```

### Documentation

- Add docstrings to all functions
- Update README when adding features
- Include examples in documentation
- Comment complex logic

### Testing

Before submitting:

```bash
# Test locally
streamlit run streamlit_app.py

# Check all features:
# - Search works
# - Upload works
# - Chat works
# - Export works
# - No errors in console
```

### Commit Messages

Follow this format:
```
<type>: <subject>

<body (optional)>

<footer (optional)>
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation
- `style`: Formatting
- `refactor`: Code restructuring
- `test`: Adding tests
- `chore`: Maintenance

**Examples:**
```
feat: Add support for PDF export

- Implemented PDF generation using ReportLab
- Added PDF button to export tab
- Updated documentation

Closes #42
```

---

## 🐛 Reporting Bugs

### Before Reporting

1. **Check existing issues** - Maybe it's already reported
2. **Test on latest version** - Is it still a problem?
3. **Verify it's reproducible** - Can you make it happen again?

### Bug Report Template

```markdown
**Describe the bug**
A clear description of what's wrong.

**To Reproduce**
Steps to reproduce:
1. Go to '...'
2. Click on '...'
3. See error

**Expected behavior**
What should happen instead.

**Screenshots**
If applicable, add screenshots.

**Environment:**
- OS: [e.g., Windows 10, macOS 14]
- Browser: [e.g., Chrome 120, Firefox 121]
- LIBRIS version: [e.g., v1.0]

**Additional context**
Any other relevant information.
```

---

## 💡 Suggesting Features

### Feature Request Template

```markdown
**Is your feature request related to a problem?**
A clear description of the problem.

**Describe the solution you'd like**
What you want to happen.

**Describe alternatives you've considered**
Other approaches you thought about.

**Additional context**
Why this would be useful, who would benefit, etc.

**Would you be willing to implement this?**
[ ] Yes, I can help code this
[ ] Yes, I can help test this
[ ] No, but I'd use it
```

---

## 🎯 Priority Areas for Contribution

We especially welcome help with:

### High Priority
1. **Performance Optimization**
   - Caching frequently searched queries
   - Reducing API calls
   - Faster document processing

2. **Mobile Experience**
   - Better mobile UI
   - Touch-friendly controls
   - Responsive design improvements

3. **Accessibility**
   - Screen reader support
   - Keyboard navigation
   - ARIA labels
   - High contrast mode

### Medium Priority
4. **New Export Formats**
   - EndNote
   - RIS
   - Zotero integration
   - Mendeley integration

5. **Advanced Search**
   - Date range filtering
   - Region/culture filtering
   - Combine multiple filters
   - Save search queries

6. **Visualization**
   - Timeline of intellectual history
   - Connection graphs between texts
   - Geographic distribution

### Nice to Have
7. **User Accounts** (optional)
   - Save collections
   - Track reading lists
   - Share collections

8. **API for Developers**
   - REST API endpoints
   - Python SDK
   - JavaScript SDK

9. **Internationalization**
   - Multi-language UI
   - Translation support
   - RTL language support

---

## 🧪 Testing Guidelines

### Manual Testing Checklist

Before submitting PR, verify:

**Search Functionality:**
- [ ] Simple keyword search works
- [ ] Author search works
- [ ] Multi-word queries work
- [ ] Special characters handled
- [ ] No search returns appropriate message

**Document Upload:**
- [ ] TXT files process correctly
- [ ] MD files process correctly
- [ ] CSV files process correctly
- [ ] Large files (>100KB) handle gracefully
- [ ] Error handling for invalid files

**Chat:**
- [ ] Conversation maintains context
- [ ] Long conversations don't crash
- [ ] Special characters in messages work

**Export:**
- [ ] BibTeX format correct
- [ ] CSV format correct
- [ ] JSON format correct
- [ ] Plain text readable

**UI/UX:**
- [ ] Works on desktop (Chrome, Firefox, Safari)
- [ ] Works on mobile (iOS Safari, Android Chrome)
- [ ] Loading indicators show
- [ ] Error messages clear and helpful
- [ ] No console errors

### Adding Automated Tests (Future)

We'd love help adding:
```python
# Example test structure
def test_search_functionality():
    """Test that search returns expected results"""
    result = search_books("Plato")
    assert len(result) > 0
    assert "Republic" in str(result)
```

---

## 📜 Code Review Process

### What to Expect

1. **Initial Review** (1-3 days)
   - Maintainer reviews your PR
   - May ask questions or request changes

2. **Discussion** (ongoing)
   - Collaborate on improvements
   - Answer questions
   - Make requested changes

3. **Approval & Merge** (1-7 days)
   - Once approved, maintainer merges
   - Your contribution is live! 🎉

### Review Criteria

We check for:
- ✅ Code quality and style
- ✅ Functionality works as described
- ✅ No breaking changes
- ✅ Documentation updated
- ✅ Follows project structure
- ✅ Doesn't introduce security issues

---

## 🏆 Recognition

### Contributors

All contributors are recognized in:
- README.md contributors section
- GitHub contributors page
- Release notes (for significant contributions)

### Types of Recognition

- **Code Contributors** - Added to Contributors list
- **Bug Reporters** - Credited in fix commits
- **Feature Suggesters** - Credited in implementation
- **Documentation Helpers** - Credited in docs

---

## 📞 Getting Help

### Before Asking

1. Check existing documentation
2. Search closed issues
3. Read this guide thoroughly

### How to Ask

**Good Questions:**
```
Title: How do I add a new export format?

I want to add RIS export format. I've read the export code 
in streamlit_app.py (lines 450-500) but I'm not sure how to:

1. Format RIS correctly
2. Add the button to the UI
3. Test it properly

Any guidance would be appreciated!
```

**Questions to Avoid:**
```
Title: Help
How do I contribute?
```

### Where to Ask

- **GitHub Discussions** - General questions
- **GitHub Issues** - Bug reports, feature requests
- **Pull Request Comments** - Specific code questions

---

## 🌍 Community Guidelines

### Be Respectful
- Treat everyone with kindness
- Welcome newcomers
- Assume good intent
- Give constructive feedback

### Be Collaborative
- Help others learn
- Share knowledge
- Ask questions
- Celebrate successes

### Be Professional
- No harassment or discrimination
- Keep discussions on-topic
- Respect different viewpoints
- Follow code of conduct

---

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

## ❓ Questions?

- **General:** Open a GitHub Discussion
- **Bugs:** Open an Issue
- **Security:** Email (add email address)
- **Other:** Contact maintainer

---

## 🎉 Thank You!

Every contribution, no matter how small, makes LIBRIS better for everyone.

**Together, we're making knowledge more accessible worldwide!** 🌍

---

## 📚 Additional Resources

- [GitHub Flow Guide](https://guides.github.com/introduction/flow/)
- [How to Write Good Commit Messages](https://chris.beams.io/posts/git-commit/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Python Style Guide (PEP 8)](https://pep8.org/)

---

**Ready to contribute?** Pick an issue labeled `good first issue` and get started! 🚀
