from pathlib import Path
from time import ctime
import shutil
source = Path("path_p.py")
target = Path() / "__init__.py"
shutil.copy(source, target)

'''path.exists()
path.is_file()
path.is_dir()
print(path.name)
print(path.stem)
print(path.suffix)
print(path.parent)
path1 = path.with_name("file.txt")
print(path1)
print(path1.absolute())
print(path1.with_stem("oop_1"))
print(path1.with_suffix(".py"))'''

'''for p in path.iterdir():
    print(p)'''


print(source.exists())
print(source.iterdir())
# path_c = path.rename("path_p.txt")
# print(path_c)
# print(ctime(path.stat().st_ctime))
print(source.read_text())
