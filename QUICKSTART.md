# ⚡ LIBRIS Quick Start Guide
## Deploy to the World in 15 Minutes!

The fastest path from zero to deployed LIBRIS.

---

## ✅ What You Need (5 minutes to gather)

1. **GitHub Account** → https://github.com/signup
2. **Streamlit Cloud Account** → https://share.streamlit.io (sign up with GitHub)
3. **Anthropic API Key** → https://console.anthropic.com/settings/keys

**Have these ready?** Let's go! ⚡

---

## 🚀 Step 1: Create GitHub Repository (5 minutes)

1. Go to https://github.com
2. Click `+` → "New repository"
3. Name it: `libris`
4. Make it **Public**
5. Click "Create repository"
6. Click "uploading an existing file"
7. **Drag and drop ALL files from your `libris_streamlit` folder**
8. Commit with message: "Initial LIBRIS deployment"

**Done!** ✅

---

## ☁️ Step 2: Deploy to Streamlit (5 minutes)

1. Go to https://share.streamlit.io
2. Click "New app"
3. Fill in:
   - **Repository:** `yourusername/libris`
   - **Branch:** `main`
   - **File:** `streamlit_app.py`
   - **URL:** Choose a name like `my-libris`
4. Click "Deploy!"
5. Wait 2-3 minutes... ☕

**Deployed!** (But needs API key) ✅

---

## 🔑 Step 3: Add API Key (2 minutes)

1. On your app page, click "⚙️ Settings"
2. Scroll to "Secrets"
3. Click "Edit"
4. Add this (with YOUR actual key):
   ```toml
   ANTHROPIC_API_KEY = "sk-ant-your-key-here"
   ```
5. Click "Save"
6. Click "Reboot app"
7. Wait 30 seconds...

**Working!** ✅

---

## 🎉 Step 4: Test & Share (3 minutes)

1. **Test Search:**
   - Try: "ancient Greek philosophy"
   - Should return Plato, Aristotle, etc.

2. **Get Your URL:**
   - It's: `https://your-chosen-name.streamlit.app`

3. **Share it!**
   - Email colleagues
   - Post on social media
   - Add to your bio
   - Tell the world! 🌍

**DONE!** Your LIBRIS is LIVE! 🎊

---

## 🆘 Something Wrong?

### App shows "API Key Required"
→ Go back to Step 3, recheck your secret format

### Search returns error
→ Verify your API key at console.anthropic.com

### App won't deploy
→ Check all files uploaded to GitHub (especially `requirements.txt`)

### Still stuck?
→ See [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) for detailed troubleshooting

---

## 💰 Costs

- **GitHub:** FREE ✅
- **Streamlit Hosting:** FREE ✅
- **API Usage:** ~$5-15/month (you can set limits)

**Total: < $20/month to serve the world** 🌍

---

## 📈 Next Steps

After it's working:

1. **Update README** with your actual URL
2. **Set API spending limits** (console.anthropic.com)
3. **Share widely** on social media
4. **Monitor usage** on Streamlit dashboard
5. **Gather feedback** from users

---

## 🎯 Quick Links

- **Your GitHub:** `https://github.com/yourusername/libris`
- **Your App:** `https://your-name.streamlit.app`
- **Streamlit Dashboard:** https://share.streamlit.io
- **API Console:** https://console.anthropic.com

---

## ⏱️ Timeline Recap

- ✅ **5 min** - Create GitHub repo + upload files
- ✅ **5 min** - Deploy to Streamlit (mostly waiting)
- ✅ **2 min** - Add API key
- ✅ **3 min** - Test and share

**Total: 15 minutes** ⚡

**You just deployed an AI application to the world!** 🚀

---

**Want more details?** Read [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)

**Have issues?** Open an issue on your GitHub repo

**Made it work?** Share your URL! 🎉
