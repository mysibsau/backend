from re import sub


def replace_vk_links_on_markdown(text: str) -> str:
    mask = r'(\[((id|club)\d+)\|([a-zA-Zа-яА-Я0-9 ]+)\])'
    repl = r'(https://vk.com/\2)[\4]'

    return sub(mask, repl, text)
