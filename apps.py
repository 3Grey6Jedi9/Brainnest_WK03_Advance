import os
import ftplib
import shutil
import schedule
import logging

# Define FTP server credentials
ftp_host = "ftp.example.com"
ftp_user = "username"
ftp_password = "password"

# Define local directory for storing downloaded files
local_dir = "/path/to/local/directory"

# Define internal network directory for storing transferred files
internal_dir = "/path/to/internal/network/directory"

# Define function to download files from FTP server
def download_files():
    # Connect to FTP server
    with ftplib.FTP(ftp_host, ftp_user, ftp_password) as ftp:
        # List files in FTP directory
        files = ftp.nlst()
        # Check if local directory exists, if not create it
        if not os.path.exists(local_dir):
            os.makedirs(local_dir)
        # Download each file to local directory
        for file in files:
            with open(os.path.join(local_dir, file), "wb") as f:
                ftp.retrbinary("RETR " + file, f.write)
        # Move files from local directory to internal network directory
        for file in os.listdir(local_dir):
            shutil.move(os.path.join(local_dir, file), os.path.join(internal_dir, file))
        # Log successful transfer
        logging.info("Files transferred successfully")

# Schedule script to run daily at a specific time
schedule.every().day.at("10:00").do(download_files)

# Set up logging
logging.basicConfig(filename="file_transfer.log", level=logging.INFO)

# Start scheduled script
while True:
    schedule.run_pending()
