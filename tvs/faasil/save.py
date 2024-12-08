import os
import requests

def download_s3_files(s3_links, save_folder):
    """̀
    Download files from a list of S3 links and save them to a specific folder.

    Args:
        s3_links (list): Lis`t of S3 URLs to download.
        save_folder (str): The folder where files should be saved.
    """
    # Create the folder if it doesn't exist
    os.makedirs(save_folder, exist_ok=True)

    for link in s3_links:
        try:
            # Extract file name from the link
            file_name = link.split("/")[-1]
            if not file_name:
                file_name = "vaishakcustomer_id57"

            # Create the full path for the file
            save_path = os.path.join(save_folder, file_name)

            # Download the file
            response = requests.get(link, stream=True)
            response.raise_for_status()

            with open(save_path, "wb") as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)

            print(f"Downloaded: {file_name} -> {save_path}")

        except requests.exceptions.RequestException as e:
            print(f"Failed to download {link}: {e}")

# List of S3 links
s3_links = [
    "   https://hogspot.s3.amazonaws.com/21ee532d-6c36-4d96-a606-8e79fd8a0092.jpg",
    "https://hogspot.s3.amazonaws.com/a24e26e7-344a-4603-81e9-85f361683867.jpg",
    " https://hogspot.s3.amazonaws.com/8f043c79-5d48-42e0-ae99-dbb752ca1fbe.blob",
 " https://hogspot.s3.amazonaws.com/e2cc37e7-6e09-43ab-868c-5cbf957eed56.copysign",
]

# Folder to save the files
save_folder = "vaishakcustomerid57"

# Download the files
download_s3_files(s3_links, save_folder)