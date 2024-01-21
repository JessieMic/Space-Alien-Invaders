import sys
from time import sleep

import pygame

from data.settings import Settings
from data.ship import Ship
from data.bullet import Bullet
from data.alien import Alien
from data.stars import Stars
from random import randint
from data.game_stats import GameStats
from data.button import Button
from data.scoreboard import Scoreboard
from data.exit import Exit


class AlienInvasion:
    """Overall class to manage game assets and nehavior"""

    def __init__(self):
        """Initialize the game, and create game resources"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width,self.settings.screen_hight))
        pygame.display.set_caption("Alien Invasion")
        #Creating an instance to store game stats
        #Creating an instance to store game stats
        self.stats = GameStats(self)
        self.exit = Exit(self)
        self.sb = Scoreboard(self)
        self.ship = Ship(self)
        self.menu = 0
        self.difficulty = 0

        pygame.mixer.music.load(r'C:\Users\Jessi\Desktop\AI\data\game_music.wav')
        pygame.mixer.music.set_volume(1.0)
        pygame.mixer.music.play(-1)
        print(sys.version)
        self.clock = pygame.time.Clock()
        #Group creat list helps to draw each updated bullet throgh main loop
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.star_b = pygame.sprite.Group()

        self._create_fleet()
        self._first_stars()
        self._create_space()
        #Make the play button
        self.play_button = Button(self)
        self.play_button.main_mode()
        self.ship.full_heart()


    def run_game(self):
        """start the main loop for the game"""
        while True:
            self._check_events()
            self._update_stars()
            if self.stats.game_active:
                if not self.stats.game_exit:
                    self.ship.update()
                    self._update_bullets()
                    self._update_aliens()
            self.clock.tick(120)
            self._update_screen()





    def _update_bullets(self):
        """Update position of bullets and delete old"""
        #Update position
        self.bullets.update()
        # Get rid of old bullets
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Checks to see if there is a bullet collision with
        an alien, if so, removes both rects"""
        bullet_mode = True
        if self.settings.alien_speed > 7:
            bullet_mode = False
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens , bullet_mode, True)

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

            #If we write True then the key or the value will be deleted
        if not self.aliens:
            #If there isn't anymore aliens it will destroy all
            #bullets and call a new fleet
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            self.stats.level += 1
            self.sb.prep_level()

    def _update_aliens(self):
        """Check to see if fleet is on the edge,
        them update the positions of all aliens in the fleet."""
        self._check_fleet_edges()
        self.aliens.update()

        #Look for alien bullet collisions
        #Tloops runs until it finds a collision, then does the task
        if pygame.sprite.spritecollideany(self.ship , self.aliens):
            self._ship_hit()
        #Look for aliens hitting the bottom
        self._check_aliens_bottom()

    def _check_aliens_bottom(self):
        """Resents everything if an alien has reached the bottom"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break

    def _ship_hit(self):
        """Respond to the ship being hit by an alien"""
        if self.stats.ships_left > 1:
            #Decrement ships_left
            self.stats.ships_left -= 1

            #Get rid of any aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            #Create new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()

            #Pause
            sleep(0.5)
        else:
            self.stats.ships_left -= 1
            self.stats.game_active = False
            self.difficulty = 0
            pygame.mouse.set_visible(True)

    def _update_stars(self):
        self.star_b.update()
        for star in self.star_b:
            if len(self.star_b) < 20:
                if star.rect.y == 100 or star.rect.y == 700 or star.rect.y == 500:
                    self._create_space()
        for star in self.star_b.copy():
            if star.rect.top > 800:
                self.star_b.remove(star)

    def _check_fleet_edges(self):
        """Respond if alien has touched an edge"""
        for alien in self.aliens.sprites():
            #This will only work if the prog has detected that one of the
            #alien has reached his edge and returned true
            if alien.check_edges():
                self._change_fleet_direction()
                #We ask to get out of the loop once we change direction we want
                #the fleet to drop once and not endless amount of times
                break

    def _change_fleet_direction(self):
        """Drop the fleet and change direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        #We multiply the fleep direction value by -1 to change the dir
        self.settings.fleet_direction *= -1

    def  _create_fleet(self):
        """Create a feel of aliens"""
        #Creat an alien and find how many you can fit
        #Spacing between each alien is one alien width
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2*alien_width)
        number_aliens_x = available_space_x // (2*alien_width)

        #Determine the number of rows of aliens that fit on screen
        ship_height= self.ship.rect.height
        available_space_y = (self.settings.screen_hight -
                            (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2*alien_height)

        #Create full fleet of aliens.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x ):
                self._create_alien(alien_number, row_number)

    def _create_space(self):
        for star in range(1):
            self._create_stars()


    def _update_screen(self):
        # Redraw the screen during each pass through the loop
        self.screen.fill(self.settings.bg_color)
        self.star_b.draw(self.screen)
        self.ship.blitme()
        if self.stats.ships_left == 3:
            self.ship.full_heart()
            self.ship.show_heart()
        if self.stats.ships_left == 2:
            self.ship.two_heart()
            self.ship.show_heart()
        if self.stats.ships_left == 1:
            self.ship.one_heart()
            self.ship.show_heart()
        if self.stats.ships_left == 0:
            self.ship.zero_heart()
            self.ship.show_heart()
        # Draw stars at random places
        self.bullets.draw(self.screen)
        #When draw on a group,draws each element in po/(a surface to draw ele)
        self.aliens.draw(self.screen)
        #Drwa the play button if the game is inactivce
        if not self.stats.game_active:
            if self.difficulty == 0:
                self.play_button.main_mode()
                self.play_button.draw_button()
            if self.difficulty == 1:
                self.play_button.easy_mode()
                self.play_button.draw_button()
            if self.difficulty == 2:
                self.play_button.medium_mode()
                self.play_button.draw_button()
            if self.difficulty == 3:
                self.play_button.hard_mode()
                self.play_button.draw_button()

        self.sb.show_score()


        if self.stats.game_exit == True:
            self.exit.draw_exit()
        # Make the most recently drawn screen visible.
        pygame.display.flip()

    def _start_game(self):
        # Reset the game statistics
        self.stats.reset_stats()

        if self.difficulty == 1:
            self.settings.initialize_dynamic_settings_easy()
            self.play_button.easy_mode()
        if self.difficulty == 2:
            self.settings.initialize_dynamic_settings_medium()
            self.play_button.medium_mode()
        if self.difficulty == 3:
            self.settings.initialize_dynamic_settings_hard()
            self.play_button.hard_mode()


        self.stats.game_active = True
        self.sb.prep_score()
        self.sb.prep_level()

        # Hide mouse
        pygame.mouse.set_visible(False)

        # Get rid of any aliens and bullets
        self.aliens.empty()
        self.bullets.empty()

        # Create a new fleet and center the ship
        self._create_fleet()
        self.ship.center_ship()



    def _check_events(self):
        """Respond to key presses and mouse events"""
        #Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                with  open(r'C:\Users\Jessi\Desktop\AI\data\high_score.txt','w') as high_score:
                    self.stats.high_score = str(self.stats.high_score)
                    high_score.write(self.stats.high_score)
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.stats.game_active == False:
                    self._check_play_button(mouse_pos)
                elif self.stats.game_exit == True:
                    self._check_exit_button(mouse_pos)

    def _check_exit_button(self,mouse_pos):
        button_click = self.exit.rect.collidepoint(mouse_pos)
        if button_click and self.stats.game_exit == True:
            #Resume button
            if mouse_pos[0] >= 489 and mouse_pos[0] <= 708:
                if mouse_pos[1] >= 289 and mouse_pos[1] <= 340:
                    self.menu = 1
                    self._exit()

            #Replay button
            if mouse_pos[0] >= 489 and mouse_pos[0] <= 708:
                if mouse_pos[1] >= 371 and mouse_pos[1] <= 417:
                    self.menu = 2
                    self._exit()

            #Exit button
            if mouse_pos[0] >= 489 and mouse_pos[0] <= 708:
                if mouse_pos[1] >= 457 and mouse_pos[1] <= 500:
                    self.menu = 3
                    self._exit()

    def _check_play_button(self,mouse_pos):
        """Start new game when player clicks this area"""
        #If there is a collide then it will be True
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            #Easy mode
            if mouse_pos[0] >= 293 and mouse_pos[0] <= 466:
                if mouse_pos[1] >= 371 and mouse_pos[1] <= 420:
                    self.difficulty = 1


            #Mediume mode
            if mouse_pos[0] >= 498 and mouse_pos[0] <= 697:
                if mouse_pos[1] >= 371 and mouse_pos[1] <= 420:
                    self.difficulty = 2


            #Hard mode
            if mouse_pos[0] >= 734 and mouse_pos[0] <= 903:
                if mouse_pos[1] >= 371 and mouse_pos[1] <= 420:
                    self.difficulty = 3

            #Start button
            if mouse_pos[0] >= 512 and mouse_pos[0] <= 682:
                if mouse_pos[1] >= 524 and mouse_pos[1] <= 576:
                    if self.difficulty > 0:
                        self._start_game()

            mouse_pos = 0

    def _check_keydown_events(self, event):
        """Respond to key presses"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_RETURN and not self.stats.game_active:
            if self.difficulty > 0:
                self._start_game()
        elif event.key == pygame.K_ESCAPE:
            if self.stats.game_active:
                self._exit()
            if not self.stats.game_active:
                with  open('high_score.txt', 'w') as high_score:
                    self.stats.high_score = str(self.stats.high_score)
                    high_score.write(self.stats.high_score)
                sys.exit()
        #Evey time we press key it goes to fun that makes a new bullet
        #adds it to group that is like a list that goes through a loop
        #that asks to draw a bullet on the screen which keeps getting updated
        #if the while loop so the position changes
        elif event.key == pygame.K_SPACE and self.stats.game_active:
            if not self.stats.game_exit:
                effect = pygame.mixer.Sound(r'C:\Users\Jessi\Desktop\AI\data\pew.wav')
                pygame.mixer.music.set_volume(0.1)
                effect.play()

                self._fire_bullet()

    def _exit(self):
        self.stats.game_exit = True
        pygame.mouse.set_visible(True)
        if self.menu == 1:
            self.menu = 0
            pygame.mouse.set_visible(False)
            self.stats.game_exit = False

        if self.menu == 2:
            self.menu = 0
            self.stats.game_exit = False
            self.stats.reset_stats()
            self.difficulty = 0
            self.stats.game_active = False


        if self.menu == 3:
            with  open(r'C:\Users\Jessi\Desktop\AI\data\high_score.txt', 'w') as high_score:
                self.stats.high_score = str(self.stats.high_score)
                high_score.write(self.stats.high_score)
            sys.exit()


    def _check_keyup_events(self, event):
        """Responds to key releases"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to bullets group"""
        # Creates an instance of the class Bullet
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            # Adds the new bullet to the group by add()
            self.bullets.add(new_bullet)

    def _create_alien(self,alien_number,row_number):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _create_stars(self):
        """Creates stars and adds them to a group"""
        #We make a star instance and then we use the class Star
        #to fill in the info
        star = Stars(self)
        random_number_x = randint(0,1200)
        random_number_y = -320
        star.x = random_number_x
        star.y = random_number_y
        star.rect.x = star.x
        star.rect.y = star.y
        self.star_b.add(star)

    def _first_stars(self):
        """The first few strars that will be desplayed at the start"""
        for star_num in range(15):
            star = Stars(self)
            ran_num_x = randint(0,1200)
            ran_num_y = randint(0,800)
            star.x = ran_num_x
            star.y = ran_num_y
            star.rect.x = star.x
            star.rect.y = star.y
            self.star_b.add(star)

if __name__ == '__main__':
    #Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()




























