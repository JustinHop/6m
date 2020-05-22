# 6m
*Mini MultiMedia Multiplexing Menu Maker*


Run 6m tray to run a system tray app that allows you to choose from programs
you set up to run multimedia commands.


I use a bunch of different media players on several systems. I keep my window
manager bindings the same, and keep my media controls the same while switching
between as many programs or scripts as I want. I suggest adding it to your
desktop startup.


Look at the yaml file, it should make sense


>   Usage: 6m [OPTIONS] COMMAND [ARGS]...
>
>   Options:
>     -l, --loglevel [debug|warn|info|error]
>                                     Logging level  [default: info]
>     --help                          Show this message and exit.
>
>   Commands:
>     add      Execute add command
>     list     List available players
>     next     Execute next command
>     pause    Execute pause command
>     play     Execute play command
>     prev     Execute prev command
>     set      Sets player, Stateful
>     status   Execute status command
>     stop     Execute stop command
>     toggle   Execute toggle command
>     tray     Runs the system tray selector
>     voldown  Execute voldown command
>     volup    Execute volup command

