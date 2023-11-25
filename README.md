
# "Speech to Text: Умный перевод записи лекций"



## 📋 Оглавление
1) [О проекте](#about_project)
2) [Запуск проекта](#setting)
3) [Как все работает...](#work)
4) [Алгоритм работы приложения](#project_structure)
5) [Необходимые библиотеки](#libraries)
6) [Необходимые модели](#models)
7) [Структура поекта](#hahaha)
   

   

## <a name="about_project"> 📱 О проекте </a> 
<p> "Speech to Text: Умный перевод записи лекций" - прототип интеллектуальной системы, который может создать готовые структурированные конспекты на основе аудиозаписей лекций, который ускорит и облегчит процесс подготовки материалов.  </p>
<p> В современном образовательном процессе качество подготовленных материалов — ключевой фактор успешного образовательного процесса. Методисты, преподаватели и студенты тратят значительное количество времени на анализ и совершенствование своих лекционных материалов и конспектов.
Поэтому было бы здорово иметь возможность быстро и безболезненно перевести запись лекций в текст.
</p>

## <a name="setting"> ⚙️ Запуск проекта </a>
<p> «Speech to Text» является универсальным помощником, с которым Вы можете работать по следующей схеме:
</p>
<p>
    1.Клонируйте репозиторий:
   
</p>

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

## <a name = "work"> 🤖 Как все работает...</a>
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

## <a name ="project_structure">👷Структура проекта</a>
<p>
<p align="center">
<img src="https://sun9-58.userapi.com/impg/pzoUuChC6UEqmDW_mA_t2BEMuKPn1GuM673gSA/fZmkZSzMQwk.jpg?size=1920x1080&quality=96&sign=d4ca30350efc218ce42bff09954f4cae&type=album" alt=“Speech to Text: Умный перевод записи лекций”![image]
 width="200"/>
   
</p>

## <a name ="libraries"> 🔨 Необходимые библиотеки</a>
<p>
   1.VOSK
</p>

## <a name ="models">👨‍💻 Необходимые модели</a>
<p>
   1. vosk-model-small-ru-0.22 (переводит данные из аудиоформата в текстовый формат)
   [ссылка 1](https://proglib.io/p/reshaem-zadachu-perevoda-russkoy-rechi-v-tekst-s-pomoshchyu-python-i-biblioteki-vosk-2022-06-30)
   [ссылка 2](https://github.com/gleb-skobinsky/ru_punct)
</p>
<p>
   2. Большая языковая модель (расставляет знаки препинания и выделяет термины)
   [ссылка](https://huggingface.co/IlyaGusev/saiga2_7b_lora)

</p>

## <a name ="hahaha">Структура поекта</a>
<p>
app/ приложение Django/ пользовательский интерфейс
</p>
<p>
model/ модель перевода аудио в сырой текст 
</p>
<p>
ru_punct-main / модель для расстановки пунктуации
</p>
<p>
Speech_to_text/ saiga2-7b и запуск моделей 
</p>
