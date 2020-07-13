1. Git

git init

`echo .idea/ > .gitignore`
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
git checkout hash_commitu #przelaczymy sie do stanu z tego commita

2. Metody dunder

pycharm > jak stajemy na argumencie klasy Alt + Enter tworzy selfa w konstruktorze.

metody dander zwracja dane wartosci jezeli sa deklarowane w klasie.
jak zawolamy dana metode na instacji obiektu to bedzie zwracane

__repr__ oficjalna reprezentacja tekstowa, jezlei nie ma w klasie __str__ to python wywola __repr__ jako domyslnie.
__int__ jak mamy zdefinowane w klasie to jak zawolamy int(instacja_klasy) to zwruci liczbe z deklaraci. 
tak samo dla float __float__
__len__ zwraca liczbe calkowita dlugosci
__bool__ zwaca true lub false  >> jezeli nie ma to zwrac __len__ jak 0 to false
jezlei nie ma bool anie len to zwarsze zwruci true z instancji poprzez wwolanie np print(bool(school))
__add__ +, __sub__ -, __mul__ *, __truediv__ /
trzeba przekazac do tej metody parametry np __add__(self, other) > self.cos + other
__class__ 
- metody porównania

`== __eq__`
`!= __ne__`
`< __lt__`
`<= __le__`
`> __gt__`
`>= __ge__`

jezeli porownamy == dwie instacje ktore nie sa w kalsie > __eq__ zadeklarowane to
python bedzie porownywal nie jakow artosci tylko jako obiekty w pamieci bedzie pokazywal ze 100==100 daje False
