import streamlit as st
import os
import glob
import backend.core.extractor as ex
import io
import contextlib

# -----------------------------------------------------------------------------
# Helper Functions
# -----------------------------------------------------------------------------
def clear_existing_files():
    """Clear existing metadata files before starting new extraction"""
    metadata_dir = "data/00-metadata"
    json_dir = os.path.join(metadata_dir, "json")
    
    files_cleared = []
    
    # Clear .xlsx files from metadata directory
    if os.path.exists(metadata_dir):
        xlsx_files = glob.glob(os.path.join(metadata_dir, "*.xlsx"))
        for file_path in xlsx_files:
            try:
                os.remove(file_path)
                files_cleared.append(os.path.basename(file_path))
            except Exception as e:
                print(f"Warning: Could not remove {file_path}: {e}")
    
    # Clear JSON files from json subfolder
    if os.path.exists(json_dir):
        json_files = glob.glob(os.path.join(json_dir, "*.json"))
        for file_path in json_files:
            try:
                os.remove(file_path)
                files_cleared.append(f"json/{os.path.basename(file_path)}")
            except Exception as e:
                print(f"Warning: Could not remove {file_path}: {e}")
    
    return files_cleared

def get_bestandsbeschrijvingen():
    """Get all bestandsbeschrijving files from the input directory"""
    input_dir = "data/01-input"
    if not os.path.exists(input_dir):
        return []
    
    txt_files = glob.glob(os.path.join(input_dir, "*.txt"))
    bestandsbeschrijvingen = []
    
    for file_path in txt_files:
        filename = os.path.basename(file_path)
        if 'bestandsbeschrijving' in filename.lower():
            bestandsbeschrijvingen.append(filename)
    
    return sorted(bestandsbeschrijvingen)

# -----------------------------------------------------------------------------
# Main Content
# -----------------------------------------------------------------------------
st.title("🔍 Extract Metadata")

# Intro text
st.write("""
**Step 1: Extracting Data Structure**

We'll now read your Bestandsbeschrijving files to find where each field is positioned in your main/dec files. This creates the "map" we need to properly split your fixed-width data.

What happens:
- Extract field positions from your .txt files
- Convert to JSON format, then Excel
- Save to `data/00-metadata/` folder
""")

# Get files and display status
bestandsbeschrijvingen = get_bestandsbeschrijvingen()

if not bestandsbeschrijvingen:
    st.error("🚨 **No Bestandsbeschrijving files found in `data/01-input`**")
else:
    st.success(f"✅ **{len(bestandsbeschrijvingen)} Bestandsbeschrijving file(s) found**")
    st.info("💡 You are able to proceed, even with errors - do this with caution!")
    
    # Side-by-side buttons with equal width
    col1, col2 = st.columns(2)
    
    with col1:
        extract_clicked = st.button("🔍 Start Extraction", type="primary", use_container_width=True)
    
    with col2:
        # Check if metadata exists to enable/disable the validate button
        logs_dir = "data/00-metadata/logs"
        extraction_complete = False
        
        if os.path.exists("data/00-metadata") and os.listdir("data/00-metadata") and os.path.exists(logs_dir):
            # Check for the required extraction log file
            xlsx_processing_log_files = glob.glob(os.path.join(logs_dir, "*xlsx_processing_log_latest.json"))
            extraction_complete = len(xlsx_processing_log_files) > 0
        
        validate_clicked = st.button("➡️ Continue to Step 2", type="secondary", disabled=not extraction_complete, use_container_width=True)
    
    # Handle validate button click
    if validate_clicked:
        st.switch_page("frontend/Modules/Validate_Metadata.py")

    # Handle extraction logic
    if extract_clicked:
        # Reset console log at the start of each extraction
        st.session_state.extract_console_log = ""
        
        with st.spinner("Extracting..."):
            try:
                st.session_state.extract_console_log += "🔄 Starting extraction process...\n"
                
                # Clear existing files first
                st.session_state.extract_console_log += "🧹 Clearing existing metadata files...\n"
                cleared_files = clear_existing_files()
                if cleared_files:
                    st.session_state.extract_console_log += f"✅ Cleared {len(cleared_files)} existing files: {', '.join(cleared_files[:3])}{'...' if len(cleared_files) > 3 else ''}\n"
                else:
                    st.session_state.extract_console_log += "✅ No existing files to clear\n"
                
                st.session_state.extract_console_log += "📁 Processing TXT files...\n"
                
                # Capture stdout from process_txt_folder
                captured_output = io.StringIO()
                with contextlib.redirect_stdout(captured_output):
                    ex.process_txt_folder("data/01-input")
                st.session_state.extract_console_log += captured_output.getvalue()
                st.session_state.extract_console_log += "✅ TXT files processed successfully\n"
                
                st.session_state.extract_console_log += "📊 Converting JSON to Excel...\n"
                # Capture stdout from process_json_folder  
                captured_output = io.StringIO()
                with contextlib.redirect_stdout(captured_output):
                    ex.process_json_folder()
                st.session_state.extract_console_log += captured_output.getvalue()
                st.session_state.extract_console_log += "✅ JSON conversion completed\n"
                st.session_state.extract_console_log += "🎉 Extraction completed successfully!\n"
                
                st.success("✅ **Extraction completed!** Files saved to `data/00-metadata/`, Logs saved to `data/00-metadata/logs/`, You can now validate the metadata.")
                
                # Rerun to update the validate button state
                st.rerun()
                
            except Exception as e:
                st.session_state.extract_console_log += f"❌ Error: {str(e)}\n"
                st.error(f"❌ **Extraction failed:** Logs saved to `data/00-metadata/logs/` {str(e)}")

    # Console Log expander
    with st.expander("📋 Console Log", expanded=True):
        if 'extract_console_log' in st.session_state and st.session_state.extract_console_log:
            st.code(st.session_state.extract_console_log, language=None)
        else:
            st.info("No extraction process started yet. Click 'Start Extraction' to begin.")
    
    # Warning about existing files
    if os.path.exists("data/00-metadata") and os.listdir("data/00-metadata"):
        st.warning("⚠️ Extraction will overwrite existing files in `data/00-metadata/`")
