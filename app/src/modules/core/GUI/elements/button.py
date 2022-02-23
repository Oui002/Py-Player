from pygame import image

class Button():

    def __init__(self, image_path, pos, text_input, font, base_color, hovering_color, _type) -> None:
        self.image = image.load(f"../assets/buttons/{image_path}")
        self.x = pos[0]
        self.y = pos[1]
        self.text_input = text_input
        self.font = font
        self.base_color = base_color
        self.hovering_color = hovering_color

        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image == None:
            self.image = self.text
        
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.text_rect = self.text.get_rect(center=(self.x, self.y))

        self.type = _type
    
    def update(self, screen,) -> None:
        if self.image != None:
            screen.blit(self.image, self.rect)

        screen.blit(self.text, self.text_rect)
    
    def check_for_input(self, pos):
        if pos[0] in range(self.rect.left, self.rect.right) and pos[1] in range(self.rect.top, self.rect.bottom):
            return True

        return

    def change_color(self, pos,) -> None:
        if pos[0] in range(self.rect.left, self.rect.right) and pos[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)