import os
from pathlib import Path
import shutil

def file_organizer(source_dir, destination_dir):
    path = Path(source_dir)
    

    for f in path.iterdir():
        if f.absolute().is_file():
            destination_path = Path(destination_dir)

            ext = os.path.splitext(f)[-1].lower()
            print("# Filetype: ", ext)

            destination_sub_dir = destination_path.joinpath(ext[1:].upper())

            print("Destination Sub Directory: ", destination_sub_dir)

            if not Path(destination_dir).exists():
                print(f"# Creting {destination_sub_dir} directory")
                os.mkdir(destination_sub_dir)
            # else:
            #     print("Directory already exists")


            src = f.absolute()
            print("Source : ", src)
            dst = Path(str(destination_sub_dir)+"\\"+str(f.name))
            print("Destination : ", dst)
            print(f"# Moving {src} to {dst}")

            shutil.move(src, dst)

if __name__ == "__main__":
    source_dir = input("Source Dir: ")
    destination_dir = input("Destination Dir: ")
    file_organizer(source_dir, destination_dir)
    print("\n\nProcess Completed..")