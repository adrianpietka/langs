# Future Of Development

Technology Trends

Live demo: [future-of-development.azurewebsites.net](http://future-of-development.azurewebsites.net)

## Technologies

Python 3.4 + Flask + MySQL

## How to run?

```
$: cd /path/to/project
$: python -m pip install -r requirements.txt
```

### How to run Jobs?

```
$: cd /path/to/project
$: python executejob.py [job_name]
```

### How to run API?

```
$: cd /path/to/project
$: python runserver.py
```

## Jobs - List

```
github-index - Update index of repositories from GitHub
github-metadata - Update metadata for repositories (stars count, last push etc.)
```

## API - Access

[http://localhost:5555](http://localhost:5555)

## API - Endpoints

```
/ - Hello World!
/github/languages - Number of all repositories per programming language
/github/new-repositories - Number of new repositories by programming language and date
```

## Sources of information

- [x] GitHub
- [ ] Twitter
- [ ] StackOverflow