import compileall
import glob
import os
import sys
 
def compile_all_py_to_pyc(directory):
    """
    將指定目錄及其所有子目錄下的 .py 檔案編譯為 .pyc 檔案
    """
    for py_file in glob.iglob(os.path.join(directory, '**/*.py'), recursive=True):
        compileall.compile_file(py_file, force=True, legacy=True)
        print(f"已將 {py_file} 編譯為 .pyc 檔案。")

def delete_pyc_files(directory):
    """
    刪除指定目錄及其所有子目錄下的 .pyc 文件
    """
    for pyc_file in glob.iglob(os.path.join(directory, '**/*.pyc'), recursive=True):
        os.remove(pyc_file)
        print(f"Deleted .pyc file: {pyc_file}")
        
def delete_py_files(directory):
    """
    刪除指定目錄及其所有子目錄下的 .py 文件
    """
    for pyc_file in glob.iglob(os.path.join(directory, '**/*.py'), recursive=True):
        os.remove(pyc_file)
        print(f"Deleted .py file: {pyc_file}")
        
