from typing import List  # noqa: F401

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
import os

mod = "mod4"
terminal = "alacritty"

colors = [
    ['#ffffff', '#ffffff'],
    # ['#de4aff', '#de4aff'],  blue color
    # ['#ca1cff', '#ca1cff'],  purple color
    ['#ffaa3b', '#ffaa3b'],
    ['#9582ff', '#9582ff'],
    ['#000000', '#000000']
]

widget_defaults = dict(
    font='Ubuntu Bold',
    fontsize=12,
    padding=6,
)

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    Key([mod], "i", lazy.layout.grow()),
    Key([mod], "m", lazy.layout.shrink()),
    Key([mod], "n", lazy.layout.normalize()),
    Key([mod], "o", lazy.layout.maximize()),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

    #MENU
    Key([mod, "control"], "m", lazy.spawn('dmenu_run -i -fn "Ubuntu Bold-11" -nb ' + colors[3][0] + ' -sb ' + colors[1][0] + ' -nf ' + colors[0][0]),
        desc="Spawn a command using a prompt widget"),

    # SETTINGS
    # BRIGHTNESS
    Key([mod], "F5", lazy.spawn('xrandr --output eDP-1 --brightness 1'),
        desc="turn up brightness"),

    Key([mod], "F4", lazy.spawn('xrandr --output eDP-1 --brightness 0.8'),
        desc="turn down brightness"),

    # VOLUME
    Key([mod], "F11", lazy.spawn('pactl -- set-sink-volume 0 -2%'),
        desc="turn down volume"),

    Key([mod], "F12", lazy.spawn('pactl -- set-sink-volume 0 +2%'),
        desc="turn up volume"),

    Key([mod], "p", lazy.spawn('/home/jonathan/.config/qtile/scripts/power.sh'),
        desc="turn up volume")

]

groups = [
    Group('WWW', layout="Max", matches=[Match(wm_class=['Brave'])]),
    Group('TERM', layout="MonadTall", matches=[Match(wm_class=['alacritty'])]),
    Group('DEV', layout="MonadTall", matches=[Match(wm_class=['android-studio']), Match(wm_class=['code'])]),
    Group('MUS', layout="MonadTall", matches=[Match(wm_class=['spotify'])]),
    Group('TOOLS', layout="MonadTall")
]

for i in range(len(groups)):
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], str(i + 1), lazy.group[groups[i].name].toscreen(),
            desc="Switch to group {}".format(groups[i].name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], str(i + 1), lazy.window.togroup(groups[i].name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(groups[i].name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])


layouts = [
    layout.MonadTall(
        border_focus=colors[1][0],
        border_width=2,
        margin=4,
        single_margin=4,
        single_border_width=2
    ),
    layout.Max(),
    layout.Columns(border_focus_stack='#d75f5f'),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                # widget.CurrentLayout(),
                widget.GroupBox(
                    font='Ubuntu Bold',
                    fontsize = 10,
                    padding=5,
                    border_width=1,
                    active=colors[0],
                    inactive=colors[0],
                    foreground=colors[1],
                    this_current_screen_border=colors[1],
                    rounded=False,
                    highlight_method='block'
                ),
                widget.Prompt(),
                widget.WindowName(),
                widget.Systray(),
                widget.Battery(
                    background=colors[2],
                    font='Ubuntu Bold',
                    energy_now_file='charge_now',
                    update_interval=10
                ),
                widget.Clock(foreground=colors[0], background=colors[1], format='%Y-%m-%d %a %I:%M %p')
            ],
            20
        ),
    ),
    Screen(
        top=bar.Bar(
            [
                # widget.CurrentLayout(),
                widget.GroupBox(
                    font='Ubuntu Bold',
                    fontsize = 10,
                    padding=5,
                    border_width=1,
                    active=colors[0],
                    inactive=colors[0],
                    foreground=colors[1],
                    this_current_screen_border=colors[1],
                    rounded=False,
                    highlight_method='block'
                ),
                widget.Prompt(),
                widget.WindowName(),
                widget.Systray(),
                widget.Battery(
                    background=colors[2],
                    font='Ubuntu Bold',
                    energy_now_file='charge_now',
                    update_interval=10
                ),
                widget.Clock(foreground=colors[0], background=colors[1], format='%Y-%m-%d %a %I:%M %p')
            ],
            20
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
frame_opacity=0.8
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"


commands = [
    "setxbmap es",
    "feh --bg-fill /home/jonathan/Pictures/wallpapers/wallpaper10.jpg",
    "compton &"
]

for cmd in commands:
    os.system(cmd)

