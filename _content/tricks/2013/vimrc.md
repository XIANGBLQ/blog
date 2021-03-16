# Preferences for Vim

- date: 2013-09-23 23:16
- tags: linux, vim
- category: tricks

-----------------------------

These are settings that to improve usage of VI text editor for various purposes.


### 1. Whitespaces and indent

Copy & paste below lines to __*~/.vimrc*__:

```
set smartindent
set tabstop=4
set shiftwidth=4
set expandtab
set number
```

1. smartindent - Do smart autoindenting when starting a new line for C-like programs.
2. tabstop - Number of spaces that a <Tab> in the file counts for.
3. shiftwidth - Number of spaces to use for each step of (auto)indent.
4. expandtab - Spaces are used in indents with <Tab>.
5. number(nu) - Show line number

### 2. Color scheme

For color scheme preferences:

```
colorscheme torte
```

It is the default black/white scheme.


### 3. Markdown syntax support

For markdown syntax highlight, by default it supports only the ".markdown" extension but not ".md".

You can try this in VIM and get the correct syntax highlight:

```
:set syntax=markdown
```

So if you want it to support the ".md" file also, add this line to the ~/.vimrc:

```
au BufNewFile,BufFilePre,BufRead *.md set filetype=markdown
```

### 4. All kinds of tricks here

#### 4.1 Set fixed width to 80 columns, and soft wrap text automatically

```
:set columns=80
```

#### 4.2 Set preference according to File Type

The file type plugin for Vim can help you set preferences for a specific file type.

```
# Show detected file type
:echo &ft

# List Vim's file types and syntax definitions
:echo glob($VIMRUNTIME . '/ftplugin/*.vim')
:echo glob($VIMRUNTIME . '/syntax/*.vim')

# Check file type plugin status
:filetype

```

If the file type detection is wrong or not recognized, you can set the file type:

```
:set filetype=html
```

Now if you want to add customize settings according to file type, you can edit a file under `~/.vim/ftplugin/<filetype>.vim` where `<filetype>` should be replace by the defined file type. For example:

```
$ vi ~/.vim/ftplugin/html.vim
set ts=2
set sw=2
set expandtab

```





