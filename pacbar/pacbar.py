# -*- coding: utf-8 -*-
from colorama import Fore, Style

import click

pacbar_char_index = 0


def pacbar(*arg, **kwargs):
    from click._termui_impl import ProgressBar

    class _PatchedProgressbar(ProgressBar):

        @property
        def fill_char(cls):
            global pacbar_char_index

            pacman_opened = Fore.YELLOW + Style.BRIGHT + 'C' + Fore.RESET + Style.RESET_ALL
            pacman_closed = Fore.YELLOW + Style.BRIGHT + 'c' + Fore.RESET + Style.RESET_ALL
            pacbar_char_index = (pacbar_char_index + 1) % 2

            if pacbar_char_index == 1:
                return f'\b {pacman_opened}'
            else:
                return f'\b {pacman_closed}'

    bar = click.progressbar(
        bar_template='%(label)s %(bar)s %(info)s',
        empty_char=Style.BRIGHT + '•' + Style.RESET_ALL,
        *arg, **kwargs
    )
    bar.__class__ = _PatchedProgressbar

    return bar
