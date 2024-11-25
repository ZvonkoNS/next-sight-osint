import re
import requests
from bs4 import BeautifulSoup
import openpyxl
from openpyxl.styles import Alignment

# ASCII Art Header for Branding
ascii_header = """
####################################################################################################
####################################################################################################
##########################      NEXT SIGHT - Cutting Edge Intelligence      #########################
####################################################################################################
www.next-sight.com
For professional OSINT and other investigations contact us at info@next-sight.com
"""

# Module: Email Validation
def validate_email(email):
    """Validate email syntax and domain existence."""
    print("\n[Step 1] Validating Email...")
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(regex, email):
        return False, "Invalid email format! Check your input. 🐾"
    domain = email.split('@')[1]
    try:
        requests.get(f"http://{domain}", timeout=5)
        return True, "Email domain is valid! ✅"
    except requests.exceptions.RequestException:
        return False, "Domain not reachable! 🛑"

# Module: WHOIS Lookup
def domain_whois(email):
    """Get WHOIS information for the email's domain."""
    print("\n[Step 2] Fetching WHOIS Information...")
    domain = email.split('@')[1]
    whois_url = f"https://www.whois.com/whois/{domain}"
    try:
        response = requests.get(whois_url, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            raw_data = soup.find("pre")
            return raw_data.text if raw_data else "No WHOIS data found. 🕵️"
        else:
            return "Unable to fetch WHOIS data. 🤷‍♂️"
    except requests.exceptions.RequestException as e:
        return f"Error fetching WHOIS data: {str(e)}"

# Module: Social Media Lookup
def social_media_lookup(email):
    """Look for potential social media accounts."""
    print("\n[Step 3] Performing Social Media Lookup...")
    username = email.split('@')[0]  # Extract username from email
    platforms = {
        "Twitter": f"https://twitter.com/{username}",
        "GitHub": f"https://github.com/{username}",
        "Instagram": f"https://instagram.com/{username}",
        "Facebook": f"https://facebook.com/{username}"
    }
    found_accounts = {}

    for platform, url in platforms.items():
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                found_accounts[platform] = url
        except requests.exceptions.RequestException:
            pass

    if found_accounts:
        print(f"Found social media accounts: {found_accounts}")
    else:
        print("No accounts found. The user is a ghost online. 👻")
    return found_accounts

# Module: Have I Been Pwned Check
def hibp_check(email):
    """Check if the email is in data breaches using Have I Been Pwned API."""
    print("\n[Step 4] Checking Data Breaches with HIBP...")
    hibp_api_key = input("Enter your HIBP API key (or press Enter to skip): ")
    if not hibp_api_key:
        print("Skipping HIBP check. Want to know if you've been pwned? Get your API key at https://haveibeenpwned.com/API! 🔑")
        return False, "HIBP check skipped."

    hibp_api = "https://haveibeenpwned.com/api/v3/breachedaccount/"
    headers = {
        "hibp-api-key": hibp_api_key,
        "User-Agent": "OSINT-Email-Checker"
    }
    try:
        response = requests.get(f"{hibp_api}{email}", headers=headers)
        if response.status_code == 200:
            breaches = response.json()
            return True, breaches
        elif response.status_code == 404:
            return False, "No breaches found! 🔒"
        else:
            return False, f"Error: {response.status_code} - {response.text}"
    except Exception as e:
        return False, f"Error querying HIBP: {str(e)}"

# Module: Save Results to Excel
def save_results_to_excel(email, validation_result, whois_data, social_accounts, breach_results):
    """Save the OSINT results to an Excel file with wrapped text."""
    print("\n[Step 5] Saving Results to Excel...")
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "OSINT Results"
    
    # Add header row
    sheet.append(["Email Address", "Validation Result", "WHOIS Information", "Social Media Accounts", "Data Breaches"])
    
    # Prepare data
    social_links = "\n".join([f"{platform}: {url}" for platform, url in social_accounts.items()])
    if isinstance(breach_results, list):
        breach_info = "\n".join([f"{breach['Name']}: {breach['Description']}" for breach in breach_results])
    else:
        breach_info = breach_results

    # Add results
    sheet.append([email, validation_result, whois_data, social_links, breach_info])
    
    # Apply "Wrap Text" formatting
    for col in sheet.columns:
        for cell in col:
            cell.alignment = Alignment(wrap_text=True)

    # Adjust column widths for better readability
    sheet.column_dimensions['A'].width = 30  # Email Address
    sheet.column_dimensions['B'].width = 30  # Validation Result
    sheet.column_dimensions['C'].width = 50  # WHOIS Information
    sheet.column_dimensions['D'].width = 50  # Social Media Accounts
    sheet.column_dimensions['E'].width = 50  # Data Breaches
    
    # Save the workbook
    output_file = "osint_results.xlsx"
    workbook.save(output_file)
    print(f"Results saved to {output_file}! 📂")

# Main Execution
def main():
    print(ascii_header)
    email = input("Enter an email to perform OSINT: ")

    # Validate email
    is_valid, validation_message = validate_email(email)
    print(validation_message)
    if not is_valid:
        return

    # Check domain WHOIS
    whois_info = domain_whois(email)
    print(f"WHOIS Data:\n{whois_info}")

    # Social media lookup
    social_accounts = social_media_lookup(email)

    # HIBP Check
    breached, breach_results = hibp_check(email)
    if breached:
        print("Breaches found:")
        for breach in breach_results:
            print(f"- {breach['Name']}: {breach['Description']}")
    else:
        print(breach_results)

    # Save results
    save_results_to_excel(email, validation_message, whois_info, social_accounts, breach_results)

if __name__ == "__main__":
    main()

# Python script content (already written previously) here
# For brevity, this content is omitted in this cell
