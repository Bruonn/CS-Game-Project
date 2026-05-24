"""

NOT USED IN GAME!!!

"""



import pygame as py
from pygame import mixer
import sys

py.init()
py.mixer.init()

# Menu dimensions
MENU_WIDTH = 600
MENU_HEIGHT = 700
BUTTON_WIDTH = 150
BUTTON_HEIGHT = 50

class MenuButton:
    """A simple button class for menu items"""
    def __init__(self, x, y, width, height, text, color=(100, 100, 100), text_color=(255, 255, 255)):
        self.rect = py.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.text_color = text_color
        self.hovered = False
        
    def draw(self, screen, font):
        """Draw the button"""
        color = tuple(min(c + 30, 255) for c in self.color) if self.hovered else self.color
        py.draw.rect(screen, color, self.rect)
        py.draw.rect(screen, (255, 255, 255), self.rect, 2)  # Border
        
        text_surface = font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)
        
    def is_clicked(self, pos):
        """Check if button is clicked"""
        return self.rect.collidepoint(pos)
    
    def update_hover(self, pos):
        """Update hover state"""
        self.hovered = self.rect.collidepoint(pos)


class CharacterPreview:
    """Display a character preview with name"""
    def __init__(self, x, y, size, img_path, name):
        self.x = x
        self.y = y
        self.size = size
        self.name = name
        self.rect = py.Rect(x, y, size, size)
        self.selected = False
        
        try:
            self.img = py.image.load(img_path)
            self.img = py.transform.scale(self.img, (size, size))
        except:
            self.img = None
            
    def draw(self, screen, font):
        """Draw the character preview"""
        # Draw border
        border_color = (255, 200, 0) if self.selected else (100, 100, 100)
        border_width = 4 if self.selected else 2
        py.draw.rect(screen, border_color, self.rect, border_width)
        
        # Draw image
        if self.img:
            screen.blit(self.img, (self.x, self.y))
        else:
            py.draw.rect(screen, (200, 200, 200), self.rect)
            
        # Draw name
        name_surface = font.render(self.name, True, (255, 255, 255))
        name_rect = name_surface.get_rect(centerx=self.x + self.size//2, top=self.y + self.size + 10)
        screen.blit(name_surface, name_rect)
        
    def is_clicked(self, pos):
        """Check if preview is clicked"""
        return self.rect.collidepoint(pos)


class Menu:
    """Main menu class"""
    def __init__(self):
        self.screen = py.display.set_mode((MENU_WIDTH, MENU_HEIGHT))
        py.display.set_caption("Game Menu - Select Your Character")
        self.clock = py.time.Clock()
        self.font_large = py.font.SysFont(None, 50)
        self.font_medium = py.font.SysFont(None, 35)
        self.font_small = py.font.SysFont(None, 25)
        
        # Character options - using available images from the repo
        self.characters = [
            CharacterPreview(80, 150, 100, 'smiler.png', 'Smiler'),
            CharacterPreview(220, 150, 100, 'Funkykong.webp', 'Funky'),
            CharacterPreview(360, 150, 100, 'taco.png', 'Taco'),
        ]
        
        self.selected_character = None
        self.selected_character_path = None
        
        # Play button
        self.play_button = MenuButton(
            MENU_WIDTH // 2 - BUTTON_WIDTH // 2,
            MENU_HEIGHT - 100,
            BUTTON_WIDTH,
            BUTTON_HEIGHT,
            "PLAY",
            color=(50, 150, 50),
            text_color=(255, 255, 255)
        )
        
    def handle_events(self):
        """Handle menu events"""
        for event in py.event.get():
            if event.type == py.QUIT:
                return False
                
            if event.type == py.MOUSEBUTTONDOWN:
                pos = py.mouse.get_pos()
                
                # Check character selection
                for i, character in enumerate(self.characters):
                    if character.is_clicked(pos):
                        # Deselect previous character
                        if self.selected_character is not None:
                            self.characters[self.selected_character].selected = False
                        
                        # Select new character
                        self.selected_character = i
                        character.selected = True
                        self.selected_character_path = character.img
                        
                # Check play button
                if self.play_button.is_clicked(pos):
                    if self.selected_character_path is not None:
                        return True  # Start game
                        
            if event.type == py.MOUSEMOTION:
                self.play_button.update_hover(py.mouse.get_pos())
                
        return None  # Continue menu
        
    def draw(self):
        """Draw the menu"""
        self.screen.fill((30, 30, 30))
        
        # Title
        title_surface = self.font_large.render("SELECT YOUR CHARACTER", True, (255, 255, 255))
        title_rect = title_surface.get_rect(centerx=MENU_WIDTH // 2, top=20)
        self.screen.blit(title_surface, title_rect)
        
        # Draw characters
        for character in self.characters:
            character.draw(self.screen, self.font_small)
            
        # Draw hint text
        hint_text = "Click a character to select" if self.selected_character is None else "Press PLAY to start!"
        hint_surface = self.font_small.render(hint_text, True, (200, 200, 200))
        hint_rect = hint_surface.get_rect(centerx=MENU_WIDTH // 2, top=280)
        self.screen.blit(hint_surface, hint_rect)
        
        # Draw play button
        self.play_button.draw(self.screen, self.font_medium)
        
        py.display.flip()
        
    def run(self):
        """Run the menu loop"""
        running = True
        while running:
            result = self.handle_events()
            
            if result is False:  # Quit
                py.quit()
                sys.exit()
            elif result is True:  # Play pressed
                return self.selected_character_path
                
            self.draw()
            self.clock.tick(60)


def show_menu():
    """Show the menu and return the selected character image"""
    menu = Menu()
    selected_img = menu.run()
    menu.screen = None  # Close the menu screen
    return selected_img
