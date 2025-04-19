import pygame
import random
import psycopg2

conn = psycopg2.connect(
    dbname="snake_game",
    user="postgres",
    password="paradise",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

def show_scores():
    print("\n Leaderboard:")
    cur.execute('SELECT nickname, score FROM user_score ORDER BY score DESC')
    rows = cur.fetchall()
    for idx, (name, sc) in enumerate(rows, 1):
        print(f"{idx}. {name} — {sc}")

def play_game(username, score):
    pygame.init()
    width, height = 600, 400
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Snake Game')
    clock = pygame.time.Clock()
    font = pygame.font.SysFont('Arial', 24)

    snake_pos = [100, 50]
    snake_body = [[100, 50], [90, 50], [80, 50]]
    direction = 'RIGHT'
    change_to = direction

    food_pos = [random.randrange(1, width // 10) * 10, random.randrange(1, height // 10) * 10]
    food_spawn = True

    level = min(1 + score // 3, 5)
    speed = 10 + (level - 1) * 3
    food_eaten = score % 3
    color_value = 0
    paused = False
    game_over = False

    def show_score():
        score_surface = font.render(f'Score: {score} Level: {level}', True, (0, 0, 0))
        screen.blit(score_surface, [10, 10])

    def draw_walls(level):
        if level >= 2:
            pygame.draw.rect(screen, (100, 100, 100), pygame.Rect(200, 100, 10, 200))
        if level >= 4:
            pygame.draw.rect(screen, (100, 100, 100), pygame.Rect(400, 0, 10, 300))

    def check_collision_with_walls(pos, level):
        if level >= 2 and 200 <= pos[0] <= 210 and 100 <= pos[1] <= 300:
            return True
        if level >= 4 and 400 <= pos[0] <= 410 and 0 <= pos[1] <= 300:
            return True
        return False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return 'exit'
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = not paused
                    if paused:
                        cur.execute('UPDATE user_score SET score = %s WHERE nickname = %s', (score, username))
                        conn.commit()
                        print("⏸ Paused and saved.")
                    else:
                        print("▶️ Resumed.")
                elif not paused:
                    if event.key == pygame.K_UP and direction != 'DOWN':
                        change_to = 'UP'
                    elif event.key == pygame.K_DOWN and direction != 'UP':
                        change_to = 'DOWN'
                    elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                        change_to = 'LEFT'
                    elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                        change_to = 'RIGHT'

        if paused:
            continue

        direction = change_to
        if direction == 'UP':
            snake_pos[1] -= 10
        elif direction == 'DOWN':
            snake_pos[1] += 10
        elif direction == 'LEFT':
            snake_pos[0] -= 10
        elif direction == 'RIGHT':
            snake_pos[0] += 10

        if (
            snake_pos[0] < 0 or snake_pos[0] >= width or
            snake_pos[1] < 0 or snake_pos[1] >= height or
            snake_pos in snake_body[1:] or
            check_collision_with_walls(snake_pos, level)
        ):
            game_over = True
            break

        snake_body.insert(0, list(snake_pos))

        if snake_pos == food_pos:
            score += 1
            food_eaten += 1
            food_spawn = False
            color_value += 100
        else:
            snake_body.pop()

        if not food_spawn:
            food_pos = [random.randrange(1, width // 10) * 10, random.randrange(1, height // 10) * 10]
            while food_pos in snake_body:
                food_pos = [random.randrange(1, width // 10) * 10, random.randrange(1, height // 10) * 10]
            food_spawn = True

        if food_eaten >= 3:
            level = min(1 + score // 3, 5)
            speed = 10 + (level - 1) * 3
            food_eaten = 0

        screen.fill((255, 255, 255))
        draw_walls(level)

        for pos in snake_body:
            pygame.draw.rect(screen, (0, color_value % 256, 0), pygame.Rect(pos[0], pos[1], 10, 10))

        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(food_pos[0], food_pos[1], 10, 10))
        show_score()
        pygame.display.flip()
        clock.tick(speed)

    cur.execute('UPDATE user_score SET score = %s WHERE nickname = %s', (score, username))
    conn.commit()
    print(f"💀 Game Over! Final Score: {score}")
    pygame.quit()
    return 'menu'

# --- Главное меню ---
def main_menu():
    while True:
        print("\n Main Menu:")
        print("1. Login and Play")
        print("2. Show Leaderboard")
        print("0. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            username = input("Enter username: ").strip()
            cur.execute('SELECT score FROM user_score WHERE nickname = %s', (username,))
            row = cur.fetchone()
            if row:
                score = row[0]
                print(f"Welcome back, {username}! Current score: {score}")
            else:
                score = 0
                cur.execute('INSERT INTO user_score (nickname, score) VALUES (%s, %s)', (username, score))
                conn.commit()
                print(f"🆕 New user {username} created.")

            result = play_game(username, score)
            if result == 'exit':
                break

        elif choice == "2":
            show_scores()

        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

    cur.close()
    conn.close()
main_menu()