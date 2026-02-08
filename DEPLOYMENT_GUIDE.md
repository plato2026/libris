# 🚀 LIBRIS Deployment Guide
## Complete Step-by-Step Instructions for GitHub + Streamlit Cloud

This guide will help you deploy LIBRIS to the world **completely FREE** using GitHub and Streamlit Cloud.

**Estimated Time:** 30-45 minutes (mostly waiting for deployments)

---

## 📋 Table of Contents

1. [Prerequisites](#prerequisites)
2. [Part 1: Get Your Files Ready](#part-1-get-your-files-ready)
3. [Part 2: Set Up GitHub Repository](#part-2-set-up-github-repository)
4. [Part 3: Deploy to Streamlit Cloud](#part-3-deploy-to-streamlit-cloud)
5. [Part 4: Configure API Key](#part-4-configure-api-key)
6. [Part 5: Test & Share](#part-5-test--share)
7. [Troubleshooting](#troubleshooting)
8. [Maintenance & Updates](#maintenance--updates)

---

## ✅ Prerequisites

### What You'll Need:

1. **GitHub Account** (Free)
   - Go to: https://github.com/signup
   - Create an account if you don't have one

2. **Streamlit Cloud Account** (Free)
   - Go to: https://share.streamlit.io
   - Sign up with your GitHub account (easiest method)

3. **Anthropic API Key**
   - Go to: https://console.anthropic.com/settings/keys
   - Create an API key
   - Save it somewhere safe (you'll need it later)

4. **Your LIBRIS Files**
   - You should have the `libris_streamlit` folder with all files

### ⏱️ Time Commitment:
- Setup: 15-20 minutes
- First deployment: 5-10 minutes
- Testing: 5-10 minutes
- **Total: 30-45 minutes**

---

## 🗂️ Part 1: Get Your Files Ready

### Step 1.1: Verify Your Files

Make sure you have these files in your `libris_streamlit` folder:

```
libris_streamlit/
├── streamlit_app.py          ✅ Main application
├── requirements.txt           ✅ Python dependencies
├── README.md                  ✅ Project documentation
├── .gitignore                 ✅ Git ignore file
└── .streamlit/
    └── config.toml            ✅ Streamlit configuration
```

### Step 1.2: Quick Local Test (Optional but Recommended)

Before deploying, test locally:

```bash
cd libris_streamlit
pip install -r requirements.txt
export ANTHROPIC_API_KEY="your-key-here"
streamlit run streamlit_app.py
```

If it works locally (opens at http://localhost:8501), you're ready to deploy!

---

## 🐙 Part 2: Set Up GitHub Repository

### Step 2.1: Create New Repository on GitHub

1. **Go to GitHub:** https://github.com
2. **Click** the `+` icon (top right) → "New repository"
3. **Fill in details:**
   - **Repository name:** `libris` (or any name you like)
   - **Description:** `LIBRIS - Advanced Librarian AI Agent - Free for the world`
   - **Visibility:** Choose `Public` (so anyone can use it)
   - **Initialize:** Do NOT check any boxes (we have our own files)
4. **Click** "Create repository"

### Step 2.2: Upload Your Files to GitHub

**Option A: Using GitHub Web Interface (Easiest for Beginners)**

1. **On your new repository page**, click "uploading an existing file"
2. **Drag and drop** all files from `libris_streamlit` folder:
   - `streamlit_app.py`
   - `requirements.txt`
   - `README.md`
   - `.gitignore`
3. **For the `.streamlit` folder:**
   - Click "Add file" → "Create new file"
   - Type: `.streamlit/config.toml`
   - Paste the contents of your `config.toml` file
   - Click "Commit new file"
4. **Commit changes:**
   - Scroll down
   - Add commit message: "Initial commit - LIBRIS v1.0"
   - Click "Commit changes"

**Option B: Using Git Command Line (For Developers)**

```bash
# Navigate to your libris_streamlit folder
cd libris_streamlit

# Initialize git repository
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit - LIBRIS v1.0"

# Add remote (replace USERNAME and REPO with yours)
git remote add origin https://github.com/USERNAME/REPO.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### Step 2.3: Verify Upload

1. **Refresh** your GitHub repository page
2. **You should see** all your files:
   - ✅ streamlit_app.py
   - ✅ requirements.txt
   - ✅ README.md
   - ✅ .gitignore
   - ✅ .streamlit/config.toml

**⚠️ IMPORTANT:** Make sure `.gitignore` is there! It prevents accidentally committing your API key.

---

## ☁️ Part 3: Deploy to Streamlit Cloud

### Step 3.1: Sign Up for Streamlit Cloud

1. **Go to:** https://share.streamlit.io
2. **Click** "Sign up"
3. **Choose** "Continue with GitHub" (easiest option)
4. **Authorize** Streamlit to access your GitHub account

### Step 3.2: Create New App

1. **On Streamlit Cloud dashboard**, click "New app"
2. **Fill in deployment details:**

   **Repository:**
   - Choose your GitHub repository: `yourusername/libris`
   
   **Branch:**
   - Select: `main`
   
   **Main file path:**
   - Enter: `streamlit_app.py`
   
   **App URL (optional):**
   - Choose a custom URL like: `libris-ai` or `my-libris`
   - Final URL will be: `https://libris-ai.streamlit.app`

3. **Click** "Deploy!" (Don't add secrets yet - we'll do that next)

### Step 3.3: Wait for Initial Deployment

- Streamlit will start building your app
- This takes **2-5 minutes** for first deployment
- You'll see a progress log
- **Expected behavior:** App will show "API Key Required" message (this is correct!)

**What's happening:**
```
⏳ Installing dependencies...
⏳ Running your app...
✅ App is live!
⚠️ But needs API key (we'll add it next)
```

---

## 🔑 Part 4: Configure API Key

### Step 4.1: Access App Settings

1. **On your app page**, click the menu (three dots) → "Settings"
2. **Or** click the "⚙️ Settings" button

### Step 4.2: Add Secrets

1. **In Settings**, scroll to "Secrets"
2. **Click** "Edit secrets"
3. **Add your API key** in this exact format:

   ```toml
   ANTHROPIC_API_KEY = "sk-ant-your-actual-key-here"
   ```

   **⚠️ Important formatting:**
   - Use exact spelling: `ANTHROPIC_API_KEY` (all caps)
   - Include the quotes around your key
   - Replace `sk-ant-your-actual-key-here` with your real API key

4. **Click** "Save"

### Step 4.3: Reboot App

1. **Click** the menu → "Reboot app"
2. **Or** just refresh the page
3. **Wait** 10-20 seconds for app to restart

### Step 4.4: Verify API Key Works

1. **Your app should now show** the full LIBRIS interface (not the error message)
2. **Test it:**
   - Go to "🔍 Search" tab
   - Try a quick search: "Ancient Greek philosophy"
   - You should see results!

**✅ If you see results, your API is working!**
**❌ If still getting errors, see [Troubleshooting](#troubleshooting)**

---

## 🎉 Part 5: Test & Share

### Step 5.1: Comprehensive Testing

Test all features to make sure everything works:

**1. Search Functionality:**
```
✅ Try: "Ancient Greek ethics"
✅ Try: "Social contract theory"
✅ Try: "Buddhist philosophy"
```

**2. Document Upload:**
```
✅ Create a test file with some book titles
✅ Upload it
✅ Verify it processes correctly
```

**3. Chat:**
```
✅ Ask: "What are the major works of Plato?"
✅ Ask: "Explain natural law theory"
```

**4. Export:**
```
✅ Search for something
✅ Export as BibTeX
✅ Verify formatting is correct
```

### Step 5.2: Get Your Public URL

Your app is now live at:
```
https://your-app-name.streamlit.app
```

**Find your exact URL:**
- Look at the top of your Streamlit Cloud dashboard
- It will show: `https://[your-chosen-name].streamlit.app`

### Step 5.3: Share with the World! 🌍

**Your LIBRIS is now PUBLIC and FREE for anyone to use!**

Share your URL:
- 📧 Email it to colleagues and students
- 🐦 Tweet it: "Just deployed LIBRIS, a free AI librarian! Check it out: [your-url]"
- 📱 Post on social media
- 📚 Share on academic forums
- 🎓 Add to your university's resources page

**Add the link to your GitHub README:**
1. **Edit** `README.md` on GitHub
2. **Replace** `https://your-app-name.streamlit.app` with your actual URL
3. **Commit** the change

---

## 🛠️ Troubleshooting

### Problem: "App didn't wake up" or "App crashed"

**Cause:** Streamlit Cloud puts inactive apps to sleep after 7 days

**Solution:**
1. Go to your Streamlit Cloud dashboard
2. Click "Reboot app"
3. Wait 30 seconds

**Prevention:** Visit your app at least once a week

---

### Problem: "ANTHROPIC_API_KEY not found"

**Solutions to try:**

**Check 1: Verify Secret Format**
```toml
✅ Correct: ANTHROPIC_API_KEY = "sk-ant-..."
❌ Wrong: anthropic_api_key = "sk-ant-..."
❌ Wrong: ANTHROPIC_API_KEY = sk-ant-...
```

**Check 2: Reboot App**
- Settings → Reboot app
- Secrets only load on app start

**Check 3: Verify API Key is Valid**
- Test it at: https://console.anthropic.com
- Generate a new one if needed

---

### Problem: App loads but searches fail

**Check 1: API Key Permissions**
- Make sure key hasn't been deleted
- Check it has API access (not just dashboard access)

**Check 2: Rate Limits**
- Check console.anthropic.com for rate limit errors
- Wait a few minutes and try again

**Check 3: Billing**
- Make sure you have credits in Anthropic account
- Add payment method if needed

---

### Problem: Files not showing up on GitHub

**Solution:**
1. Check `.gitignore` isn't blocking important files
2. Files starting with `.` (like `.streamlit`) need to be added explicitly:
   ```bash
   git add .streamlit/config.toml
   git commit -m "Add streamlit config"
   git push
   ```

---

### Problem: "Module not found" errors

**Solution:**
1. Check `requirements.txt` has:
   ```
   streamlit>=1.28.0
   anthropic>=0.43.0
   ```
2. No extra spaces or blank lines
3. Reboot app after fixing

---

### Problem: App works locally but not on Streamlit Cloud

**Common causes:**

**1. Environment Variables:**
- Local: Using `.env` file or `export`
- Cloud: Must use Streamlit Secrets

**2. File Paths:**
- Local: Absolute paths like `/home/user/file.txt`
- Cloud: Use relative paths like `./file.txt`

**3. Permissions:**
- Cloud apps can't write to filesystem
- Store data in session_state instead

---

### Problem: Slow performance or timeouts

**Solutions:**

**1. API Response Times:**
- Claude API can take 5-15 seconds
- This is normal for complex queries
- Streamlit shows spinner automatically

**2. Large Documents:**
- Split very large files (>100KB) into smaller chunks
- Process incrementally

**3. Memory Issues:**
- Clear session state periodically
- Use "Reset Session" button

---

## 🔄 Maintenance & Updates

### How to Update Your Deployed App

**Option 1: Edit on GitHub Directly**
1. Go to your repository on GitHub
2. Click on the file you want to edit
3. Click the pencil icon (Edit)
4. Make changes
5. Commit changes
6. Streamlit Cloud automatically redeploys (takes ~1 minute)

**Option 2: Push from Local**
```bash
# Make your changes locally
# Then:
git add .
git commit -m "Description of changes"
git push

# Streamlit Cloud redeploys automatically
```

### Monitoring Your App

**1. Check Usage:**
- Streamlit Cloud dashboard shows:
  - Number of visitors
  - Active sessions
  - Resource usage

**2. Check API Costs:**
- Go to: https://console.anthropic.com/settings/billing
- Monitor your usage
- Set up billing alerts

**3. Set Usage Limits (Recommended):**
- Console → Settings → Limits
- Set monthly spending cap (e.g., $20/month)
- Get email alerts at 50% and 90%

### Regular Maintenance Tasks

**Weekly:**
- ✅ Visit your app to keep it awake
- ✅ Check for any error reports

**Monthly:**
- ✅ Review API usage and costs
- ✅ Check for Streamlit updates
- ✅ Review GitHub Issues (if people are using your app)

**As Needed:**
- ✅ Update to newer Claude models
- ✅ Fix bugs
- ✅ Add requested features

---

## 💰 Cost Management

### Controlling Costs

**1. Set Anthropic Spending Limits:**
```
Console → Settings → Limits
- Set monthly cap: $20 (or your budget)
- Enable email alerts
```

**2. Monitor Usage Patterns:**
- Which features are used most?
- Are there any unusual spikes?
- Adjust as needed

**3. Communicate Costs to Users:**
- Add a note to your README
- "This is a free service, please use responsibly"
- Consider adding usage guidelines

### Expected Costs (Monthly)

**Light Use (< 100 searches/day):**
- API: $5-10/month
- Hosting: FREE

**Medium Use (100-500 searches/day):**
- API: $20-50/month
- Hosting: FREE

**Heavy Use (> 500 searches/day):**
- API: $50-200/month
- Hosting: FREE
- Consider adding authentication

**Optimization Tips:**
- Cache common queries
- Set reasonable token limits
- Monitor for abuse

---

## 🌟 Making Your App Popular

### 1. Improve Discoverability

**Add to GitHub:**
- Add topics/tags: `ai`, `claude`, `library-science`, `philosophy`
- Write good description
- Add screenshots to README

**Add to Streamlit Gallery:**
- Submit your app: https://streamlit.io/gallery
- Categories: Education, Research, AI

### 2. Promote Your App

**Academic Channels:**
- Post on academic Twitter/X
- Share in relevant Discord servers
- Reddit: r/AcademicPhilosophy, r/HistoryOfIdeas
- Share with your department/university

**Social Media:**
- LinkedIn post
- Facebook academic groups
- Twitter thread with examples

**Direct Outreach:**
- Email professors who might find it useful
- Contact library associations
- Share with philosophy departments

### 3. Gather Feedback

**Add to README:**
```markdown
## 💬 Feedback

I'd love to hear from you!
- Found it useful? [Leave a star](https://github.com/yourusername/libris)
- Have ideas? [Open an issue](https://github.com/yourusername/libris/issues)
- Questions? [Start a discussion](https://github.com/yourusername/libris/discussions)
```

---

## 📊 Success Metrics

You'll know your deployment is successful when:

✅ App loads without errors  
✅ Search returns relevant results  
✅ Documents process correctly  
✅ Export functions work  
✅ API key is secure  
✅ URL is shareable and public  
✅ Others can use it without issues  

---

## 🎯 Next Steps

After successful deployment:

1. **Test thoroughly** - Try all features
2. **Share widely** - Post on social media
3. **Monitor usage** - Check Streamlit analytics
4. **Gather feedback** - Listen to users
5. **Iterate** - Add requested features
6. **Document** - Keep README updated

---

## 📞 Getting Help

**Streamlit Issues:**
- Docs: https://docs.streamlit.io
- Forum: https://discuss.streamlit.io
- Discord: https://discord.gg/streamlit

**GitHub Issues:**
- General Git: https://github.com/git-guides
- GitHub Docs: https://docs.github.com

**Anthropic API:**
- Docs: https://docs.anthropic.com
- Support: https://support.anthropic.com

**LIBRIS-Specific:**
- Your GitHub Issues: `https://github.com/yourusername/libris/issues`

---

## ✅ Deployment Checklist

Before going live, verify:

- [ ] All files uploaded to GitHub
- [ ] `.gitignore` is present (no API keys committed)
- [ ] README updated with your URL
- [ ] Streamlit Cloud deployment successful
- [ ] API key added to secrets
- [ ] App loads without errors
- [ ] Search functionality tested
- [ ] Document upload tested
- [ ] Export functions tested
- [ ] Mobile responsive (test on phone)
- [ ] API usage limits set
- [ ] Billing alerts configured
- [ ] URL shared with initial users
- [ ] Feedback mechanism in place

---

## 🎉 Congratulations!

Your LIBRIS agent is now **LIVE** and **FREE** for the world to use!

**You've accomplished:**
✅ Built an advanced AI application  
✅ Deployed to the cloud for free  
✅ Made knowledge more accessible  
✅ Contributed to open source  

**Impact:**
- Students worldwide can research better
- Researchers can find sources faster
- Knowledge becomes more accessible
- You've made a difference! 🌍

---

## 📜 License Note

When deploying publicly, consider adding a LICENSE file:

**MIT License (Recommended):**
```
Copyright (c) 2025 [Your Name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

[Full MIT license text]
```

This lets others:
- Use your code
- Modify it
- Share it
- Build upon it

While requiring:
- Attribution
- License inclusion

---

**🚀 Your LIBRIS is ready to change the world!**

**Questions?** Open an issue on your GitHub repo and tag me! I'm here to help.

**Share your success:** Tweet your deployed URL with #LIBRIS #ClaudeAI #OpenSource
