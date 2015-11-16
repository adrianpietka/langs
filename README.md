# Future Of Development

Analysis of technology trends using information from GitHub repositories.

Live demo: [future-of-development.azurewebsites.net](http://future-of-development.azurewebsites.net)

## Technologies

Python 3.4 + Flask + MySQL

## How to run?

```
$: cd /path/to/project
$: python -m pip install -r requirements.txt
```

### Executing commands

```
$: cd /path/to/project
$: python console.py [command]
```

### How to run web application?

```
$: cd /path/to/project
$: python server.py
```

## Commands - List

```
prepare-database-sharding - Update index of repositories from GitHub *temp command - to remove after migration to new db schema*
github-index - Update index of repositories from GitHub
github-metadata - Update metadata for repositories (stars count, last push etc.)
```

## Web application - Access

[http://localhost:5555](http://localhost:5555)

## Web application - Endpoints

```
/ - UI Dashboard
/github/stats - Statistics - number of all repositories, latest repository etc.
/github/languages - List of all programming languages
/github/languages/stats - Number of all repositories per programming language
/github/new-repositories/monthly - Number of new repositories by programming language per month
/github/new-repositories/yearly - Number of new repositories by programming language per year
```