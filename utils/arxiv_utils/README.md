# arxiv_utils

- **fetch**: download arxiv paper pdf with url
- **sync**: collect and organize paper urls in markdown, automatically download pdfs and update markdown content

## Install

requirements: Python >= 3.9

```
git clone git@github.com:huxycn/arxiv_utils.git
cd arxiv_utils
pip install .
```

## Example

```
arxiver fetch https://arxiv.org/abs/1706.03762

arxiver sync ./tests/mds/test.md
```

## Rule

test.md
```
- {{https://arxiv.org/abs/1706.03762}}
- ResNet: {{https://arxiv.org/abs/1512.03385}}
```

pdf save name: first paper will use full title, second paper will use alias title -- "ResNet"


# Acknowledgements

- https://github.com/wilmerwang/autoLiterature
