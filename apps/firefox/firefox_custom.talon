app: firefox
-

last six hours:
    user.mouse_helper_position_save()
    user.mouse_helper_move_image_relative("2022-03-29_16.16.00.858270.png", 0)
    sleep(0.05)
    mouse_click(0)
    sleep(0.05)
    user.mouse_helper_position_restore()

convert to issue:
    user.mouse_helper_position_save()
    user.mouse_helper_move_image_relative("2022-03-29_17.01.11.730606.png", 0)
    sleep(0.05)
    mouse_click(0)
    sleep(0.05)
    user.mouse_helper_position_restore()

go link:
    key(cmd-t)
    key(g)
    key(o)
    key(space)

