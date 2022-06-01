os: mac
app: slack
-
unread: key(alt-shift-down)

open thread:
    user.select_thread()

focus text:
    user.focus_text_box()

view message:
    matches = user.mouse_helper_find_template_relative("2022-03-29_09.02.43.999932.png")
    user.marker_ui_show(matches)

open [direct] message:
    bounding_rectangle = user.mouse_helper_calculate_relative_rect("280.0 174.0 314.0 -19.0", "active_window")
    user.mouse_helper_blob_picker(bounding_rectangle)

open (pr|code review):
    matches = user.mouse_helper_find_template_relative("2022-03-29_09.43.10.615165.png", 22, 4)
    user.marker_ui_show(matches)

load new messages:
    user.mouse_helper_position_save()
    user.mouse_helper_move_image_relative("2022-03-29_13.26.34.690914.png", 0)
    sleep(0.05)
    mouse_click(0)
    sleep(0.05)
    user.mouse_helper_position_restore()
