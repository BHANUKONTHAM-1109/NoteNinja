import os

def save_uploaded_file(uploaded_file, upload_dir="data"):
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)

    try:
        file_path = os.path.join(upload_dir, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        return file_path
    except Exception as e:
        print("❌ Error saving file:", e)
        return None
