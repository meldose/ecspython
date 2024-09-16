import raylibpy as ry

# Initialize window
ry.init_window(800, 600, b"Move the square")
player_pos = [400, 300]
player_speed = 5

ry.set_target_fps(60)

while not ry.window_should_close():
    # Input handling
    if ry.is_key_down(ry.KEY_RIGHT): player_pos[0] += player_speed
    if ry.is_key_down(ry.KEY_LEFT): player_pos[0] -= player_speed
    if ry.is_key_down(ry.KEY_UP): player_pos[1] -= player_speed
    if ry.is_key_down(ry.KEY_DOWN): player_pos[1] += player_speed

    # Drawing the player
    ry.begin_drawing()
    ry.clear_background(ry.RAYWHITE)
    ry.draw_rectangle(player_pos[0], player_pos[1], 50, 50, ry.RED)
    ry.end_drawing()

ry.close_window()
