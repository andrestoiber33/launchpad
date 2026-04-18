from PIL import Image

def make_transparent(input_path, output_path):
    img = Image.open(input_path).convert('RGBA')
    datas = img.getdata()
    
    new_data = []
    for item in datas:
        # Change all white (also shades of white)
        # to transparent
        if item[0] > 200 and item[1] > 200 and item[2] > 200:
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)
            
    img.putdata(new_data)
    img.save(output_path, 'PNG')

make_transparent(r'C:\Users\a.stoiber.machado\.gemini\antigravity\brain\bcf93f28-ce2a-4f2c-ba29-16eb191d1094\media__1776548337039.png', r'c:\Users\a.stoiber.machado\Desktop\launchpad\images\logo.png')
