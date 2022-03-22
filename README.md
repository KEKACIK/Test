<h1 align="center">ДОКУМЕНТАЦИЯ</h1>
В данном файле описаны инструкции взаимодействия человека с исходным кодом программы. Не рекомендуется менять что-либо не описанное в данном файле без специальных знаний.
<h2>Каталог с языками.</h2>
Для изменения текста вам необходимо войти в папку с ботом и найти там каталог, который назвается <b><i>locales</i></b>, в нем будут лежать все использующиеся в боте языки в виде файла <b><i>обозначение_языка.yml</i></b>. 
Для открытия YAML-файла подойдет любой текстовый редактор (блокнот), рекомендуется использовать продвинутые текстовые редакторы (Notepad++) 

<h2>Изменение Текста.</h2>
Для начала необходимо войти в каталог с языками, затем в нем найти нужный файл, после открытия вы увидите блок <b><i>messages</i></b>, содержащий множество ключей с текстом в таких видах, как:
<code>
	ключ: 'Текст'
	ключ: |
	  Текст
	ключ: |
	  Текст {параметр}
</code>
Не в коем случае <b><i>нельзя изменять структуру, а также поля ключ и параметр</i></b>. Изменению подлежит только <b><i>текст</i></b>, а также включенные в него <b><i>эмодзи</i></b>.
<h2>Изменение Кнопок.</h2>
Для начала необходимо войти в каталог с языками, затем в нем найти нужный файл, после открытия вы увидите блок <b><i>buttons</i></b>, содержащий множество ключей с текстом в таких видах, как:
<code>
	ключ: 'Текст кнопки'
</code>
Не в коем случае <b><i>нельзя изменять структуру</i></b>, а также поля <b><i>ключ</i></b>. Изменению подлежит только <b><i>текст кнопки</i></b>, а также включенные в него <b><i>эмодзи</i></b>.

