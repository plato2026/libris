"""
LIBRIS - Advanced Librarian AI Agent
Streamlit Web Application for Public Deployment

FREE for the world to use!
Powered by Anthropic's Claude AI

VERSION 2.0 - Professional CSV/Excel Export with Template Formatting
"""

import streamlit as st
import anthropic
import os
from datetime import datetime
import csv
import io
import re

# ============================================================================
# Import libraries for document processing
# ============================================================================
from pypdf import PdfReader
from docx import Document
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment

# ============================================================================
# PAGE CONFIGURATION
# ============================================================================

st.set_page_config(
    page_title="LIBRIS - Advanced Librarian AI",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================================
# LIBRIS SYSTEM PROMPT - UPDATED FOR STRUCTURED OUTPUT
# ============================================================================

LIBRIS_SYSTEM_PROMPT = """You are LIBRIS, an expert librarian and document analysis system specializing in historical and philosophical collections.

CORE CAPABILITIES:
1. Document Processing: Extract bibliographic data from uploaded documents
2. Intelligent Search: Search across ~1,100 historical/philosophical works
3. Thematic Analysis: Identify patterns and connections across texts
4. Export Formats: Provide results in structured CSV/Excel format

CRITICAL OUTPUT FORMAT:
When providing search results, you MUST format each result as a structured data block using this EXACT format:

---ENTRY---
Publication Date: [date]
Author: [author name]
Book Title: [title]
Key Themes: [comma-separated themes]
Source Type: [Base Knowledge OR User Document]
---END ENTRY---

Example:
---ENTRY---
Publication Date: 380 BCE
Author: Plato
Book Title: The Republic
Key Themes: Justice, ideal state, philosopher-kings, forms and reality, education, soul and virtue
Source Type: Base Knowledge
---END ENTRY---

DOCUMENT PROCESSING PROTOCOL:
When a user uploads a document:
1. Extract bibliographic data (author, title, date, themes)
2. Structure into standardized entries using the format above
3. Integrate with existing knowledge
4. Provide processing statistics

SEARCH PROTOCOL:
1. Provide results using the structured format above (one ---ENTRY--- block per result)
2. After all entries, provide a markdown table summary for visual display
3. Include analysis of patterns and connections

Source Type Rules:
- Use "Base Knowledge" for works from your training data
- Use "User Document" for works from uploaded documents

ANALYSIS:
After providing structured entries, add:
- Patterns observed (chronological, thematic)
- Insights from uploaded documents
- Suggested next steps

TONE:
Professional but approachable, like a knowledgeable university librarian. Be precise, transparent about limitations, and enthusiastic about intellectual connections.

SPECIAL FEATURES:
- Transliteration-aware (match "Confucius" with "Kong Fuzi")
- Conceptual search (match "justice" with "dharma", "dikaiosyne")
- Multi-lingual titles (show original and translation)
- Cross-cultural perspectives

REMEMBER: Always use the ---ENTRY--- format for search results so they can be exported to CSV/Excel properly!
"""

# ============================================================================
# Document Processing Functions
# ============================================================================

def extract_text_from_pdf(uploaded_file):
    """Extract text from a PDF file."""
    try:
        pdf_reader = PdfReader(uploaded_file)
        text = ""
        for page_num, page in enumerate(pdf_reader.pages, 1):
            page_text = page.extract_text()
            if page_text:
                text += f"\n--- Page {page_num} ---\n"
                text += page_text
        
        if not text.strip():
            return "⚠️ Could not extract text from PDF. The PDF might be image-based or encrypted."
        
        return text
    
    except Exception as e:
        return f"⚠️ Error reading PDF: {str(e)}"


def extract_text_from_docx(uploaded_file):
    """Extract text from a Word document (.docx)."""
    try:
        doc = Document(uploaded_file)
        text = ""
        for para in doc.paragraphs:
            if para.text.strip():
                text += para.text + "\n"
        
        for table in doc.tables:
            for row in table.rows:
                for cell in row.cells:
                    if cell.text.strip():
                        text += cell.text + "\n"
        
        if not text.strip():
            return "⚠️ Could not extract text from Word document. The document might be empty."
        
        return text
    
    except Exception as e:
        return f"⚠️ Error reading Word document: {str(e)}"


def process_uploaded_file(uploaded_file):
    """Process an uploaded file based on its type."""
    filename = uploaded_file.name.lower()
    
    if filename.endswith('.pdf'):
        return extract_text_from_pdf(uploaded_file)
    elif filename.endswith('.docx'):
        return extract_text_from_docx(uploaded_file)
    elif filename.endswith(('.txt', '.md', '.csv')):
        try:
            content = uploaded_file.read().decode('utf-8')
            return content
        except UnicodeDecodeError:
            uploaded_file.seek(0)
            content = uploaded_file.read().decode('latin-1')
            return content
    else:
        return f"⚠️ Unsupported file type: {filename}"

# ============================================================================
# NEW: Data Extraction and Export Functions
# ============================================================================

def parse_entries_from_response(response_text):
    """
    Extract structured entries from LIBRIS response.
    
    Returns:
        list of dict: Each dict has keys matching template columns
    """
    entries = []
    
    # Find all entries between ---ENTRY--- and ---END ENTRY--- markers
    entry_pattern = r'---ENTRY---(.*?)---END ENTRY---'
    matches = re.findall(entry_pattern, response_text, re.DOTALL)
    
    for match in matches:
        entry = {}
        
        # Extract each field
        pub_date_match = re.search(r'Publication Date:\s*(.+?)(?:\n|$)', match)
        author_match = re.search(r'Author:\s*(.+?)(?:\n|$)', match)
        title_match = re.search(r'Book Title:\s*(.+?)(?:\n|$)', match)
        themes_match = re.search(r'Key Themes:\s*(.+?)(?:\n|$)', match)
        source_match = re.search(r'Source Type:\s*(.+?)(?:\n|$)', match)
        
        if pub_date_match and author_match and title_match:
            entry['Publication Date'] = pub_date_match.group(1).strip()
            entry['Author'] = author_match.group(1).strip()
            entry['Book Title'] = title_match.group(1).strip()
            entry['Key Themes'] = themes_match.group(1).strip() if themes_match else ""
            entry['Source Type'] = source_match.group(1).strip() if source_match else "Base Knowledge"
            
            entries.append(entry)
    
    return entries


def create_csv_download(entries):
    """
    Create CSV file matching the template format.
    
    Args:
        entries: list of dict with keys: Publication Date, Author, Book Title, Key Themes, Source Type
        
    Returns:
        bytes: CSV file content
    """
    output = io.StringIO()
    
    # Column headers matching template
    fieldnames = ['Publication Date', 'Author', 'Book Title', 'Key Themes', 'Source Type']
    
    writer = csv.DictWriter(output, fieldnames=fieldnames)
    writer.writeheader()
    
    for entry in entries:
        writer.writerow(entry)
    
    return output.getvalue().encode('utf-8')


def create_excel_download(entries):
    """
    Create Excel file matching the template format.
    
    Args:
        entries: list of dict with keys: Publication Date, Author, Book Title, Key Themes, Source Type
        
    Returns:
        bytes: Excel file content
    """
    wb = Workbook()
    ws = wb.active
    ws.title = "LIBRIS Results"
    
    # Column headers
    headers = ['Publication Date', 'Author', 'Book Title', 'Key Themes', 'Source Type']
    
    # Style for headers
    header_font = Font(bold=True, color="FFFFFF")
    header_fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
    header_alignment = Alignment(horizontal="center", vertical="center")
    
    # Write headers
    for col_num, header in enumerate(headers, 1):
        cell = ws.cell(row=1, column=col_num, value=header)
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = header_alignment
    
    # Write data
    for row_num, entry in enumerate(entries, 2):
        ws.cell(row=row_num, column=1, value=entry.get('Publication Date', ''))
        ws.cell(row=row_num, column=2, value=entry.get('Author', ''))
        ws.cell(row=row_num, column=3, value=entry.get('Book Title', ''))
        ws.cell(row=row_num, column=4, value=entry.get('Key Themes', ''))
        ws.cell(row=row_num, column=5, value=entry.get('Source Type', ''))
    
    # Adjust column widths
    ws.column_dimensions['A'].width = 18  # Publication Date
    ws.column_dimensions['B'].width = 35  # Author
    ws.column_dimensions['C'].width = 50  # Book Title
    ws.column_dimensions['D'].width = 60  # Key Themes
    ws.column_dimensions['E'].width = 18  # Source Type
    
    # Save to bytes
    output = io.BytesIO()
    wb.save(output)
    output.seek(0)
    
    return output.getvalue()

# ============================================================================
# SESSION STATE INITIALIZATION
# ============================================================================

def init_session_state():
    """Initialize session state variables"""
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    if 'documents' not in st.session_state:
        st.session_state.documents = []
    if 'api_key' not in st.session_state:
        st.session_state.api_key = os.environ.get("ANTHROPIC_API_KEY", "")
    if 'conversation_count' not in st.session_state:
        st.session_state.conversation_count = 0
    if 'current_results' not in st.session_state:
        st.session_state.current_results = []
    if 'last_search_query' not in st.session_state:
        st.session_state.last_search_query = ""

# ============================================================================
# ANTHROPIC API FUNCTIONS
# ============================================================================

def chat_with_libris(user_message, api_key):
    """Send message to LIBRIS and get response"""
    try:
        client = anthropic.Anthropic(api_key=api_key)
        
        # Build message history
        messages = st.session_state.messages + [
            {"role": "user", "content": user_message}
        ]
        
        # Call Claude API
        response = client.messages.create(
            model="claude-sonnet-4-5-20250929",
            max_tokens=4000,
            system=LIBRIS_SYSTEM_PROMPT,
            messages=messages
        )
        
        assistant_message = response.content[0].text
        
        # Update conversation history
        st.session_state.messages.append({"role": "user", "content": user_message})
        st.session_state.messages.append({"role": "assistant", "content": assistant_message})
        st.session_state.conversation_count += 1
        
        # Extract and store structured entries
        entries = parse_entries_from_response(assistant_message)
        if entries:
            st.session_state.current_results = entries
            st.session_state.last_search_query = user_message
        
        return assistant_message
        
    except anthropic.AuthenticationError:
        return "❌ **Authentication Error**: Invalid API key. Please check your API key in the sidebar."
    except anthropic.RateLimitError:
        return "⚠️ **Rate Limit**: Too many requests. Please wait a moment and try again."
    except Exception as e:
        return f"❌ **Error**: {str(e)}"

# ============================================================================
# UI COMPONENTS
# ============================================================================

def render_header():
    """Render the app header"""
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("""
        <h1 style='text-align: center; color: #6366f1;'>
            📚 LIBRIS
        </h1>
        <p style='text-align: center; font-size: 1.2em; color: #94a3b8;'>
            Advanced Librarian AI Agent
        </p>
        <p style='text-align: center; color: #64748b;'>
            Free for the world to use • Powered by Claude AI
        </p>
        """, unsafe_allow_html=True)

def render_sidebar():
    """Render the sidebar with info and stats"""
    with st.sidebar:
        st.markdown("### 🎯 About LIBRIS")
        st.markdown("""
        LIBRIS specializes in:
        - 📄 Document processing
        - 🔍 Intelligent search
        - 📊 Professional CSV/Excel export
        - 🌍 Cross-cultural perspectives
        - 📚 ~1,100 historical & philosophical works
        """)
        
        st.markdown("---")
        
        st.markdown("### 📊 Your Session")
        st.metric("Documents Processed", len(st.session_state.documents))
        st.metric("Queries Made", st.session_state.conversation_count)
        st.metric("Results Ready to Export", len(st.session_state.current_results))
        
        st.markdown("---")
        
        st.markdown("### 🔑 API Configuration")
        
        if st.session_state.api_key:
            st.success("✅ API key configured")
            if st.button("🔄 Reset Session"):
                st.session_state.messages = []
                st.session_state.documents = []
                st.session_state.conversation_count = 0
                st.session_state.current_results = []
                st.session_state.last_search_query = ""
                st.rerun()
        else:
            st.warning("⚠️ No API key configured")
            st.markdown("""
            **For Administrators:**
            Set `ANTHROPIC_API_KEY` in Streamlit secrets.
            
            **For Local Testing:**
            Set environment variable or enter key below.
            """)
            
            temp_key = st.text_input("Temporary API Key (testing only)", type="password")
            if temp_key:
                st.session_state.api_key = temp_key
                st.rerun()
        
        st.markdown("---")
        
        st.markdown("### 💡 Example Queries")
        examples = [
            "Ancient Greek philosophy",
            "Social contract theory",
            "Buddhist ethics",
            "Medieval Islamic philosophy",
            "Confucian virtue ethics",
            "Natural law tradition"
        ]
        
        for example in examples:
            st.markdown(f"- {example}")
        
        st.markdown("---")
        
        st.markdown("### ℹ️ How to Use")
        st.markdown("""
        1. **Search**: Enter queries to find books
        2. **Upload**: Process documents
        3. **Chat**: Ask questions about texts
        4. **Export**: Download CSV or Excel files
        """)
        
        st.markdown("---")
        
        st.markdown("""
        <div style='text-align: center; font-size: 0.8em; color: #64748b;'>
        Made with ❤️ for the world<br>
        Open source • Free forever<br>
        v2.0 - Professional Export
        </div>
        """, unsafe_allow_html=True)

def render_welcome():
    """Render welcome message"""
    st.markdown("""
    <div style='padding: 2rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                border-radius: 10px; color: white; text-align: center; margin: 2rem 0;'>
        <h2>👋 Welcome to LIBRIS v2.0!</h2>
        <p style='font-size: 1.1em;'>Now with professional CSV/Excel export matching your template format!</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        ### 🔍 **Search**
        Find books and texts across thousands of years of human thought.
        """)
    
    with col2:
        st.markdown("""
        ### 📄 **Process Documents**
        Upload reading lists, syllabi, or bibliographies in PDF, Word, or text format.
        """)
    
    with col3:
        st.markdown("""
        ### 📊 **Export**
        Download results as CSV or Excel files with proper column formatting!
        """)

# ============================================================================
# MAIN APP
# ============================================================================

def main():
    """Main application logic"""
    
    init_session_state()
    render_header()
    render_sidebar()
    
    if not st.session_state.api_key:
        st.error("⚠️ **API Key Required**: LIBRIS requires an Anthropic API key to function. Please configure it in the sidebar.")
        st.info("💡 **Note for Users**: If you're seeing this on a public deployment, the administrator needs to configure the API key in Streamlit Cloud secrets.")
        return
    
    # Create tabs
    tab1, tab2, tab3, tab4 = st.tabs(["🔍 Search", "📄 Upload Document", "💬 Chat", "📊 Export"])
    
    # TAB 1: SEARCH
    with tab1:
        st.markdown("### 🔍 Search LIBRIS Knowledge Base")
        
        col1, col2 = st.columns([4, 1])
        with col1:
            search_query = st.text_input(
                "Search Query",
                placeholder="e.g., 'ancient Greek ethics', 'works by Plato', '18th century social contract'",
                label_visibility="collapsed"
            )
        with col2:
            search_button = st.button("🔍 Search", use_container_width=True)
        
        if search_button and search_query:
            with st.spinner("🔍 Searching LIBRIS knowledge base..."):
                response = chat_with_libris(f"Search for: {search_query}", st.session_state.api_key)
                st.markdown(response)
                
                # Show export notification if results were found
                if st.session_state.current_results:
                    st.success(f"✅ Found {len(st.session_state.current_results)} results! Go to the **Export** tab to download as CSV or Excel.")
        
        # Quick search buttons
        st.markdown("**Quick searches:**")
        quick_cols = st.columns(3)
        quick_searches = [
            "Ancient Greek philosophy",
            "Social contract theory", 
            "Buddhist ethics",
            "Medieval Islamic philosophy",
            "Confucian virtue",
            "Natural law"
        ]
        
        for idx, qs in enumerate(quick_searches):
            with quick_cols[idx % 3]:
                if st.button(qs, key=f"quick_{idx}"):
                    with st.spinner(f"Searching for {qs}..."):
                        response = chat_with_libris(f"Search for: {qs}", st.session_state.api_key)
                        st.markdown(response)
                        
                        if st.session_state.current_results:
                            st.success(f"✅ Found {len(st.session_state.current_results)} results! Go to the **Export** tab to download.")
    
    # TAB 2: UPLOAD DOCUMENT
    with tab2:
        st.markdown("### 📄 Upload Document for Processing")
        
        uploaded_file = st.file_uploader(
            "Choose a file",
            type=['txt', 'md', 'csv', 'pdf', 'docx'],
            help="Upload reading lists, syllabi, bibliographies, PDFs, or Word documents"
        )
        
        if uploaded_file is not None:
            with st.spinner(f"Reading {uploaded_file.name}..."):
                content = process_uploaded_file(uploaded_file)
            
            if content.startswith("⚠️"):
                st.warning(content)
                st.info("💡 **Tip**: For image-based PDFs, try converting to text first using an OCR tool.")
            else:
                st.success(f"✅ File loaded: {uploaded_file.name}")
                
                if uploaded_file.name.lower().endswith('.pdf'):
                    st.info("📄 **PDF Document** - Text extracted from all pages")
                elif uploaded_file.name.lower().endswith('.docx'):
                    st.info("📝 **Word Document** - Text extracted from paragraphs and tables")
                
                with st.expander("Preview file content"):
                    preview_length = 2000
                    if len(content) > preview_length:
                        st.text(content[:preview_length] + f"\n\n... ({len(content) - preview_length} more characters)")
                    else:
                        st.text(content)
                
                if st.button("📚 Process Document", type="primary"):
                    with st.spinner(f"Processing {uploaded_file.name}..."):
                        message = f"I'm uploading a document called '{uploaded_file.name}'. Please process it and extract bibliographic information in the structured format.\n\nDocument content:\n{content}"
                        response = chat_with_libris(message, st.session_state.api_key)
                        
                        st.session_state.documents.append({
                            'filename': uploaded_file.name,
                            'processed_at': datetime.now().isoformat(),
                            'file_type': uploaded_file.type
                        })
                        
                        st.markdown(response)
                        
                        if st.session_state.current_results:
                            st.success(f"✅ Extracted {len(st.session_state.current_results)} entries! Go to the **Export** tab to download.")
        
        st.markdown("---")
        st.markdown("""
        **Supported formats:**
        - 📄 `.pdf` - PDF documents (text-based)
        - 📝 `.docx` - Word documents
        - 📝 `.txt` - Plain text files
        - 📝 `.md` - Markdown files
        - 📊 `.csv` - CSV files
        """)
    
    # TAB 3: CHAT
    with tab3:
        st.markdown("### 💬 Chat with LIBRIS")
        
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
        
        if prompt := st.chat_input("Ask LIBRIS anything about historical or philosophical texts..."):
            with st.chat_message("user"):
                st.markdown(prompt)
            
            with st.chat_message("assistant"):
                with st.spinner("LIBRIS is thinking..."):
                    response = chat_with_libris(prompt, st.session_state.api_key)
                    st.markdown(response)
    
    # TAB 4: EXPORT - COMPLETELY REDESIGNED!
    with tab4:
        st.markdown("### 📊 Export Search Results")
        
        if not st.session_state.current_results:
            st.info("""
            **No results to export yet!**
            
            First, perform a search in the **Search** tab or upload a document in the **Upload** tab.
            Then come back here to download your results as CSV or Excel files.
            """)
        else:
            st.success(f"✅ **{len(st.session_state.current_results)} results ready to export!**")
            
            if st.session_state.last_search_query:
                st.markdown(f"**Last search:** {st.session_state.last_search_query}")
            
            st.markdown("---")
            
            # Preview results
            with st.expander("📋 Preview Results", expanded=True):
                st.markdown("**Results that will be exported:**")
                
                for idx, entry in enumerate(st.session_state.current_results, 1):
                    st.markdown(f"""
                    **{idx}. {entry.get('Book Title', 'Unknown')}**
                    - **Author:** {entry.get('Author', 'Unknown')}
                    - **Date:** {entry.get('Publication Date', 'Unknown')}
                    - **Themes:** {entry.get('Key Themes', 'None listed')}
                    - **Source:** {entry.get('Source Type', 'Unknown')}
                    """)
            
            st.markdown("---")
            
            # Download buttons
            st.markdown("### 💾 Download Options")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("#### 📄 CSV Format")
                st.markdown("Compatible with Excel, Google Sheets, and any spreadsheet software")
                
                csv_data = create_csv_download(st.session_state.current_results)
                
                st.download_button(
                    label="📥 Download CSV",
                    data=csv_data,
                    file_name=f"LIBRIS_Results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                    mime="text/csv",
                    use_container_width=True
                )
            
            with col2:
                st.markdown("#### 📊 Excel Format")
                st.markdown("Professional formatting with headers and adjusted columns")
                
                excel_data = create_excel_download(st.session_state.current_results)
                
                st.download_button(
                    label="📥 Download Excel",
                    data=excel_data,
                    file_name=f"LIBRIS_Results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                    use_container_width=True
                )
            
            st.markdown("---")
            
            st.markdown("""
            **Column Structure (matches your template):**
            1. Publication Date
            2. Author
            3. Book Title
            4. Key Themes
            5. Source Type
            
            Both formats use the exact same column structure as your template!
            """)
    
    # Show welcome message if no conversation
    if len(st.session_state.messages) == 0:
        st.markdown("---")
        render_welcome()

# ============================================================================
# RUN APP
# ============================================================================

if __name__ == "__main__":
    main()
