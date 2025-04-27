from PIL import Image, ImageDraw
import colorsys

#il y a que deux sections à modifier, les codes des couleurs et les parametres du tableau.


# ICI
# mettre les couleurs en hexadecimal peu importe l'ordre
colors = [
    "#3e3733", "#63415b", "#63415b", "#dbb9b9", "#a29b97", "#b8a4a3", "#5b2b1f",
    "#828282", "#2a3540", "#425934", "#86805a", "#d4dcef", "#7caebb", "#5499a0",
    "#837182", "#8e5c35", "#b9a06f", "#dfdba8", "#a67e4f", "#c8ab69", "#b27b11"
]

#----------------------------------------------------------------
def hex_to_hsl(hex_color):
    hex_color = hex_color.lstrip("#")
    r, g, b = tuple(int(hex_color[i:i+2], 16)/255.0 for i in (0, 2, 4))
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    return h, l, s 

#----------------------------------------------------------------
colors_sorted = sorted(colors, key=lambda x: hex_to_hsl(x)[0])


# ET ICI AUSSI
# là c'est pour faire un tab;eau avec les colonne, les lignes, la taille des carrés et entre les carrés. Après c'est écrit en fait
# faut faire attention à ca que le compte tombe juste parce que jsp ce que ca fait sinon
cols = 7
rows = 3
size = 100
margin = 10

#----------------------------------------------------------------
img_width = cols * size + (cols + 1) * margin
img_height = rows * size + (rows + 1) * margin
# pour avoir des rectangles rajoutez juste un size2 à mattre soit dans width soit dans height
# mais c'est plus joli des carrés.


img = Image.new("RGB", (img_width, img_height), "white")
draw = ImageDraw.Draw(img)

#----------------------------------------------------------------
for idx, color in enumerate(colors_sorted):
    col = idx % cols
    row = idx // cols
    x1 = margin + col * (size + margin)
    y1 = margin + row * (size + margin)
    x2 = x1 + size
    y2 = y1 + size
    draw.rectangle([x1, y1, x2, y2], fill=color)

#----------------------------------------------------------------
img.save("color_lalala.png")
print("Image sauvegardée sous 'color_lalala.png'")
# ça se save là ou est le fichier .py