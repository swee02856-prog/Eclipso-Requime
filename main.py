import pygame
import sys
pygame.init()
clock = pygame.time.Clock()
# DAY 1
# Build player movement
# Make it so that player image goes left or right to movement
# Add shooting mechanic

# DAY 2
# Add Jumping system
# Add Test enemy
# Make the bullets damage

window = pygame.display.set_mode((1000, 600))
window.fill((0, 0, 0))
pygame.display.set_caption("Eclipso requime")

PlayerFrameLeft = pygame.image.load(("PlayerSpriteLeft.png")).convert_alpha()
PlayerFrameLeft = pygame.transform.scale(PlayerFrameLeft, (100, 100))
PlayerFrameRight = pygame.image.load(("PlayerSpriteRight.png")).convert_alpha()
PlayerFrameRight = pygame.transform.scale(PlayerFrameRight, (100, 100))

player_x = 300
player_y = 100
player_vel_x = 0
player_vel_y = 0

PlayerSide = ("Right") # List for current player direction

Bulletsprite = pygame.image.load(("Bullet.png")).convert_alpha()
Bulletsprite = pygame.transform.scale(Bulletsprite, (15, 15))

bullet_x = 0
bullet_y = 0
bullet_vel_x = 0
bullet_vel_y = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit(0)

        keys = pygame.key.get_pressed()
        # PLAYER MOVEMENT
        if keys[pygame.K_d]:
            player_vel_x = 5
            PlayerSide = ("Right")
        elif keys[pygame.K_a]:
            player_vel_x = -5
            PlayerSide = ("Left")
        else:
            player_vel_x = 0
        # GUN SYSTEM
        if event.type == pygame.MOUSEBUTTONDOWN:
            bullet_x = player_x # Bullet stays next to player so it
            bullet_y = player_y # dont spawn outside of the player
            if PlayerSide == ("Right"):
                window.blit(Bulletsprite, (bullet_x, bullet_y))
                bullet_vel_x = 15
            elif PlayerSide == ("Left"):
                window.blit(Bulletsprite, (bullet_x, bullet_y))
                bullet_vel_x = -15
    player_x += player_vel_x
    player_y += player_vel_y
    bullet_x += bullet_vel_x
    bullet_y += bullet_vel_y

    window.fill((0, 0, 0))
    window.blit(Bulletsprite, (bullet_x + 90, bullet_y + 45)) # BULLET PLACEMENT
    # PLAYER SPRITE DIRECTION CHANGE
    if PlayerSide == ("Right"):
        window.blit(PlayerFrameRight, (player_x, player_y))
    elif PlayerSide == ("Left"):
        window.blit(PlayerFrameLeft, (player_x, player_y))
    pygame.display.flip() # Need this for refreshing screen
    clock.tick(60) # Fps limit