import dropbox
import sys

# Replace with your access token
ACCESS_TOKEN = 'your_access_token_here'

def upload_pdf(file_path):
    dbx = dropbox.Dropbox(ACCESS_TOKEN)

    with open(file_path, 'rb') as f:
        file_name = '/' + file_path.split('/')[-1]
        dbx.files_upload(f.read(), file_name, mode=dropbox.files.WriteMode('overwrite'))

    return file_name

def get_shareable_link(file_path):
    dbx = dropbox.Dropbox(ACCESS_TOKEN)
    shared_link_metadata = dbx.sharing_create_shared_link_with_settings(file_path)
    return shared_link_metadata.url.replace('?dl=0', '.pdf')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <pdf_file_path>")
        sys.exit(1)

    pdf_file_path = sys.argv[1]
    uploaded_file_path = upload_pdf(pdf_file_path)
    shareable_link = get_shareable_link(uploaded_file_path)
    print("Shareable link:", shareable_link)