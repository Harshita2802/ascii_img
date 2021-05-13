import ascii_magic
output = ascii_magic.from_image_file("hs1.jpg",columns=80,char="s")
ascii_magic.to_terminal(output)