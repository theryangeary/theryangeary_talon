from talon import Module, Context, actions
mod = Module()
ctx = Context()

@mod.action_class
class SlackCustomAction:
    def select_thread():
        """
        select the slack thread to expand
        """
        matches = actions.user.mouse_helper_find_template_relative("2022-03-28_16.53.46.088362.png")
        matches += actions.user.mouse_helper_find_template_relative("2022-03-28_16.45.54.321011.png")
        matches += actions.user.mouse_helper_find_template_relative("2022-03-28_17.03.11.561768.png")
        matches += actions.user.mouse_helper_find_template_relative("2022-03-29_09.04.34.025582.png")
        matches += actions.user.mouse_helper_find_template_relative("2022-03-31_11.16.01.650882.png")
        actions.user.marker_ui_show(matches)

    def focus_text_box():
        """select textbox"""
        matches = actions.user.mouse_helper_find_template_relative("2022-03-29_13.29.11.001187.png", -32, 2)
        actions.user.marker_ui_show(matches)
