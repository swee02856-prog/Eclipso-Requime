import pygame
import math
import sys
pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()
# DAY 1 -- Done
# Build player movement
# Make it so that player image goes left or right to movement
# Add shooting mechanic

# DAY 2 -- Done
# Add Jumping system
# Add Test enemy
# Make the bullets damage

# DAY 3 -- Done
# Add Title Screen
# Add Sound effects
# Add win screen
# Make boss attack back

# DAY 4 -- Done
# Make boss attack damage player
# Make boss move 
# Add barrier to prevent player from running out of screen
# Add cheering sound effect when player wins

# DAY 5 
# Make boss keep attacking until player dies or player kills boss
# Make boss actually move from left to right part  of the screen
# Add player recoil when shooting & effects

window = pygame.display.set_mode((1000, 600))
window.fill((0, 0, 0))
pygame.display.set_caption("Eclipso requime")

FONT = pygame.font.Font("augiepixel.ttf", 75)
GAMEWINFONT = pygame.font.Font("augiepixel.ttf", 90)

PlayButtonRect = pygame.Rect(400, 200, 150, 150) # Play button

Background = pygame.image.load(("Background.png")).convert_alpha()
Background = pygame.transform.scale(Background, (1000, 600))

TitleScreenBackground = pygame.image.load(("EclipsoRequimTitleBackground.png"))
TitleScreenBackground = pygame.transform.scale(TitleScreenBackground, (1000, 600))

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

BOSS_X = 600
BOSS_Y = 50
BOSS_VEL_X = 0
BOSS_VEL_Y = 0

BossHitbox = pygame.Rect(BOSS_X, BOSS_Y, 350, 350) # Boss hitbox 

Floor = pygame.surface.Surface((1000, 200))
Floor.fill((0, 0,0 ))

PlayerHealth = 150

PLAYER_X = 300
PLAYER_Y = 400
PLAYER_VEL_X = 0
PLAYER_VEL_Y = 0

PlayerHitbox = pygame.Rect(PLAYER_X, PLAYER_Y, 100, 100) # Player hitbox

# Jumping system stuff I copied off youtube
Y_GRAVITY = 1
JUMP_HEIGHT = 20
Y_VELOCITY = JUMP_HEIGHT
jumping = False
JumpSound = pygame.mixer.Sound("jumpsoundeffect.mp3")
JumpSound.set_volume(0.5)

PlayerSide = ("Right") # List for current player direction

Bulletsprite = pygame.image.load(("Bullet.png")).convert_alpha()
Bulletsprite = pygame.transform.scale(Bulletsprite, (15, 15))

BULLET_X = 0
BULLET_Y = 0
BULLET_VEL_X = 0
BULLET_VEL_Y = 0

BulletHitbox = pygame.Rect(BULLET_X, BULLET_Y, 25, 25) # Bullet hitbox
BulletShot = False
BulletDamage = 25

Orbsprite = pygame.image.load(("orbprojectile.png")).convert_alpha()
Orbsprite = pygame.transform.scale(Orbsprite, (100, 100))

ORBSPRITE_X = 0
ORBSPRITE_Y = 0
ORBSPRITE_VEL_X = -1
ORBSPRITE_VEL_Y = 0

ORBSPRITE_X += BOSS_X + 150
ORBSPRITE_Y += BOSS_Y + 150

OrbHitbox = pygame.Rect(ORBSPRITE_X, ORBSPRITE_Y, 110, 110)

ShootSound = pygame.mixer.Sound("shootsoundeffect.mp3")
ShootSound.set_volume(0.3)

FrameTime = pygame.time.get_ticks()
StartTime = pygame.time.get_ticks()
CurrentTime = 0

CurrentEvent = "TitleScreen"

while True:
    CurrentTime = pygame.time.get_ticks()
    BossHealthFloat = math.sin(CurrentTime * 0.005) * 10
    BossFloat = math.sin(CurrentTime * 0.002) * 7
    PlayerIdleFloat = math.sin(CurrentTime * 0.005) * 2
    if PLAYER_VEL_X != 0:
        PlayerIdleFloat = math.sin(CurrentTime * 0.01) * 4
    if CurrentTime - FrameTime >= 500:
        BossFrames.append(BossFrames.pop(0))
        FrameTime = CurrentTime
    for event in pygame.event.get():
        MousePosition = pygame.mouse.get_pos()
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
        if keys[pygame.K_w]:
            jumping = True
        # GUN SYSTEM
        if event.type == pygame.MOUSEBUTTONDOWN:
            BulletShot = True
            ShootSound.play()
            BULLET_X = PLAYER_X # Bullet stays next to player so it
            BULLET_Y = PLAYER_Y # dont spawn outside of the player
            if PlayerSide == ("Right"):
                window.blit(Bulletsprite, (BULLET_X, BULLET_Y))
                BULLET_VEL_X = 35
            elif PlayerSide == ("Left"):
                window.blit(Bulletsprite, (BULLET_X, BULLET_Y))
                BULLET_VEL_X = -35

    if jumping and CurrentEvent == "Playing": # Jumping system
        PLAYER_Y -= Y_VELOCITY
        Y_VELOCITY -= Y_GRAVITY
        if Y_VELOCITY < -JUMP_HEIGHT:
            JumpSound.play()
            jumping = False
            Y_VELOCITY = JUMP_HEIGHT
# BARRIER (Why does this actually work)
    if PLAYER_X < 0:
        PLAYER_X = 0
    if PLAYER_X > 900:
        PLAYER_X = 900

    PLAYER_X += PLAYER_VEL_X
    PLAYER_Y += PLAYER_VEL_Y
    PlayerHitbox.x = PLAYER_X
    PlayerHitbox.y = PLAYER_Y
    BULLET_X += BULLET_VEL_X
    BULLET_Y += BULLET_VEL_Y
    BulletHitbox.x = BULLET_X + 75
    BulletHitbox.y = BULLET_Y + 45
    BOSS_X += BOSS_VEL_X
    BOSS_Y += BOSS_VEL_Y
    BossHitbox.x = BOSS_X
    BossHitbox.y = BOSS_Y + BossFloat
    ORBSPRITE_X += ORBSPRITE_VEL_X
    ORBSPRITE_Y += ORBSPRITE_VEL_Y
    OrbHitbox.x = ORBSPRITE_X
    OrbHitbox.y = ORBSPRITE_Y


    # DRAW SPRITES AFTER THIS!!! Cuz i keep making the same dumb mistake
    window.blit(Background, (0, 0)) 
    if BulletShot == True:    
        window.blit(Bulletsprite, (BULLET_X + 75, BULLET_Y + 45)) # BULLET PLACEMENT
    if PlayerSide == ("Right"): # PLAYER SPRITE DIRECTION CHANGE
        window.blit(PlayerFrameRight, (PLAYER_X, PLAYER_Y + PlayerIdleFloat))
    elif PlayerSide == ("Left"):
        window.blit(PlayerFrameLeft, (PLAYER_X, PLAYER_Y + PlayerIdleFloat))
    if BulletShot == True and BulletHitbox.colliderect(BossHitbox):
        BulletShot = False  # Preventing boss from recieving more than 25 dmg per hit
        BossHealth -= BulletDamage
    if PlayerHitbox.colliderect(OrbHitbox):
        PlayerHealth -= 15
    if CurrentEvent == "TitleScreen":
        window.blit(TitleScreenBackground, (0, 0))
        PlayText = GAMEWINFONT.render("-play-", True, (0, 255, 251))
        window.blit(PlayText, (400, 200))
        if event.type == pygame.MOUSEBUTTONDOWN:
            if PlayButtonRect.collidepoint(MousePosition):
                CurrentEvent = "Playing"
    if CurrentEvent == "Playing":
        window.blit(Floor, (0, 500))
        window.blit(Orbsprite, (ORBSPRITE_X, ORBSPRITE_Y))
        BossHealthText = FONT.render(f"Boss Health: {BossHealth}", True, (255, 255, 255))
        PlayerHealthText = FONT.render(f"You got {PlayerHealth} left..", True, (255, 255, 255))
        window.blit(BossFrames[0], (BOSS_X, BOSS_Y + BossFloat))
        window.blit(BossHealthText, (50, 15 + BossHealthFloat))
        window.blit(PlayerHealthText, (50, 500 + BossHealthFloat))
        if BossHealth == 0:
            CurrentEvent = "Win"
    if CurrentEvent == "Win":
        WinText = GAMEWINFONT.render("You beat Verndastare!", True, (255, 255, 255))
        window.blit(WinText, (75, 300 + BossHealthFloat))

    pygame.display.flip() # Need this for refreshing screen
    clock.tick(60) # Fps limit cuz I keep forgetting