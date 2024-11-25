
# Next Sight OSINT Email Checker 🕵️‍♂️

The **Next Sight OSINT Email Checker** is a Python-based tool for investigating email addresses. This script validates email syntax, checks domain WHOIS information, performs social media lookups, and optionally queries the "Have I Been Pwned" (HIBP) API for data breaches.

## Features
- **Email Validation**: Checks syntax and domain existence.
- **WHOIS Lookup**: Retrieves domain registration details.
- **Social Media Lookup**: Checks for matching profiles on platforms like Twitter, GitHub, Instagram, and Facebook.
- **HIBP Integration**: Optionally checks for data breaches using the "Have I Been Pwned" API.
- **Excel Report**: Saves OSINT results in a neatly formatted `.xlsx` file.

## Requirements
- Python 3.7 or higher
- Internet connection
- Optional: HIBP API key (for breach checks)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/next-sight-osint.git
   cd next-sight-osint
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the script:
   ```bash
   python NextSightEmailOSINT.py
   ```

2. Follow the on-screen instructions:
   - Enter an email address to analyze.
   - Input your HIBP API key (optional). If skipped, the HIBP check will not run.

3. Results will be saved in `osint_results.xlsx`:
   - **Email Validation**: Confirms if the email is valid.
   - **WHOIS Data**: Displays domain registration details.
   - **Social Media Accounts**: Lists discovered accounts.
   - **Data Breaches**: Displays breach details if found.

## Example Output
- **Terminal**: Displays validation, WHOIS, and social media results.
- **Excel Report**: Saves all results in `osint_results.xlsx`.

## Notes
- To get an HIBP API key, visit [https://haveibeenpwned.com/API](https://haveibeenpwned.com/API).
- Social media lookups depend on the email username matching the platform handle.

## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute.

---

**Next Sight**  
Website: [www.next-sight.com](http://www.next-sight.com)  
Email: info@next-sight.com
