import pygame
import random
import sys
import time
import json
import os

pygame.init()
pygame.mixer.init()

# 游戏设置
WIDTH, HEIGHT = 600, 400
BLOCK_SIZE = 20
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("贪吃蛇完整版")
CLOCK = pygame.time.Clock()
FONT = pygame.font.SysFont(None, 36)

# 颜色定义
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN_HEAD = (0, 200, 0)
GRID_COLOR = (200, 200, 200)
PAUSE_OVERLAY_COLOR = (255, 255, 255, 180)
TOOLTIP_COLOR = (255, 50, 50)

# 文件保存最高分路径
HIGH_SCORE_FILE = "highscore.json"

# 音效加载
try:
    pygame.mixer.music.load("background.mp3")
    pygame.mixer.music.play(-1)
    eat_sound = pygame.mixer.Sound("eat.wav")
    speedup_sound = pygame.mixer.Sound("speedup.wav")
    slowdown_sound = pygame.mixer.Sound("slowdown.wav")
except Exception:
    print("音频文件未找到，跳过声音加载。")
    eat_sound = speedup_sound = slowdown_sound = None

# 方向映射（单位格方向）
DIRECTIONS = {
    pygame.K_UP: (0, -1),
    pygame.K_w: (0, -1),
    pygame.K_DOWN: (0, 1),
    pygame.K_s: (0, 1),
    pygame.K_LEFT: (-1, 0),
    pygame.K_a: (-1, 0),
    pygame.K_RIGHT: (1, 0),
    pygame.K_d: (1, 0)
}

def load_highscore():
    if os.path.exists(HIGH_SCORE_FILE):
        with open(HIGH_SCORE_FILE, "r") as f:
            return json.load(f).get("highscore", 0)
    return 0

def save_highscore(score):
    with open(HIGH_SCORE_FILE, "w") as f:
        json.dump({"highscore": score}, f)

def random_color():
    return random.choice([
        (255, 0, 0), (255, 128, 0), (255, 255, 0),
        (0, 255, 0), (0, 255, 255), (0, 128, 255),
        (255, 0, 255)
    ])

def generate_food(snake, special=False, max_attempts=1000):
    for _ in range(max_attempts):
        pos = (random.randint(0, (WIDTH // BLOCK_SIZE) - 1),
               random.randint(0, (HEIGHT // BLOCK_SIZE) - 1))
        pixel_pos = (pos[0] * BLOCK_SIZE, pos[1] * BLOCK_SIZE)
        if pixel_pos not in snake:
            if special:
                # 道具颜色区分食物
                color = (255, 105, 180)  # 粉色作为加减速道具颜色
            else:
                color = random_color()
            return pixel_pos, color
    raise RuntimeError("无法生成食物或道具，蛇占满屏幕")

def draw_rect(color, pos):
    pygame.draw.rect(SCREEN, color, (*pos, BLOCK_SIZE, BLOCK_SIZE))

def draw_grid():
    for x in range(0, WIDTH, BLOCK_SIZE):
        pygame.draw.line(SCREEN, GRID_COLOR, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, BLOCK_SIZE):
        pygame.draw.line(SCREEN, GRID_COLOR, (0, y), (WIDTH, y))

def draw_snake(snake, interp_pos):
    # 蛇头颜色固定绿色，身体渐变色
    head_pos = interp_pos
    pygame.draw.rect(SCREEN, GREEN_HEAD, (*head_pos, BLOCK_SIZE, BLOCK_SIZE))
    for i, segment in enumerate(snake[1:], start=1):
        ratio = i / len(snake)
        color = (int(0 * (1-ratio) + 0 * ratio),
                 int(200 * (1-ratio) + 255 * ratio),
                 int(0 * (1-ratio) + 0 * ratio))
        pygame.draw.rect(SCREEN, color, (*segment, BLOCK_SIZE, BLOCK_SIZE))

def show_score(score, highscore, elapsed):
    score_surf = FONT.render(f"分数: {score}  最高分: {highscore}  时间: {int(elapsed)}s", True, BLACK)
    SCREEN.blit(score_surf, (10, 10))

def pause_screen():
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill(PAUSE_OVERLAY_COLOR)
    SCREEN.blit(overlay, (0, 0))
    pause_text = FONT.render("游戏已暂停，按空格继续", True, TOOLTIP_COLOR)
    SCREEN.blit(pause_text, (WIDTH // 2 - pause_text.get_width() // 2, HEIGHT // 2))
    pygame.display.flip()

def handle_event_input(current_dir, event):
    if event.type == pygame.KEYDOWN and event.key in DIRECTIONS:
        new_dir = DIRECTIONS[event.key]
        if (new_dir[0] != -current_dir[0] or new_dir[1] != -current_dir[1]):
            return new_dir
    return current_dir

def is_collision(head, snake):
    x, y = head
    return (
        x < 0 or x >= WIDTH or
        y < 0 or y >= HEIGHT or
        head in snake[1:]
    )

def move_head(head, direction):
    return (head[0] + direction[0] * BLOCK_SIZE, head[1] + direction[1] * BLOCK_SIZE)

def game_over(score, highscore):
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((255, 255, 255, 220))
    SCREEN.blit(overlay, (0, 0))

    big_font = pygame.font.SysFont(None, 70)
    small_font = pygame.font.SysFont(None, 40)

    title = big_font.render("游戏结束", True, RED)
    final_score = small_font.render(f"你的分数: {score}", True, BLACK)
    best_score = small_font.render(f"最高分: {highscore}", True, BLACK)
    tip = small_font.render("按 R 重新开始，按 Q 退出", True, BLACK)

    SCREEN.blit(title, (WIDTH//2 - title.get_width()//2, HEIGHT//2 - 120))
    SCREEN.blit(final_score, (WIDTH//2 - final_score.get_width()//2, HEIGHT//2 - 50))
    SCREEN.blit(best_score, (WIDTH//2 - best_score.get_width()//2, HEIGHT//2))
    SCREEN.blit(tip, (WIDTH//2 - tip.get_width()//2, HEIGHT//2 + 70))
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    game()
                    return
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

def choose_difficulty():
    prompt = FONT.render("按数字键选择难度：1-慢，2-中，3-快", True, BLACK)
    SCREEN.fill(WHITE)
    SCREEN.blit(prompt, (WIDTH // 2 - prompt.get_width() // 2, HEIGHT // 2))
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return 5
                elif event.key == pygame.K_2:
                    return 10
                elif event.key == pygame.K_3:
                    return 15

def pause_game():
    pause_screen()
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                paused = False

def game():
    highscore = load_highscore()
    FPS_BASE = choose_difficulty()

    snake = [(100, 100)]
    direction = (1, 0)  # 方向单位格数
    food, food_color = generate_food(snake)
    # 道具加速或减速控制
    special_item = None
    special_item_color = None
    special_item_timer = 0
    special_effect_duration = 200  # 持续帧数
    speed_modifier = 0

    score = 0
    start_time = time.time()

    # 平滑移动控制
    moving_steps = 0
    move_delay = max(1, (FPS_BASE * 3))  # 控制移动的帧数周期

    running = True
    while running:
        SCREEN.fill(WHITE)
        draw_grid()

        elapsed_time = time.time() - start_time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pause_game()
                else:
                    direction = handle_event_input(direction, event)

        moving_steps += 1
        adjusted_delay = max(1, int(move_delay / (1 + speed_modifier)))
        if moving_steps >= adjusted_delay:
            moving_steps = 0
            new_head = move_head(snake[0], direction)
            if is_collision(new_head, snake):
                if score > highscore:
                    save_highscore(score)
                    highscore = score
                game_over(score, highscore)
                return

            snake.insert(0, new_head)
            if special_item and new_head == special_item:
                special_item_timer = special_effect_duration
                speed_modifier = random.choice([0.5, -0.5])
                if speed_modifier > 0 and speedup_sound:
                    speedup_sound.play()
                elif speed_modifier < 0 and slowdown_sound:
                    slowdown_sound.play()
                special_item = None
                special_item_color = None
            elif new_head == food:
                score += 1
                if eat_sound:
                    eat_sound.play()
                food, food_color = generate_food(snake)
                # 10%概率生成道具
                if special_item is None and random.random() < 0.1:
                    special_item, special_item_color = generate_food(snake, special=True)
            else:
                snake.pop()

        interp_ratio = moving_steps / adjusted_delay
        head_x = snake[1][0] + (snake[0][0] - snake[1][0]) * interp_ratio if len(snake) > 1 else snake[0][0]
        head_y = snake[1][1] + (snake[0][1] - snake[1][1]) * interp_ratio if len(snake) > 1 else snake[0][1]
        interp_head_pos = (head_x, head_y)

        if special_item_timer > 0:
            special_item_timer -= 1
            if special_item_timer == 0:
                speed_modifier = 0

        draw_rect(food_color, food)
        if special_item:
            draw_rect(special_item_color, special_item)

        draw_snake(snake, interp_head_pos)
        show_score(score, highscore, elapsed_time)

        pygame.display.flip()
        CLOCK.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    game()
