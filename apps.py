import os
import ftplib
import shutil
import schedule
import logging



# Defining FTP server credentials
ftp_host = "ftp.gnu.org"
ftp_user = "anonymous"
ftp_password = ""

# Defining local directory for storing downloaded files
local_dir = "/Users/danielmulatarancon/Desktop/Documents/HACKING TIME/Brainnest /Week 03/Advance Tasks/Downloaded_files"

# Defining internal network directory for storing transferred files
internal_dir = "/Users/danielmulatarancon/Desktop/Documents/HACKING TIME/Brainnest /Week 03/Advance Tasks/Internal_directory"

# Defining a function to download files from the FTP server
def download_files():
    # Connecting to the FTP server
    with ftplib.FTP(ftp_host, ftp_user, ftp_password) as ftp:
        # Listing files in the FTP directory
        files = ftp.nlst()
        # Checking if the local directory exists, if not I create it
        if not os.path.exists(local_dir):
            os.makedirs(local_dir)
        # Downloading each file to the local directory
        for file in files:
            local_file_path = os.path.join(local_dir, file)
            try:
                with open(local_file_path, "wb") as f:
                    ftp.retrbinary("RETR " + file, f.write)
                print(f"Successfully downloaded {file} to {local_file_path}")
            except ftplib.error_perm as e:
                print(f"Error downloading {file}: {e}")
            except Exception as e:
                print(f"Unexpected error downloading {file}: {e}")
        # Moving files from the local directory to the internal network directory
        for file in os.listdir(local_dir):
            shutil.move(os.path.join(local_dir, file), os.path.join(internal_dir, file))
        # Logging successful transfer message
        logging.info("Files transferred successfully")

# Scheduling the script to run daily at a specific time
schedule.every().day.at("16:53").do(download_files)

# Setting up logging
logging.basicConfig(filename="file_transfer.log", level=logging.INFO)

# Defining the 'dunder main' block
if __name__ == '__main__':
    # Start scheduled script
    while True:
        schedule.run_pending()
