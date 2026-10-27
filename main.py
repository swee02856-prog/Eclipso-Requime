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

BossFrame1 = pygame.image.load(("Monster1Frame1.png")).convert_alpha()
BossFrame1 = pygame.transform.scale(BossFrame1, (400, 400))
BossFrame2 = pygame.image.load(("Monster1Frame2.png")).convert_alpha()
BossFrame2 = pygame.transform.scale(BossFrame2, (400, 400))
BossFrame3 = pygame.image.load(("Monster1Frame3.png")).convert_alpha()
BossFrame3 = pygame.transform.scale(BossFrame3, (400, 400))

BossFrames = [BossFrame1, BossFrame2, BossFrame3]

BossHealth = 1000

PLAYER_X = 300
PLAYER_Y = 400
PLAYER_VEL_X = 0
PLAYER_VEL_Y = 0

# Jumping system stuff I copied off youtube
Y_GRAVITY = 1
JUMP_HEIGHT = 20
Y_VELOCITY = JUMP_HEIGHT
jumping = False

PlayerSide = ("Right") # List for current player direction

Bulletsprite = pygame.image.load(("Bullet.png")).convert_alpha()
Bulletsprite = pygame.transform.scale(Bulletsprite, (15, 15))

BULLET_X = 0
BULLET_Y = 0
BULLET_VEL_X = 0
BULLET_VEL_Y = 0

BULLET_DAMAGE = 25

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit(0)

        keys = pygame.key.get_pressed()
        # PLAYER MOVEMENT
        if keys[pygame.K_d]:
            PLAYER_VEL_X = 5
            PlayerSide = ("Right")
        elif keys[pygame.K_a]:
            PLAYER_VEL_X = -5
            PlayerSide = ("Left")
        else:
            PLAYER_VEL_X = 0

        if keys[pygame.K_SPACE]:
            jumping = True
        # GUN SYSTEM
        if event.type == pygame.MOUSEBUTTONDOWN:
            BULLET_X = PLAYER_X # Bullet stays next to player so it
            BULLET_Y = PLAYER_Y # dont spawn outside of the player
            if PlayerSide == ("Right"):
                window.blit(Bulletsprite, (BULLET_X, BULLET_Y))
                BULLET_VEL_X = 25
            elif PlayerSide == ("Left"):
                window.blit(Bulletsprite, (BULLET_X, BULLET_Y))
                BULLET_VEL_X = -25

    if jumping: # Jumping system
        PLAYER_Y -= Y_VELOCITY
        Y_VELOCITY -= Y_GRAVITY
        if Y_VELOCITY < -JUMP_HEIGHT:
            jumping = False
            Y_VELOCITY = JUMP_HEIGHT

    PLAYER_X += PLAYER_VEL_X
    PLAYER_Y += PLAYER_VEL_Y
    BULLET_X += BULLET_VEL_X
    BULLET_Y += BULLET_VEL_Y

    window.fill((0, 0, 0))
    window.blit(Bulletsprite, (BULLET_X + 75, BULLET_Y + 45)) # BULLET PLACEMENT
    # PLAYER SPRITE DIRECTION CHANGE
    if PlayerSide == ("Right"):
        window.blit(PlayerFrameRight, (PLAYER_X, PLAYER_Y))
    elif PlayerSide == ("Left"):
        window.blit(PlayerFrameLeft, (PLAYER_X, PLAYER_Y))
    window.blit(BossFrame1, (600, 300))
    pygame.display.flip() # Need this for refreshing screen
    clock.tick(60) # Fps limit