import pygame as pg
import colors as c

class TextBox:

    def __init__(self, x: int, y: int, w: int, h: int=32, text: str=''):
        self.FONT = pg.font.SysFont('consolas', 24)
        self.rect = pg.Rect(x, y, w, h)
        self.color = c.WHITE
        self.text = text
        self.txt_surface = self.FONT.render(text, True, self.color)
        self.active = True
        self.returned = ''

    def handle_event(self, event: pg.event.EventType) -> None:
        if event.type == pg.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False
        if event.type == pg.KEYDOWN:
            if self.active:
                self.returned = self.text
                if event.key == pg.K_RETURN:
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                elif event.key == pg.K_ESCAPE:
                    self.text = ''
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = self.FONT.render(self.text, True, self.color)

    def update(self) -> None:
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen: pg.display) -> None:
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(screen, self.color, self.rect, 2)

    def get_returned(self) -> str:
        return self.returned
