<h1>RoltonLang</h1>

<p>RoltonLang - безлексерный динамически типизированный процедурно-функциональный язык программирования с python-like синтаксисом </p>

<h2>Как установить</h2>

1. Скачайте ZIP-архив репозитория, EXE-файл в релизах или же выполните команду в командной оболочке:

```bash/cmd
git clone "https://github.com/KirillMos1/RoltonLang.git"
```

2. Если вы на Windows, то

3. Запустите EXE-файл, или

4. В CMD выполните команду:

```cmd
python <путь до файла .py> <путь до файла .rolton, необязательно>
```

(обязательно разархивируйте ZIP-архив!)

2. Если вы на UNIX-подобных системах (Linux/MacOS):

3. Разархивируйте ZIP-архив

4. Выполните команду

```bash
python3 <путь до файла .py> <путь до файла .rolton, необязательно>
```

<h2>Советы для автоматизации запуска файлов .rolton и вообще запуска RoltonLang</h2>

<h3>Windows</h3>
1. Введите в поиск в меню управления (кнопка Win) строку "Изменение переменн"

2. Выберите пункт "Изменение системных переменных среды"
  
3. Выберите "Переменные среды"
  
4. Выберите Path в "Переменных среды для _name_" (_name_ - имя пользователя в системе)

5. Нажмите "Изменить"
   
6. В появившемся окошке выберите "Создать"
  
7. Введите путь до папки где лежит EXE-файл

8. Нажмите "ОК" и закройте все окна

9. Попробуйте теперь открыть CMD (Win+R -> cmd) и ввести там следующее:

```cmd
rolton
```

У вас должно открыться приветственное окно RoltonLang

10. Попробуйте запустить .rolton файл. Вам предложат приложения где его запустить. Вы листате до самого конце и нажимайте на "Выбрать приложение на компьюторе" (или что-то подобное)

11. Выберите EXE-файл rolton.exe и нажимаете "ОК"

12. У вас запустится файл, а Windows тем временем связала .rolton файлы с rolton.exe
