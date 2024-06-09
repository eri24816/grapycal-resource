import os
import subprocess

def png2svg(file_name:str):
    # Use ffmpeg to convert the png to a bmp
    png_path = file_name+'.png'
    bmp_path = file_name+'.bmp'
    res = subprocess.run(['ffmpeg','-i',png_path,bmp_path])
    if res.returncode != 0:
        raise Exception(f'ffmpeg failed with return code {res.returncode}')
    # Use potrace to convert the bmp to a svg
    svg_path = '../'+file_name+'.svg'
    res = subprocess.run(['./potrace','-s','-o',svg_path,bmp_path])
    if res.returncode != 0:
        raise Exception(f'potrace failed with return code {res.returncode}')
    # Remove the bmp
    os.remove(bmp_path)
    # Remove the png
    os.remove(png_path)

if __name__ == '__main__':
    # change cwd to the directory of this file
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    # convert the pngs
    for file_name in os.listdir('.'):
        if file_name.endswith('.png'):
            png2svg(file_name[:-4])

    # list all svgs in ../list.txt
    with open('../list.txt','w') as f:
        for file_name in os.listdir('..'):
            if file_name.endswith('.svg'):
                f.write(file_name[:-4]+'\n')