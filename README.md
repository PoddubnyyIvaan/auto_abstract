
# "Speech to Text: Умный перевод записи лекций"


## Оглавление
1) [О проекте](#about_project)
2) [Установка](#setting)
3) [Как все работает...](#work)

   

## <a name="about_project"> О проекте </a> 
<p> "Speech to Text: Умный перевод записи лекций" - прототип интеллектуальной системы, который может создать готовые структурированные конспекты на основе аудиозаписей лекций, который ускорит и облегчит процесс подготовки материалов.  </p>
<p> В современном образовательном процессе качество подготовленных материалов — ключевой фактор успешного образовательного процесса. Методисты, преподаватели и студенты тратят значительное количество времени на анализ и совершенствование своих лекционных материалов и конспектов.
Поэтому было бы здорово иметь возможность быстро и безболезненно перевести запись лекций в текст.
</p>

## <a name="setting"> Установка </a>
<p> «Speech to Text» является универсальным помощником, с которым Вы можете работать по следующей схеме:
</p>
**здесь нужно уточнить **
<p>
    1. Пройдите по ссылке:
   
    ("https://github.com/PoddubnyyIvaan/auto_abstract/edit/main/README.md")</p>

</p>
<p>
    2. Загрузите на сервер Вашу аудиозапись
</p>
   
<p>
    3. Выпейте чашку чая пока "Speech to Text: Умный перевод записи лекций" собирает конспект
</p>
   
<p>
    4. Формируется the_name_of_file.txt, который можно скачать с сервера, или он будет отправлен на почту пользователя :3
</p>

## <a name = "work"> Как все работает...</a>
<p>
    1. Загружаем на сервер аудиозапись (оболочка написана на Python c использованием Django)
</p>
<p>
    2. Модель vosk-model-small-ru-0.22, используя библиотеку VOSK, переводит данные из аудиоформата в текстовый формат (транскрибирует данные)
</p>
<p>
    3. Полученный текст подается на большую языковую модель, которая расставляет знаки препинания и выделяет термины
</p>
<p>
    4. Формируется текстовый файл 
</p>
