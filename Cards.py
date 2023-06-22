from PIL import Image 
class Cards:

    def __init__(self, suit, denom, value, image_path):
        self.suit = suit 
        self.denom = denom
        self.value = value
        self.image_path = image_path

    def get_img(self):
        img = Image.open(self.image_path)
        return img 

    