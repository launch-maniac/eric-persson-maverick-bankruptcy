# RunItOneTime LLC Bankruptcy - PDF Download Instructions

**Case No. 25-90191**  
**Court:** U.S. Bankruptcy Court for the Southern District of Texas

## Overview

This package contains a Python script to download PDF files from the Kroll Restructuring Administration website for the RunItOneTime LLC bankruptcy case.

## What's Included

The website contains the following categories of documents:

### Quick Links (Single Documents)
- Press Release 7.14.25
- Notice of Commencement  
- Sale Notice
- Bar Date Notice

### Quick Links (Multiple Documents - Requires Manual Download)
- Voluntary Petition (68+ documents)
- First Day Motions
- First Day Orders
- Schedules & SOFA
- Sale Documents
- Master Service List

### Docket Entries
- 729 docket entries with attachments

## Installation & Usage

### Prerequisites
```bash
# Install Python 3 (if not already installed)
# Install required package
pip3 install requests
```

### Running the Script

1. Open Terminal on your Mac
2. Navigate to the directory containing the script:
   ```bash
   cd ~/Downloads
   ```

3. Run the script:
   ```bash
   python3 download_runitonetime_pdfs.py
   ```

4. The script will:
   - Create the directory structure at `/Users/geoffreyflores/Downloads/RunItOneTime-Bankruptcy`
   - Download all single-document Quick Links PDFs
   - Display progress and summary

## Important Notes

### CAPTCHA Protection
The Kroll website has CAPTCHA protection for bulk downloads. This means:

1. **Single documents** (Press Release, Notice of Commencement, etc.) can be downloaded via the script
2. **Multiple document categories** (Voluntary Petition, First Day Motions, etc.) require manual download due to CAPTCHA verification

### Manual Download for Multi-Document Categories

For categories with multiple documents, you'll need to:

1. Visit the URLs listed below
2. Click on each document's attachment icon
3. Complete the CAPTCHA verification
4. Download the PDF

**URLs for Manual Download:**

- **Voluntary Petition:**  
  https://restructuring.ra.kroll.com/RunItOneTime/Home-DocketInfo?DocAttribute=4971&DocAttrName=VOLUNTARYPETITION_Q

- **First Day Motions:**  
  https://restructuring.ra.kroll.com/RunItOneTime/Home-DocketInfo?DocAttribute=4972&DocAttrName=FIRSTDAYMOTIONS_Q

- **First Day Orders:**  
  https://restructuring.ra.kroll.com/RunItOneTime/Home-DocketInfo?DocAttribute=4973&DocAttrName=FIRSTDAYORDERS_Q

- **Schedules & SOFA:**  
  https://restructuring.ra.kroll.com/RunItOneTime/Home-DocketInfo?DocAttribute=4974&DocAttrName=SCHEDULESSOFA_Q

- **Main Docket (729 entries):**  
  https://restructuring.ra.kroll.com/RunItOneTime/Home-DocketInfo

## Directory Structure

The script creates the following folder structure:

```
/Users/geoffreyflores/Downloads/RunItOneTime-Bankruptcy/
├── Quick_Links/
│   ├── Press_Release_7.14.25.pdf
│   ├── Notice_of_Commencement.pdf
│   ├── Sale_Notice.pdf
│   └── Bar_Date_Notice.pdf
├── Voluntary_Petition/
├── First_Day_Motions/
├── First_Day_Orders/
├── Schedules_SOFA/
├── Sale_Documents/
└── Docket_Entries/
```

## Troubleshooting

### Script doesn't run
- Ensure Python 3 is installed: `python3 --version`
- Install requests: `pip3 install requests`

### Downloads fail
- Check your internet connection
- The website may be temporarily unavailable
- CAPTCHA protection may be blocking automated downloads

### Permission errors
- Ensure you have write permissions to `/Users/geoffreyflores/Downloads/`
- Try running with: `sudo python3 download_runitonetime_pdfs.py`

## Alternative: Browser-Based Download

If the script doesn't work due to CAPTCHA or other restrictions, you can:

1. Visit: https://restructuring.ra.kroll.com/RunItOneTime/Home-DocketInfo
2. Click "Menu" → "Quick Links"
3. Click on each category
4. Download PDFs individually

## Support

For questions about the bankruptcy case or document access, contact:
- Phone: 877.814.0967 or +1.646.440.4376
- Website: https://restructuring.ra.kroll.com/RunItOneTime

---

**Last Updated:** November 4, 2025
