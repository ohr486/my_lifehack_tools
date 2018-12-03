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

## serverless

### setup

```bash
$ npm install serverless -g
$ npm install serverless-python-requirements -g
$ npm install serverless-domain-manager -g
```

### create domain

```bash
$ sls create_domain --stage=develop --profile=my-sls
```

### deploy lambda

```bash
$ sls deploy --stage=develop --profile=my-sls
```
