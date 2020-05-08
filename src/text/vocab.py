from osprey.voice import Context, insert

vocab_list = [
    'callable',
    'cardioid',
    'changelog',
    'config',
    'Erlang',
    'formatter',
    'git',
    'GitLab',
    'gitter',
    'grep',
    'json',
    'Kaldi',
    'kinesis',
    'Neovim',
    'prepend',
    'readd',
    'refactor',
    'struct',
    'structs',
    'subprocess',
    'subprocesses',
    'sudo',
    'tendon',
    'tendons',
    'tendonitis',
    'tig',
    'TypeScript',
    'Vim',
    'vocab',
]

ctx = Context('vocab')
ctx.set_commands({
    'vocab <vocab>': lambda m: insert(m['vocab']),
    'vocab lower <vocab>': lambda m: insert(m['vocab'].lower()),
    'vocab upper <vocab>': lambda m: insert(m['vocab'].capitalize()),
})
ctx.set_choices({
    'vocab': vocab_list,
})
