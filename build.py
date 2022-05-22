import os

def build(mds, path):
    contents = []
    for md in mds:
        with open(md, 'r', encoding = 'utf-8') as file:
            contents.append(file.read() + "\n")
    with open(path, "w", encoding = 'utf-8') as file:
        file.writelines(contents)

cwd = os.getcwd()

path = cwd + "\\build\\" + "软件过程与软件项目管理.md"
mds = ["1.概论.md", "2.软件质量管理.md", "3.软件项目管理.md", "4.经典的软件过程管理.md", "5.敏捷软件开发.md"]

if os.path.exists(cwd + "\\build"):
    print(111111)
    build(mds, path)
else:
    print(222222)
    os.mkdir(cwd + "\\build")
    build(mds, path)
