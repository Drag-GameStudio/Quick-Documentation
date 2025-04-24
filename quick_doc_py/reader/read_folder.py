import os


class FilesReader:
    def __init__(self):
        self.files = {}

    def read_file(self, file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
            return content
        
        except Exception as e:
            # print(f"Error reading file {file_path}: {e}")
            # with open(file_path, "rb") as file:
            #     content = file.read()
            return None
        

    def add_file(self, file_path, file_name):
        content = self.read_file(file_path)
        if content is not None:
            self.files[file_name] = content
        

    def get_all_prompt(self):
        return self.files

class Reader:
    def __init__(self, path, ignore_files: list = []):
        self.path = path
        self.ignore_files = ignore_files


    def read_folder(self):
        files_reader = FilesReader()

        for root, dirs, files in os.walk(self.path):
            if self.check_ignore_folders(self.get_local_path(root)):
                print(f"Root: {self.get_local_path(root)}")

                print(f"Root: {root}")
                print(f"Directories: {dirs}")
                print(f"Files: {files}")
                print("-" * 20)
                for file_name in files:
                    local_file_path = self.get_local_path(root) + file_name
                    isNotIgnored = self.check_ignore_files(local_file_path, file_name)
                    if isNotIgnored:
                        files_reader.add_file(root + "/" + file_name, local_file_path)

        

        return files_reader

    def get_local_path(self, file_path):
        local_path = os.path.relpath(file_path, self.path)
        return f"{local_path}\\"

    def check_ignore_files(self, local_file_path, file_name):
        # print(local_file_path)
        for ignore_file in self.ignore_files:
            if ignore_file[0] == "*":
                if file_name == ignore_file[1:]:
                    return False
            
            if local_file_path == ignore_file:
                return False
            
        return True
    
    def check_ignore_folders(self, local_folder_path):
        all_folders = local_folder_path.split("\\")

        for i, folder in enumerate(all_folders):
            for ignore_folder in self.ignore_files:
                if ignore_folder[0] == "*":
                    if folder == ignore_folder[1:]:
                        return False
                
                ld = ""
                for j, el in enumerate(all_folders[0:i+2]):
                    if j < i:
                        ld += el + "\\"
                        continue
                    ld += el
                # print(ld)
                if ld == ignore_folder:
                    return False

        return True


        # if len(local_folder_path.split("\\")) < 2:
        #     return True
        # folder_name = local_folder_path.split("\\")[-2]
        # print(f"Folder name: {folder_name} {local_folder_path} {local_folder_path.split("\\")}")

        # for ignore_folder in self.ignore_files:
        #     if local_folder_path == ignore_folder:
        #         return False
            
        #     if ignore_folder[0] == "*":
        #         if folder_name == ignore_folder[1:]:
        #             return False
                
        # all_local_folders = local_folder_path.split("\\")
        # all_local_folders = all_local_folders[:-1]

        # if len(all_local_folders) < 1:
        #     return True
        
        # new_local_folder_path = "\\".join(all_local_folders[:-1])
        # # print(f"{all_local_folders}, { all_local_folders[-1]} {new_local_folder_path}")

        # return self.check_ignore_folders(new_local_folder_path)

if __name__ == "__main__":
    fr = Reader(r"C:\Users\huina\Python Projects\Impotant projects\Libs\Quick Documentation\quick_doc_py", ["*__init__.py", "*__pycache__"]).read_folder()
# print(fr.get_all_prompt())