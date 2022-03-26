from tkinter import *
import os
import tkinter
from tkinter import filedialog
from PIL import ImageFont
from PIL import ImageDraw
from PIL import Image, ImageTk


def copyright_apply():
    global image_file

    try:

        photo_dir = entry_escolher_imagem_principal.get()
        # photo_dir = "Screenshot_53.png"

        with Image.open(photo_dir) as photo:
            # print(photo)

            entry_escolher_imagem_marca_dagua.delete(first=0, last=END)
            # Store image width and height

            w, h = photo.size
            print(w, h)
            drawing = ImageDraw.Draw(photo)

            # make the image editable
            font = ImageFont.truetype("arial.ttf", 62)

            # get text width and height
            texto_marca = str(entry_escolher_texto_marca_dagua.get())
            texto_marca = "© " + texto_marca + "  "
            texto_marca_width, texto_marca_height = drawing.textsize(
                texto_marca, font)

            pos = w - texto_marca_width, (h - texto_marca_height) - 50

            c_text = Image.new(
                'RGB', (texto_marca_width, (texto_marca_height)), color='#000000')
            drawing = ImageDraw.Draw(c_text)

            drawing.text((0, 0), texto_marca, fill="#ffffff", font=font)
            c_text.putalpha(100)

            photo.paste(c_text, pos, c_text)
            # photo.save(output_image_path)

            # #######################################
            height_img = float(photo.height / 400)
            width_img = float(photo.width / 600)

            print(height_img, width_img)

            if height_img > width_img:
                new_size = height_img
            else:
                new_size = width_img

            new_width = int(photo.width/new_size)
            new_height = int(photo.height/new_size)
            resize_image = photo.resize(
                (
                    new_width,
                    new_height
                ))
            image_file = ImageTk.PhotoImage(resize_image)

            canvas.create_image(
                int(new_width/2),
                int(new_height/2),
                image=image_file)

            return photo

    except Exception as e:
        print(e)
        return


def watermark_image_apply():
    global image_file

    try:

        photo_dir = entry_escolher_imagem_principal.get()
        # photo_dir = "Screenshot_53.png"

        with Image.open(photo_dir) as photo:
            # print(photo)
            # Store image width and height
            w, h = photo.size
            print(w, h)

            # drawing = ImageDraw.Draw(photo)

            watermark_photo_dir = openimgfile()

            entry_escolher_texto_marca_dagua.delete(first=0, last=END)
            entry_escolher_imagem_marca_dagua.delete(first=0, last=END)
            entry_escolher_imagem_marca_dagua.insert(
                0, str(watermark_photo_dir))

            watermark_image = Image.open(watermark_photo_dir)
            # watermark_image.load(transparency=True)
            watermark_image = watermark_image.resize(
                (w, h), Image.LANCZOS,).convert("RGBA")

            transparent = Image.new('RGBA', (w, h), (0, 0, 0, 0))
            transparent.paste(photo, (0, 0))
            # transparent.paste(watermark_image, (0, 0),
            #                   mask=watermark_image)
            # watermark_image.putalpha(100)
            transparent.paste(watermark_image, (0, 0),
                              mask=watermark_image)

            """
            return newImage

            # Take two images    
            image1 = Image.open("./sky.png")
            image2 = Image.open("./plane.png")

            # Make the sizes of images uniform
            image3 = changeImageSize(800, 500, image1)
            image4 = changeImageSize(800, 500, image2)

            # Make sure the images have alpha channels
            image3.putalpha(1)
            image4.putalpha(1)

            # Display the images
            image3.show()
            image4.show()

            # Do an alpha composite of image4 over image3
            alphaComposited = Image.alpha_composite(image3, image4)
            #alphaBlended = Image.blend(image4, image3,.1)
            #alphaBlended.show()

            # Display the alpha composited image
            alphaComposited.show()
            """

            # photo = Image.composite(
            #     watermark_image, photo, mask=watermark_image)

            # texto_marca_width, texto_marca_height = drawing.textsize(
            #     texto_marca, font)

            # pos = w - texto_marca_width, (h - texto_marca_height) - 50

            # c_text = Image.new(
            #     'RGB', (texto_marca_width, (texto_marca_height)), color='#000000')
            # drawing = ImageDraw.Draw(c_text)

            # drawing.text((0, 0), texto_marca, fill="#ffffff", font=font)
            # c_text.putalpha(100)

            # transparent.putalpha(50)

            # photo.paste(transparent)
            photo = transparent
            # photo.save(output_image_path)

            # #######################################
            height_img = float(photo.height / 400)
            width_img = float(photo.width / 600)

            print(height_img, width_img)

            if height_img > width_img:
                new_size = height_img
            else:
                new_size = width_img

            new_width = int(photo.width/new_size)
            new_height = int(photo.height/new_size)
            resize_image = photo.resize(
                (
                    new_width,
                    new_height
                ))
            image_file = ImageTk.PhotoImage(resize_image)

            canvas.create_image(
                int(new_width/2),
                int(new_height/2),
                image=image_file)

            return photo

    except Exception as e:
        print(e)
        return


# ---------------------------- GET IMAGE --------------------------------- #
def openimgfile():
    currdir = os.getcwd()
    name = filedialog.askopenfile(
        initialdir=currdir,
        title="Select a Image",
        filetype=(
            ("PNG", "*.png"), ("JPEG", "*.jpg;.*jpeg"), ("All files", "*.*")))
    return name.name


def save_image_dir():
    currdir = os.getcwd()
    file = filedialog.asksaveasfilename(
        initialdir=currdir,
        title="Save Image",
        filetypes=(
            ("PNG", "*.png"), ("JPEG", "*.jpg;.*jpeg"), ("All files", "*.*")),
    )
    print(file)
    return file


def save_image():
    main_image = str(entry_escolher_imagem_principal.get())
    mark_image = str(entry_escolher_imagem_marca_dagua.get())
    mark_text = str(entry_escolher_texto_marca_dagua.get())
    print(
        f"main_image: '{main_image}', mark_image: '{mark_image}', mark_text: '{mark_text}'")
    if main_image:
        if mark_image and not mark_text:
            print("Salvando com marca de imagem.")
            photo_image = watermark_image_apply()
            print(photo_image)
            photo_image.save(
                save_image_dir()
            )
        elif not mark_image and mark_text:
            print("Salvando com marca de texto.")
            photo_image = copyright_apply()

            print(photo_image)
            photo_image.save(
                save_image_dir()
            )
        else:
            print("Inserir um modo de marca d'agua")
            entry_escolher_imagem_marca_dagua.delete(0, END)
            entry_escolher_texto_marca_dagua.delete(0, END)
    else:
        print('Inserir imagem principal de fundo.')


def open_file():
    global image_file

    name_file = openimgfile()
    image_file_dir = Image.open(name_file)

    height_img = float(image_file_dir.height / 400)
    width_img = float(image_file_dir.width / 600)

    if height_img > width_img:
        new_size = height_img
    else:
        new_size = width_img

    new_width = int(image_file_dir.width/new_size)
    new_height = int(image_file_dir.height/new_size)
    resize_image = image_file_dir.resize(
        (
            new_width,
            new_height
        ))
    image_file = ImageTk.PhotoImage(resize_image)

    canvas.create_image(
        int(new_width/2),
        int(new_height/2),
        image=image_file)

    entry_escolher_imagem_principal.delete(first=0, last=END)
    entry_escolher_imagem_principal.insert(0, str(name_file))


# ---------------------------- RESIZE IMAGE ------------------------------ #
# ---------------------------- SAVE IMAGE -------------------------------- #


# ---------------------------- UI SETUP ------------------------------------ #
window = tkinter.Tk()
window.title("Water Mark")
window.config(padx=50, pady=50)

canvas = tkinter.Canvas(width=600, height=400)
image_file = tkinter.PhotoImage(file="day84\\assets\\no-image.png")
canvas.create_image(300, 200, image=image_file)
canvas.grid(row=0, column=0, columnspan=3)

# labels
# label_website = tkinter.Label(text="Website:")
# label_website.grid(row=5, column=0)

# label_username = tkinter.Label(text="Email/Username:")
# label_username.grid(row=2, column=0)

# label_password = tkinter.Label(text="Password:")
# label_password.grid(row=3, column=0)

# Entries
entry_escolher_imagem_principal = tkinter.Entry(width=62)
entry_escolher_imagem_principal.grid(row=1, column=0, columnspan=2)

entry_escolher_imagem_marca_dagua = tkinter.Entry(width=62)
entry_escolher_imagem_marca_dagua.grid(row=2, column=0, columnspan=2)

entry_escolher_texto_marca_dagua = tkinter.Entry(width=62)
entry_escolher_texto_marca_dagua.grid(row=3, column=0, columnspan=2)


# buttons
button_escolher_imagem_principal = tkinter.Button(
    text="Escolher Imagem principal", command=open_file, width=28)
button_escolher_imagem_principal.grid(row=1, column=2)

button_escolher_imagem_marca_dagua = tkinter.Button(
    text="Escolher Marca d'Agua", command=watermark_image_apply, width=28)
button_escolher_imagem_marca_dagua.grid(row=2, column=2)

button_escolher_texto_marca_dagua = tkinter.Button(
    text="Aplicar Texto Marca d'Agua", command=copyright_apply, width=28)
button_escolher_texto_marca_dagua.grid(row=3, column=2)

button_salvar = tkinter.Button(
    text="Salvar", command=save_image, width=28)
button_salvar.grid(row=4, column=2)


window.mainloop()
