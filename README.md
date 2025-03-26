![Braille fonts](https://see.fontimg.com/api/rf5/DOeDd/MGE4NTM1Njg3NjZhNDZhZTgwNTE0MjE5YzUxMzA0OTgudHRm/VEVYVCBBTkFMWVNJUw/braille-cc0.png?r=dw&h=81&w=1250&fg=00B17E&bg=000000&s=65)

<div align="center">
  <h1>1CijferHO Tool</h1>

  <p>🔍 An advanced data transformation tool that makes understanding your 1 Cijfer HO data simple and intuitive.</p>

  <p>
    <a href="#"><img src="https://custom-icon-badges.demolab.com/badge/Windows-0078D6?logo=windows11&logoColor=white" alt="Windows"></a>
    <a href="#"><img src="https://img.shields.io/badge/macOS-000000?logo=apple&logoColor=F0F0F0" alt="macOS"></a>
    <a href="#"><img src="https://img.shields.io/badge/Linux-FCC624?logo=linux&logoColor=black" alt="Linux"></a>
    <img src="https://badgen.net/github/last-commit/cedanl/1cijferho" alt="GitHub Last Commit">
    <img src="https://badgen.net/github/contributors/cedanl/1cijferho" alt="Contributors">
    <img src="https://img.shields.io/github/license/cedanl/1cijferho" alt="GitHub License">
  </p>

  <p>🎬 Demo Video (Coming Soon!)</p>
</div>

## 📋 Overview
> [!NOTE]
> No Python or technical knowledge required! This tool is designed for everyone, regardless of programming experience.


1CijferHO Tool provides researchers and analysts with powerful data transformation capabilities, helping you uncover patterns and insights in your 1 Cijfer HO data. Particularly effective for analyzing:

- 1 Cijfer HO ASCII files
- Decode files
- Educational Data Sets

## ✨ Features
- [x] **Data Transformation**: Process and transform your 1 Cijfer HO data using advanced algorithms
- [x] **Visual Data Representations**: Generate interactive visualizations of your educational data
- [x] **Data Validation**: Comprehensive error checking and validation reporting
- [x] **User-friendly Interface**: Streamlit-based UI requiring no coding knowledge
- [x] **`uv` Powered Setup**: One-click installation that installs Python and all dependencies in seconds - no technical knowledge needed!

<br>

## 🔧 First Time Setup
> [!WARNING]
> Do not skip these steps if this is your first time using this application. It will not work without them.

> [!TIP]
> Save the repository in a Projects/CEDA folder on your main drive for quick access.


### 1. Get the Repository

#### Option A: Clone with Git (or [Github Desktop](https://github.com/apps/desktop))
```bash
git clone https://github.com/cedanl/1cijferho.git
cd 1cijferho
```

#### Option B: Download ZIP
[![Download Repository](https://img.shields.io/badge/Download-Repository-green)](https://github.com/cedanl/1cijferho/archive/refs/heads/main.zip)

After downloading extract the ZIP file and navigate into the folder.

### 2. Install [![uv Badge](https://img.shields.io/badge/uv-DE5FE9?logo=uv&logoColor=fff&style=flat)](https://docs.astral.sh/uv/)

#### MacOS & Linux (Terminal)
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

#### Windows (Powershell or [Windows Terminal](https://apps.microsoft.com/detail/9n0dx20hk701?hl=nl-NL&gl=NL))
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
Close and reopen your terminal after installation.

#### Verify installation

```bash
uv self update
```

See the [installation documentation](https://docs.astral.sh/uv/getting-started/installation/) for
details and alternative installation methods.

<br>

## 🚀 Running the Application

Ready to see the magic happen? Your 1CijferHO Tool is just one command away! ✨

### First, get to the right spot:

Open a terminal in your `1cijferho` folder - it's super easy!
- **Windows**: `Shift + Right-click` in folder → `Open in Windows Terminal` 
- **Mac**: `Right-click` folder → `New Terminal at Folder`
- **VS Code**: Just click `Terminal` → `New Terminal`

Or simply navigate there:
```bash
cd path/to/1cijferho
```

### Then, launch with a single command:

```bash
uv run streamlit run src/main.py
```

That's it! The app will automatically spring to life in your browser. If you've completed all the steps in the First Time Setup correctly, this is the **only command** you'll need going forward. 🎉

> **Pro Tip**: Create a shortcut: `.bat` file (Windows) or `.sh` script (macOS/Linux)
> **Pro Tip**: Check out our [architecture.md](architecture.md) for technical details!

Happy analyzing! ✨📊📝


<br>

## 🛠️ Built With
[![uv Badge](https://img.shields.io/badge/uv-DE5FE9?logo=uv&logoColor=fff&style=flat)](https://docs.astral.sh/uv/)
[![Streamlit Badge](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=fff&style=flat)](https://streamlit.io/)
[![Python Badge](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff&style=flat)](https://www.python.org/)

## 🤲 Support
If you find this project helpful, please consider:
- ⭐ Starring the repo
- 🐛 Reporting bugs
- 💡 Suggesting features
- 💻 Contributing code

If you encounter any issues or need further assistance, please feel free to [open an issue](https://github.com/cedanl/1cijferho/issues) or contact a.sewnandan@hhs.nl | t.iwan@vu.nl

## 🙏 Acknowledgements
<strong>Special thanks to:</strong>
- [Ash Sewnandan](https://github.com/asewnandan) & [Tomer Iwan](https://github.com/Tomeriko96) for setting the foundation with a clean, user-friendly interface and robust architecture.
- [CEDA & Npuls](https://community-data-ai.npuls.nl/groups/view/44d20066-53a8-48c2-b4e9-be348e05d273/project-center-for-educational-data-analytics-ceda) for making this project possible by providing valuable resources and support.


## 🫂 Contributors
Thank you to all the [people](https://github.com/cedanl/1cijferho/graphs/contributors) who have already contributed to 1cijferho.


[![](https://github.com/asewnandan.png?size=50)](https://github.com/asewnandan)
[![](https://github.com/tin900.png?size=50)](https://github.com/tin900)
[![](https://github.com/Tomeriko96.png?size=50)](https://github.com/Tomeriko96)

## 🚦 License
![GitHub License](https://img.shields.io/github/license/cedanl/1cijferho)
