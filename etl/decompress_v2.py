# from urllib.request import urlretrieve
# import py7zr
# import os

# basepath = "./data"
# dlpath = f"{basepath}/rais"

# lista_path = os.listdir(dlpath)

# def decompress(arquivo):
#     filename = dlpath + '/' + arquivo    
#     print(filename)
#     archive = py7zr.SevenZipFile(filename)
#     archive.extractall(path=dlpath)
#     archive.close()
#     os.remove(filename)
#     return True
    
# if __name__ == "__main__":
#     os.makedirs(dlpath, exist_ok=True)

#     for i in range(len(lista_path)):
#         print(f"Extracting from {lista_path[i]}")
#         res = decompress(lista_path[i])
#         print(res)
    
#     print("Done!")