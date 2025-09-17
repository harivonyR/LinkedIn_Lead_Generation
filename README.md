# LinkedInLeadGeneration
LinkedInLeadGeneration is a Python project using Piloterr API that leverages Google Dorks to scrape and extract specific LinkedIn Lead profiles (CEOs, founders, decision-makers). 
Designed for lead generation, recruiting, and market intelligence.
This tool automates Google search queries and exports results in structured formats (CSV/JSON).


## Installation & Usage

### 1. Clone the repository
```bash
git clone https://github.com/harivonyR/LinkedIn_Lead_Generation
```

### 2. Open the project folder
```bash
cd LinkedIn_Lead_Generation
```

### 3. Create your credential file
Copy the example file:
```bash
copy credential.example.py credential.py
```

Open `credential.py` and paste your **PILOTERR API KEY**:
```python
x_api_key = "Paste your API key here !"
```

### 4. Install dependencies
```bash
pip install requests
```

### 5. Run the Lead Generation
This command will run a sample query for lead generation in the main script.
> See 10 more sample in main.py
```bash
python main.py
```
