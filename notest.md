1. Git

git init

`echo ./idea > .gitignore`
`touch .gitignore`
.ignore
- .idea/
- *.pyc #cash

git add - A # add all
git commit -m "text"

#zdalne repo - polaczenie z lokalnego ze zdalnym
git remote add origin sciezka_do_repo_na_git_hub
git push -u origin master #-u = set up stream

git diff hash_commita #zmiany 
git log --onelie #historia zmian
git rollback #cofniecie zmiany do ostatniego commita
git checkout sciezka_do_pliku# przełaczenie się na  wersje po pliku z ostatniego commita
git revert hash_commita #wycofanie danego  commita
