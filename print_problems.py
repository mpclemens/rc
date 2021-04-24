from lib.epd2in7b import EPD, EPD_HEIGHT, EPD_WIDTH
from PIL import Image, ImageDraw, ImageFont


def printToDisplay(epd, string):
    HBlackImage = Image.new("1", (EPD_HEIGHT, EPD_WIDTH), 264)
    HRedImage = Image.new("1", (EPD_HEIGHT, EPD_WIDTH), 176)

    draw = ImageDraw.Draw(
        HBlackImage
    )  # Create draw object and pass in the image layer we want to work with (HBlackImage)
    font = ImageFont.truetype(
        "/usr/share/fonts/truetype/Piboto-Bold.ttf", 30
    )  # Create our font, passing in the font file and font size

    draw.text((25, 65), string, font=font, fill=0)
    try:
        epd.display(epd.getbuffer(HBlackImage), epd.getbuffer(HRedImage))
    except Exception as e:
        # Try to figure out why it's sad
        print(f"Could not call display on {epd}:\n{e}")


epd = EPD()  # get the display
epd.init()  # initialize the display

print("Clear...")  # prints to console, not the display, for debugging
# epd.Clear(0xFF)            # clear the display (this also throws an error when in code)
printToDisplay(epd, "Hello, World!")
