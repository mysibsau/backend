from re import sub, findall


def replace_vk_links_on_markdown(text: str) -> str:
    mask = r'(\[((id|club)\d+)\|(.+)\])'
    repl = r'[\4](https://vk.com/\2)'

    return sub(mask, repl, text)


def from_tags_to_links(text: str) -> str:
    mask = r'(#(\w+))'
    repl = r'[\1](https://vk.com/feed?c%5Bq%5D=%23\2&section=search)'

    return sub(mask, repl, text)
