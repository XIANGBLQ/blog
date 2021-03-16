This web site is powered by the amazing static content generator [liquidluck](http://liquidluck.readthedocs.org/en/latest/)

In convention, all the posts are written down and organized under the below path:

    _content/   - for root level html pages
    _content/<year>/    - for posts

To generate site content, use the follow command:

```bash
$ ./_gen_site.sh
```

To preview the web site, use the following command:

```bash
$ ./_preview.sh
```

Create a page:
```bash
$ ./_newpage.sh
```


Template for a Markdown post(_scripts/templates/page.md):

```markdown
# Post Title

- date: 2013-01-01 21:30
- tags: linux, tutorial
- category: tricks

-----------------------------

Post body...

```
