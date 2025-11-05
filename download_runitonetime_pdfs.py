#!/usr/bin/env python3
"""
RunItOneTime LLC Bankruptcy Case - PDF Downloader
Case No. 25-90191

This script downloads all PDF files from the Kroll Restructuring Administration website.
It handles session management and provides progress tracking.

Usage:
    python3 download_runitonetime_pdfs.py

The script will create a folder structure and download all available PDFs.
"""

import requests
import os
import time
import json
from pathlib import Path

# Configuration
BASE_DIR = "/Users/geoffreyflores/Downloads/RunItOneTime-Bankruptcy"
BASE_URL = "https://restructuring.ra.kroll.com"

# Quick Links PDFs (single documents)
QUICK_LINKS_SINGLE = {
    "Press_Release_7.14.25.pdf": "https://restructuring.ra.kroll.com/RunItOneTime/Home-DownloadPDF?id1=Mzc2MjA3Nw%3D%3D&id2=0",
    "Notice_of_Commencement.pdf": "https://restructuring.ra.kroll.com/RunItOneTime/Home-DownloadPDF?id1=Mzc1ODQxNA%3D%3D&id2=0",
    "Sale_Notice.pdf": "https://restructuring.ra.kroll.com/RunItOneTime/Home-DownloadPDF?id1=MzkxNTk3NQ%3D%3D&id2=0",
    "Bar_Date_Notice.pdf": "https://restructuring.ra.kroll.com/RunItOneTime/Home-DownloadPDF?id1=Mzk1NTY2Nw%3D%3D&id2=0",
}

# Quick Links categories with multiple documents
QUICK_LINKS_MULTI = {
    "Voluntary_Petition": "https://restructuring.ra.kroll.com/RunItOneTime/Home-DocketInfo?DocAttribute=4971&DocAttrName=VOLUNTARYPETITION_Q",
    "First_Day_Motions": "https://restructuring.ra.kroll.com/RunItOneTime/Home-DocketInfo?DocAttribute=4972&DocAttrName=FIRSTDAYMOTIONS_Q",
    "First_Day_Orders": "https://restructuring.ra.kroll.com/RunItOneTime/Home-DocketInfo?DocAttribute=4973&DocAttrName=FIRSTDAYORDERS_Q",
    "Schedules_SOFA": "https://restructuring.ra.kroll.com/RunItOneTime/Home-DocketInfo?DocAttribute=4974&DocAttrName=SCHEDULESSOFA_Q",
}

def create_directory_structure():
    """Create the base directory and subdirectories."""
    print(f"Creating directory structure at: {BASE_DIR}")
    
    dirs = [
        BASE_DIR,
        f"{BASE_DIR}/Quick_Links",
        f"{BASE_DIR}/Voluntary_Petition",
        f"{BASE_DIR}/First_Day_Motions",
        f"{BASE_DIR}/First_Day_Orders",
        f"{BASE_DIR}/Schedules_SOFA",
        f"{BASE_DIR}/Sale_Documents",
        f"{BASE_DIR}/Docket_Entries",
    ]
    
    for directory in dirs:
        Path(directory).mkdir(parents=True, exist_ok=True)
    
    print("✓ Directory structure created")

def download_pdf(url, filepath, session):
    """Download a single PDF file."""
    try:
        print(f"  Downloading: {os.path.basename(filepath)}")
        response = session.get(url, timeout=30)
        
        if response.status_code == 200:
            # Check if we actually got a PDF (not an HTML error page)
            content_type = response.headers.get('content-type', '')
            if 'pdf' in content_type.lower() or len(response.content) > 1000:
                with open(filepath, 'wb') as f:
                    f.write(response.content)
                print(f"  ✓ Downloaded: {os.path.basename(filepath)} ({len(response.content)} bytes)")
                return True
            else:
                print(f"  ✗ Invalid content type: {content_type}")
                return False
        else:
            print(f"  ✗ HTTP {response.status_code}")
            return False
            
    except Exception as e:
        print(f"  ✗ Error: {str(e)}")
        return False

def download_quick_links_single(session):
    """Download single-document Quick Links PDFs."""
    print("\n" + "="*60)
    print("DOWNLOADING QUICK LINKS (Single Documents)")
    print("="*60)
    
    success_count = 0
    for filename, url in QUICK_LINKS_SINGLE.items():
        filepath = f"{BASE_DIR}/Quick_Links/{filename}"
        if download_pdf(url, filepath, session):
            success_count += 1
        time.sleep(1)  # Be polite to the server
    
    print(f"\nCompleted: {success_count}/{len(QUICK_LINKS_SINGLE)} files downloaded")
    return success_count

def main():
    """Main execution function."""
    print("="*60)
    print("RunItOneTime LLC - PDF Downloader")
    print("Case No. 25-90191")
    print("="*60)
    print()
    
    # Create directory structure
    create_directory_structure()
    
    # Create session with headers
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
        'Accept': 'application/pdf,text/html,application/xhtml+xml',
    })
    
    # Download Quick Links (single documents)
    quick_links_count = download_quick_links_single(session)
    
    print("\n" + "="*60)
    print("DOWNLOAD SUMMARY")
    print("="*60)
    print(f"Quick Links (Single): {quick_links_count} files")
    print()
    print("NOTE: This script downloads the directly accessible PDF files.")
    print("For categories with multiple documents (Voluntary Petition, etc.),")
    print("you may need to manually navigate to those pages and download")
    print("individual files, as they may require CAPTCHA verification.")
    print()
    print(f"Files saved to: {BASE_DIR}")
    print("="*60)

if __name__ == "__main__":
    main()
