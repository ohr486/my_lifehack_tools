# my\_lifehack\_tools
lifehack tools

## how to add lambda func

```bash
$ virtualenv tmp/lambda-env
$ source tmp/lambda-env/bin/activate
$ mkdir tmp/func-xxx
$ cd tmp/func-xxx
$ vi func.py
$ pip install requests -t .
$ zip -r package.zip *
```

## how to deploy to heroku

```bash
$ git subtree push --prefix bot/ heroku master
```
