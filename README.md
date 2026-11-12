Kom godt i gang med Snake i Pygame
1. Introduktion
I denne guide gennemgår vi de vigtigste dele af et Snake-spil lavet med Python og Pygame.

Vi kommer ind på, hvordan man opretter spillet, styrer slangen, laver mad, registrerer kollisioner og håndterer Game Over.
2. Import af biblioteker
Først importerer vi de biblioteker, vi skal bruge.

```python
import pygame
from sys import exit
import random
```
- pygame bruges til at lave selve spillet.
- sys bruges til at afslutte programmet.
- random bruges til tilfældige placeringer af maden.
3. Spillets størrelse
Vi bestemmer størrelsen på spillet ved at bruge rækker, kolonner og størrelsen på hvert felt.

```python
ROWS = 25
COLUMNS = ROWS
TILE_SIZE = 25

GAME_WIDTH = TILE_SIZE * COLUMNS
GAME_HEIGHT = TILE_SIZE * ROWS
```

Spillet bliver 625 × 625 pixels. Ved at bruge TILE_SIZE sikrer vi, at slangen altid bevæger sig ét felt ad gangen.
4. Oprettelse af spilvinduet
Nu opretter vi selve spilvinduet.

```python
pygame.init()

window = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
pygame.display.set_caption("Snake")

clock = pygame.time.Clock()
```

pygame.init() starter Pygame, mens set_mode() opretter vinduet. clock bruges til at styre spillets hastighed.
5. Slangen og maden
Slangen oprettes som en liste, hvor hver kropsdel er et rektangel.

```python
snake = []

snake.append(
    pygame.Rect(100, 100, TILE_SIZE, TILE_SIZE)
)
```

Maden får en tilfældig placering ved hjælp af denne funktion:

```python
def get_random(limit):
    return random.randint(0, limit - 1) * TILE_SIZE
```

Vi ganger med TILE_SIZE, så maden altid placeres korrekt på spillebanens felter.
6. Styring af slangen
Vi bruger tastaturets KEYDOWN-event til at registrere spillerens input.

```python
if event.key in (pygame.K_UP, pygame.K_w):
    if snake_velocity != (0, TILE_SIZE):
        snake_velocity = (0, -TILE_SIZE)
```

Her bevæger slangen sig opad, hvis den ikke allerede bevæger sig nedad.

Vi bruger samme princip til de andre retninger. Det forhindrer slangen i at vende direkte om og ramme sig selv.
7. Bevægelse af slangen
For at få slangens krop til at følge hovedet bruger vi et for-loop.

```python
for i in range(len(snake) - 1, 0, -1):
    snake[i] = snake[i - 1].copy()

snake[0].move_ip(snake_velocity)
```

Vi starter bagfra i listen, så hver kropsdel får den tidligere kropsdels position.

Til sidst flytter vi hovedet med move_ip().
8. Mad og score
Når slangens hoved rammer maden, skal slangen vokse.

```python
if snake[0].center == food.center:
    snake.append(old_tail)
```

Vi tilføjer en ny kropsdel ved at bruge append().

Vi kan også bruge slangens længde til at vise spillerens score:

```python
counter_text = font.render(
    f"Count: {len(snake) - 1}",
    True,
    "white"
)
window.blit(counter_text, (10, 10))
```

len(snake) finder slangens længde, og window.blit() viser teksten på skærmen.
9. Kollisioner
Vi skal registrere, hvis slangen rammer væggene eller sin egen krop.

Kollision med væggen:

```python
if not window.get_rect().contains(snake[0]):
    GAME_OVER = True
```

Kollision med sig selv:

```python
for part in snake[1:]:
    if snake[0].colliderect(part):
        GAME_OVER = True
```

Hvis en af kollisionerne sker, bliver GAME_OVER sat til True, og spillet slutter.
10. Game Over og Retry
Når spilleren taber, viser vi en Game Over-skærm og en Retry-knap.

```python
lose_text = font.render("YOU LOSE", True, "white")
lose_rect = lose_text.get_rect(
    center=(GAME_WIDTH // 2, 200)
)

window.blit(lose_text, lose_rect)
```

Vi registrerer et klik på Retry-knappen med:

```python
if GAME_OVER and event.type == pygame.MOUSEBUTTONDOWN:
    if retry_button.collidepoint(event.pos):
        reset_game()
```

collidepoint() undersøger, om musen er placeret inden for knappen. Hvis den er, starter vi spillet forfra med reset_game().
11. Spillets hastighed
Til sidst bestemmer vi, hvor hurtigt spillet opdateres.

```python
clock.tick(15)
```

Tallet bestemmer spillets maksimale opdateringer pr. sekund. Jo højere tallet er, desto hurtigere bevæger slangen sig.